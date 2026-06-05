from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.infrastructure.db.session import Base
from app.infrastructure.db.repository_impl import SqlAlchemyOrderRepository
from app.domain.entities.order import Order


def test_repository_with_sqlite():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    repo = SqlAlchemyOrderRepository(session)

    order = Order("1", "Integration", 200)
    repo.save(order)

    found = repo.get_by_id("1")

    assert found is not None
    assert found.customer_name == "Integration"
