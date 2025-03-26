# FormalizeFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**output_format** | [**SupportedConversionsFormats**](SupportedConversionsFormats.md) |  | 
**format** | [**FormalizeSupportedFromats**](FormalizeSupportedFromats.md) |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.formalize_file_request import FormalizeFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FormalizeFileRequest from a JSON string
formalize_file_request_instance = FormalizeFileRequest.from_json(json)
# print the JSON string representation of the object
print(FormalizeFileRequest.to_json())

# convert the object into a dict
formalize_file_request_dict = formalize_file_request_instance.to_dict()
# create an instance of FormalizeFileRequest from a dict
formalize_file_request_from_dict = FormalizeFileRequest.from_dict(formalize_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


