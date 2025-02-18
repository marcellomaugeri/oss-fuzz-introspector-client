from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaginationMetadata")


@_attrs_define
class PaginationMetadata:
    """
    Attributes:
        total (Union[Unset, int]):
        total_pages (Union[Unset, int]):
        first_page (Union[Unset, int]):
        last_page (Union[Unset, int]):
        page (Union[Unset, int]):
        previous_page (Union[Unset, int]):
        next_page (Union[Unset, int]):
    """

    total: Union[Unset, int] = UNSET
    total_pages: Union[Unset, int] = UNSET
    first_page: Union[Unset, int] = UNSET
    last_page: Union[Unset, int] = UNSET
    page: Union[Unset, int] = UNSET
    previous_page: Union[Unset, int] = UNSET
    next_page: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        total_pages = self.total_pages

        first_page = self.first_page

        last_page = self.last_page

        page = self.page

        previous_page = self.previous_page

        next_page = self.next_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if first_page is not UNSET:
            field_dict["first_page"] = first_page
        if last_page is not UNSET:
            field_dict["last_page"] = last_page
        if page is not UNSET:
            field_dict["page"] = page
        if previous_page is not UNSET:
            field_dict["previous_page"] = previous_page
        if next_page is not UNSET:
            field_dict["next_page"] = next_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        first_page = d.pop("first_page", UNSET)

        last_page = d.pop("last_page", UNSET)

        page = d.pop("page", UNSET)

        previous_page = d.pop("previous_page", UNSET)

        next_page = d.pop("next_page", UNSET)

        pagination_metadata = cls(
            total=total,
            total_pages=total_pages,
            first_page=first_page,
            last_page=last_page,
            page=page,
            previous_page=previous_page,
            next_page=next_page,
        )

        pagination_metadata.additional_properties = d
        return pagination_metadata

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
