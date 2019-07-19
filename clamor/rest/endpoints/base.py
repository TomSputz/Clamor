# -*- coding: utf-8 -*-

from contextlib import contextmanager
from typing import NewType, Union

from ..http import HTTP

__all__ = (
    'Snowflake',
    'optional',
    'EndpointsWrapper',
)

#: A type for denoting raw snowflake parameters.
Snowflake = NewType('Snowflake', Union[int, str])


def optional(**kwargs) -> dict:
    """"""

    return {
        key: value for key, value in kwargs.items()
        if value is not None
    }


class EndpointsWrapper:
    """"""

    __slots__ = ('http',)

    def __init__(self, token: str):
        self.http = HTTP(token)

    @property
    def token(self) -> str:
        """"""

        return self.http.token

    @contextmanager
    def raw_responses(self):
        """"""

        try:
            yield self.http.responses
        finally:
            self.http.responses.clear()

    def new_instance(self) -> 'EndpointsWrapper':
        """"""

        return self.__class__(self.token)
