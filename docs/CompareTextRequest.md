# CompareTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_text** | **str** | Original text | [optional] 
**alternative_text** | **str** | Modified text | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.compare_text_request import CompareTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CompareTextRequest from a JSON string
compare_text_request_instance = CompareTextRequest.from_json(json)
# print the JSON string representation of the object
print(CompareTextRequest.to_json())

# convert the object into a dict
compare_text_request_dict = compare_text_request_instance.to_dict()
# create an instance of CompareTextRequest from a dict
compare_text_request_from_dict = CompareTextRequest.from_dict(compare_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


