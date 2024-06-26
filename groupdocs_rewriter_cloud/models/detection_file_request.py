# coding: utf-8

"""
    GroupDocs.Rewriter API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 24.4.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, constr
from groupdocs_rewriter_cloud.models.detection_supported_formats import DetectionSupportedFormats
from groupdocs_rewriter_cloud.models.file_saving_mode import FileSavingMode

class DetectionFileRequest(BaseModel):
    """
    DetectionFileRequest
    """
    language: constr(strict=True, min_length=1) = Field(..., description="Set language of text")
    url: Optional[StrictStr] = None
    origin: Optional[StrictStr] = Field(None, description="Information about SDK user, like a User-Agent")
    original_name: Optional[StrictStr] = Field(None, alias="originalName")
    saving_mode: Optional[FileSavingMode] = Field(None, alias="savingMode")
    min_length: Optional[StrictInt] = Field(None, alias="minLength")
    format: Optional[DetectionSupportedFormats] = None
    __properties = ["language", "url", "origin", "originalName", "savingMode", "minLength", "format"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DetectionFileRequest:
        """Create an instance of DetectionFileRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DetectionFileRequest:
        """Create an instance of DetectionFileRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DetectionFileRequest.parse_obj(obj)

        _obj = DetectionFileRequest.parse_obj({
            "language": obj.get("language"),
            "url": obj.get("url"),
            "origin": obj.get("origin"),
            "original_name": obj.get("originalName"),
            "saving_mode": obj.get("savingMode"),
            "min_length": obj.get("minLength"),
            "format": obj.get("format")
        })
        return _obj

