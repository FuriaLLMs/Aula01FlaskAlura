from pydantic import BaseModel
from datetime import date

class Sale(BaseModel):
    id: int 
    sale_date: date
    product_id: int # Alterado para int para bater com a rota <int:product_id>
    quantity: int
    total_value: float
