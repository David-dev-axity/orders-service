from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.schemas import OrderCreate, OrderResponse
from app.application.use_cases.create_order import CreateOrder
from app.application.use_cases.get_order import GetOrder
from app.application.use_cases.list_orders import ListOrders
from app.application.use_cases.delete_order import DeleteOrder
from app.infrastructure.db.session import get_db
from app.infrastructure.db.repository_impl import SqlAlchemyOrderRepository
from fastapi.security import OAuth2PasswordRequestForm
from app.api.security import authenticate_user, create_access_token
from datetime import timedelta
from app.api.security import get_current_user

router = APIRouter(prefix="/orders", tags=["Orders"])


# Dependency to inject repository
def get_repository(db: Session = Depends(get_db)):
    return SqlAlchemyOrderRepository(db)


@router.post("/", response_model=OrderResponse)
def create_order(
    order_data: OrderCreate,
    repository=Depends(get_repository),
    user=Depends(get_current_user),  # 🔐 Protección
):
    use_case = CreateOrder(repository)

    return use_case.execute(
        customer_name=order_data.customer_name,
        total_amount=order_data.total_amount,
    )


@router.get("/", response_model=list[OrderResponse])
def list_orders(
    repository=Depends(get_repository),
    user=Depends(get_current_user),  # 🔐 protegido
):
    use_case = ListOrders(repository)
    return use_case.execute()


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: str,
    repository=Depends(get_repository),
    user=Depends(get_current_user),  # 🔐 protegido
):
    use_case = GetOrder(repository)
    order = use_case.execute(order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@router.delete("/{order_id}")
def delete_order(
    order_id: str,
    repository=Depends(get_repository),
    user=Depends(get_current_user),  # 🔐 protegido
):
    use_case = DeleteOrder(repository)
    use_case.execute(order_id)

    return {"message": "Order deleted successfully"}

