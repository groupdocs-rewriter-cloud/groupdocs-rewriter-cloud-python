# SimplifyTextResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**simplify_reult** | **str** |  | [optional] 
**simplify_results** | **List[str]** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.simplify_text_response import SimplifyTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifyTextResponse from a JSON string
simplify_text_response_instance = SimplifyTextResponse.from_json(json)
# print the JSON string representation of the object
print SimplifyTextResponse.to_json()

# convert the object into a dict
simplify_text_response_dict = simplify_text_response_instance.to_dict()
# create an instance of SimplifyTextResponse from a dict
simplify_text_response_form_dict = simplify_text_response.from_dict(simplify_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


