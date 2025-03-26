# DetectionOcrRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**format** | [**OcrInputFormat**](OcrInputFormat.md) |  | 
**min_length** | **int** | Minimum length of the original text to detect | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.detection_ocr_request import DetectionOcrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DetectionOcrRequest from a JSON string
detection_ocr_request_instance = DetectionOcrRequest.from_json(json)
# print the JSON string representation of the object
print(DetectionOcrRequest.to_json())

# convert the object into a dict
detection_ocr_request_dict = detection_ocr_request_instance.to_dict()
# create an instance of DetectionOcrRequest from a dict
detection_ocr_request_from_dict = DetectionOcrRequest.from_dict(detection_ocr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


