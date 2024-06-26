# coding: utf-8

"""
    GroupDocs.Rewriter API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 24.4.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class FileSavingMode(str, Enum):
    """
    FileSavingMode
    """

    """
    allowed enum values
    """
    FILES = 'Files'
    ARCHIVE = 'Archive'
    BOTH = 'Both'

    @classmethod
    def from_json(cls, json_str: str) -> FileSavingMode:
        """Create an instance of FileSavingMode from a JSON string"""
        return FileSavingMode(json.loads(json_str))


