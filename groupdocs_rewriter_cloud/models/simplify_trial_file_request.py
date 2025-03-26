# coding: utf-8

"""
    GroupDocs.Rewriter API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 25.3.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from groupdocs_rewriter_cloud.models.file_saving_mode import FileSavingMode
from typing import Optional, Set
from typing_extensions import Self

class SimplifyTrialFileRequest(BaseModel):
    """
    SimplifyTrialFileRequest
    """ # noqa: E501
    language: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Set language of text")
    url: Optional[StrictStr] = None
    origin: Optional[StrictStr] = Field(default=None, description="Information about SDK user, like a User-Agent")
    original_name: Optional[StrictStr] = Field(default=None, alias="originalName")
    saving_mode: Optional[FileSavingMode] = Field(default=None, alias="savingMode")
    format: Optional[StrictStr] = Field(default=None, description="Set the file format.")
    __properties: ClassVar[List[str]] = ["language", "url", "origin", "originalName", "savingMode", "format"]

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Docx', 'Pdf']):
            raise ValueError("must be one of enum values ('Docx', 'Pdf')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SimplifyTrialFileRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SimplifyTrialFileRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "language": obj.get("language"),
            "url": obj.get("url"),
            "origin": obj.get("origin"),
            "originalName": obj.get("originalName"),
            "savingMode": obj.get("savingMode"),
            "format": obj.get("format")
        })
        return _obj


