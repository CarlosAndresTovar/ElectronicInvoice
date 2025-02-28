from sqlalchemy import create_engine
from sqlachemy.engine import URL
from sqlalchemy.orm import sessionmaker

url = URL(
    drivername = "postgresql+asyncpg",
    username = "odoo",
    password = "odoo",
    host = "172.28.0.5",
    port = "5432",
    database = "electronicinvoice"
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()