# SummarizationOcrRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**output_format** | [**OcrOutputFormat**](OcrOutputFormat.md) |  | 
**summarization_degree** | [**DegreeEnum**](DegreeEnum.md) |  | [optional] 
**format** | [**OcrInputFormat**](OcrInputFormat.md) |  | 
**min_length** | **int** | Minimum length of the original text to summarize | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.summarization_ocr_request import SummarizationOcrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SummarizationOcrRequest from a JSON string
summarization_ocr_request_instance = SummarizationOcrRequest.from_json(json)
# print the JSON string representation of the object
print(SummarizationOcrRequest.to_json())

# convert the object into a dict
summarization_ocr_request_dict = summarization_ocr_request_instance.to_dict()
# create an instance of SummarizationOcrRequest from a dict
summarization_ocr_request_from_dict = SummarizationOcrRequest.from_dict(summarization_ocr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


