# groupdocs_rewriter_cloud.FileApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_upload_post**](FileApi.md#file_upload_post) | **POST** /file/upload | 


# **file_upload_post**
> str file_upload_post(format=format, file=file)



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
    api_instance = groupdocs_rewriter_cloud.FileApi(api_client)
    format = 'format_example' # str |  (optional)
    file = None # bytearray |  (optional)

    try:
        api_response = api_instance.file_upload_post(format=format, file=file)
        print("The response of FileApi->file_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileApi->file_upload_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  | [optional] 
 **file** | **bytearray**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

