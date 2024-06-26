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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from groupdocs_rewriter_cloud.models.http_status_code import HttpStatusCode

class DetectionTextResponse(BaseModel):
    """
    DetectionTextResponse
    """
    status: Optional[HttpStatusCode] = None
    message: Optional[StrictStr] = Field(None, description="Information about process")
    probability: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The probability that the text turned out to be paraphrased")
    is_paraphrased: Optional[StrictBool] = Field(None, alias="isParaphrased")
    __properties = ["status", "message", "probability", "isParaphrased"]

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
    def from_json(cls, json_str: str) -> DetectionTextResponse:
        """Create an instance of DetectionTextResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DetectionTextResponse:
        """Create an instance of DetectionTextResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DetectionTextResponse.parse_obj(obj)

        _obj = DetectionTextResponse.parse_obj({
            "status": obj.get("status"),
            "message": obj.get("message"),
            "probability": obj.get("probability"),
            "is_paraphrased": obj.get("isParaphrased")
        })
        return _obj

