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
from groupdocs_rewriter_cloud.models.opt import Opt  # noqa: E501
from groupdocs_rewriter_cloud.rest import ApiException

class TestOpt(unittest.TestCase):
    """Opt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Opt
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Opt`
        """
        model = groupdocs_rewriter_cloud.models.opt.Opt()  # noqa: E501
        if include_optional :
            return Opt(
                beam_size = 56, 
                gpu = 56, 
                replace_unk = True
            )
        else :
            return Opt(
        )
        """

    def testOpt(self):
        """Test Opt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()