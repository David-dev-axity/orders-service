🛒 Orders Service API
       
Servicio de gestión de órdenes construido con FastAPI, PostgreSQL, aplicando principios de Clean Architecture y Domain-Driven Design (DDD).
________________________________________
📌 Descripción
Orders Service es una API RESTful diseñada para gestionar órdenes de manera segura, escalable y mantenible. Implementa buenas prácticas modernas de desarrollo backend, incluyendo separación por capas, pruebas automatizadas, análisis estático, seguridad y pipeline de CI/CD.
________________________________________
🚀 Características Principales
•	✅ API RESTful con FastAPI
•	✅ Autenticación JWT con tokens Bearer
•	✅ Clean Architecture (Domain, Application, Infrastructure)
•	✅ Domain-Driven Design (DDD)
•	✅ PostgreSQL con SQLAlchemy 2.0
•	✅ Migraciones con Alembic
•	✅ Docker y Docker Compose
•	✅ CI/CD con GitHub Actions
•	✅ Tests automatizados con pytest (>80% cobertura)
•	✅ Linting (black, flake8, isort)
•	✅ Type checking con mypy
•	✅ Auditoría de seguridad con pip-audit
•	✅ Documentación automática (Swagger y ReDoc)
________________________________________
🏗️ Arquitectura
El proyecto sigue Clean Architecture separando responsabilidades en capas bien definidas.
🔹 Capas
1️⃣ API Layer
•	Rutas (Controllers)
•	Esquemas Request/Response (Pydantic)
•	Seguridad y autenticación
2️⃣ Application Layer
•	Casos de uso:
–	CreateOrder
–	GetOrder
–	ListOrders
–	UpdateOrder
–	DeleteOrder
3️⃣ Domain Layer
•	Entidades (Order)
•	Interfaces de repositorio
•	Excepciones de dominio
4️⃣ Infrastructure Layer
•	Implementación de repositorios
•	Modelos SQLAlchemy
•	Gestión de sesión de base de datos
5️⃣ Base de Datos
•	PostgreSQL 15
________________________________________
🔄 Flujo de una petición
sequenceDiagram
    participant Client
    participant API
    participant Auth
    participant UseCase
    participant Repository
    participant DB

    Client->>API: POST /login
    API->>Auth: Validate credentials
    Auth-->>API: JWT Token
    API-->>Client: Return token

    Client->>API: POST /orders/ (+ JWT)
    API->>Auth: Validate token
    Auth-->>API: Token valid
    API->>UseCase: CreateOrderUseCase.execute()
    UseCase->>Repository: save(order)
    Repository->>DB: INSERT INTO orders
    DB-->>Repository: Order created
    Repository-->>UseCase: Order entity
    UseCase-->>API: Order created
    API-->>Client: 201 Created
________________________________________
🛠️ Stack Tecnológico
Backend
•	Python 3.11
•	FastAPI 0.136.3
•	Pydantic 2.5+
•	SQLAlchemy 2.0+
•	Alembic 1.12+
•	PostgreSQL 15
•	Python-Jose (JWT)
•	Passlib + Bcrypt
DevOps
•	Docker
•	Docker Compose
•	GitHub Actions
Testing & Calidad
•	Pytest
•	Pytest-cov
•	Black
•	Flake8
•	isort
•	mypy
•	pip-audit
Gestión de Dependencias
•	Poetry 1.8+
________________________________________
📋 Prerequisitos
•	Python 3.11+
•	Docker y Docker Compose
•	Poetry (opcional para desarrollo local)
•	Git
________________________________________
🐳 Instalación con Docker
git clone https://github.com/David-dev-axity/orders-service.git
cd orders-service
cp .env.example .env
docker compose up --build
API disponible en: - http://localhost:8000 - http://localhost:8000/docs - http://localhost:8000/redoc
________________________________________
💻 Desarrollo Local
git clone https://github.com/David-dev-axity/orders-service.git
cd orders-service
curl -sSL https://install.python-poetry.org | python3 -
poetry install
poetry shell
cp .env.example .env
poetry run alembic upgrade head
poetry run uvicorn app.main:app --reload
________________________________________
🔐 Uso de la API
Obtener Token
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=david@example.com&password=123456"
Crear Orden
curl -X POST "http://localhost:8000/orders/" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "John Doe",
    "total_amount": 1500.50
  }'
Listar Órdenes
curl -X GET "http://localhost:8000/orders/" \
  -H "Authorization: Bearer YOUR_TOKEN"
________________________________________
📡 Endpoints
🔐 Autenticación
Método	Endpoint	Descripción	Auth
POST	/login	Obtener token JWT	❌
📦 Órdenes
Método	Endpoint	Descripción	Auth
GET	/orders/	Listar órdenes	✅
POST	/orders/	Crear orden	✅
GET	/orders/{id}	Obtener orden por ID	✅
PUT	/orders/{id}	Actualizar orden	✅
DELETE	/orders/{id}	Eliminar orden	✅
________________________________________
🧪 Testing
poetry run pytest tests/ -v
poetry run pytest tests/ -v --cov=app --cov-report=html
________________________________________
🔄 CI/CD
Pipeline automatizado con GitHub Actions:
✅ lint-and-test
•	Linting
•	Type checking
•	Tests
•	Auditoría de seguridad
✅ docker-build
•	Build de imágenes
•	Verificación de servicios
________________________________________
🗄️ Migraciones
docker compose exec app alembic revision --autogenerate -m "descripcion"
docker compose exec app alembic upgrade head
docker compose exec app alembic downgrade -1
________________________________________
🛠️ Comandos Útiles
Docker
docker compose up -d
docker compose logs -f
docker compose down
docker compose build --no-cache
Calidad de Código
poetry run black app/ tests/
poetry run isort app/ tests/
poetry run flake8 app/ tests/
poetry run mypy app/
________________________________________
📂 Estructura del Proyecto
orders-service/
├── .github/
├── alembic/
├── app/
│   ├── api/
│   ├── application/
│   ├── domain/
│   ├── infrastructure/
│   └── main.py
├── tests/
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
└── README.md
________________________________________
🔒 Seguridad
•	JWT con tokens Bearer
•	Contraseñas hasheadas con bcrypt
•	Validación con Pydantic
•	Auditoría con pip-audit
•	Uso de variables de entorno para secretos
________________________________________
🤝 Contribuir
1.	Fork el proyecto
2.	Crear rama (git checkout -b feature/AmazingFeature)
3.	Commit (git commit -m 'Add AmazingFeature')
4.	Push (git push origin feature/AmazingFeature)
5.	Abrir Pull Request
________________________________________
📄 Licencia
MIT License — ver archivo LICENSE
________________________________________
👤 Autor
David Fonseca
GitHub: https://github.com/David-dev-axity
