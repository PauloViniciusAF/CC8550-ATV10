import pytest
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError

BASE_URL = "https://fakestoreapi.com/products"

PRODUCT_SCHEMA = {
    "type": "object",
    "required": [
        "id",
        "title",
        "price",
        "description",
        "category",
        "image",
        "rating",
    ],
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string", "minLength": 1},
        "price": {"type": ["number", "integer"]},
        "description": {"type": "string"},
        "category": {"type": "string", "enum": [
            "electronics",
            "jewelery",
            "men's clothing",
            "women's clothing",
        ]},
        "image": {"type": "string"},
        "rating": {
            "type": "object",
            "required": ["rate", "count"],
            "properties": {
                "rate": {"type": ["number", "integer"]},
                "count": {"type": "integer"},
            },
        },
    },
}


@pytest.fixture(scope="module")
def session():
    with requests.Session() as s:
        yield s


def test_listar_todos_produtos(session):
    response = session.get(BASE_URL, timeout=10)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    produto = data[0]
    for key in ("id", "title", "price", "description", "category", "image", "rating"):
        assert key in produto


def test_buscar_produto_por_id(session):
    response = session.get(f"{BASE_URL}/1", timeout=10)
    assert response.status_code == 200
    produto = response.json()
    assert produto.get("id") == 1
    assert produto.get("title")
    assert produto.get("category") in [
        "electronics",
        "jewelery",
        "men's clothing",
        "women's clothing",
    ]


@pytest.mark.parametrize(
    "categoria",
    ["electronics", "jewelery", "men's clothing", "women's clothing"],
)
def test_filtrar_produtos_por_categoria(session, categoria):
    response = session.get(f"{BASE_URL}/category/{categoria}", timeout=10)
    assert response.status_code == 200
    produtos = response.json()
    assert isinstance(produtos, list)
    assert len(produtos) > 0
    for produto in produtos:
        assert produto.get("category") == categoria


def test_validar_schema_produtos(session):
    response = session.get(BASE_URL, timeout=10)
    assert response.status_code == 200
    produtos = response.json()
    erros = []
    for produto in produtos:
        try:
            validate(instance=produto, schema=PRODUCT_SCHEMA)
        except ValidationError as exc:
            erros.append(str(exc))
    assert not erros, f"Produtos fora do schema: {erros}"


@pytest.mark.parametrize("limite", [1, 3, 5])
def test_limite_produtos_retorno(session, limite):
    response = session.get(BASE_URL, params={"limit": limite}, timeout=10)
    assert response.status_code == 200
    produtos = response.json()
    assert isinstance(produtos, list)
    assert len(produtos) == limite
