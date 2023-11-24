# SummarizationTextRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Set language of text | 
**text** | **str** | Single text paragraph | [optional] 
**texts** | **List[str]** | Text paragraphs | [optional] 
**origin** | **str** | Information about SDK user, like a User-Agent | [optional] 
**summarization_degree** | [**DegreeEnum**](DegreeEnum.md) |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.summarization_text_request import SummarizationTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SummarizationTextRequest from a JSON string
summarization_text_request_instance = SummarizationTextRequest.from_json(json)
# print the JSON string representation of the object
print SummarizationTextRequest.to_json()

# convert the object into a dict
summarization_text_request_dict = summarization_text_request_instance.to_dict()
# create an instance of SummarizationTextRequest from a dict
summarization_text_request_form_dict = summarization_text_request.from_dict(summarization_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


