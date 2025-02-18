from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project: Union[Unset, str] = UNSET,
    function_signature: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["project"] = project

    params["function_signature"] = function_signature

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/function-source-code",
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
    function_signature: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Gets the source code of a given function.

     The function signature provided is the value as is returned by
    other APIs, such as `/api/function-signature`.

    The function is identified by function signature.

    On success and the function is found, then the return value
    is data in json format including the source code itself,
    the filepath, the source line number where the function begins
    and the source line number where the function ends.

    # Examples
    ## Example 1:
    - `project`: `htslib`
    - `function_signature`: `void sam_hrecs_remove_ref_altnames(sam_hrecs_t *, int, const char *)`

    Args:
        project (Union[Unset, str]):
        function_signature (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project=project,
        function_signature=function_signature,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    project: Union[Unset, str] = UNSET,
    function_signature: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Gets the source code of a given function.

     The function signature provided is the value as is returned by
    other APIs, such as `/api/function-signature`.

    The function is identified by function signature.

    On success and the function is found, then the return value
    is data in json format including the source code itself,
    the filepath, the source line number where the function begins
    and the source line number where the function ends.

    # Examples
    ## Example 1:
    - `project`: `htslib`
    - `function_signature`: `void sam_hrecs_remove_ref_altnames(sam_hrecs_t *, int, const char *)`

    Args:
        project (Union[Unset, str]):
        function_signature (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project=project,
        function_signature=function_signature,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
