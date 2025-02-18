"""A client library for accessing Fuzz Introspector Web API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
