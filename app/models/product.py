from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    """
    Modelo de dados para um Produto.
    """
    name: str
    sku: str  # <--- Novo campo obrigatório (Desafio)
    price: float
    description: Optional[str] = None
    stock: int
