# coding: utf-8

"""
    GroupDocs.Rewriter API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 24.4.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.summarization_text_response import SummarizationTextResponse  # noqa: E501
from groupdocs_rewriter_cloud.rest import ApiException

class TestSummarizationTextResponse(unittest.TestCase):
    """SummarizationTextResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SummarizationTextResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SummarizationTextResponse`
        """
        model = groupdocs_rewriter_cloud.models.summarization_text_response.SummarizationTextResponse()  # noqa: E501
        if include_optional :
            return SummarizationTextResponse(
                status = 'Continue', 
                message = '', 
                summarization_result = '', 
                summarization_results = [
                    ''
                    ]
            )
        else :
            return SummarizationTextResponse(
        )
        """

    def testSummarizationTextResponse(self):
        """Test SummarizationTextResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
