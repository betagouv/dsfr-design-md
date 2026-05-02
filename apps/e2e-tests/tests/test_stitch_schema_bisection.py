import pytest
import asyncio
import os
import time
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
    """Creates a new project for this test run to ensure a clean state."""
    project_title = f"E2E Bisect Run - {int(time.time())}"
    
    async def _create_project():
        async with stdio_client(mcp_server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool("create_project", {
                    "title": project_title
                })
                if result.isError:
                    pytest.fail(f"Failed to create isolated project: {result.content}")
                
                # The result should contain the new project name/ID in its text payload.
                # Since Stitch MCP returns text, we need to extract the ID.
                # Usually it looks like "Project created: projects/12345..."
                # Let's extract the digits.
                import re
                text = result.content[0].text
                match = re.search(r'projects/(\d+)', text)
                if match:
                    return match.group(1)
                else:
                    pytest.fail(f"Could not parse projectId from result: {text}")
                    
    return asyncio.run(_create_project())

async def _create_design_system_with_payload(server_params, project_id, test_name, theme_payload):
    """Helper to send a payload to Stitch MCP and return the result."""
    design_system = {
        "displayName": f"{test_name}",
        "theme": theme_payload
    }
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            result = await session.call_tool("create_design_system", {
                "projectId": project_id,
                "designSystem": design_system
            })
            
            if result.isError:
                error_msg = result.content[0].text if result.content else "Unknown error"
                pytest.fail(f"Stitch API rejected payload: {error_msg}")
            
            return result

def test_01_minimal_valid_schema(mcp_server_params, stitch_project_id):
    """Test the absolute minimum theme schema required by Stitch."""
    theme = {
        "colorMode": "LIGHT"
    }
    asyncio.run(_create_design_system_with_payload(mcp_server_params, stitch_project_id, "Minimal", theme))

def test_02_adding_primary_color(mcp_server_params, stitch_project_id):
    """Test adding just the primary color override."""
    theme = {
        "colorMode": "LIGHT",
        "overridePrimaryColor": "#000091" # Bleu France
    }
    asyncio.run(_create_design_system_with_payload(mcp_server_params, stitch_project_id, "PrimaryColor", theme))

def test_03_adding_design_md_basics(mcp_server_params, stitch_project_id):
    """Test adding a basic designMd string."""
    theme = {
        "colorMode": "LIGHT",
        "designMd": "## Brand\\nThis is the Marianne DSFR system."
    }
    asyncio.run(_create_design_system_with_payload(mcp_server_params, stitch_project_id, "BasicDesignMd", theme))

def test_04_full_dsfr_design_md(mcp_server_params, stitch_project_id):
    """Test injecting the full DSFR Markdown document without any JSON shape overrides."""
    with open("packages/dsfr-design-md/DESIGN.md", "r") as f:
        full_md = f.read()
        
    theme = {
        "colorMode": "LIGHT",
        "designMd": full_md
    }
    asyncio.run(_create_design_system_with_payload(mcp_server_params, stitch_project_id, "FullDesignMd", theme))

def test_05_breaking_schema_reproduction(mcp_server_params, stitch_project_id):
    """
    Attempt to reproduce the exact schema that causes 'Invalid Argument'.
    """
    theme = {
        "colorMode": "LIGHT",
        "font": "INTER", 
        "overridePrimaryColor": "#000091",
        "overrideSecondaryColor": "#E1000F",
        "roundness": "ROUND_NONE"
    }
    
    try:
        asyncio.run(_create_design_system_with_payload(mcp_server_params, stitch_project_id, "BrokenSchema", theme))
    except BaseException:
        pytest.xfail("Schema intentionally broken to verify API limits")
