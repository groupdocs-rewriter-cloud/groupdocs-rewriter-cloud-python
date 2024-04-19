# ParaphraseFileResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**HttpStatusCode**](HttpStatusCode.md) |  | [optional] 
**message** | **str** | Information about process | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.paraphrase_file_response import ParaphraseFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ParaphraseFileResponse from a JSON string
paraphrase_file_response_instance = ParaphraseFileResponse.from_json(json)
# print the JSON string representation of the object
print ParaphraseFileResponse.to_json()

# convert the object into a dict
paraphrase_file_response_dict = paraphrase_file_response_instance.to_dict()
# create an instance of ParaphraseFileResponse from a dict
paraphrase_file_response_form_dict = paraphrase_file_response.from_dict(paraphrase_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


