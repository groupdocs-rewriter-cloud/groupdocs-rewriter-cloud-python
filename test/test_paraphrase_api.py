# coding: utf-8

"""
    GroupDocs.Rewriter API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 23.11.1
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""
import time, os
import unittest

import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.api.paraphrase_api import ParaphraseApi  # noqa: E501
from groupdocs_rewriter_cloud.rest import ApiException
from groupdocs_rewriter_cloud.models import HttpStatusCode, FileSavingMode, ParaphraseFileRequest, ParaphraseSupportedFormats, SupportedConversionsFormats

class TestParaphraseApi(unittest.TestCase):
    """ParaphraseApi unit test stubs"""

    def get_file_result(self, request_id: str):
        while True:
            file_response = self.api.paraphrase_document_request_id_get(request_id)
            if file_response.status == groupdocs_rewriter_cloud.models.HttpStatusCode.OK:
                print(f'[{file_response.status}] {file_response.message}')
                break
            time.sleep(2)

    def setUp(self):
        self.api = groupdocs_rewriter_cloud.api.paraphrase_api.ParaphraseApi()  # noqa: E501
        self.file_api = groupdocs_rewriter_cloud.FileApi()
        self.api.api_client.configuration.client_id = os.getenv('GROUPDOCS_REWRITER_API_ID')
        self.api.api_client.configuration.client_secret = os.getenv('GROUPDOCS_REWRITER_API_SECRET')
        self.api.api_client.configuration.host = 'http://localhost:5000'
        self.api.api_client.configuration.auth_settings()
        self.pdf_url = self.file_api.file_upload_post(format='pdf', file='test_data/rewriter_test.pdf')
        self.docx_url = self.file_api.file_upload_post(format='docx', file='test_data/rewriter_test.docx')

    def test_paraphrase_document_post(self):
        request = groupdocs_rewriter_cloud.ParaphraseFileRequest(language='en', url=self.pdf_url, format=ParaphraseSupportedFormats.PDF, outputFormat=SupportedConversionsFormats.PDF)
        status = self.api.paraphrase_document_post(request)
        if status.status == groupdocs_rewriter_cloud.models.HttpStatusCode.ACCEPTED:
            print(f'Pdf document paraphrasing started: {status.id}')
            self.get_file_result(status.id)
        pass


if __name__ == '__main__':
    unittest.main()
