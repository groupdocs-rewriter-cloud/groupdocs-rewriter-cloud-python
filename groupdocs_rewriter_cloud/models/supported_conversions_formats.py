# coding: utf-8

"""
    GroupDocs.Rewriter API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 23.11.1
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class SupportedConversionsFormats(str, Enum):
    """
    SupportedConversionsFormats
    """

    """
    allowed enum values
    """
    DOCX = 'Docx'
    RTF = 'Rtf'
    HTML = 'Html'
    ODT = 'Odt'
    TXT = 'Txt'
    MD = 'Md'
    PDF = 'Pdf'
    TIFF = 'Tiff'
    SVG = 'Svg'
    XPS = 'Xps'
    PPTX = 'Pptx'
    GIT = 'Git'

    @classmethod
    def from_json(cls, json_str: str) -> SupportedConversionsFormats:
        """Create an instance of SupportedConversionsFormats from a JSON string"""
        return SupportedConversionsFormats(json.loads(json_str))


