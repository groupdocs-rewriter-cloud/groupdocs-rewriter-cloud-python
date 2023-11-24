# groupdocs_rewriter_cloud.SummarizeApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**summarize_document_post**](SummarizeApi.md#summarize_document_post) | **POST** /summarize/document | Summarize document
[**summarize_document_request_id_get**](SummarizeApi.md#summarize_document_request_id_get) | **GET** /summarize/document/{requestId} | Return document summarizing status.  Also return URLs for downloading of summarized document if summarization was successful
[**summarize_document_trial_post**](SummarizeApi.md#summarize_document_trial_post) | **POST** /summarize/document/trial | Trial summarize document
[**summarize_hc_get**](SummarizeApi.md#summarize_hc_get) | **GET** /summarize/hc | Health check for all summarize services.
[**summarize_supported_conversions_get**](SummarizeApi.md#summarize_supported_conversions_get) | **GET** /summarize/supportedConversions | 
[**summarize_text_post**](SummarizeApi.md#summarize_text_post) | **POST** /summarize/text | Summarize text
[**summarize_text_request_id_get**](SummarizeApi.md#summarize_text_request_id_get) | **GET** /summarize/text/{requestId} | Return text summarizing status status.  Also return rewrote text if translation was successful
[**summarize_text_trial_post**](SummarizeApi.md#summarize_text_trial_post) | **POST** /summarize/text/trial | Trial summarize text


# **summarize_document_post**
> StatusResponse summarize_document_post(summarization_file_request=summarization_file_request)

Summarize document

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.models.summarization_file_request import SummarizationFileRequest
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
    api_instance = groupdocs_rewriter_cloud.SummarizeApi(api_client)
    summarization_file_request = groupdocs_rewriter_cloud.SummarizationFileRequest() # SummarizationFileRequest | String in body of request, containing JSON with parameters for summarizing. (optional)

    try:
        # Summarize document
        api_response = api_instance.summarize_document_post(summarization_file_request=summarization_file_request)
        print("The response of SummarizeApi->summarize_document_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizeApi->summarize_document_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summarization_file_request** | [**SummarizationFileRequest**](SummarizationFileRequest.md)| String in body of request, containing JSON with parameters for summarizing. | [optional] 

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

# **summarize_document_request_id_get**
> SummarizationFileResponse summarize_document_request_id_get(request_id)

Return document summarizing status.  Also return URLs for downloading of summarized document if summarization was successful

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.summarization_file_response import SummarizationFileResponse
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
    api_instance = groupdocs_rewriter_cloud.SummarizeApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/rewriter/document response

    try:
        # Return document summarizing status.  Also return URLs for downloading of summarized document if summarization was successful
        api_response = api_instance.summarize_document_request_id_get(request_id)
        print("The response of SummarizeApi->summarize_document_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizeApi->summarize_document_request_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/rewriter/document response | 

### Return type

[**SummarizationFileResponse**](SummarizationFileResponse.md)

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

# **summarize_document_trial_post**
> StatusResponse summarize_document_trial_post(summarization_trial_file_request=summarization_trial_file_request)

Trial summarize document

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.models.summarization_trial_file_request import SummarizationTrialFileRequest
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
    api_instance = groupdocs_rewriter_cloud.SummarizeApi(api_client)
    summarization_trial_file_request = groupdocs_rewriter_cloud.SummarizationTrialFileRequest() # SummarizationTrialFileRequest | String in body of request, containing JSON with parameters for summarizing. (optional)

    try:
        # Trial summarize document
        api_response = api_instance.summarize_document_trial_post(summarization_trial_file_request=summarization_trial_file_request)
        print("The response of SummarizeApi->summarize_document_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizeApi->summarize_document_trial_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summarization_trial_file_request** | [**SummarizationTrialFileRequest**](SummarizationTrialFileRequest.md)| String in body of request, containing JSON with parameters for summarizing. | [optional] 

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

# **summarize_hc_get**
> HealthCheckResponse summarize_hc_get()

Health check for all summarize services.

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
    api_instance = groupdocs_rewriter_cloud.SummarizeApi(api_client)

    try:
        # Health check for all summarize services.
        api_response = api_instance.summarize_hc_get()
        print("The response of SummarizeApi->summarize_hc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizeApi->summarize_hc_get: %s\n" % e)
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

# **summarize_supported_conversions_get**
> List[str] summarize_supported_conversions_get(format=format)



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
    api_instance = groupdocs_rewriter_cloud.SummarizeApi(api_client)
    format = 'format_example' # str |  (optional)

    try:
        api_response = api_instance.summarize_supported_conversions_get(format=format)
        print("The response of SummarizeApi->summarize_supported_conversions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizeApi->summarize_supported_conversions_get: %s\n" % e)
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

# **summarize_text_post**
> StatusResponse summarize_text_post(summarization_text_request=summarization_text_request)

Summarize text

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.models.summarization_text_request import SummarizationTextRequest
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
    api_instance = groupdocs_rewriter_cloud.SummarizeApi(api_client)
    summarization_text_request = groupdocs_rewriter_cloud.SummarizationTextRequest() # SummarizationTextRequest |  (optional)

    try:
        # Summarize text
        api_response = api_instance.summarize_text_post(summarization_text_request=summarization_text_request)
        print("The response of SummarizeApi->summarize_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizeApi->summarize_text_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summarization_text_request** | [**SummarizationTextRequest**](SummarizationTextRequest.md)|  | [optional] 

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

# **summarize_text_request_id_get**
> SummarizationTextResponse summarize_text_request_id_get(request_id)

Return text summarizing status status.  Also return rewrote text if translation was successful

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.summarization_text_response import SummarizationTextResponse
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
    api_instance = groupdocs_rewriter_cloud.SummarizeApi(api_client)
    request_id = 'request_id_example' # str | GUID which got from /v3/rewriter/text response

    try:
        # Return text summarizing status status.  Also return rewrote text if translation was successful
        api_response = api_instance.summarize_text_request_id_get(request_id)
        print("The response of SummarizeApi->summarize_text_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizeApi->summarize_text_request_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| GUID which got from /v3/rewriter/text response | 

### Return type

[**SummarizationTextResponse**](SummarizationTextResponse.md)

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

# **summarize_text_trial_post**
> StatusResponse summarize_text_trial_post(summarization_text_request=summarization_text_request)

Trial summarize text

### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.status_response import StatusResponse
from groupdocs_rewriter_cloud.models.summarization_text_request import SummarizationTextRequest
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
    api_instance = groupdocs_rewriter_cloud.SummarizeApi(api_client)
    summarization_text_request = groupdocs_rewriter_cloud.SummarizationTextRequest() # SummarizationTextRequest | String in body of request, containing JSON with parameters for summarizing. Maximum 1000 characters (optional)

    try:
        # Trial summarize text
        api_response = api_instance.summarize_text_trial_post(summarization_text_request=summarization_text_request)
        print("The response of SummarizeApi->summarize_text_trial_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SummarizeApi->summarize_text_trial_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summarization_text_request** | [**SummarizationTextRequest**](SummarizationTextRequest.md)| String in body of request, containing JSON with parameters for summarizing. Maximum 1000 characters | [optional] 

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

