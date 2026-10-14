import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

def main():
    load_dotenv()

    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    metadata = MetaData()

    personas = Table(
        "personas_juanfelipe",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("nombre", String(100)),
        Column("correo", String(150)),
        Column("ciudad", String(100)),
        Column("telefono", String(50)),
        Column("ocupacion", String(100)),
        Column("direccion", String(200)),
        Column("edad", Integer),
    )

    metadata.create_all(engine)
    print("Estructura de tabla personas_juanfelipe creada exitosamente.")

if __name__ == "__main__":
    main()
