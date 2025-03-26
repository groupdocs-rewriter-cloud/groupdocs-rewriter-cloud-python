# SummarizationFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.summarization_file_response import SummarizationFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SummarizationFileResponse from a JSON string
summarization_file_response_instance = SummarizationFileResponse.from_json(json)
# print the JSON string representation of the object
print(SummarizationFileResponse.to_json())

# convert the object into a dict
summarization_file_response_dict = summarization_file_response_instance.to_dict()
# create an instance of SummarizationFileResponse from a dict
summarization_file_response_from_dict = SummarizationFileResponse.from_dict(summarization_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


