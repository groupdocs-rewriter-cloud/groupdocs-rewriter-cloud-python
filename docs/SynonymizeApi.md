# groupdocs_rewriter_cloud.SynonymizeApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**synonymize_document_post**](SynonymizeApi.md#synonymize_document_post) | **POST** /synonymize/document | Synonyize document
[**synonymize_hc_get**](SynonymizeApi.md#synonymize_hc_get) | **GET** /synonymize/hc | Health check for all synonymizer services.
[**synonymize_ocr_post**](SynonymizeApi.md#synonymize_ocr_post) | **POST** /synonymize/ocr | Synonymize scanned image or document
[**synonymize_text_post**](SynonymizeApi.md#synonymize_text_post) | **POST** /synonymize/text | Synonymize word
[**synonymize_text_request_id_get**](SynonymizeApi.md#synonymize_text_request_id_get) | **GET** /synonymize/text/{requestId} | Return text synonymizing status.  Also return list of synonyms if it was successful
[**synonymize_text_trial_post**](SynonymizeApi.md#synonymize_text_trial_post) | **POST** /synonymize/text/trial | Trial synonymize word


# **synonymize_document_post**
> StatusResponse synonymize_document_post(synonymize_file_request=synonymize_file_request)

Synonyize document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.models.synonymize_file_request import SynonymizeFileRequest
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
    api_instance = groupdocs_rewriter_cloud.SynonymizeApi(api_client)
    synonymize_file_request = groupdocs_rewriter_cloud.SynonymizeFileRequest() # SynonymizeFileRequest | String in body of request, containing JSON with parameters for synonymizing. (optional)

    try:
        # Synonyize document
        api_response = api_instance.synonymize_document_post(synonymize_file_request=synonymize_file_request)
        print("The response of SynonymizeApi->synonymize_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SynonymizeApi->synonymize_document_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synonymize_file_request** | [**SynonymizeFileRequest**](SynonymizeFileRequest.md)| String in body of request, containing JSON with parameters for synonymizing. | [optional] 

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

# **synonymize_hc_get**
> HealthCheckResponse synonymize_hc_get()

Health check for all synonymizer services.

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
    api_instance = groupdocs_rewriter_cloud.SynonymizeApi(api_client)

    try:
        # Health check for all synonymizer services.
        api_response = api_instance.synonymize_hc_get()
        print("The response of SynonymizeApi->synonymize_hc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SynonymizeApi->synonymize_hc_get: %s\n" % e)
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

# **synonymize_ocr_post**
> StatusResponse synonymize_ocr_post(synonymize_ocr_request=synonymize_ocr_request)

Synonymize scanned image or document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.models.synonymize_ocr_request import SynonymizeOcrRequest
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
    api_instance = groupdocs_rewriter_cloud.SynonymizeApi(api_client)
    synonymize_ocr_request = groupdocs_rewriter_cloud.SynonymizeOcrRequest() # SynonymizeOcrRequest | String in body of request, containing JSON with parameters for synonymizing. (optional)

    try:
        # Synonymize scanned image or document
        api_response = api_instance.synonymize_ocr_post(synonymize_ocr_request=synonymize_ocr_request)
        print("The response of SynonymizeApi->synonymize_ocr_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SynonymizeApi->synonymize_ocr_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synonymize_ocr_request** | [**SynonymizeOcrRequest**](SynonymizeOcrRequest.md)| String in body of request, containing JSON with parameters for synonymizing. | [optional] 

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

# **synonymize_text_post**
> StatusResponse synonymize_text_post(synonymize_text_request=synonymize_text_request)

Synonymize word

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.models.synonymize_text_request import SynonymizeTextRequest
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
    api_instance = groupdocs_rewriter_cloud.SynonymizeApi(api_client)
    synonymize_text_request = groupdocs_rewriter_cloud.SynonymizeTextRequest() # SynonymizeTextRequest | String in body of request, containing JSON with parameters for synonymizing. (optional)

    try:
        # Synonymize word
        api_response = api_instance.synonymize_text_post(synonymize_text_request=synonymize_text_request)
        print("The response of SynonymizeApi->synonymize_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SynonymizeApi->synonymize_text_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synonymize_text_request** | [**SynonymizeTextRequest**](SynonymizeTextRequest.md)| String in body of request, containing JSON with parameters for synonymizing. | [optional] 

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

# **synonymize_text_request_id_get**
> SynonymizeTextResponse synonymize_text_request_id_get(request_id)

Return text synonymizing status.  Also return list of synonyms if it was successful

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.synonymize_text_response import SynonymizeTextResponse
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
    api_instance = groupdocs_rewriter_cloud.SynonymizeApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/rewriter/text response

    try:
        # Return text synonymizing status.  Also return list of synonyms if it was successful
        api_response = api_instance.synonymize_text_request_id_get(request_id)
        print("The response of SynonymizeApi->synonymize_text_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SynonymizeApi->synonymize_text_request_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/rewriter/text response | 

### Return type

[**SynonymizeTextResponse**](SynonymizeTextResponse.md)

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

# **synonymize_text_trial_post**
> StatusResponse synonymize_text_trial_post(synonymize_text_request=synonymize_text_request)

Trial synonymize word

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.models.synonymize_text_request import SynonymizeTextRequest
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
    api_instance = groupdocs_rewriter_cloud.SynonymizeApi(api_client)
    synonymize_text_request = groupdocs_rewriter_cloud.SynonymizeTextRequest() # SynonymizeTextRequest | String in body of request, containing JSON with parameters for synonymizing. Maximum 1000 characters (optional)

    try:
        # Trial synonymize word
        api_response = api_instance.synonymize_text_trial_post(synonymize_text_request=synonymize_text_request)
        print("The response of SynonymizeApi->synonymize_text_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SynonymizeApi->synonymize_text_trial_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synonymize_text_request** | [**SynonymizeTextRequest**](SynonymizeTextRequest.md)| String in body of request, containing JSON with parameters for synonymizing. Maximum 1000 characters | [optional] 

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

