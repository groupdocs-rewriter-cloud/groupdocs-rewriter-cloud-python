# Model


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loaded** | **bool** |  | [optional] 
**models_id** | **int** |  | [optional] 
**models** | **List[str]** |  | [optional] 
**opt** | [**Opt**](Opt.md) |  | [optional] 
**timeout** | **int** |  | [optional] 
**tokenizer** | [**Tokenizer**](Tokenizer.md) |  | [optional] 

## Example

```python
from groupdocs_rewriter_cloud.models.model import Model

# TODO update the JSON string below
json = "{}"
# create an instance of Model from a JSON string
model_instance = Model.from_json(json)
# print the JSON string representation of the object
print Model.to_json()

# convert the object into a dict
model_dict = model_instance.to_dict()
# create an instance of Model from a dict
model_form_dict = model.from_dict(model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


