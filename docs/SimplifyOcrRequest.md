# SimplifyOcrRequest


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
from groupdocs_rewriter_cloud.models.simplify_ocr_request import SimplifyOcrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifyOcrRequest from a JSON string
simplify_ocr_request_instance = SimplifyOcrRequest.from_json(json)
# print the JSON string representation of the object
print(SimplifyOcrRequest.to_json())

# convert the object into a dict
simplify_ocr_request_dict = simplify_ocr_request_instance.to_dict()
# create an instance of SimplifyOcrRequest from a dict
simplify_ocr_request_from_dict = SimplifyOcrRequest.from_dict(simplify_ocr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


