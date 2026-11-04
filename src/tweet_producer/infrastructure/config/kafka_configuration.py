class KafkaConfiguration:
    def __init__(
        self,
        kafka_host: str,
        kafka_port: int = 9092,
        security_protocol: str = "SSL",
    ):
        self._kafka_host = kafka_host
        self._kafka_port = kafka_port
        self._security_protocol = security_protocol

    @property
    def kafka_connection_url(self) -> str:
        return f"{self._kafka_host}:{self._kafka_port}"
