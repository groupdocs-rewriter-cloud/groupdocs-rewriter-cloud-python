# SummarizationTrialFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**url** | **str** |  | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**original_name** | **str** |  | [optional] 
**saving_mode** | [**FileSavingMode**](FileSavingMode.md) |  | [optional] 
**summarization_degree** | [**DegreeEnum**](DegreeEnum.md) |  | [optional] 
**min_length** | **int** | Minimum length of the target text | [optional] 
**format** | [**TrialSupportedFormats**](TrialSupportedFormats.md) |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.summarization_trial_file_request import SummarizationTrialFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SummarizationTrialFileRequest from a JSON string
summarization_trial_file_request_instance = SummarizationTrialFileRequest.from_json(json)
# print the JSON string representation of the object
print(SummarizationTrialFileRequest.to_json())

# convert the object into a dict
summarization_trial_file_request_dict = summarization_trial_file_request_instance.to_dict()
# create an instance of SummarizationTrialFileRequest from a dict
summarization_trial_file_request_from_dict = SummarizationTrialFileRequest.from_dict(summarization_trial_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


