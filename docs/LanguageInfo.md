# LanguageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**actions** | **List[str]** |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.language_info import LanguageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageInfo from a JSON string
language_info_instance = LanguageInfo.from_json(json)
# print the JSON string representation of the object
print(LanguageInfo.to_json())

# convert the object into a dict
language_info_dict = language_info_instance.to_dict()
# create an instance of LanguageInfo from a dict
language_info_from_dict = LanguageInfo.from_dict(language_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


