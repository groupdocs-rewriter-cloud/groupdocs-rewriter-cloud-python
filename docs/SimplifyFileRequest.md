# SimplifyFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**output_format** | [**SupportedConversionsFormats**](SupportedConversionsFormats.md) |  | 
**format** | [**SimplifySupportedFromats**](SimplifySupportedFromats.md) |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.simplify_file_request import SimplifyFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifyFileRequest from a JSON string
simplify_file_request_instance = SimplifyFileRequest.from_json(json)
# print the JSON string representation of the object
print(SimplifyFileRequest.to_json())

# convert the object into a dict
simplify_file_request_dict = simplify_file_request_instance.to_dict()
# create an instance of SimplifyFileRequest from a dict
simplify_file_request_from_dict = SimplifyFileRequest.from_dict(simplify_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


