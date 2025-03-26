# HealthCheckInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_processor_status** | **str** |  | [optional] 
**paraphrasing_status** | **str** |  | [optional] 
**detector_status** | **str** |  | [optional] 
**summarization_status** | **str** |  | [optional] 
**gpu_info_status_code** | **str** |  | [optional] 
**gpu_info_message** | **str** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.health_check_info import HealthCheckInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HealthCheckInfo from a JSON string
health_check_info_instance = HealthCheckInfo.from_json(json)
# print the JSON string representation of the object
print(HealthCheckInfo.to_json())

# convert the object into a dict
health_check_info_dict = health_check_info_instance.to_dict()
# create an instance of HealthCheckInfo from a dict
health_check_info_from_dict = HealthCheckInfo.from_dict(health_check_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


