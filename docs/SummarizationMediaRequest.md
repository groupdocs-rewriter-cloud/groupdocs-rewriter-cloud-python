# SummarizationMediaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**summarization_degree** | [**DegreeEnum**](DegreeEnum.md) |  | [optional] 
**format** | [**MediaInputFormat**](MediaInputFormat.md) |  | 
**outputformat** | **str** | Output format, text or file | [default to 'Text']
**min_length** | **int** | Minimum length of the original text to summarize | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.summarization_media_request import SummarizationMediaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SummarizationMediaRequest from a JSON string
summarization_media_request_instance = SummarizationMediaRequest.from_json(json)
# print the JSON string representation of the object
print(SummarizationMediaRequest.to_json())

# convert the object into a dict
summarization_media_request_dict = summarization_media_request_instance.to_dict()
# create an instance of SummarizationMediaRequest from a dict
summarization_media_request_from_dict = SummarizationMediaRequest.from_dict(summarization_media_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


