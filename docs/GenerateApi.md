# groupdocs_rewriter_cloud.GenerateApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_cover_letter_post**](GenerateApi.md#generate_cover_letter_post) | **POST** /generate/cover-letter | Generate cover letter based on job description and optionally CV and cover letter that should be adopted to this offer
[**generate_hc_get**](GenerateApi.md#generate_hc_get) | **GET** /generate/hc | Health check for generation services.
[**generate_request_id_get**](GenerateApi.md#generate_request_id_get) | **GET** /generate/{requestId} | Return generation status.  Also return generated result
[**generate_test_exercise_post**](GenerateApi.md#generate_test_exercise_post) | **POST** /generate/test-exercise | Generate test exercise based on job description and optionally CV
[**generate_test_questions_post**](GenerateApi.md#generate_test_questions_post) | **POST** /generate/test-questions | Generate questions for technical interview based on job description and optionally CV


# **generate_cover_letter_post**
> StatusResponse generate_cover_letter_post(generate_request=generate_request)

Generate cover letter based on job description and optionally CV and cover letter that should be adopted to this offer

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.generate_request import GenerateRequest
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
    api_instance = groupdocs_rewriter_cloud.GenerateApi(api_client)
    generate_request = groupdocs_rewriter_cloud.GenerateRequest() # GenerateRequest | String in body of request, containing JSON with parameters for comparison. (optional)

    try:
        # Generate cover letter based on job description and optionally CV and cover letter that should be adopted to this offer
        api_response = api_instance.generate_cover_letter_post(generate_request=generate_request)
        print("The response of GenerateApi->generate_cover_letter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerateApi->generate_cover_letter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_request** | [**GenerateRequest**](GenerateRequest.md)| String in body of request, containing JSON with parameters for comparison. | [optional] 

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

# **generate_hc_get**
> HealthCheckResponse generate_hc_get()

Health check for generation services.

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
    api_instance = groupdocs_rewriter_cloud.GenerateApi(api_client)

    try:
        # Health check for generation services.
        api_response = api_instance.generate_hc_get()
        print("The response of GenerateApi->generate_hc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerateApi->generate_hc_get: %s\n" % e)
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

# **generate_request_id_get**
> GenerateResponse generate_request_id_get(request_id)

Return generation status.  Also return generated result

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.generate_response import GenerateResponse
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
    api_instance = groupdocs_rewriter_cloud.GenerateApi(api_client)
    request_id = 'request_id_example' # str | GUID

    try:
        # Return generation status.  Also return generated result
        api_response = api_instance.generate_request_id_get(request_id)
        print("The response of GenerateApi->generate_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerateApi->generate_request_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID | 

### Return type

[**GenerateResponse**](GenerateResponse.md)

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

# **generate_test_exercise_post**
> StatusResponse generate_test_exercise_post(generate_request=generate_request)

Generate test exercise based on job description and optionally CV

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.generate_request import GenerateRequest
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
    api_instance = groupdocs_rewriter_cloud.GenerateApi(api_client)
    generate_request = groupdocs_rewriter_cloud.GenerateRequest() # GenerateRequest | String in body of request, containing JSON with parameters for comparison. (optional)

    try:
        # Generate test exercise based on job description and optionally CV
        api_response = api_instance.generate_test_exercise_post(generate_request=generate_request)
        print("The response of GenerateApi->generate_test_exercise_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerateApi->generate_test_exercise_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_request** | [**GenerateRequest**](GenerateRequest.md)| String in body of request, containing JSON with parameters for comparison. | [optional] 

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

# **generate_test_questions_post**
> StatusResponse generate_test_questions_post(generate_request=generate_request)

Generate questions for technical interview based on job description and optionally CV

### Example

* OAuth Authentication (JWT):

```python
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.generate_request import GenerateRequest
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
    api_instance = groupdocs_rewriter_cloud.GenerateApi(api_client)
    generate_request = groupdocs_rewriter_cloud.GenerateRequest() # GenerateRequest | String in body of request, containing JSON with parameters for comparison. (optional)

    try:
        # Generate questions for technical interview based on job description and optionally CV
        api_response = api_instance.generate_test_questions_post(generate_request=generate_request)
        print("The response of GenerateApi->generate_test_questions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenerateApi->generate_test_questions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_request** | [**GenerateRequest**](GenerateRequest.md)| String in body of request, containing JSON with parameters for comparison. | [optional] 

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

