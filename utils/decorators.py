from rest_framework import exceptions as rest_exceptions
from elasticsearch import exceptions


def with_es_exceptions(f):
    def new_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except exceptions.NotFoundError:
            raise rest_exceptions.NotFound()

        except exceptions.AuthenticationException:
            raise rest_exceptions.AuthenticationFailed()

        except exceptions.SerializationError:
            raise rest_exceptions.ParseError()

    return new_f
