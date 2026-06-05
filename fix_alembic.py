from sqlalchemy import create_engine, text

# Copia tu DATABASE_URL desde alembic.ini o .env
# Ejemplo: postgresql://usuario:contraseña@localhost:5432/orders_db
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/orders_db"

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS alembic_version;"))
        conn.commit()
        print("✅ Tabla alembic_version eliminada correctamente")
except Exception as e:
    print(f"❌ Error: {e}")
