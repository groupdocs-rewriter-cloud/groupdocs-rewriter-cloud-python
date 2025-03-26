# CloudTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **int** | Language of original text | [optional] 
**handler** | **str** | Defines handler in cloud service | [optional] 
**text** | **str** | Text to rewrite | [optional] 
**action** | **str** | Rewrite or summarize | [optional] 
**jobofferurl** | **str** | Link to job offer | [optional] 
**cvurl** | **str** | Link to candidates CV | [optional] 
**coverletterurl** | **str** | Link to candidates cover letter | [optional] 
**texts** | **List[str]** | Text array to rewrite | [optional] 
**suggestions** | **int** | Number of suggested variants, 3 maximum | [optional] 
**diversity** | **int** | Diversity of text | [optional] 
**tokenize** | **bool** | Should source and target texts be returned in tokenized form | [optional] 
**origin** | **str** | for analysis only | [optional] 
**originaltext** | **str** | Original text | [optional] 
**alternativetext** | **str** | Modified text | [optional] 
**request_id** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.cloud_text_request import CloudTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloudTextRequest from a JSON string
cloud_text_request_instance = CloudTextRequest.from_json(json)
# print the JSON string representation of the object
print(CloudTextRequest.to_json())

# convert the object into a dict
cloud_text_request_dict = cloud_text_request_instance.to_dict()
# create an instance of CloudTextRequest from a dict
cloud_text_request_from_dict = CloudTextRequest.from_dict(cloud_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


