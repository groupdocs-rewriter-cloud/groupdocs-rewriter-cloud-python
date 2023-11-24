# DetectionFileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**file** | **bytearray** | Source file format | [optional] 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**min_length** | **int** |  | [optional] 
**format** | **str** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.detection_file_request import DetectionFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DetectionFileRequest from a JSON string
detection_file_request_instance = DetectionFileRequest.from_json(json)
# print the JSON string representation of the object
print DetectionFileRequest.to_json()

# convert the object into a dict
detection_file_request_dict = detection_file_request_instance.to_dict()
# create an instance of DetectionFileRequest from a dict
detection_file_request_form_dict = detection_file_request.from_dict(detection_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


