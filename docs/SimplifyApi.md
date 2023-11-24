# groupdocs_rewriter_cloud.SimplifyApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**simplify_document_post**](SimplifyApi.md#simplify_document_post) | **POST** /simplify/document | Simplify document
[**simplify_document_request_id_get**](SimplifyApi.md#simplify_document_request_id_get) | **GET** /simplify/document/{requestId} | Return document simplifying status.  Also return URLs for downloading of simplified document if paraphrasig was successful
[**simplify_document_trial_post**](SimplifyApi.md#simplify_document_trial_post) | **POST** /simplify/document/trial | Trial simplify document
[**simplify_hc_get**](SimplifyApi.md#simplify_hc_get) | **GET** /simplify/hc | Health check for all simplify services.
[**simplify_supported_conversions_get**](SimplifyApi.md#simplify_supported_conversions_get) | **GET** /simplify/supportedConversions | 
[**simplify_text_post**](SimplifyApi.md#simplify_text_post) | **POST** /simplify/text | Simplify text
[**simplify_text_request_id_get**](SimplifyApi.md#simplify_text_request_id_get) | **GET** /simplify/text/{requestId} | Return text simplifying status.  Also return simplified text if paraphrasing was successful
[**simplify_text_trial_post**](SimplifyApi.md#simplify_text_trial_post) | **POST** /simplify/text/trial | Trial simplify text


# **simplify_document_post**
> StatusResponse simplify_document_post(simplify_file_request=simplify_file_request)

Simplify document

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.simplify_file_request import SimplifyFileRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
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
    api_instance = groupdocs_rewriter_cloud.SimplifyApi(api_client)
    simplify_file_request = groupdocs_rewriter_cloud.SimplifyFileRequest() # SimplifyFileRequest | String in body of request, containing JSON with parameters for simplifying. (optional)

    try:
        # Simplify document
        api_response = api_instance.simplify_document_post(simplify_file_request=simplify_file_request)
        print("The response of SimplifyApi->simplify_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimplifyApi->simplify_document_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simplify_file_request** | [**SimplifyFileRequest**](SimplifyFileRequest.md)| String in body of request, containing JSON with parameters for simplifying. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simplify_document_request_id_get**
> SimplifyFileResponse simplify_document_request_id_get(request_id)

Return document simplifying status.  Also return URLs for downloading of simplified document if paraphrasig was successful

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.simplify_file_response import SimplifyFileResponse
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
    api_instance = groupdocs_rewriter_cloud.SimplifyApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/rewriter/document response

    try:
        # Return document simplifying status.  Also return URLs for downloading of simplified document if paraphrasig was successful
        api_response = api_instance.simplify_document_request_id_get(request_id)
        print("The response of SimplifyApi->simplify_document_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimplifyApi->simplify_document_request_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/rewriter/document response | 

### Return type

[**SimplifyFileResponse**](SimplifyFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simplify_document_trial_post**
> StatusResponse simplify_document_trial_post(simplify_trial_file_request=simplify_trial_file_request)

Trial simplify document

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.simplify_trial_file_request import SimplifyTrialFileRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
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
    api_instance = groupdocs_rewriter_cloud.SimplifyApi(api_client)
    simplify_trial_file_request = groupdocs_rewriter_cloud.SimplifyTrialFileRequest() # SimplifyTrialFileRequest | String in body of request, containing JSON with parameters for simplifying. (optional)

    try:
        # Trial simplify document
        api_response = api_instance.simplify_document_trial_post(simplify_trial_file_request=simplify_trial_file_request)
        print("The response of SimplifyApi->simplify_document_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimplifyApi->simplify_document_trial_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simplify_trial_file_request** | [**SimplifyTrialFileRequest**](SimplifyTrialFileRequest.md)| String in body of request, containing JSON with parameters for simplifying. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simplify_hc_get**
> HealthCheckResponse simplify_hc_get()

Health check for all simplify services.

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.health_check_response import HealthCheckResponse
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
    api_instance = groupdocs_rewriter_cloud.SimplifyApi(api_client)

    try:
        # Health check for all simplify services.
        api_response = api_instance.simplify_hc_get()
        print("The response of SimplifyApi->simplify_hc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimplifyApi->simplify_hc_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthCheckResponse**](HealthCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simplify_supported_conversions_get**
> List[str] simplify_supported_conversions_get(format=format)



### Example

```python
import time
import os
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
    api_instance = groupdocs_rewriter_cloud.SimplifyApi(api_client)
    format = 'format_example' # str |  (optional)

    try:
        api_response = api_instance.simplify_supported_conversions_get(format=format)
        print("The response of SimplifyApi->simplify_supported_conversions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimplifyApi->simplify_supported_conversions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simplify_text_post**
> StatusResponse simplify_text_post(base_text_request=base_text_request)

Simplify text

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.base_text_request import BaseTextRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
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
    api_instance = groupdocs_rewriter_cloud.SimplifyApi(api_client)
    base_text_request = groupdocs_rewriter_cloud.BaseTextRequest() # BaseTextRequest | String in body of request, containing JSON with parameters for simplifying. (optional)

    try:
        # Simplify text
        api_response = api_instance.simplify_text_post(base_text_request=base_text_request)
        print("The response of SimplifyApi->simplify_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimplifyApi->simplify_text_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_text_request** | [**BaseTextRequest**](BaseTextRequest.md)| String in body of request, containing JSON with parameters for simplifying. | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simplify_text_request_id_get**
> SimplifyTextResponse simplify_text_request_id_get(request_id)

Return text simplifying status.  Also return simplified text if paraphrasing was successful

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.simplify_text_response import SimplifyTextResponse
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
    api_instance = groupdocs_rewriter_cloud.SimplifyApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/rewriter/text response

    try:
        # Return text simplifying status.  Also return simplified text if paraphrasing was successful
        api_response = api_instance.simplify_text_request_id_get(request_id)
        print("The response of SimplifyApi->simplify_text_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimplifyApi->simplify_text_request_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/rewriter/text response | 

### Return type

[**SimplifyTextResponse**](SimplifyTextResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **simplify_text_trial_post**
> StatusResponse simplify_text_trial_post(base_text_request=base_text_request)

Trial simplify text

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.base_text_request import BaseTextRequest
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
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
    api_instance = groupdocs_rewriter_cloud.SimplifyApi(api_client)
    base_text_request = groupdocs_rewriter_cloud.BaseTextRequest() # BaseTextRequest | String in body of request, containing JSON with parameters for simplifying. Maximum 1000 characters (optional)

    try:
        # Trial simplify text
        api_response = api_instance.simplify_text_trial_post(base_text_request=base_text_request)
        print("The response of SimplifyApi->simplify_text_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SimplifyApi->simplify_text_trial_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_text_request** | [**BaseTextRequest**](BaseTextRequest.md)| String in body of request, containing JSON with parameters for simplifying. Maximum 1000 characters | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

