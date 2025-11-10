import pytest

@pytest.mark.asyncio
async def test_post_payment(async_client):
    # Create a client first
    client_resp = await async_client.post("/clients", json={"name": "Bob", "initial_due": "300.00"})
    client_id = client_resp.json()["id"]

    # Post a payment
    payment_resp = await async_client.post("/payments", json={"client_id": client_id, "amount": "100.00"})
    assert payment_resp.status_code == 201
    assert payment_resp.json()["amount"] == "100.00"
