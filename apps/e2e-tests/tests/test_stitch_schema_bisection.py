import pytest
import asyncio
import os
import time
import re
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

@pytest.fixture(scope="module")
def mcp_server_params():
    api_key = os.environ.get("STITCH_API_KEY")
    if not api_key or api_key == "dummy_key_for_testing":
        pytest.skip("STITCH_API_KEY is missing or invalid.")
        
    return StdioServerParameters(
        command="npx",
        args=[
            "-y",
            "mcp-remote",
            "https://stitch.googleapis.com/mcp",
            "--header",
            f"X-Goog-Api-Key: {api_key}"
        ],
    )

@pytest.fixture(scope="module")
def stitch_project_id(mcp_server_params):
    """Creates a new project for this test run. Synchronous to avoid scope issues."""
    project_title = f"E2E Bisect Run - {int(time.time())}"
    
    async def _create():
        async with stdio_client(mcp_server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool("create_project", {"title": project_title})
                if result.isError:
                    return None
                from mcp.types import TextContent
                if isinstance(result.content[0], TextContent):
                    match = re.search(r'projects/(\d+)', result.content[0].text)
                    return match.group(1) if match else None
        return None

    pid = asyncio.run(_create())
    if not pid:
        pytest.fail("Failed to create isolated project for test run")
    print(f"\n📁 Created Project: {pid} ({project_title})")
    return pid

@asynccontextmanager
async def get_stitch_session(params):
    """Helper context manager to avoid anyio ScopeMismatch errors in fixtures."""
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            yield session

async def _create_ds(session, project_id, test_name, theme):
    """Helper to send payload to Stitch."""
    design_system = {"displayName": test_name, "theme": theme}
    result = await session.call_tool("create_design_system", {
        "projectId": project_id,
        "designSystem": design_system
    })
    if result.isError:
        from mcp.types import TextContent
        msg = result.content[0].text if (result.content and isinstance(result.content[0], TextContent)) else "Unknown"
        pytest.fail(f"Stitch API rejected payload: {msg}")
    return result

@pytest.mark.asyncio
async def test_01_minimal_valid_schema(mcp_server_params, stitch_project_id):
    async with get_stitch_session(mcp_server_params) as session:
        await _create_ds(session, stitch_project_id, "Minimal", {"colorMode": "LIGHT"})

@pytest.mark.asyncio
async def test_02_adding_primary_color(mcp_server_params, stitch_project_id):
    async with get_stitch_session(mcp_server_params) as session:
        await _create_ds(session, stitch_project_id, "Primary", {"colorMode": "LIGHT", "overridePrimaryColor": "#000091"})

@pytest.mark.asyncio
async def test_03_adding_design_md_basics(mcp_server_params, stitch_project_id):
    async with get_stitch_session(mcp_server_params) as session:
        await _create_ds(session, stitch_project_id, "BasicMd", {"colorMode": "LIGHT", "designMd": "## Brand"})

@pytest.mark.asyncio
async def test_04_full_dsfr_design_md(mcp_server_params, stitch_project_id):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, "../../../packages/dsfr-design-md/DESIGN.md")
    with open(path, "r") as f:
        full_md = f.read()
    async with get_stitch_session(mcp_server_params) as session:
        await _create_ds(session, stitch_project_id, "FullDSFR", {"colorMode": "LIGHT", "designMd": full_md})

@pytest.mark.xfail(reason="Schema intentionally broken to verify API limits")
@pytest.mark.asyncio
async def test_05_breaking_schema_reproduction(mcp_server_params, stitch_project_id):
    theme = {"colorMode": "LIGHT", "roundness": "ROUND_NONE"}
    async with get_stitch_session(mcp_server_params) as session:
        await _create_ds(session, stitch_project_id, "Broken", theme)
