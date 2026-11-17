from abc import ABC, abstractmethod
from collections.abc import Collection
from typing import TypeVar

T = TypeVar("T")


class DatabaseMessageRepository[T](ABC):
    def __init__(self):
        pass

    @abstractmethod
    def save_message(
        self, processed_message: T, batch_id: int | None = None
    ) -> None: ...

    @abstractmethod
    def get_messages(self) -> Collection[T]: ...
