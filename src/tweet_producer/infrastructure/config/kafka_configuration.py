from dataclasses import dataclass


@dataclass
class KafkaConfiguration:
    kafka_host: str
    kafka_port: int = 9092
    security_protocol: str = "SSL"

    @property
    def kafka_connection_url(self) -> str:
        return f"{self._kafka_host}:{self._kafka_port}"
