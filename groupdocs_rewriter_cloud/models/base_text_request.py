# coding: utf-8

"""
    GroupDocs.Rewriter API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 23.11.1
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr

class BaseTextRequest(BaseModel):
    """
    BaseTextRequest
    """
    language: constr(strict=True, min_length=1) = Field(..., description="Set language of text")
    text: Optional[StrictStr] = Field(None, description="Single text paragraph")
    texts: Optional[conlist(StrictStr)] = Field(None, description="Text paragraphs")
    origin: Optional[StrictStr] = Field(None, description="Information about SDK user, like a User-Agent")
    __properties = ["language", "text", "texts", "origin"]

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
    def from_json(cls, json_str: str) -> BaseTextRequest:
        """Create an instance of BaseTextRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BaseTextRequest:
        """Create an instance of BaseTextRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BaseTextRequest.parse_obj(obj)

        _obj = BaseTextRequest.parse_obj({
            "language": obj.get("language"),
            "text": obj.get("text"),
            "texts": obj.get("texts"),
            "origin": obj.get("origin")
        })
        return _obj
