# groupdocs_rewriter_cloud.SwaggerApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**swagger_spec_get**](SwaggerApi.md#swagger_spec_get) | **GET** /swagger/spec | 


# **swagger_spec_get**
> swagger_spec_get(is_yaml=is_yaml, serialaize_as_v2=serialaize_as_v2)



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
    api_instance = groupdocs_rewriter_cloud.SwaggerApi(api_client)
    is_yaml = False # bool |  (optional) (default to False)
    serialaize_as_v2 = False # bool |  (optional) (default to False)

    try:
        api_instance.swagger_spec_get(is_yaml=is_yaml, serialaize_as_v2=serialaize_as_v2)
    except Exception as e:
        print("Exception when calling SwaggerApi->swagger_spec_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_yaml** | **bool**|  | [optional] [default to False]
 **serialaize_as_v2** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

