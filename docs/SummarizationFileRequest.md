# SummarizationFileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**output_format** | [**SupportedConversionsFormats**](SupportedConversionsFormats.md) |  | 
**summarization_degree** | [**DegreeEnum**](DegreeEnum.md) |  | [optional] 
**min_length** | **int** | Minimum length of the target text | [optional] 
**format** | [**SummarizationSupportedFormats**](SummarizationSupportedFormats.md) |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.summarization_file_request import SummarizationFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SummarizationFileRequest from a JSON string
summarization_file_request_instance = SummarizationFileRequest.from_json(json)
# print the JSON string representation of the object
print SummarizationFileRequest.to_json()

# convert the object into a dict
summarization_file_request_dict = summarization_file_request_instance.to_dict()
# create an instance of SummarizationFileRequest from a dict
summarization_file_request_form_dict = summarization_file_request.from_dict(summarization_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


