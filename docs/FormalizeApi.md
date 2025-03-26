# groupdocs_rewriter_cloud.FormalizeApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**formalize_document_post**](FormalizeApi.md#formalize_document_post) | **POST** /formalize/document | Formalize document
[**formalize_document_request_id_get**](FormalizeApi.md#formalize_document_request_id_get) | **GET** /formalize/document/{requestId} | Return document formalizinh status.  Also return URLs for downloading of formalized document if paraphrasing was successful
[**formalize_hc_get**](FormalizeApi.md#formalize_hc_get) | **GET** /formalize/hc | Health check for all simplify services.
[**formalize_ocr_post**](FormalizeApi.md#formalize_ocr_post) | **POST** /formalize/ocr | Formalize scanned image or document
[**formalize_supported_conversions_get**](FormalizeApi.md#formalize_supported_conversions_get) | **GET** /formalize/supportedConversions | 
[**formalize_text_post**](FormalizeApi.md#formalize_text_post) | **POST** /formalize/text | Formalize text
[**formalize_text_request_id_get**](FormalizeApi.md#formalize_text_request_id_get) | **GET** /formalize/text/{requestId} | Return text formalizing status.  Also return formalized text if paraphrasing was successful


# **formalize_document_post**
> StatusResponse formalize_document_post(formalize_file_request=formalize_file_request)

Formalize document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.formalize_file_request import FormalizeFileRequest
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
    api_instance = groupdocs_rewriter_cloud.FormalizeApi(api_client)
    formalize_file_request = groupdocs_rewriter_cloud.FormalizeFileRequest() # FormalizeFileRequest | String in body of request, containing JSON with parameters for formalizing. (optional)

    try:
        # Formalize document
        api_response = api_instance.formalize_document_post(formalize_file_request=formalize_file_request)
        print("The response of FormalizeApi->formalize_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormalizeApi->formalize_document_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **formalize_file_request** | [**FormalizeFileRequest**](FormalizeFileRequest.md)| String in body of request, containing JSON with parameters for formalizing. | [optional] 

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

# **formalize_document_request_id_get**
> FormalizeFileResponse formalize_document_request_id_get(request_id)

Return document formalizinh status.  Also return URLs for downloading of formalized document if paraphrasing was successful

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.formalize_file_response import FormalizeFileResponse
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
    api_instance = groupdocs_rewriter_cloud.FormalizeApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/rewriter/document response

    try:
        # Return document formalizinh status.  Also return URLs for downloading of formalized document if paraphrasing was successful
        api_response = api_instance.formalize_document_request_id_get(request_id)
        print("The response of FormalizeApi->formalize_document_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormalizeApi->formalize_document_request_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/rewriter/document response | 

### Return type

[**FormalizeFileResponse**](FormalizeFileResponse.md)

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

# **formalize_hc_get**
> HealthCheckResponse formalize_hc_get()

Health check for all simplify services.

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
    api_instance = groupdocs_rewriter_cloud.FormalizeApi(api_client)

    try:
        # Health check for all simplify services.
        api_response = api_instance.formalize_hc_get()
        print("The response of FormalizeApi->formalize_hc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormalizeApi->formalize_hc_get: %s\n" % e)
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

# **formalize_ocr_post**
> StatusResponse formalize_ocr_post(formalize_ocr_request=formalize_ocr_request)

Formalize scanned image or document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.formalize_ocr_request import FormalizeOcrRequest
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
    api_instance = groupdocs_rewriter_cloud.FormalizeApi(api_client)
    formalize_ocr_request = groupdocs_rewriter_cloud.FormalizeOcrRequest() # FormalizeOcrRequest | String in body of request, containing JSON with parameters for formalizing. (optional)

    try:
        # Formalize scanned image or document
        api_response = api_instance.formalize_ocr_post(formalize_ocr_request=formalize_ocr_request)
        print("The response of FormalizeApi->formalize_ocr_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormalizeApi->formalize_ocr_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **formalize_ocr_request** | [**FormalizeOcrRequest**](FormalizeOcrRequest.md)| String in body of request, containing JSON with parameters for formalizing. | [optional] 

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

# **formalize_supported_conversions_get**
> List[str] formalize_supported_conversions_get(format=format)



### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
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
    api_instance = groupdocs_rewriter_cloud.FormalizeApi(api_client)
    format = 'format_example' # str |  (optional)

    try:
        api_response = api_instance.formalize_supported_conversions_get(format=format)
        print("The response of FormalizeApi->formalize_supported_conversions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormalizeApi->formalize_supported_conversions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 

### Return type

**List[str]**

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

# **formalize_text_post**
> StatusResponse formalize_text_post(formalize_text_request=formalize_text_request)

Formalize text

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.formalize_text_request import FormalizeTextRequest
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
    api_instance = groupdocs_rewriter_cloud.FormalizeApi(api_client)
    formalize_text_request = groupdocs_rewriter_cloud.FormalizeTextRequest() # FormalizeTextRequest | String in body of request, containing JSON with parameters for formalizing. (optional)

    try:
        # Formalize text
        api_response = api_instance.formalize_text_post(formalize_text_request=formalize_text_request)
        print("The response of FormalizeApi->formalize_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormalizeApi->formalize_text_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **formalize_text_request** | [**FormalizeTextRequest**](FormalizeTextRequest.md)| String in body of request, containing JSON with parameters for formalizing. | [optional] 

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

# **formalize_text_request_id_get**
> FormalizeTextResponse formalize_text_request_id_get(request_id)

Return text formalizing status.  Also return formalized text if paraphrasing was successful

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.formalize_text_response import FormalizeTextResponse
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
    api_instance = groupdocs_rewriter_cloud.FormalizeApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/rewriter/text response

    try:
        # Return text formalizing status.  Also return formalized text if paraphrasing was successful
        api_response = api_instance.formalize_text_request_id_get(request_id)
        print("The response of FormalizeApi->formalize_text_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormalizeApi->formalize_text_request_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/rewriter/text response | 

### Return type

[**FormalizeTextResponse**](FormalizeTextResponse.md)

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

