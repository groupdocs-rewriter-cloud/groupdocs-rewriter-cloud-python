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

import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.api.summarize_api import SummarizeApi  # noqa: E501
from groupdocs_rewriter_cloud.rest import ApiException


class TestSummarizeApi(unittest.TestCase):
    """SummarizeApi unit test stubs"""

    def setUp(self):
        self.api = groupdocs_rewriter_cloud.api.summarize_api.SummarizeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_summarize_document_post(self):
        """Test case for summarize_document_post

        Summarize document  # noqa: E501
        """
        pass

    def test_summarize_document_request_id_get(self):
        """Test case for summarize_document_request_id_get

        Return document summarizing status.  Also return URLs for downloading of summarized document if summarization was successful  # noqa: E501
        """
        pass

    def test_summarize_document_trial_post(self):
        """Test case for summarize_document_trial_post

        Trial summarize document  # noqa: E501
        """
        pass

    def test_summarize_hc_get(self):
        """Test case for summarize_hc_get

        Health check for all summarize services.  # noqa: E501
        """
        pass

    def test_summarize_supported_conversions_get(self):
        """Test case for summarize_supported_conversions_get

        """
        pass

    def test_summarize_text_post(self):
        """Test case for summarize_text_post

        Summarize text  # noqa: E501
        """
        pass

    def test_summarize_text_request_id_get(self):
        """Test case for summarize_text_request_id_get

        Return text summarizing status status.  Also return rewrote text if translation was successful  # noqa: E501
        """
        pass

    def test_summarize_text_trial_post(self):
        """Test case for summarize_text_trial_post

        Trial summarize text  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()