from app.models.product import Product
from app.models.user import LoginPayload
from app.models.sale import Sale
from datetime import date
import pytest
from pydantic import ValidationError

def test_product_model_valid():
    p = Product(name="Camiseta", price=29.90, stock=10)
    assert p.name == "Camiseta"
    assert p.price == 29.90
    assert p.description is None

def test_product_model_invalid():
    with pytest.raises(ValidationError):
        Product(name="Camiseta", price="invalid", stock=10)

def test_login_payload():
    l = LoginPayload(username="user", password="123")
    assert l.username == "user"

def test_sale_model():
    s = Sale(id=1, sale_date=date(2023, 1, 1), product_id=10, quantity=2, total_value=100.0)
    assert s.product_id == 10
