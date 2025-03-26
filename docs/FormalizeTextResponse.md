# FormalizeTextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**formalize_result** | **str** |  | [optional] 
**formalize_results** | **List[str]** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.formalize_text_response import FormalizeTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FormalizeTextResponse from a JSON string
formalize_text_response_instance = FormalizeTextResponse.from_json(json)
# print the JSON string representation of the object
print(FormalizeTextResponse.to_json())

# convert the object into a dict
formalize_text_response_dict = formalize_text_response_instance.to_dict()
# create an instance of FormalizeTextResponse from a dict
formalize_text_response_from_dict = FormalizeTextResponse.from_dict(formalize_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


