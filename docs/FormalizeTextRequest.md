# FormalizeTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**text** | **str** | Single text paragraph | [optional] 
**texts** | **List[str]** | Text paragraphs | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.formalize_text_request import FormalizeTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FormalizeTextRequest from a JSON string
formalize_text_request_instance = FormalizeTextRequest.from_json(json)
# print the JSON string representation of the object
print(FormalizeTextRequest.to_json())

# convert the object into a dict
formalize_text_request_dict = formalize_text_request_instance.to_dict()
# create an instance of FormalizeTextRequest from a dict
formalize_text_request_from_dict = FormalizeTextRequest.from_dict(formalize_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


