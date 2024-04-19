# coding: utf-8

"""
    GroupDocs.Rewriter API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 23.11.1
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest, os, time

import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.api.detect_api import DetectApi  # noqa: E501
from groupdocs_rewriter_cloud.api.file_api import FileApi
from groupdocs_rewriter_cloud.models.detection_file_request import DetectionSupportedFormats, DetectionFileRequest
from groupdocs_rewriter_cloud.rest import ApiException


class TestDetectApi(unittest.TestCase):
    """DetectApi unit test stubs"""

    def get_file_result(self, request_id: str):
        while True:
            file_response = self.api.detect_document_request_id_get(request_id)
            if file_response.status == groupdocs_rewriter_cloud.models.HttpStatusCode.OK:
                print(f'[{file_response.status}] {file_response.message}')
                break
            time.sleep(2)

    def setUp(self):
        self.api = DetectApi()  # noqa: E501
        self.file_api = FileApi()
        self.api.api_client.configuration.client_id = os.getenv('GROUPDOCS_REWRITER_API_ID')
        self.api.api_client.configuration.client_secret = os.getenv('GROUPDOCS_REWRITER_API_SECRET')

        self.pdf_url = self.file_api.file_upload_post(format='Pdf', file='test_data/rewriter_test.pdf')
        self.docx_url = self.file_api.file_upload_post(format='Docx', file='test_data/rewriter_test.docx')

    def test_detect_document_post(self):
        request = DetectionFileRequest(language='en', url=self.docx_url, format=DetectionSupportedFormats.PDF)
        status = self.api.detect_document_post(request)
        if status.status == groupdocs_rewriter_cloud.models.HttpStatusCode.ACCEPTED:
            print(f'Docx document detecting started: {status.id}')
            self.get_file_result(status.id)
        pass


if __name__ == '__main__':
    unittest.main()
