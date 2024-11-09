from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

class DatabaseUtil:
    def __init__(self, database_url: str):
        """
        Initialize the DatabaseUtil with a database URL.
        :param database_url: The database URL (e.g., 'sqlite:///example.db').
        """
        self.database_url = database_url
        self.engine: Engine = create_engine(self.database_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self) -> Session:
        """
        Create and return a new SQLAlchemy session.
        """
        return self.Session()
    
    def reflect_table(self, table_name: str):
        """
        Reflects the table from the database and returns a Table object.
        :param table_name: Name of the table to reflect.
        :return: Reflected Table object.
        """
        metadata = MetaData()
        metadata.reflect(bind=self.engine, only=[table_name])
        return metadata.tables[table_name]

    def create_all_tables(self, base):
        """
        Create all tables in the database based on the provided Base class.
        :param base: The SQLAlchemy Base class with the table definitions.
        """
        base.metadata.create_all(self.engine)

    def drop_all_tables(self, base):
        """
        Drop all tables from the database based on the provided Base class.
        :param base: The SQLAlchemy Base class with the table definitions.
        """
        base.metadata.drop_all(self.engine)

    def close(self):
        """
        Close the database engine connection.
        """
        self.engine.dispose()
