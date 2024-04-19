# SynonymizeTextResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**synonymizer_results** | **List[str]** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.synonymize_text_response import SynonymizeTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SynonymizeTextResponse from a JSON string
synonymize_text_response_instance = SynonymizeTextResponse.from_json(json)
# print the JSON string representation of the object
print SynonymizeTextResponse.to_json()

# convert the object into a dict
synonymize_text_response_dict = synonymize_text_response_instance.to_dict()
# create an instance of SynonymizeTextResponse from a dict
synonymize_text_response_form_dict = synonymize_text_response.from_dict(synonymize_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


