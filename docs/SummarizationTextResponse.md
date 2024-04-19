# SummarizationTextResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**summarization_result** | **str** |  | [optional] 
**summarization_results** | **List[str]** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.summarization_text_response import SummarizationTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SummarizationTextResponse from a JSON string
summarization_text_response_instance = SummarizationTextResponse.from_json(json)
# print the JSON string representation of the object
print SummarizationTextResponse.to_json()

# convert the object into a dict
summarization_text_response_dict = summarization_text_response_instance.to_dict()
# create an instance of SummarizationTextResponse from a dict
summarization_text_response_form_dict = summarization_text_response.from_dict(summarization_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


