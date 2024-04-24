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


from typing import List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, conlist

class LanguageInfo(BaseModel):
    """
    LanguageInfo
    """
    id: Optional[StrictInt] = None
    code: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    actions: Optional[conlist(StrictStr)] = None
    __properties = ["id", "code", "name", "actions"]

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
    def from_json(cls, json_str: str) -> LanguageInfo:
        """Create an instance of LanguageInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LanguageInfo:
        """Create an instance of LanguageInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LanguageInfo.parse_obj(obj)

        _obj = LanguageInfo.parse_obj({
            "id": obj.get("id"),
            "code": obj.get("code"),
            "name": obj.get("name"),
            "actions": obj.get("actions")
        })
        return _obj
