# DetectionTextRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**text** | **str** | Single text paragraph | [optional] 
**texts** | **List[str]** | Text paragraphs | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.detection_text_request import DetectionTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DetectionTextRequest from a JSON string
detection_text_request_instance = DetectionTextRequest.from_json(json)
# print the JSON string representation of the object
print DetectionTextRequest.to_json()

# convert the object into a dict
detection_text_request_dict = detection_text_request_instance.to_dict()
# create an instance of DetectionTextRequest from a dict
detection_text_request_form_dict = detection_text_request.from_dict(detection_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


