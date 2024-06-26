# Python SDK for GroupDocs.Rewriter Cloud

![](https://img.shields.io/badge/api-v2.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/groupdocs-rewriter-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/groupdocs-rewriter-cloud) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/groupdocs-rewriter-cloud) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/groupdocs-rewriter-cloud) [![GitHub license](https://img.shields.io/github/license/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-python)](https://github.com/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-python/blob/master/LICENSE)

[Product Page](https://products.groupdocs.cloud/rewriter/python/) | [Documentation](https://docs.groupdocs.cloud/rewriter/) | [Demos](https://products.groupdocs.app/rewriter/family) | [Swagger UI](https://reference.groupdocs.cloud/rewriter/) | [Examples](https://github.com/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-python) | [Blog](https://blog.groupdocs.cloud/category/rewriter/) | [Search](https://search.groupdocs.cloud/) | [Free Support](https://forum.groupdocs.cloud/c/rewriter) | [Free Trial](https://purchase.groupdocs.cloud/trial)

GroupDocs.Rewriter Cloud SDK for Python is a simple Python SDK that enables your cloud Apps to perform paraphrasing, simplification, summarization and paraphrasing detection of Microsoft Word®, OpenOffice, Markdown, HTML and Adobe Acrobat® PDF documents as well as plain text by adding just a few lines of code.

In other words, it's a SDK for document and plain text rewriting, summarization, etc. in our Cloud, that supports paraphrasing of .doc, .docx, .docm, .pdf, .rtf, .odt, .md, .html, .txt files. Just pass a specific file or text to the GroupDocs.Rewriter Cloud API, and it will process and save result in our Cloud or will return resulting text.

It is easy to get started with GroupDocs.Rewriter Cloud and there is nothing to install. Create an account at GroupDocs Cloud and get your application information, then you are ready to use SDKs.

## Cloud Features

- Paraphrasing / summarization / simplification / paraphrase detection of documents
- Paraphrasing / summarization / simplification / paraphrase detection / comparison of plain text
- Words and idioms synonyms finder
- Return resulting text in response
- Save processed file in cloud
- No need to install any 3rd party software

## Supported Document Formats

You can specify format of document to process putting in the request’s body:

- **Microsoft Word®:** DOC, DOCX, DOCM
- **Adobe®:** PDF
- **Markdown:** MD
- **HTML:** HTML
- **Other:** RTF, ODT, TXT

Additionally, user could obtain processed file in any other format available for conversion. Just specify output format of paraphrased document by putting file extension in the request’s body:

- **doc, docx** — docx, rtf, html, odt, txt, md, pdf, tiff, svg, xps
- **pdf** — docx, pptx, html, svg, xps
- **html** — md, pdf, docx, tiff, xps

Please visit [Supported Formats](https://docs.groupdocs.cloud/rewriter/supported-formats/) for details.

## Supported Languages

- **ar** — to process Arabic text or document
- **de** — to process German text or document
- **en** — to process English text or document
- **es** — to process Spanish text or document
- **fr** — to process French text or document
- **id** — to process Indonesian text or document
- **ru** — to process Russian text or document
- **uk** — to process Ukrainian text or document
- **sk** — to process Slovak text or document
- **pt** — to process Portuguese text or document
- **it** — to process Italian text or document

## JSON Request Details

To paraphrase plain text the following information should be put in the requests body:

- **language** — language of text (e.g. en)
- **text** — text to paraphrase (e.g. hello world)
- **diversityDegree** — diversity of paraphrasing, "medium" or "high", default is "off"
- **suggestions** — to receive several suggested variants of paraphrasing (from 1 to 3)

To suummarize plain text:

- **language** — language of text
- **text** — text to paraphrase
- **summarizationDegree** — degree of summarization, "off", "medium" or "high"

To simplify plain text:

- **language** — language of text
- **text** — text to paraphrase

To find synonyms:

- **language** — language of text
- **text** — word or phrase to find synonyms
- **synonyms** — number of synonyms to return



SDK also provides a tool for summarizing texts and documents in English. To do this, put the same parameters as for paraphrasing (except for "diversity" and "suggestions") in the requests body.

## How to use the SDK?

Our API is completely independent of your operating system, database system, or development language. You can use any language and platform that supports HTTP to interact with our API. However, manually writing client code can be difficult, error-prone, and time-consuming. Therefore, we provide and support [SDKs](https://github.com/groupdocs-rewriter-cloud) in many development languages to make it easier for your Cloud Apps to integrate with us.


## Quickstart

#### 1. Get Started

It is easy to get started with GroupDocs.Rewriter Cloud. Simply, create an account at [GroupDocs Cloud](https://dashboard.groupdocs.cloud/#/apps) and get your application information, then you are ready to use the [SDKs](https://github.com/groupdocs-rewriter-cloud).

#### 2. Run Demo
  * Checkout the SDK
  * Open .NET core demo project
  * Set Your ClientId & ClientSecret
  * Run


## Rewrite plain text

```python
import time
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.api.paraphrase_api import ParaphraseApi  
from groupdocs_rewriter_cloud.rest import ApiException
from groupdocs_rewriter_cloud.models import HttpStatusCode, ParaphraseTextRequest

api = ParaphraseApi()
file_api = FileApi()
api.api_client.configuration.client_id = "CLIENT_ID"
api.api_client.configuration.client_secret = "CLIENT_SECRET"
language = "en"
src_text = "YOUR_TEXT"
request = ParaphraseTextRequest(language=language, text=src_text)
status = api.paraphrase_text_post(request)
if status.status == groupdocs_rewriter_cloud.models.HttpStatusCode.ACCEPTED:
    while True:
        text_response = api.paraphrase_text_request_id_get(status.id)
        if text_response.status == groupdocs_rewriter_cloud.models.HttpStatusCode.OK:
            print(text_response.paraphrase_result)
            break
        time.sleep(2)
```

## GroupDocs.Rewriter Cloud SDKs in Popular Languages

| .NET | Python |
|---|---|
| [GitHub](https://github.com/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-dotnet) | [GitHub](https://github.com/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-dotnet) |
| [NuGet](https://www.nuget.org/packages/GroupDocs.Rewriter-Cloud/) | [PyPi](https://pypi.org/project/groupdocs-rewriter-cloud/) |

---

[Product Page](https://products.groupdocs.cloud/rewriter/python/) | [Docs](https://docs.groupdocs.cloud/rewriter/) | [Demos](https://products.groupdocs.app/rewriter/family) | [Swagger UI](https://apireference.groupdocs.cloud/rewriter/) | [Examples](https://github.com/groupdocs-rewriter-cloud/groupdocs-rewriter-cloud-python) | [Blog](https://blog.groupdocs.cloud/category/rewriter/) | [Search](https://search.groupdocs.cloud/) | [Free Support](https://forum.groupdocs.cloud/c/rewriter) | [Free Trial](https://purchase.groupdocs.cloud/trial)
