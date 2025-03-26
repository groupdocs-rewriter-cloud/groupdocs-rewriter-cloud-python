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
from groupdocs_rewriter_cloud.models.health_check_response import HealthCheckResponse  # noqa: E501
from groupdocs_rewriter_cloud.rest import ApiException

class TestHealthCheckResponse(unittest.TestCase):
    """HealthCheckResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HealthCheckResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HealthCheckResponse`
        """
        model = groupdocs_rewriter_cloud.models.health_check_response.HealthCheckResponse()  # noqa: E501
        if include_optional :
            return HealthCheckResponse(
                initial_request = groupdocs_rewriter_cloud.models.cloud_text_request.CloudTextRequest(
                    language = 56, 
                    text = '', 
                    action = '', 
                    texts = [
                        ''
                        ], 
                    suggestions = 56, 
                    diversity = 56, 
                    tokenize = True, 
                    origin = '', 
                    request_id = '', ), 
                health_check_info = groupdocs_rewriter_cloud.models.health_check_info.HealthCheckInfo(
                    files_processor_status = '', 
                    paraphrasing_status = '', 
                    detector_status = '', 
                    summarization_status = '', ), 
                models = [
                    groupdocs_rewriter_cloud.models.model.Model(
                        loaded = True, 
                        models_id = 56, 
                        models = [
                            ''
                            ], 
                        opt = groupdocs_rewriter_cloud.models.opt.Opt(
                            beam_size = 56, 
                            gpu = 56, 
                            replace_unk = True, ), 
                        timeout = 56, 
                        tokenizer = groupdocs_rewriter_cloud.models.tokenizer.Tokenizer(
                            model = '', 
                            type = '', ), )
                    ]
            )
        else :
            return HealthCheckResponse(
        )
        """

    def testHealthCheckResponse(self):
        """Test HealthCheckResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
