def test_register_success(client):
    response=client.post("/auth/register",json={"email":"test1@test.com","username":"tester1","password":"test120711"})
    assert response.status_code == 201
    assert response.json()["email"]

def test_register_duplicate_email(client):
    client.post("/auth/register",json={"email":"test2@test.com","username":"tester2","password":"test220711"})
    response=client.post("/auth/register",json={"email":"test2@test.com","username":"tester3","password":"test320711"})
    assert response.status_code == 400

def test_login_success(client):
    client.post("/auth/register",json={"email":"test3@test.com","username":"tester3","password":"test320711"})
    response=client.post("/auth/login",json={"email":"test3@test.com","password":"test320711"})
    assert response.status_code == 200
    assert response.json()["access_token"]

def test_login_wrong_password(client):
    client.post("/auth/register",json={"email":"test4@test.com","username":"tester4","password":"test420711"})
    response=client.post("/auth/login",json={"email":"test4@test.com","password":"testx20711"})
    assert response.status_code == 401