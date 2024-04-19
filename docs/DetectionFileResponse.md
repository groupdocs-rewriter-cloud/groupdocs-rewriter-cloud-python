# DetectionFileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**probability** | **float** | The probability that the text turned out to be paraphrased | [optional] 
**is_paraphrased** | **bool** |  | [optional] 
**per_paragraph_probability** | **List[float]** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.detection_file_response import DetectionFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DetectionFileResponse from a JSON string
detection_file_response_instance = DetectionFileResponse.from_json(json)
# print the JSON string representation of the object
print DetectionFileResponse.to_json()

# convert the object into a dict
detection_file_response_dict = detection_file_response_instance.to_dict()
# create an instance of DetectionFileResponse from a dict
detection_file_response_form_dict = detection_file_response.from_dict(detection_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


