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

import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.api.synonymize_api import SynonymizeApi  # noqa: E501
from groupdocs_rewriter_cloud.rest import ApiException


class TestSynonymizeApi(unittest.TestCase):
    """SynonymizeApi unit test stubs"""

    def setUp(self):
        self.api = groupdocs_rewriter_cloud.api.synonymize_api.SynonymizeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_synonymize_hc_get(self):
        """Test case for synonymize_hc_get

        Health check for all synonymizer services.  # noqa: E501
        """
        pass

    def test_synonymize_text_post(self):
        """Test case for synonymize_text_post

        Synonymize word  # noqa: E501
        """
        pass

    def test_synonymize_text_request_id_get(self):
        """Test case for synonymize_text_request_id_get

        Return text synonymizing status.  Also return list of synonyms if it was successful  # noqa: E501
        """
        pass

    def test_synonymize_text_trial_post(self):
        """Test case for synonymize_text_trial_post

        Trial synonymize word  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
