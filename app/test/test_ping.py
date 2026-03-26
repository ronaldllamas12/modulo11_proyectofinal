from urllib import response

from fastapi.testclient import TestClient
from main import app

client_test = TestClient(app)





def test_status():
    response = client_test.get("/ping")
    assert response.status_code == 200
    
    
def test_response():
    response = client_test.get("/ping")
    assert response.json() == {"mensaje":"pong"}