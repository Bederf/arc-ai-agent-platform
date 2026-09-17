from app.mcp_server import mcp


def test_mcp_exposes_read_only_evidence_tools():
    names = {tool.name for tool in mcp._tool_manager.list_tools()}
    assert names == {"get_claim", "get_policy", "search_policy"}
