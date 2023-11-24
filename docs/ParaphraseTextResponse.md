# ParaphraseTextResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**paraphrase_reult** | **str** |  | [optional] 
**paraphrase_results** | **List[str]** |  | [optional] 
**source_list** | **List[str]** | Return tokenized source text | [optional] 
**target_list** | **List[str]** | Return tokenized target text | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.paraphrase_text_response import ParaphraseTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ParaphraseTextResponse from a JSON string
paraphrase_text_response_instance = ParaphraseTextResponse.from_json(json)
# print the JSON string representation of the object
print ParaphraseTextResponse.to_json()

# convert the object into a dict
paraphrase_text_response_dict = paraphrase_text_response_instance.to_dict()
# create an instance of ParaphraseTextResponse from a dict
paraphrase_text_response_form_dict = paraphrase_text_response.from_dict(paraphrase_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


