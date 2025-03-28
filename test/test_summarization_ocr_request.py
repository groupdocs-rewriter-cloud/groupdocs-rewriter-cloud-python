# coding: utf-8

"""
    GroupDocs.Rewriter API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 24.11.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from groupdocs_rewriter_cloud.models.summarization_ocr_request import SummarizationOcrRequest

class TestSummarizationOcrRequest(unittest.TestCase):
    """SummarizationOcrRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SummarizationOcrRequest:
        """Test SummarizationOcrRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SummarizationOcrRequest`
        """
        model = SummarizationOcrRequest()
        if include_optional:
            return SummarizationOcrRequest(
                language = '0',
                url = '',
                origin = '',
                original_name = '',
                saving_mode = 'Files',
                output_format = 'Text',
                summarization_degree = 'Off',
                format = 'Unknown',
                min_length = 56
            )
        else:
            return SummarizationOcrRequest(
                language = '0',
                output_format = 'Text',
                format = 'Unknown',
        )
        """

    def testSummarizationOcrRequest(self):
        """Test SummarizationOcrRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
