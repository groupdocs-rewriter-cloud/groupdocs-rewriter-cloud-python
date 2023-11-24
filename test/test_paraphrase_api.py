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
from groupdocs_rewriter_cloud.api.paraphrase_api import ParaphraseApi  # noqa: E501
from groupdocs_rewriter_cloud.rest import ApiException


class TestParaphraseApi(unittest.TestCase):
    """ParaphraseApi unit test stubs"""

    def setUp(self):
        self.api = groupdocs_rewriter_cloud.api.paraphrase_api.ParaphraseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_paraphrase_document_post(self):
        """Test case for paraphrase_document_post

        Paraphrase document  # noqa: E501
        """
        pass

    def test_paraphrase_document_request_id_get(self):
        """Test case for paraphrase_document_request_id_get

        Return document rewriting status.  Also return URLs for downloading of rewritten document if paraphrasig was successful  # noqa: E501
        """
        pass

    def test_paraphrase_document_trial_post(self):
        """Test case for paraphrase_document_trial_post

        Trial paraphrase document  # noqa: E501
        """
        pass

    def test_paraphrase_hc_get(self):
        """Test case for paraphrase_hc_get

        Health check for all paraphrase services.  # noqa: E501
        """
        pass

    def test_paraphrase_supported_conversions_get(self):
        """Test case for paraphrase_supported_conversions_get

        """
        pass

    def test_paraphrase_text_post(self):
        """Test case for paraphrase_text_post

        Rewrite text  # noqa: E501
        """
        pass

    def test_paraphrase_text_request_id_get(self):
        """Test case for paraphrase_text_request_id_get

        Return text rewriting status.  Also return rewritten text if paraphrasing was successful  # noqa: E501
        """
        pass

    def test_paraphrase_text_trial_post(self):
        """Test case for paraphrase_text_trial_post

        Trial rewrite text  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
