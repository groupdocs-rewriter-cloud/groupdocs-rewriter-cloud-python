# coding: utf-8

"""
    GroupDocs.Rewriter API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 23.11.1
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.tokenizer import Tokenizer  # noqa: E501
from groupdocs_rewriter_cloud.rest import ApiException

class TestTokenizer(unittest.TestCase):
    """Tokenizer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Tokenizer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Tokenizer`
        """
        model = groupdocs_rewriter_cloud.models.tokenizer.Tokenizer()  # noqa: E501
        if include_optional :
            return Tokenizer(
                model = '', 
                type = ''
            )
        else :
            return Tokenizer(
        )
        """

    def testTokenizer(self):
        """Test Tokenizer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
