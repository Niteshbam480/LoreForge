def test_create_universe(client, auth_headers):
    response=client.post("/universes/",headers = auth_headers,json={"name":"test_universe1","description":"this is creation testing universe","is_public":True})
    assert response.status_code == 201
    assert response.json()["name"]

def test_list_universes(client, auth_headers):
    response=client.get("/universes",headers = auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_universe_not_found(client,auth_headers):
    response = client.get("/universes/99999",headers = auth_headers)
    assert response.status_code == 404    