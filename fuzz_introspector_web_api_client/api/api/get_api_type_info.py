from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project: Union[Unset, str] = UNSET,
    type_name: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["project"] = project

    params["type_name"] = type_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/type-info",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 422:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    project: Union[Unset, str] = UNSET,
    type_name: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Gets type information about a given type in a project.

     The `type_name` is as the type is written in the source code. For example,
    `struct sam_hrec_type_s` is a name defined in the `htslib` library. In
    order to query data about this type, use `sam_hrec_type_s` as `type_name`
    and `htslib` for `project`.

    The Fuzz Introspector analysis may extract multiple internal data
    elements that represent the same type. As such, the return value of the API
    may include multiple elements.


    # Examples

    ## Example 1:
    - `project` : `htslib`
    - `type_name`: `sam_hrec_type_s`

    Args:
        project (Union[Unset, str]):
        type_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project=project,
        type_name=type_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    project: Union[Unset, str] = UNSET,
    type_name: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Gets type information about a given type in a project.

     The `type_name` is as the type is written in the source code. For example,
    `struct sam_hrec_type_s` is a name defined in the `htslib` library. In
    order to query data about this type, use `sam_hrec_type_s` as `type_name`
    and `htslib` for `project`.

    The Fuzz Introspector analysis may extract multiple internal data
    elements that represent the same type. As such, the return value of the API
    may include multiple elements.


    # Examples

    ## Example 1:
    - `project` : `htslib`
    - `type_name`: `sam_hrec_type_s`

    Args:
        project (Union[Unset, str]):
        type_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project=project,
        type_name=type_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
