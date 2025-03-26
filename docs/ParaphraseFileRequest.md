# ParaphraseFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**output_format** | [**SupportedConversionsFormats**](SupportedConversionsFormats.md) |  | 
**diversity_degree** | [**DegreeEnum**](DegreeEnum.md) |  | [optional] 
**format** | [**ParaphraseSupportedFormats**](ParaphraseSupportedFormats.md) |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.paraphrase_file_request import ParaphraseFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ParaphraseFileRequest from a JSON string
paraphrase_file_request_instance = ParaphraseFileRequest.from_json(json)
# print the JSON string representation of the object
print(ParaphraseFileRequest.to_json())

# convert the object into a dict
paraphrase_file_request_dict = paraphrase_file_request_instance.to_dict()
# create an instance of ParaphraseFileRequest from a dict
paraphrase_file_request_from_dict = ParaphraseFileRequest.from_dict(paraphrase_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


