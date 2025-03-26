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

from groupdocs_rewriter_cloud.models.formalize_ocr_request import FormalizeOcrRequest

class TestFormalizeOcrRequest(unittest.TestCase):
    """FormalizeOcrRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FormalizeOcrRequest:
        """Test FormalizeOcrRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FormalizeOcrRequest`
        """
        model = FormalizeOcrRequest()
        if include_optional:
            return FormalizeOcrRequest(
                language = '0',
                url = '',
                origin = '',
                original_name = '',
                saving_mode = 'Files',
                output_format = 'Text',
                format = 'Unknown'
            )
        else:
            return FormalizeOcrRequest(
                language = '0',
                output_format = 'Text',
                format = 'Unknown',
        )
        """

    def testFormalizeOcrRequest(self):
        """Test FormalizeOcrRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
