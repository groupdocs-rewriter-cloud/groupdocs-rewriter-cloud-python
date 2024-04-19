# DetectionTextResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**probability** | **float** | The probability that the text turned out to be paraphrased | [optional] 
**is_paraphrased** | **bool** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.detection_text_response import DetectionTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DetectionTextResponse from a JSON string
detection_text_response_instance = DetectionTextResponse.from_json(json)
# print the JSON string representation of the object
print DetectionTextResponse.to_json()

# convert the object into a dict
detection_text_response_dict = detection_text_response_instance.to_dict()
# create an instance of DetectionTextResponse from a dict
detection_text_response_form_dict = detection_text_response.from_dict(detection_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


