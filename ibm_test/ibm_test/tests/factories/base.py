from typing import Generic, TypeVar

import factory

T = TypeVar("T")


class BaseFactory(Generic[T], factory.Factory):
    @classmethod
    def create(cls, **kwargs) -> T:
        return super().create(**kwargs)