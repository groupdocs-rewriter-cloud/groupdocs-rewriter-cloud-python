# GenerateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**generate_result** | **str** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.generate_response import GenerateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateResponse from a JSON string
generate_response_instance = GenerateResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateResponse.to_json())

# convert the object into a dict
generate_response_dict = generate_response_instance.to_dict()
# create an instance of GenerateResponse from a dict
generate_response_from_dict = GenerateResponse.from_dict(generate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


