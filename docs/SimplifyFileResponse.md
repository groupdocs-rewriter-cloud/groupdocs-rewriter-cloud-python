# SimplifyFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.simplify_file_response import SimplifyFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifyFileResponse from a JSON string
simplify_file_response_instance = SimplifyFileResponse.from_json(json)
# print the JSON string representation of the object
print(SimplifyFileResponse.to_json())

# convert the object into a dict
simplify_file_response_dict = simplify_file_response_instance.to_dict()
# create an instance of SimplifyFileResponse from a dict
simplify_file_response_from_dict = SimplifyFileResponse.from_dict(simplify_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


