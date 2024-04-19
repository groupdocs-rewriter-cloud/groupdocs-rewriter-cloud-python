# Python SDK for GroupDocs.Rewriter Cloud

![](https://img.shields.io/badge/api-v1.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/groupdocs-rewriter-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/groupdocs-rewriter-cloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/groupdocs-rewriter-cloud) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/groupdocs-rewriter-cloud) [![GitHub license](https://img.shields.io/github/license/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-python)](https://github.com/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-python/blob/master/LICENSE)

[Product Page](https://products.groupdocs.cloud/rewriter/python/) | [Documentation](https://docs.groupdocs.cloud/rewriter/) | [Demos](https://products.groupdocs.app/rewriter/family) | [Swagger UI](https://apireference.groupdocs.cloud/rewriter/) | [Examples](https://github.com/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-python) | [Blog](https://blog.groupdocs.cloud/category/rewriter/) | [Search](https://search.groupdocs.cloud/) | [Free Support](https://forum.groupdocs.cloud/c/rewriter) | [Free Trial](https://purchase.groupdocs.cloud/trial)

[GroupDocs.Rewriter Cloud](https://products.groupdocs.cloud/rewriter/) is an easy-to-use and versatile online service for rephrasing the content of Microsoft Word®, OpenOffice, Adobe Acrobat® PDF documents, Markdown and HTML files as well as a plain text with full preservation of their meaning. A powerful neural network reads and understands the text and then paraphrases it with different wording, producing a plagiarism-free result. While the background process is very complex and resource-intensive, you do not have to worry about formulas, machine learning, and load - our cloud services do all the work by providing you with a REST API to interact with them.

This software development kit (SDK) simplifies the interaction with GroupDocs.Rewriter Cloud API from Python code, allowing you to focus on the task at hand rather than the technical details. It handles all the routine operations such as establishing connection, sending API requests, and parsing responses, wrapping all these tasks into a few lines of code that are very easy to read and maintain even for inexperienced developers.

## Before you begin

GroupDocs.Rewriter Cloud is an on-demand service. As such, it has no specific hardware or operating system requirements. In order to use the service, you must create an account at GroupDocs Cloud API:

1. Go to https://dashboard.groupdocs.cloud/
2. If you are already registered with Aspose, sign in with your user name and password.  
   Otherwise, click Don’t have an account? Sign Up link and create a new account.
3. [Check out](https://docs.groupdocs.cloud/translation/subscription/) more information about available subscription plans and a free tier limits.

GroupDocs values your privacy and takes technical, security and organizational measures to protect your data from unauthorized use, accidental loss or disclosure. Read our [Privacy Policy](https://about.groupdocs.cloud/legal/privacy-policy/) and [Terms of Service](https://about.groupdocs.cloud/legal/tos/) for details.

## How it works

Provide the file in one of the supported formats or a plain text. GroupDocs.Rewriter Cloud API will rephrase it and save the rewritten file to our cloud, or just return the paraphrased text.

## Supported formats

GroupDocs.Rewriter Cloud can rephrase documents in the most popular formats.

Document | Extensions | Description
-------- | ---------- | -----------
Microsoft Word | .DOCX<br />.DOCM<br />.DOC<br />.RTF | Microsoft Word 97-2021 and Microsoft 365 Word documents, including macro-enabled documents.
Portable Document Format | .PDF | An open standard cross-platform format for documents that include formatted text, images, multimedia elements, and more.
OpenDocument Text | .ODT | Documents created with a number of open source word processing applications, such as Writer from Apache OpenOffice and LibreOffice.
Markdown | .MD | Files created using one of dialects of the Markdown language.
HTML | .HTML | Files containing Hypertext Markup Language (HTML) that formats the structure of a webpage. 
Plain text | .TXT | Plain text files or text in the form of lines.

In addition to rephrasing, GroupDocs.Rewriter Cloud can save the resulting document in various file formats other than the original, with formatting preserved (where applicable).

Source file format | Paraphrased file format
------------------ | ----------------------
.DOCX              | .DOCX<br />.RTF<br />.HTML<br />.ODT<br />.TXT<br />.MD<br />.PDF<br />.TIFF<br />.SVG<br />.XPS
.DOC               | .DOC<br />.DOCX<br />.RTF<br />.HTML<br />.ODT<br />.TXT<br />.MD<br />.PDF<br />.TIFF<br />.SVG<br />.XPS
.ODT               | .DOCX<br />.RTF<br />.HTML<br />.ODT<br />.TXT<br />.MD<br />.PDF<br />.TIFF<br />.SVG<br />.XPS
.RTF               | .DOCX<br />.RTF<br />.HTML<br />.ODT<br />.TXT<br />.MD<br />.PDF<br />.TIFF<br />.SVG<br />.XPS
.PDF               | .PDF<br />.DOCX<br />.PPTX<br />.HTML<br />.XPS<br />.SVG
.MD                | .MD<br />
.HTML              | .HTML<br />.PDF<br />.DOCX<br />.TIFF<br />.XPS<br />

## Supported languages

- **ar** — to paraphrase Arabic text or document
- **de** — to paraphrase German text or document
- **en** — to paraphrase English text or document
- **es** — to paraphrase Spanish text or document
- **fr** — to paraphrase French text or document
- **id** — to paraphrase Indonesian text or document
- **ru** — to paraphrase Russian text or document
- **uk** — to paraphrase Ukrainian text or document

## Quick start

To start using GroupDocs.Rewriter Cloud in your Python applications, follow a few simple steps:

## System requirements

Supported versions of Python:

>= 3.7

See [requirements.txt](requirements.txt) for the list of dependencies.

## Getting an access token

The GroupDocs.Rewriter Cloud API is fully compliant with industry security standards and best practices. Data transfer is carried out using JWT authentication, which eliminates all possibilities of data theft or disclosure.

To obtain a JWT token, get the _Client ID_ and _Client Secret_ credentials:

1. Sign in to [GroupDocs Cloud API Dashboard](https://dashboard.groupdocs.cloud/).
2. Go to [**Applications**](https://dashboard.groupdocs.cloud/applications) page.
3. Create the `samples` storage for exchanging files by clicking the _plus_ icon and following the required steps.
4. Provide the application name.
5. Click **Save** button.
6. Click the newly created application and copy the values from **Client Id** and **Client Secret** fields. These credentials can be used to access all GroupDocs Cloud services.

Now request an access token with the following API call:

```bash
curl --location --request POST 'https://api.groupdocs.cloud/connect/token' \
     --header 'Content-Type: application/x-www-form-urlencoded' \
     --data-urlencode 'grant_type=client_credentials' \
     --data-urlencode 'client_id=CLIENT-ID-VALUE' \
     --data-urlencode 'client_secret=CLIENT-SECRET-VALUE'
```

You should get a response that looks something like this:

```json
{
	"access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...Iwr6g2zbFwf1nLtg",
	"expires_in": 3600,
	"token_type": "Bearer"
}
```
The access token will be valid for the number of seconds specified in the `expires_in` property. If it has expired, request a new one using the same credentials.

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-python.git`)

or

```sh
pip install groupdocs-rewriter-cloud
```

Then import the package:
```python
import groupdocs_rewriter_cloud
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import groupdocs_rewriter_cloud
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)



# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_file_request = groupdocs_rewriter_cloud.DetectionFileRequest() # DetectionFileRequest | String in body of request, containing JSON with parameters for detecting. (optional)

    try:
        # Detect paraphrasing in the document
        api_response = api_instance.detect_document_post(detection_file_request=detection_file_request)
        print("The response of DetectApi->detect_document_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DetectApi->detect_document_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DetectApi* | [**detect_document_post**](docs\DetectApi.md#detect_document_post) | **POST** /detect/document | Detect paraphrasing in the document
*DetectApi* | [**detect_document_request_id_get**](docs\DetectApi.md#detect_document_request_id_get) | **GET** /detect/document/{requestId} | Return document detection status.  Also return probability of paraphrasing for the whole document and per paragraph
*DetectApi* | [**detect_document_trial_post**](docs\DetectApi.md#detect_document_trial_post) | **POST** /detect/document/trial | Trial detect paraphrasing in the document
*DetectApi* | [**detect_hc_get**](docs\DetectApi.md#detect_hc_get) | **GET** /detect/hc | Health check for detect all services.
*DetectApi* | [**detect_text_post**](docs\DetectApi.md#detect_text_post) | **POST** /detect/text | Detect paraphrasing in text
*DetectApi* | [**detect_text_request_id_get**](docs\DetectApi.md#detect_text_request_id_get) | **GET** /detect/text/{requestId} | Return text detection status.  Also return probability of paraphrasing for the whole text
*DetectApi* | [**detect_text_trial_post**](docs\DetectApi.md#detect_text_trial_post) | **POST** /detect/text/trial | Trial detect paraphrasing in text
*FileApi* | [**file_upload_post**](docs\FileApi.md#file_upload_post) | **POST** /file/upload | 
*InfoApi* | [**info_available_languages_get**](docs\InfoApi.md#info_available_languages_get) | **GET** /info/availableLanguages | 
*ParaphraseApi* | [**paraphrase_document_post**](docs\ParaphraseApi.md#paraphrase_document_post) | **POST** /paraphrase/document | Paraphrase document
*ParaphraseApi* | [**paraphrase_document_request_id_get**](docs\ParaphraseApi.md#paraphrase_document_request_id_get) | **GET** /paraphrase/document/{requestId} | Return document rewriting status.  Also return URLs for downloading of rewritten document if paraphrasig was successful
*ParaphraseApi* | [**paraphrase_document_trial_post**](docs\ParaphraseApi.md#paraphrase_document_trial_post) | **POST** /paraphrase/document/trial | Trial paraphrase document
*ParaphraseApi* | [**paraphrase_hc_get**](docs\ParaphraseApi.md#paraphrase_hc_get) | **GET** /paraphrase/hc | Health check for all paraphrase services.
*ParaphraseApi* | [**paraphrase_supported_conversions_get**](docs\ParaphraseApi.md#paraphrase_supported_conversions_get) | **GET** /paraphrase/supportedConversions | 
*ParaphraseApi* | [**paraphrase_text_post**](docs\ParaphraseApi.md#paraphrase_text_post) | **POST** /paraphrase/text | Rewrite text
*ParaphraseApi* | [**paraphrase_text_request_id_get**](docs\ParaphraseApi.md#paraphrase_text_request_id_get) | **GET** /paraphrase/text/{requestId} | Return text rewriting status.  Also return rewritten text if paraphrasing was successful
*ParaphraseApi* | [**paraphrase_text_trial_post**](docs\ParaphraseApi.md#paraphrase_text_trial_post) | **POST** /paraphrase/text/trial | Trial rewrite text
*SimplifyApi* | [**simplify_document_post**](docs\SimplifyApi.md#simplify_document_post) | **POST** /simplify/document | Simplify document
*SimplifyApi* | [**simplify_document_request_id_get**](docs\SimplifyApi.md#simplify_document_request_id_get) | **GET** /simplify/document/{requestId} | Return document simplifying status.  Also return URLs for downloading of simplified document if paraphrasig was successful
*SimplifyApi* | [**simplify_document_trial_post**](docs\SimplifyApi.md#simplify_document_trial_post) | **POST** /simplify/document/trial | Trial simplify document
*SimplifyApi* | [**simplify_hc_get**](docs\SimplifyApi.md#simplify_hc_get) | **GET** /simplify/hc | Health check for all simplify services.
*SimplifyApi* | [**simplify_supported_conversions_get**](docs\SimplifyApi.md#simplify_supported_conversions_get) | **GET** /simplify/supportedConversions | 
*SimplifyApi* | [**simplify_text_post**](docs\SimplifyApi.md#simplify_text_post) | **POST** /simplify/text | Simplify text
*SimplifyApi* | [**simplify_text_request_id_get**](docs\SimplifyApi.md#simplify_text_request_id_get) | **GET** /simplify/text/{requestId} | Return text simplifying status.  Also return simplified text if paraphrasing was successful
*SimplifyApi* | [**simplify_text_trial_post**](docs\SimplifyApi.md#simplify_text_trial_post) | **POST** /simplify/text/trial | Trial simplify text
*SummarizeApi* | [**summarize_document_post**](docs\SummarizeApi.md#summarize_document_post) | **POST** /summarize/document | Summarize document
*SummarizeApi* | [**summarize_document_request_id_get**](docs\SummarizeApi.md#summarize_document_request_id_get) | **GET** /summarize/document/{requestId} | Return document summarizing status.  Also return URLs for downloading of summarized document if summarization was successful
*SummarizeApi* | [**summarize_document_trial_post**](docs\SummarizeApi.md#summarize_document_trial_post) | **POST** /summarize/document/trial | Trial summarize document
*SummarizeApi* | [**summarize_hc_get**](docs\SummarizeApi.md#summarize_hc_get) | **GET** /summarize/hc | Health check for all summarize services.
*SummarizeApi* | [**summarize_supported_conversions_get**](docs\SummarizeApi.md#summarize_supported_conversions_get) | **GET** /summarize/supportedConversions | 
*SummarizeApi* | [**summarize_text_post**](docs\SummarizeApi.md#summarize_text_post) | **POST** /summarize/text | Summarize text
*SummarizeApi* | [**summarize_text_request_id_get**](docs\SummarizeApi.md#summarize_text_request_id_get) | **GET** /summarize/text/{requestId} | Return text summarizing status status.  Also return rewrote text if translation was successful
*SummarizeApi* | [**summarize_text_trial_post**](docs\SummarizeApi.md#summarize_text_trial_post) | **POST** /summarize/text/trial | Trial summarize text
*SwaggerApi* | [**swagger_spec_get**](docs\SwaggerApi.md#swagger_spec_get) | **GET** /swagger/spec | 
*SynonymizeApi* | [**synonymize_hc_get**](docs\SynonymizeApi.md#synonymize_hc_get) | **GET** /synonymize/hc | Health check for all synonymizer services.
*SynonymizeApi* | [**synonymize_text_post**](docs\SynonymizeApi.md#synonymize_text_post) | **POST** /synonymize/text | Synonymize word
*SynonymizeApi* | [**synonymize_text_request_id_get**](docs\SynonymizeApi.md#synonymize_text_request_id_get) | **GET** /synonymize/text/{requestId} | Return text synonymizing status.  Also return list of synonyms if it was successful
*SynonymizeApi* | [**synonymize_text_trial_post**](docs\SynonymizeApi.md#synonymize_text_trial_post) | **POST** /synonymize/text/trial | Trial synonymize word


## Documentation For Models

 - [BaseTextRequest](docs\BaseTextRequest.md)
 - [CloudTextRequest](docs\CloudTextRequest.md)
 - [DegreeEnum](docs\DegreeEnum.md)
 - [DetectionFileRequest](docs\DetectionFileRequest.md)
 - [DetectionFileResponse](docs\DetectionFileResponse.md)
 - [DetectionSupportedFormats](docs\DetectionSupportedFormats.md)
 - [DetectionTextRequest](docs\DetectionTextRequest.md)
 - [DetectionTextResponse](docs\DetectionTextResponse.md)
 - [DetectionTrialFileRequest](docs\DetectionTrialFileRequest.md)
 - [FileSavingMode](docs\FileSavingMode.md)
 - [HealthCheckInfo](docs\HealthCheckInfo.md)
 - [HealthCheckResponse](docs\HealthCheckResponse.md)
 - [HttpStatusCode](docs\HttpStatusCode.md)
 - [LanguageInfo](docs\LanguageInfo.md)
 - [Model](docs\Model.md)
 - [Opt](docs\Opt.md)
 - [ParaphraseFileRequest](docs\ParaphraseFileRequest.md)
 - [ParaphraseFileResponse](docs\ParaphraseFileResponse.md)
 - [ParaphraseSupportedFormats](docs\ParaphraseSupportedFormats.md)
 - [ParaphraseTextRequest](docs\ParaphraseTextRequest.md)
 - [ParaphraseTextResponse](docs\ParaphraseTextResponse.md)
 - [ParaphraseTrialFileRequest](docs\ParaphraseTrialFileRequest.md)
 - [SimplifyFileRequest](docs\SimplifyFileRequest.md)
 - [SimplifyFileResponse](docs\SimplifyFileResponse.md)
 - [SimplifySupportedFromats](docs\SimplifySupportedFromats.md)
 - [SimplifyTextResponse](docs\SimplifyTextResponse.md)
 - [SimplifyTrialFileRequest](docs\SimplifyTrialFileRequest.md)
 - [StatusResponse](docs\StatusResponse.md)
 - [SummarizationFileRequest](docs\SummarizationFileRequest.md)
 - [SummarizationFileResponse](docs\SummarizationFileResponse.md)
 - [SummarizationSupportedFormats](docs\SummarizationSupportedFormats.md)
 - [SummarizationTextRequest](docs\SummarizationTextRequest.md)
 - [SummarizationTextResponse](docs\SummarizationTextResponse.md)
 - [SummarizationTrialFileRequest](docs\SummarizationTrialFileRequest.md)
 - [SupportedConversionsFormats](docs\SupportedConversionsFormats.md)
 - [SynonymizeTextRequest](docs\SynonymizeTextRequest.md)
 - [SynonymizeTextResponse](docs\SynonymizeTextResponse.md)
 - [Tokenizer](docs\Tokenizer.md)
 - [TrialSupportedFormats](docs\TrialSupportedFormats.md)


## Other SDKs for GroupDocs.Rewriter Cloud

GroupDocs also offers native SDK packages for other popular programming languages:

### .NET

- [NuGet](https://www.nuget.org/packages/GroupDocs.Rewriter-Cloud/)
- [GitHub](https://github.com/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-dotnet)

---

[Product Page](https://products.groupdocs.cloud/rewriter/dotnet/) | [Docs](https://docs.groupdocs.cloud/rewriter/) | [Demos](https://products.groupdocs.app/rewriter/family) | [Swagger UI](https://apireference.groupdocs.cloud/rewriter/) | [Examples](https://github.com/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-dotnet) | [Blog](https://blog.groupdocs.cloud/category/rewriter/) | [Search](https://search.groupdocs.cloud/) | [Free Support](https://forum.groupdocs.cloud/c/rewriter) | [Free Trial](https://purchase.groupdocs.cloud/trial)
