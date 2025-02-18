from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_errors import ErrorErrors


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """
    Attributes:
        code (Union[Unset, int]): Error code
        status (Union[Unset, str]): Error name
        message (Union[Unset, str]): Error message
        errors (Union[Unset, ErrorErrors]): Errors
    """

    code: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    errors: Union[Unset, "ErrorErrors"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        status = self.status

        message = self.message

        errors: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.error_errors import ErrorErrors

        d = src_dict.copy()
        code = d.pop("code", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: Union[Unset, ErrorErrors]
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = ErrorErrors.from_dict(_errors)

        error = cls(
            code=code,
            status=status,
            message=message,
            errors=errors,
        )

        error.additional_properties = d
        return error

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
