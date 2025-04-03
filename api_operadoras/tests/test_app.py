import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
  with app.test_client() as client:
    yield client

def test_noParams(client):
    response = client.get('/operadoras')
    assert response.status_code == 400
    data = response.get_json()
    assert 'erro' in data
    assert 'obrigatório' in data['erro'].lower()

def test_withResults(client):
  response = client.get('/operadoras?q=amil')
  assert response.status_code == 200
  data = response.get_json()
  assert isinstance(data, list)
  assert len(data) > 0
  assert 'nome_fantasia' in data[0]

def test_noResults(client):
  response = client.get('/operadoras?q=naoexisteoperadora')
  assert response.status_code == 200
  data = response.get_json()
  assert data == []

def test_resultLimit(client):
    response = client.get('/operadoras?q=a')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) <= 10

def test_accSearch(client):
    response = client.get('/operadoras?q=são')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 0


import time

def test_time_response(client):
    inicio = time.perf_counter()
    response = client.get('/operadoras?q=a')
    fim = time.perf_counter()
    duracao = fim - inicio

    assert response.status_code == 200
    assert duracao < 1.0
