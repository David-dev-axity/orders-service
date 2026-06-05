from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_name: str
    total_amount: float


class OrderResponse(BaseModel):
    id: str
    customer_name: str
    total_amount: float

    class Config:
        from_attributes = True
