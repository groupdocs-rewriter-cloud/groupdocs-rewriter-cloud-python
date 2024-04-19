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





class SummarizationSupportedFormats(str, Enum):
    """
    SummarizationSupportedFormats
    """

    """
    allowed enum values
    """
    UNKNOWN = 'Unknown'
    DOC = 'Doc'
    DOCX = 'Docx'
    DOCM = 'Docm'
    RTF = 'Rtf'
    ODT = 'Odt'
    TXT = 'Txt'
    PDF = 'Pdf'

    @classmethod
    def from_json(cls, json_str: str) -> SummarizationSupportedFormats:
        """Create an instance of SummarizationSupportedFormats from a JSON string"""
        return SummarizationSupportedFormats(json.loads(json_str))


