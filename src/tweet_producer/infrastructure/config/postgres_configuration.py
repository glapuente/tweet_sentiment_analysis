from dataclasses import dataclass


@dataclass
class PostgresConfiguration:
    postgres_db: str
    postgres_host: str
    postgres_user: str
    postgres_password: str
    postgres_port: int = 5432
    postgres_driver: str = "org.postgresql.Driver"


    @property
    def postgres_connection_url(self) -> str:
        return f"jdbc:postgresql://{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
