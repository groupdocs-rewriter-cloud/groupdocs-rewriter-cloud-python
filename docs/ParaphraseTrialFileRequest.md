# ParaphraseTrialFileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**diversity_degree** | [**DegreeEnum**](DegreeEnum.md) |  | [optional] 
**format** | [**TrialSupportedFormats**](TrialSupportedFormats.md) |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.paraphrase_trial_file_request import ParaphraseTrialFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ParaphraseTrialFileRequest from a JSON string
paraphrase_trial_file_request_instance = ParaphraseTrialFileRequest.from_json(json)
# print the JSON string representation of the object
print ParaphraseTrialFileRequest.to_json()

# convert the object into a dict
paraphrase_trial_file_request_dict = paraphrase_trial_file_request_instance.to_dict()
# create an instance of ParaphraseTrialFileRequest from a dict
paraphrase_trial_file_request_form_dict = paraphrase_trial_file_request.from_dict(paraphrase_trial_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


