# SimplifyTrialFileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**format** | **str** | Set the file format. | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.simplify_trial_file_request import SimplifyTrialFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifyTrialFileRequest from a JSON string
simplify_trial_file_request_instance = SimplifyTrialFileRequest.from_json(json)
# print the JSON string representation of the object
print SimplifyTrialFileRequest.to_json()

# convert the object into a dict
simplify_trial_file_request_dict = simplify_trial_file_request_instance.to_dict()
# create an instance of SimplifyTrialFileRequest from a dict
simplify_trial_file_request_form_dict = simplify_trial_file_request.from_dict(simplify_trial_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


