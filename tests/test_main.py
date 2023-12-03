import pytest
#from webapp import appCLI
#from webapp.main import app, Body
from fastapi.testclient import TestClient
import app as application


client = TestClient(app)                # Used for defining test cases for fastapi apps


def test_main():
    response = appCLI.predict('I think this life should be a long one')      # because the output is indeterminate
    assert response

def test_app():
    response = application.predict("I think this life should be a long one")          # because the ouput is indeterminate
    assert response


def test_predict():
    # Test case 1: Valid input
    response = client.post('/generate', json={'text': 'Your input text goes here.'})
    assert response.status_code == 200
    result = response.json()
    assert 'generated_text' in result  # Adjust based on the actual structure of the response

    # Test case 2: Invalid input (e.g., missing 'text' field)
    response = client.post('/generate', json={})
    assert response.status_code == 422  # HTTP 422 Unprocessable Entity for validation errors


