# CompareTextResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**probability** | **float** | The probability that the text turned out to be paraphrased | [optional] 
**is_paraphrased_or_translated** | **bool** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.compare_text_response import CompareTextResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompareTextResponse from a JSON string
compare_text_response_instance = CompareTextResponse.from_json(json)
# print the JSON string representation of the object
print(CompareTextResponse.to_json())

# convert the object into a dict
compare_text_response_dict = compare_text_response_instance.to_dict()
# create an instance of CompareTextResponse from a dict
compare_text_response_from_dict = CompareTextResponse.from_dict(compare_text_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


