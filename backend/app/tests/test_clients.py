import pytest

@pytest.mark.asyncio
async def test_create_client(async_client):
    resp = await async_client.post("/clients", json={"name": "Alice", "initial_due": "500.00"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["name"] == "Alice"
    assert data["initial_due"] == "500.00"
