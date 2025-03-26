# FormalizeFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.formalize_file_response import FormalizeFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FormalizeFileResponse from a JSON string
formalize_file_response_instance = FormalizeFileResponse.from_json(json)
# print the JSON string representation of the object
print(FormalizeFileResponse.to_json())

# convert the object into a dict
formalize_file_response_dict = formalize_file_response_instance.to_dict()
# create an instance of FormalizeFileResponse from a dict
formalize_file_response_from_dict = FormalizeFileResponse.from_dict(formalize_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


