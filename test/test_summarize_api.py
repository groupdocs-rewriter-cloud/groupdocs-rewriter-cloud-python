import unittest, os, time

import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.api.summarize_api import SummarizeApi  # noqa: E501
from groupdocs_rewriter_cloud.api.file_api import FileApi
from groupdocs_rewriter_cloud.models import SummarizationSupportedFormats, SupportedConversionsFormats
from groupdocs_rewriter_cloud.rest import ApiException


class TestSimplifyApi(unittest.TestCase):
    """SimplifyApi unit test stubs"""

    def get_file_result(self, request_id: str):
        while True:
            file_response = self.api.summarize_document_request_id_get(request_id)
            if file_response.status == groupdocs_rewriter_cloud.models.HttpStatusCode.OK:
                print(f'[{file_response.status}] {file_response.message}')
                break
            time.sleep(2)
    def setUp(self):
        self.api = groupdocs_rewriter_cloud.api.summarize_api.SummarizeApi()  # noqa: E501
        self.file_api = FileApi()
        self.api.api_client.configuration.client_id = os.getenv('GROUPDOCS_REWRITER_API_ID')
        self.api.api_client.configuration.client_secret = os.getenv('GROUPDOCS_REWRITER_API_SECRET')

        self.pdf_url = self.file_api.file_upload_post(format='Pdf', file='test_data/rewriter_test.pdf')
        self.docx_url = self.file_api.file_upload_post(format='Docx', file='test_data/rewriter_test.docx')

    def test_simplify_document_post(self):
        request = groupdocs_rewriter_cloud.SummarizationFileRequest(language='en', url=self.pdf_url,
                                                                 format=SummarizationSupportedFormats.PDF,
                                                                 outputFormat=SupportedConversionsFormats.PDF)
        status = self.api.summarize_document_post(request)
        if status.status == groupdocs_rewriter_cloud.models.HttpStatusCode.ACCEPTED:
            print(f'Pdf document summarizing started: {status.id}')
            self.get_file_result(status.id)
        pass


if __name__ == '__main__':
    unittest.main()