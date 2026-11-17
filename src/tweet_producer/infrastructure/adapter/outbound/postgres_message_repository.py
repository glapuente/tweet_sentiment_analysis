from collections.abc import Collection

from pyspark.sql import DataFrame

from tweet_producer.application.port.outbound.database_message_repository import (
    DatabaseMessageRepository,
)
from tweet_producer.infrastructure.config.postgres_configuration import (
    PostgresConfiguration,
)


class PostgresMessageRepository(DatabaseMessageRepository[DataFrame]):
    def __init__(
        self,
        postgres_configuration: PostgresConfiguration,
    ):
        self._postgres_configuration = postgres_configuration

    def save_message(
        self, processed_message: DataFrame, batch_id: int | None = None
    ) -> None:
        """
        Function for saving messages to a Postgres database
        """
        processed_message.write.jdbc(
            url=self._postgres_configuration.postgres_connection_url,
            table=self._postgres_configuration.postgres_table_name,
            mode="append",
            properties=self._postgres_configuration.postgres_connection_properties,
        )

    def get_messages(self) -> Collection[DataFrame]:
        raise NotImplementedError
