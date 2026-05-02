import pytest
import asyncio
import os
import time
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

PROJECT_ID = "5903675167927285958"

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

async def _create_design_system_with_payload(server_params, test_name, theme_payload):
    """Helper to send a payload to Stitch MCP and return the result."""
    design_system = {
        "displayName": f"E2E Bisect: {test_name} - {int(time.time())}",
        "theme": theme_payload
    }
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            result = await session.call_tool("create_design_system", {
                "projectId": PROJECT_ID,
                "designSystem": design_system
            })
            
            if result.isError:
                error_msg = result.content[0].text if result.content else "Unknown error"
                pytest.fail(f"Stitch API rejected payload: {error_msg}")
            
            return result

def test_01_minimal_valid_schema(mcp_server_params):
    """Test the absolute minimum theme schema required by Stitch."""
    theme = {
        "colorMode": "LIGHT"
    }
    asyncio.run(_create_design_system_with_payload(mcp_server_params, "Minimal", theme))

def test_02_adding_primary_color(mcp_server_params):
    """Test adding just the primary color override."""
    theme = {
        "colorMode": "LIGHT",
        "overridePrimaryColor": "#000091" # Bleu France
    }
    asyncio.run(_create_design_system_with_payload(mcp_server_params, "PrimaryColor", theme))

def test_03_adding_design_md_basics(mcp_server_params):
    """Test adding a basic designMd string."""
    theme = {
        "colorMode": "LIGHT",
        "designMd": "## Brand\\nThis is the Marianne DSFR system."
    }
    asyncio.run(_create_design_system_with_payload(mcp_server_params, "BasicDesignMd", theme))

def test_04_full_dsfr_design_md(mcp_server_params):
    """Test injecting the full DSFR Markdown document without any JSON shape overrides."""
    with open("packages/dsfr-design-md/DESIGN.md", "r") as f:
        full_md = f.read()
        
    theme = {
        "colorMode": "LIGHT",
        "designMd": full_md
    }
    asyncio.run(_create_design_system_with_payload(mcp_server_params, "FullDesignMd", theme))

def test_05_breaking_schema_reproduction(mcp_server_params):
    """
    Attempt to reproduce the exact schema that causes 'Invalid Argument'.
    We suspect fields like `roundness`, `font`, or specific `overrideSecondaryColor` might trigger it.
    """
    theme = {
        "colorMode": "LIGHT",
        "font": "INTER", 
        "overridePrimaryColor": "#000091",
        "overrideSecondaryColor": "#E1000F",
        "roundness": "ROUND_NONE"
    }
    
    # We use xfail here because we expect this specific combination to break the API as seen earlier.
    # If it passes, it means one of the fields isn't breaking it after all!
    try:
        asyncio.run(_create_design_system_with_payload(mcp_server_params, "BrokenSchema", theme))
    except BaseException:
        pytest.xfail("Schema intentionally broken to verify API limits")
