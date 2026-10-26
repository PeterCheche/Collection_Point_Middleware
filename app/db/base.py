from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

# Import your models below so Alembic can detect them, e.g.:
# from app.models.item import Item  # noqa: F401
