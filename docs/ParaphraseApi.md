# groupdocs_rewriter_cloud.ParaphraseApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paraphrase_document_post**](ParaphraseApi.md#paraphrase_document_post) | **POST** /paraphrase/document | Paraphrase document
[**paraphrase_document_request_id_get**](ParaphraseApi.md#paraphrase_document_request_id_get) | **GET** /paraphrase/document/{requestId} | Return document rewriting status.  Also return URLs for downloading of rewritten document if paraphrasig was successful
[**paraphrase_document_trial_post**](ParaphraseApi.md#paraphrase_document_trial_post) | **POST** /paraphrase/document/trial | Trial paraphrase document
[**paraphrase_hc_get**](ParaphraseApi.md#paraphrase_hc_get) | **GET** /paraphrase/hc | Health check for all paraphrase services.
[**paraphrase_ocr_post**](ParaphraseApi.md#paraphrase_ocr_post) | **POST** /paraphrase/ocr | Rewrite scanned image or PDF
[**paraphrase_supported_conversions_get**](ParaphraseApi.md#paraphrase_supported_conversions_get) | **GET** /paraphrase/supportedConversions | 
[**paraphrase_text_post**](ParaphraseApi.md#paraphrase_text_post) | **POST** /paraphrase/text | Rewrite text
[**paraphrase_text_request_id_get**](ParaphraseApi.md#paraphrase_text_request_id_get) | **GET** /paraphrase/text/{requestId} | Return text rewriting status.  Also return rewritten text if paraphrasing was successful
[**paraphrase_text_trial_post**](ParaphraseApi.md#paraphrase_text_trial_post) | **POST** /paraphrase/text/trial | Trial rewrite text


# **paraphrase_document_post**
> StatusResponse paraphrase_document_post(paraphrase_file_request=paraphrase_file_request)

Paraphrase document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.paraphrase_file_request import ParaphraseFileRequest
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
    api_instance = groupdocs_rewriter_cloud.ParaphraseApi(api_client)
    paraphrase_file_request = groupdocs_rewriter_cloud.ParaphraseFileRequest() # ParaphraseFileRequest | String in body of request, containing JSON with parameters for rewriting. (optional)

    try:
        # Paraphrase document
        api_response = api_instance.paraphrase_document_post(paraphrase_file_request=paraphrase_file_request)
        print("The response of ParaphraseApi->paraphrase_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParaphraseApi->paraphrase_document_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paraphrase_file_request** | [**ParaphraseFileRequest**](ParaphraseFileRequest.md)| String in body of request, containing JSON with parameters for rewriting. | [optional] 

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

# **paraphrase_document_request_id_get**
> ParaphraseFileResponse paraphrase_document_request_id_get(request_id)

Return document rewriting status.  Also return URLs for downloading of rewritten document if paraphrasig was successful

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.paraphrase_file_response import ParaphraseFileResponse
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
    api_instance = groupdocs_rewriter_cloud.ParaphraseApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/rewriter/document response

    try:
        # Return document rewriting status.  Also return URLs for downloading of rewritten document if paraphrasig was successful
        api_response = api_instance.paraphrase_document_request_id_get(request_id)
        print("The response of ParaphraseApi->paraphrase_document_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParaphraseApi->paraphrase_document_request_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/rewriter/document response | 

### Return type

[**ParaphraseFileResponse**](ParaphraseFileResponse.md)

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

# **paraphrase_document_trial_post**
> StatusResponse paraphrase_document_trial_post(paraphrase_trial_file_request=paraphrase_trial_file_request)

Trial paraphrase document

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.paraphrase_trial_file_request import ParaphraseTrialFileRequest
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
    api_instance = groupdocs_rewriter_cloud.ParaphraseApi(api_client)
    paraphrase_trial_file_request = groupdocs_rewriter_cloud.ParaphraseTrialFileRequest() # ParaphraseTrialFileRequest | String in body of request, containing JSON with parameters for rewriting. (optional)

    try:
        # Trial paraphrase document
        api_response = api_instance.paraphrase_document_trial_post(paraphrase_trial_file_request=paraphrase_trial_file_request)
        print("The response of ParaphraseApi->paraphrase_document_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParaphraseApi->paraphrase_document_trial_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paraphrase_trial_file_request** | [**ParaphraseTrialFileRequest**](ParaphraseTrialFileRequest.md)| String in body of request, containing JSON with parameters for rewriting. | [optional] 

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

# **paraphrase_hc_get**
> HealthCheckResponse paraphrase_hc_get()

Health check for all paraphrase services.

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
    api_instance = groupdocs_rewriter_cloud.ParaphraseApi(api_client)

    try:
        # Health check for all paraphrase services.
        api_response = api_instance.paraphrase_hc_get()
        print("The response of ParaphraseApi->paraphrase_hc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParaphraseApi->paraphrase_hc_get: %s\n" % e)
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

# **paraphrase_ocr_post**
> StatusResponse paraphrase_ocr_post(paraphrase_ocr_request=paraphrase_ocr_request)

Rewrite scanned image or PDF

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.paraphrase_ocr_request import ParaphraseOcrRequest
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
    api_instance = groupdocs_rewriter_cloud.ParaphraseApi(api_client)
    paraphrase_ocr_request = groupdocs_rewriter_cloud.ParaphraseOcrRequest() # ParaphraseOcrRequest | String in body of request, containing JSON with parameters for rewriting. (optional)

    try:
        # Rewrite scanned image or PDF
        api_response = api_instance.paraphrase_ocr_post(paraphrase_ocr_request=paraphrase_ocr_request)
        print("The response of ParaphraseApi->paraphrase_ocr_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParaphraseApi->paraphrase_ocr_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paraphrase_ocr_request** | [**ParaphraseOcrRequest**](ParaphraseOcrRequest.md)| String in body of request, containing JSON with parameters for rewriting. | [optional] 

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

# **paraphrase_supported_conversions_get**
> List[str] paraphrase_supported_conversions_get(format=format)



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
    api_instance = groupdocs_rewriter_cloud.ParaphraseApi(api_client)
    format = 'format_example' # str |  (optional)

    try:
        api_response = api_instance.paraphrase_supported_conversions_get(format=format)
        print("The response of ParaphraseApi->paraphrase_supported_conversions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParaphraseApi->paraphrase_supported_conversions_get: %s\n" % e)
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

# **paraphrase_text_post**
> StatusResponse paraphrase_text_post(paraphrase_text_request=paraphrase_text_request)

Rewrite text

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.paraphrase_text_request import ParaphraseTextRequest
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
    api_instance = groupdocs_rewriter_cloud.ParaphraseApi(api_client)
    paraphrase_text_request = groupdocs_rewriter_cloud.ParaphraseTextRequest() # ParaphraseTextRequest | String in body of request, containing JSON with parameters for rewriting. (optional)

    try:
        # Rewrite text
        api_response = api_instance.paraphrase_text_post(paraphrase_text_request=paraphrase_text_request)
        print("The response of ParaphraseApi->paraphrase_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParaphraseApi->paraphrase_text_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paraphrase_text_request** | [**ParaphraseTextRequest**](ParaphraseTextRequest.md)| String in body of request, containing JSON with parameters for rewriting. | [optional] 

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

# **paraphrase_text_request_id_get**
> ParaphraseTextResponse paraphrase_text_request_id_get(request_id)

Return text rewriting status.  Also return rewritten text if paraphrasing was successful

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.paraphrase_text_response import ParaphraseTextResponse
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
    api_instance = groupdocs_rewriter_cloud.ParaphraseApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/rewriter/text response

    try:
        # Return text rewriting status.  Also return rewritten text if paraphrasing was successful
        api_response = api_instance.paraphrase_text_request_id_get(request_id)
        print("The response of ParaphraseApi->paraphrase_text_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParaphraseApi->paraphrase_text_request_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/rewriter/text response | 

### Return type

[**ParaphraseTextResponse**](ParaphraseTextResponse.md)

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

# **paraphrase_text_trial_post**
> StatusResponse paraphrase_text_trial_post(paraphrase_text_request=paraphrase_text_request)

Trial rewrite text

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.paraphrase_text_request import ParaphraseTextRequest
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
    api_instance = groupdocs_rewriter_cloud.ParaphraseApi(api_client)
    paraphrase_text_request = groupdocs_rewriter_cloud.ParaphraseTextRequest() # ParaphraseTextRequest | String in body of request, containing JSON with parameters for summarizing. Maximum 1000 characters (optional)

    try:
        # Trial rewrite text
        api_response = api_instance.paraphrase_text_trial_post(paraphrase_text_request=paraphrase_text_request)
        print("The response of ParaphraseApi->paraphrase_text_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParaphraseApi->paraphrase_text_trial_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paraphrase_text_request** | [**ParaphraseTextRequest**](ParaphraseTextRequest.md)| String in body of request, containing JSON with parameters for summarizing. Maximum 1000 characters | [optional] 

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

