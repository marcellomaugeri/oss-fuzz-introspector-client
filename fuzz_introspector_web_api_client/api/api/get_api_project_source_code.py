from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project: Union[Unset, str] = UNSET,
    filepath: Union[Unset, str] = UNSET,
    begin_line: Union[Unset, int] = UNSET,
    end_line: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["project"] = project

    params["filepath"] = filepath

    params["begin_line"] = begin_line

    params["end_line"] = end_line

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/project-source-code",
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
    filepath: Union[Unset, str] = UNSET,
    begin_line: Union[Unset, int] = UNSET,
    end_line: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Returns the source code at a specified location for a given project.

     # Examples
    ## Example 1
    - `project`: `htslib`
    - `filepath`: `/src/htslib/htsfile.c`
    - `begin_line`: `10`
    - `end_line`: `90`

    Args:
        project (Union[Unset, str]):
        filepath (Union[Unset, str]):
        begin_line (Union[Unset, int]):
        end_line (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project=project,
        filepath=filepath,
        begin_line=begin_line,
        end_line=end_line,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    project: Union[Unset, str] = UNSET,
    filepath: Union[Unset, str] = UNSET,
    begin_line: Union[Unset, int] = UNSET,
    end_line: Union[Unset, int] = UNSET,
) -> Response[Any]:
    """Returns the source code at a specified location for a given project.

     # Examples
    ## Example 1
    - `project`: `htslib`
    - `filepath`: `/src/htslib/htsfile.c`
    - `begin_line`: `10`
    - `end_line`: `90`

    Args:
        project (Union[Unset, str]):
        filepath (Union[Unset, str]):
        begin_line (Union[Unset, int]):
        end_line (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        project=project,
        filepath=filepath,
        begin_line=begin_line,
        end_line=end_line,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
