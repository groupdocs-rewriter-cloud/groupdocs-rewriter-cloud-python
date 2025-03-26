# ParaphraseOcrRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**output_format** | [**OcrOutputFormat**](OcrOutputFormat.md) |  | 
**diversity_degree** | [**DegreeEnum**](DegreeEnum.md) |  | [optional] 
**format** | [**OcrInputFormat**](OcrInputFormat.md) |  | 

## Example

```python
from groupdocs_rewriter_cloud.models.paraphrase_ocr_request import ParaphraseOcrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ParaphraseOcrRequest from a JSON string
paraphrase_ocr_request_instance = ParaphraseOcrRequest.from_json(json)
# print the JSON string representation of the object
print(ParaphraseOcrRequest.to_json())

# convert the object into a dict
paraphrase_ocr_request_dict = paraphrase_ocr_request_instance.to_dict()
# create an instance of ParaphraseOcrRequest from a dict
paraphrase_ocr_request_from_dict = ParaphraseOcrRequest.from_dict(paraphrase_ocr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


