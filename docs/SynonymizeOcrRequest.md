# SynonymizeOcrRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**output_format** | [**OcrOutputFormat**](OcrOutputFormat.md) |  | 
**format** | [**OcrInputFormat**](OcrInputFormat.md) |  | 

## Example

```python
from groupdocs_rewriter_cloud.models.synonymize_ocr_request import SynonymizeOcrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SynonymizeOcrRequest from a JSON string
synonymize_ocr_request_instance = SynonymizeOcrRequest.from_json(json)
# print the JSON string representation of the object
print(SynonymizeOcrRequest.to_json())

# convert the object into a dict
synonymize_ocr_request_dict = synonymize_ocr_request_instance.to_dict()
# create an instance of SynonymizeOcrRequest from a dict
synonymize_ocr_request_from_dict = SynonymizeOcrRequest.from_dict(synonymize_ocr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


