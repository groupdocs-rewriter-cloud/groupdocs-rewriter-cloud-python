# groupdocs_rewriter_cloud.InfoApi

All URIs are relative to *https://api.groupdocs.cloud/v2.0/rewriter*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_available_languages_get**](InfoApi.md#info_available_languages_get) | **GET** /info/availableLanguages | 


# **info_available_languages_get**
> List[LanguageInfo] info_available_languages_get()



### Example

```python
import time
import os
import groupdocs_rewriter_cloud
from groupdocs_rewriter_cloud.models.language_info import LanguageInfo
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
    api_instance = groupdocs_rewriter_cloud.InfoApi(api_client)

    try:
        api_response = api_instance.info_available_languages_get()
        print("The response of InfoApi->info_available_languages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->info_available_languages_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[LanguageInfo]**](LanguageInfo.md)

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

