# groupdocs_rewriter_cloud.DetectApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**detect_document_post**](DetectApi.md#detect_document_post) | **POST** /detect/document | Obsolete. Will be removed in the next version, use /detect/paraphrase/document/ instead this.
[**detect_document_request_id_get**](DetectApi.md#detect_document_request_id_get) | **GET** /detect/document/{requestId} | Return document detection status.  Also return probability of paraphrasing for the whole document and per paragraph
[**detect_document_trial_post**](DetectApi.md#detect_document_trial_post) | **POST** /detect/document/trial | Trial detect paraphrasing in the document
[**detect_hc_get**](DetectApi.md#detect_hc_get) | **GET** /detect/hc | Health check for detect all services.
[**detect_ocr_ai_generation_post**](DetectApi.md#detect_ocr_ai_generation_post) | **POST** /detect/ocr-ai-generation | Detect ai generation content in the image or scanned document
[**detect_ocr_post**](DetectApi.md#detect_ocr_post) | **POST** /detect/ocr | Obsolete. Will be removed in the next version, use /detect/paraphrase/ocr instead this.
[**detect_paraphrase_document_post**](DetectApi.md#detect_paraphrase_document_post) | **POST** /detect/paraphrase/document | Detect paraphrasing in the document
[**detect_paraphrase_ocr_post**](DetectApi.md#detect_paraphrase_ocr_post) | **POST** /detect/paraphrase/ocr | Detect paraphrasing in the image or scanned document
[**detect_paraphrase_text_post**](DetectApi.md#detect_paraphrase_text_post) | **POST** /detect/paraphrase/text | Detect paraphrasing in text
[**detect_summarization_document_post**](DetectApi.md#detect_summarization_document_post) | **POST** /detect/summarization/document | Detect summarization in the document
[**detect_summarization_ocr_post**](DetectApi.md#detect_summarization_ocr_post) | **POST** /detect/summarization/ocr | Detect summarization in the image or scanned document
[**detect_summarization_text_post**](DetectApi.md#detect_summarization_text_post) | **POST** /detect/summarization/text | Detect summarization in text
[**detect_text_ai_generation_post**](DetectApi.md#detect_text_ai_generation_post) | **POST** /detect/text/ai-generation | Detect ai generated text
[**detect_text_post**](DetectApi.md#detect_text_post) | **POST** /detect/text | Obsolete. Will be removed in the next version, use /detect/paraphrase/text instead this.
[**detect_text_request_id_get**](DetectApi.md#detect_text_request_id_get) | **GET** /detect/text/{requestId} | Return text detection status.  Also return probability of paraphrasing for the whole text
[**detect_text_trial_post**](DetectApi.md#detect_text_trial_post) | **POST** /detect/text/trial | Trial detect paraphrasing in text


# **detect_document_post**
> StatusResponse detect_document_post(detection_file_request=detection_file_request)

Obsolete. Will be removed in the next version, use /detect/paraphrase/document/ instead this.

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_file_request import DetectionFileRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_file_request = groupdocs_rewriter_cloud.DetectionFileRequest() # DetectionFileRequest |  (optional)

    try:
        # Obsolete. Will be removed in the next version, use /detect/paraphrase/document/ instead this.
        api_response = api_instance.detect_document_post(detection_file_request=detection_file_request)
        print("The response of DetectApi->detect_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_document_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_file_request** | [**DetectionFileRequest**](DetectionFileRequest.md)|  | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_document_request_id_get**
> DetectionFileResponse detect_document_request_id_get(request_id)

Return document detection status.  Also return probability of paraphrasing for the whole document and per paragraph

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_file_response import DetectionFileResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/rewriter/document response

    try:
        # Return document detection status.  Also return probability of paraphrasing for the whole document and per paragraph
        api_response = api_instance.detect_document_request_id_get(request_id)
        print("The response of DetectApi->detect_document_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_document_request_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/rewriter/document response | 

### Return type

[**DetectionFileResponse**](DetectionFileResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_document_trial_post**
> StatusResponse detect_document_trial_post(detection_trial_file_request=detection_trial_file_request)

Trial detect paraphrasing in the document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_trial_file_request import DetectionTrialFileRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_trial_file_request = groupdocs_rewriter_cloud.DetectionTrialFileRequest() # DetectionTrialFileRequest | String in body of request, containing JSON with parameters for detecting. (optional)

    try:
        # Trial detect paraphrasing in the document
        api_response = api_instance.detect_document_trial_post(detection_trial_file_request=detection_trial_file_request)
        print("The response of DetectApi->detect_document_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_document_trial_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_trial_file_request** | [**DetectionTrialFileRequest**](DetectionTrialFileRequest.md)| String in body of request, containing JSON with parameters for detecting. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_hc_get**
> HealthCheckResponse detect_hc_get()

Health check for detect all services.

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.health_check_response import HealthCheckResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)

    try:
        # Health check for detect all services.
        api_response = api_instance.detect_hc_get()
        print("The response of DetectApi->detect_hc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_hc_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthCheckResponse**](HealthCheckResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_ocr_ai_generation_post**
> StatusResponse detect_ocr_ai_generation_post(detection_ocr_request=detection_ocr_request)

Detect ai generation content in the image or scanned document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_ocr_request import DetectionOcrRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_ocr_request = groupdocs_rewriter_cloud.DetectionOcrRequest() # DetectionOcrRequest | String in body of request, containing JSON with parameters for detecting. (optional)

    try:
        # Detect ai generation content in the image or scanned document
        api_response = api_instance.detect_ocr_ai_generation_post(detection_ocr_request=detection_ocr_request)
        print("The response of DetectApi->detect_ocr_ai_generation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_ocr_ai_generation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_ocr_request** | [**DetectionOcrRequest**](DetectionOcrRequest.md)| String in body of request, containing JSON with parameters for detecting. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_ocr_post**
> StatusResponse detect_ocr_post(detection_ocr_request=detection_ocr_request)

Obsolete. Will be removed in the next version, use /detect/paraphrase/ocr instead this.

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_ocr_request import DetectionOcrRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_ocr_request = groupdocs_rewriter_cloud.DetectionOcrRequest() # DetectionOcrRequest |  (optional)

    try:
        # Obsolete. Will be removed in the next version, use /detect/paraphrase/ocr instead this.
        api_response = api_instance.detect_ocr_post(detection_ocr_request=detection_ocr_request)
        print("The response of DetectApi->detect_ocr_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_ocr_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_ocr_request** | [**DetectionOcrRequest**](DetectionOcrRequest.md)|  | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_paraphrase_document_post**
> StatusResponse detect_paraphrase_document_post(detection_file_request=detection_file_request)

Detect paraphrasing in the document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_file_request import DetectionFileRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_file_request = groupdocs_rewriter_cloud.DetectionFileRequest() # DetectionFileRequest | String in body of request, containing JSON with parameters for detecting. (optional)

    try:
        # Detect paraphrasing in the document
        api_response = api_instance.detect_paraphrase_document_post(detection_file_request=detection_file_request)
        print("The response of DetectApi->detect_paraphrase_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_paraphrase_document_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_file_request** | [**DetectionFileRequest**](DetectionFileRequest.md)| String in body of request, containing JSON with parameters for detecting. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_paraphrase_ocr_post**
> StatusResponse detect_paraphrase_ocr_post(detection_ocr_request=detection_ocr_request)

Detect paraphrasing in the image or scanned document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_ocr_request import DetectionOcrRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_ocr_request = groupdocs_rewriter_cloud.DetectionOcrRequest() # DetectionOcrRequest | String in body of request, containing JSON with parameters for detecting. (optional)

    try:
        # Detect paraphrasing in the image or scanned document
        api_response = api_instance.detect_paraphrase_ocr_post(detection_ocr_request=detection_ocr_request)
        print("The response of DetectApi->detect_paraphrase_ocr_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_paraphrase_ocr_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_ocr_request** | [**DetectionOcrRequest**](DetectionOcrRequest.md)| String in body of request, containing JSON with parameters for detecting. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_paraphrase_text_post**
> StatusResponse detect_paraphrase_text_post(detection_text_request=detection_text_request)

Detect paraphrasing in text

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_text_request import DetectionTextRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_text_request = groupdocs_rewriter_cloud.DetectionTextRequest() # DetectionTextRequest | String in body of request, containing JSON with parameters for detection. (optional)

    try:
        # Detect paraphrasing in text
        api_response = api_instance.detect_paraphrase_text_post(detection_text_request=detection_text_request)
        print("The response of DetectApi->detect_paraphrase_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_paraphrase_text_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_text_request** | [**DetectionTextRequest**](DetectionTextRequest.md)| String in body of request, containing JSON with parameters for detection. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_summarization_document_post**
> StatusResponse detect_summarization_document_post(detection_file_request=detection_file_request)

Detect summarization in the document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_file_request import DetectionFileRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_file_request = groupdocs_rewriter_cloud.DetectionFileRequest() # DetectionFileRequest | String in body of request, containing JSON with parameters for detecting. (optional)

    try:
        # Detect summarization in the document
        api_response = api_instance.detect_summarization_document_post(detection_file_request=detection_file_request)
        print("The response of DetectApi->detect_summarization_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_summarization_document_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_file_request** | [**DetectionFileRequest**](DetectionFileRequest.md)| String in body of request, containing JSON with parameters for detecting. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_summarization_ocr_post**
> StatusResponse detect_summarization_ocr_post(detection_ocr_request=detection_ocr_request)

Detect summarization in the image or scanned document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_ocr_request import DetectionOcrRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_ocr_request = groupdocs_rewriter_cloud.DetectionOcrRequest() # DetectionOcrRequest | String in body of request, containing JSON with parameters for detecting. (optional)

    try:
        # Detect summarization in the image or scanned document
        api_response = api_instance.detect_summarization_ocr_post(detection_ocr_request=detection_ocr_request)
        print("The response of DetectApi->detect_summarization_ocr_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_summarization_ocr_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_ocr_request** | [**DetectionOcrRequest**](DetectionOcrRequest.md)| String in body of request, containing JSON with parameters for detecting. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_summarization_text_post**
> StatusResponse detect_summarization_text_post(detection_text_request=detection_text_request)

Detect summarization in text

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_text_request import DetectionTextRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_text_request = groupdocs_rewriter_cloud.DetectionTextRequest() # DetectionTextRequest | String in body of request, containing JSON with parameters for detection. (optional)

    try:
        # Detect summarization in text
        api_response = api_instance.detect_summarization_text_post(detection_text_request=detection_text_request)
        print("The response of DetectApi->detect_summarization_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_summarization_text_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_text_request** | [**DetectionTextRequest**](DetectionTextRequest.md)| String in body of request, containing JSON with parameters for detection. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_text_ai_generation_post**
> StatusResponse detect_text_ai_generation_post(detection_text_request=detection_text_request)

Detect ai generated text

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_text_request import DetectionTextRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_text_request = groupdocs_rewriter_cloud.DetectionTextRequest() # DetectionTextRequest | String in body of request, containing JSON with parameters for detection. (optional)

    try:
        # Detect ai generated text
        api_response = api_instance.detect_text_ai_generation_post(detection_text_request=detection_text_request)
        print("The response of DetectApi->detect_text_ai_generation_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_text_ai_generation_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_text_request** | [**DetectionTextRequest**](DetectionTextRequest.md)| String in body of request, containing JSON with parameters for detection. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_text_post**
> StatusResponse detect_text_post(detection_text_request=detection_text_request)

Obsolete. Will be removed in the next version, use /detect/paraphrase/text instead this.

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_text_request import DetectionTextRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_text_request = groupdocs_rewriter_cloud.DetectionTextRequest() # DetectionTextRequest | String in body of request, containing JSON with parameters for detection. (optional)

    try:
        # Obsolete. Will be removed in the next version, use /detect/paraphrase/text instead this.
        api_response = api_instance.detect_text_post(detection_text_request=detection_text_request)
        print("The response of DetectApi->detect_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_text_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_text_request** | [**DetectionTextRequest**](DetectionTextRequest.md)| String in body of request, containing JSON with parameters for detection. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_text_request_id_get**
> DetectionTextResponse detect_text_request_id_get(request_id)

Return text detection status.  Also return probability of paraphrasing for the whole text

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_text_response import DetectionTextResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/rewriter/document response

    try:
        # Return text detection status.  Also return probability of paraphrasing for the whole text
        api_response = api_instance.detect_text_request_id_get(request_id)
        print("The response of DetectApi->detect_text_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_text_request_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/rewriter/document response | 

### Return type

[**DetectionTextResponse**](DetectionTextResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detect_text_trial_post**
> StatusResponse detect_text_trial_post(detection_text_request=detection_text_request)

Trial detect paraphrasing in text

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.detection_text_request import DetectionTextRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.groupdocs.cloud/v2.0/rewriter
# See configuration.py for a list of all supported configuration parameters.
configuration = groupdocs_rewriter_cloud.Configuration(
    host = "https://api.groupdocs.cloud/v2.0/rewriter"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with groupdocs_rewriter_cloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = groupdocs_rewriter_cloud.DetectApi(api_client)
    detection_text_request = groupdocs_rewriter_cloud.DetectionTextRequest() # DetectionTextRequest | String in body of request, containing JSON with parameters for detection. Maximum 1000 characters (optional)

    try:
        # Trial detect paraphrasing in text
        api_response = api_instance.detect_text_trial_post(detection_text_request=detection_text_request)
        print("The response of DetectApi->detect_text_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DetectApi->detect_text_trial_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_text_request** | [**DetectionTextRequest**](DetectionTextRequest.md)| String in body of request, containing JSON with parameters for detection. Maximum 1000 characters | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

