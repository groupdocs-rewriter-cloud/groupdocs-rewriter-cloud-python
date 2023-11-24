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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBytes, StrictInt, StrictStr, constr, validator
from groupdocs_rewriter_cloud.models.degree_enum import DegreeEnum
from groupdocs_rewriter_cloud.models.file_saving_mode import FileSavingMode
from groupdocs_rewriter_cloud.models.supported_conversions_formats import SupportedConversionsFormats

class SummarizationFileRequest(BaseModel):
    """
    SummarizationFileRequest
    """
    language: constr(strict=True, min_length=1) = Field(..., description="Set language of text")
    file: Optional[Union[StrictBytes, StrictStr]] = Field(None, description="Source file format")
    url: Optional[StrictStr] = None
    origin: Optional[StrictStr] = Field(None, description="Information about SDK user, like a User-Agent")
    original_name: Optional[StrictStr] = Field(None, alias="originalName")
    saving_mode: Optional[FileSavingMode] = Field(None, alias="savingMode")
    output_format: SupportedConversionsFormats = Field(..., alias="outputFormat")
    summarization_degree: Optional[DegreeEnum] = Field(None, alias="summarizationDegree")
    min_length: Optional[StrictInt] = Field(None, alias="minLength", description="Minimum length of the target text")
    format: Optional[StrictStr] = None
    __properties = ["language", "file", "url", "origin", "originalName", "savingMode", "outputFormat", "summarizationDegree", "minLength", "format"]

    @validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Unknown', 'Doc', 'Docx', 'Docm', 'Rtf', 'Odt', 'Txt', 'Pdf'):
            raise ValueError("must be one of enum values ('Unknown', 'Doc', 'Docx', 'Docm', 'Rtf', 'Odt', 'Txt', 'Pdf')")
        return value

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
    def from_json(cls, json_str: str) -> SummarizationFileRequest:
        """Create an instance of SummarizationFileRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SummarizationFileRequest:
        """Create an instance of SummarizationFileRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SummarizationFileRequest.parse_obj(obj)

        _obj = SummarizationFileRequest.parse_obj({
            "language": obj.get("language"),
            "file": obj.get("file"),
            "url": obj.get("url"),
            "origin": obj.get("origin"),
            "original_name": obj.get("originalName"),
            "saving_mode": obj.get("savingMode"),
            "output_format": obj.get("outputFormat"),
            "summarization_degree": obj.get("summarizationDegree"),
            "min_length": obj.get("minLength"),
            "format": obj.get("format")
        })
        return _obj
