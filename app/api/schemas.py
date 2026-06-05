from pydantic import BaseModel, ConfigDict

class OrderCreate(BaseModel):
    customer_name: str
    total_amount: float


from pydantic import BaseModel, ConfigDict


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    customer_name: str
    total_amount: float
