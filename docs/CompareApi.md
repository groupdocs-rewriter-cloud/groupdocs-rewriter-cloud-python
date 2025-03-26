# groupdocs_rewriter_cloud.CompareApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_hc_get**](CompareApi.md#compare_hc_get) | **GET** /compare/hc | Health check for all comparer services.
[**compare_text_post**](CompareApi.md#compare_text_post) | **POST** /compare/text | Compare texts and detect if one is translation or paraphrase of another
[**compare_text_request_id_get**](CompareApi.md#compare_text_request_id_get) | **GET** /compare/text/{requestId} | Return text comparing status.  Also return probability if one text is paraphrasing or translation of another
[**compare_text_summarization_post**](CompareApi.md#compare_text_summarization_post) | **POST** /compare/text/summarization | Compare texts and detect if one is summarization of another


# **compare_hc_get**
> HealthCheckResponse compare_hc_get()

Health check for all comparer services.

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
    api_instance = groupdocs_rewriter_cloud.CompareApi(api_client)

    try:
        # Health check for all comparer services.
        api_response = api_instance.compare_hc_get()
        print("The response of CompareApi->compare_hc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompareApi->compare_hc_get: %s\n" % e)
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

# **compare_text_post**
> StatusResponse compare_text_post(compare_text_request=compare_text_request)

Compare texts and detect if one is translation or paraphrase of another

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.compare_text_request import CompareTextRequest
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
    api_instance = groupdocs_rewriter_cloud.CompareApi(api_client)
    compare_text_request = groupdocs_rewriter_cloud.CompareTextRequest() # CompareTextRequest | String in body of request, containing JSON with parameters for comparison. (optional)

    try:
        # Compare texts and detect if one is translation or paraphrase of another
        api_response = api_instance.compare_text_post(compare_text_request=compare_text_request)
        print("The response of CompareApi->compare_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompareApi->compare_text_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compare_text_request** | [**CompareTextRequest**](CompareTextRequest.md)| String in body of request, containing JSON with parameters for comparison. | [optional] 

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

# **compare_text_request_id_get**
> CompareTextResponse compare_text_request_id_get(request_id)

Return text comparing status.  Also return probability if one text is paraphrasing or translation of another

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.compare_text_response import CompareTextResponse
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
    api_instance = groupdocs_rewriter_cloud.CompareApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/compare/text response

    try:
        # Return text comparing status.  Also return probability if one text is paraphrasing or translation of another
        api_response = api_instance.compare_text_request_id_get(request_id)
        print("The response of CompareApi->compare_text_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompareApi->compare_text_request_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/compare/text response | 

### Return type

[**CompareTextResponse**](CompareTextResponse.md)

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

# **compare_text_summarization_post**
> StatusResponse compare_text_summarization_post(compare_text_request=compare_text_request)

Compare texts and detect if one is summarization of another

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.compare_text_request import CompareTextRequest
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
    api_instance = groupdocs_rewriter_cloud.CompareApi(api_client)
    compare_text_request = groupdocs_rewriter_cloud.CompareTextRequest() # CompareTextRequest | String in body of request, containing JSON with parameters for comparison. (optional)

    try:
        # Compare texts and detect if one is summarization of another
        api_response = api_instance.compare_text_summarization_post(compare_text_request=compare_text_request)
        print("The response of CompareApi->compare_text_summarization_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CompareApi->compare_text_summarization_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compare_text_request** | [**CompareTextRequest**](CompareTextRequest.md)| String in body of request, containing JSON with parameters for comparison. | [optional] 

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

