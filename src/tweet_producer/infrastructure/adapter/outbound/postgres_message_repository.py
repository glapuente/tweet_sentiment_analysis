from typing import Collection

from tweet_producer.application.port.outbound.database_message_repository import DatabaseMessageRepository
from tweet_producer.domain.model.message import ProcessedMessage
from tweet_producer.infrastructure.config.postgres_configuration import PostgresConfiguration


class PostgresMessageRepository(DatabaseMessageRepository):
    def __init__(
        self,
        postgres_configuration: PostgresConfiguration,

    ):
        self._postgres_configuration = postgres_configuration


    def save_message(self, processed_message: ProcessedMessage, batch_id: int) -> None:
        """
        Function for saving messages to a Postgres database
        """
        try:
            processed_message.write.jdbc(
                url=self._postgres_configuration.postgres_connection_url,
                table=self._postgres_configuration.postgres_table_name,
                mode="append",
                properties=self._postgres_configuration.postgres_connection_properties,
            )
        except Exception as e:
            print(f"Error while saving message: {e}")


    def get_messages(self) -> Collection[ProcessedMessage]:
        return NotImplementedError
