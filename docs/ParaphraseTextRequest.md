# ParaphraseTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**text** | **str** | Single text paragraph | [optional] 
**texts** | **List[str]** | Text paragraphs | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**suggestions** | **str** | Number of variants for rewriting | [optional] 
**diversity_degree** | [**DegreeEnum**](DegreeEnum.md) |  | [optional] 
**tokenize** | **bool** | Determines whether to return a tokens list | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.paraphrase_text_request import ParaphraseTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ParaphraseTextRequest from a JSON string
paraphrase_text_request_instance = ParaphraseTextRequest.from_json(json)
# print the JSON string representation of the object
print(ParaphraseTextRequest.to_json())

# convert the object into a dict
paraphrase_text_request_dict = paraphrase_text_request_instance.to_dict()
# create an instance of ParaphraseTextRequest from a dict
paraphrase_text_request_from_dict = ParaphraseTextRequest.from_dict(paraphrase_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


