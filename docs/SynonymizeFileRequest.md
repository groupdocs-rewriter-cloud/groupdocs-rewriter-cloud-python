# SynonymizeFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**output_format** | [**SupportedConversionsFormats**](SupportedConversionsFormats.md) |  | [optional] 
**format** | [**DetectionSupportedFormats**](DetectionSupportedFormats.md) |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.synonymize_file_request import SynonymizeFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SynonymizeFileRequest from a JSON string
synonymize_file_request_instance = SynonymizeFileRequest.from_json(json)
# print the JSON string representation of the object
print(SynonymizeFileRequest.to_json())

# convert the object into a dict
synonymize_file_request_dict = synonymize_file_request_instance.to_dict()
# create an instance of SynonymizeFileRequest from a dict
synonymize_file_request_from_dict = SynonymizeFileRequest.from_dict(synonymize_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


