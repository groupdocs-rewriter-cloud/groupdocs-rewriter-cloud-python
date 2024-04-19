# DetectionTrialFileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**min_length** | **int** | Minimum length of the source text | [optional] 
**format** | [**TrialSupportedFormats**](TrialSupportedFormats.md) |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.detection_trial_file_request import DetectionTrialFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DetectionTrialFileRequest from a JSON string
detection_trial_file_request_instance = DetectionTrialFileRequest.from_json(json)
# print the JSON string representation of the object
print DetectionTrialFileRequest.to_json()

# convert the object into a dict
detection_trial_file_request_dict = detection_trial_file_request_instance.to_dict()
# create an instance of DetectionTrialFileRequest from a dict
detection_trial_file_request_form_dict = detection_trial_file_request.from_dict(detection_trial_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


