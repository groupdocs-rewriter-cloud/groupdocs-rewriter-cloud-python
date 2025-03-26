# GenerateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_offer_url** | **str** | Link to job offer | 
**cv_url** | **str** | Link to candidates CV | [optional] 
**cover_letter_url** | **str** | Link to candidates cover letter | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.generate_request import GenerateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateRequest from a JSON string
generate_request_instance = GenerateRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateRequest.to_json())

# convert the object into a dict
generate_request_dict = generate_request_instance.to_dict()
# create an instance of GenerateRequest from a dict
generate_request_from_dict = GenerateRequest.from_dict(generate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


