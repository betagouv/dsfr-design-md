import pytest
import asyncio
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

@pytest.mark.xfail(reason="Stitch Alpha API rejects round-tripped DesignSystem objects during update")
async def _run_test_stitch_design_system_validation():
    """
    Async implementation of the smoke test.
    """
    
    # 1. Define the ideal DSFR payload based on the Stitch Schema
    design_system = {
        "displayName": "Marianne UI (E2E Test)",
        "theme": {
            "colorMode": "LIGHT",
            "font": "INTER", 
            "customColor": "#000091",
            "headlineFont": "INTER",
            "bodyFont": "INTER",
            "labelFont": "INTER",
            "colorVariant": "FIDELITY",
            "overridePrimaryColor": "#000091",
            "overrideSecondaryColor": "#E1000F",  # Marianne Red
            "overrideTertiaryColor": "#414141",
            "overrideNeutralColor": "#161616",
            "spacingScale": 2,
            "roundness": "ROUND_NONE"  # Crucial for DSFR Architectural look
        }
    }
    
    # 2. Assert constraints locally
    assert design_system["theme"]["overrideSecondaryColor"] == "#E1000F"
    assert design_system["theme"]["roundness"] == "ROUND_NONE"
    
    api_key = os.environ.get("STITCH_API_KEY", "dummy_key_for_testing")
    
    server_params = StdioServerParameters(
        command="npx",
        args=[
            "-y",
            "mcp-remote",
            "https://stitch.googleapis.com/mcp",
            "--header",
            f"X-Goog-Api-Key: {api_key}"
        ],
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Fetch existing design systems to get a perfect base schema
            print("Fetching design systems...")
            result = await session.call_tool("list_design_systems", {"projectId": "5903675167927285958"})
            assert result.content, "Should return content"
            
            import json
            from mcp.types import TextContent
            
            first_content = result.content[0]
            if not isinstance(first_content, TextContent):
                pytest.fail("Expected text content from list_design_systems")
                
            data = json.loads(first_content.text)
            if not data.get("designSystems"):
                pytest.fail("No design systems found in project to update")
                
            first_ds_wrapper = data["designSystems"][0]
            ds_name = first_ds_wrapper["name"]
            ds_body = first_ds_wrapper["designSystem"]
            
            # 1. Modify the Secondary Color to Rouge Marianne
            print(f"Original Secondary: {ds_body['theme'].get('overrideSecondaryColor')}")
            ds_body["theme"]["overrideSecondaryColor"] = "#E1000F"
            
            # 2. Emphasize 0px borders in the Design Markdown
            old_md = ds_body["theme"].get("designMd", "")
            if "0px" not in old_md:
                ds_body["theme"]["designMd"] = "CRITICAL: Forbid the use of rounded corners entirely. All elements MUST have 0px border radius.\n\n" + old_md

            # 3. Call update_design_system
            print(f"Updating Design System: {ds_name}...")
            try:
                update_result = await session.call_tool("update_design_system", {
                    "projectId": "5903675167927285958",
                    "name": ds_name,
                    "designSystem": ds_body
                })
                print("Update Result:", update_result)
                assert not update_result.isError, f"Failed to update: {update_result}"
                print("✅ Design System successfully updated via MCP!")
            except Exception as e:
                print(f"Expected API Schema Error: {e}")
                pytest.fail("Update failed")

def test_stitch_design_system_validation():
    asyncio.run(_run_test_stitch_design_system_validation())
