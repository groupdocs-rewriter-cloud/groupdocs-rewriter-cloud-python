# groupdocs_rewriter_cloud.SynonymizeApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**synonymize_hc_get**](SynonymizeApi.md#synonymize_hc_get) | **GET** /synonymize/hc | Health check for all synonymizer services.
[**synonymize_text_post**](SynonymizeApi.md#synonymize_text_post) | **POST** /synonymize/text | Synonymize word
[**synonymize_text_request_id_get**](SynonymizeApi.md#synonymize_text_request_id_get) | **GET** /synonymize/text/{requestId} | Return text synonymizing status.  Also return list of synonyms if it was successful
[**synonymize_text_trial_post**](SynonymizeApi.md#synonymize_text_trial_post) | **POST** /synonymize/text/trial | Trial synonymize word


# **synonymize_hc_get**
> HealthCheckResponse synonymize_hc_get()

Health check for all synonymizer services.

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

```python
import time
import os
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

No authorization required

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

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.synonymize_text_response import SynonymizeTextResponse
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

No authorization required

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

```python
import time
import os
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

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

