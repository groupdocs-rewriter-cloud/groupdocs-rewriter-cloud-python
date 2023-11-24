# SynonymizeTextRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**text** | **str** | Single text paragraph | [optional] 
**texts** | **List[str]** | Text paragraphs | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**synonyms** | **str** | Number of variants for rewriting | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.synonymize_text_request import SynonymizeTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SynonymizeTextRequest from a JSON string
synonymize_text_request_instance = SynonymizeTextRequest.from_json(json)
# print the JSON string representation of the object
print SynonymizeTextRequest.to_json()

# convert the object into a dict
synonymize_text_request_dict = synonymize_text_request_instance.to_dict()
# create an instance of SynonymizeTextRequest from a dict
synonymize_text_request_form_dict = synonymize_text_request.from_dict(synonymize_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


