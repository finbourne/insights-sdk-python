# AuditData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**category** | **str** |  | 
**user_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**resource** | [**Resource**](Resource.md) |  | [optional] 
**details_type** | **str** |  | [optional] 
**details** | **object** |  | [optional] 

## Example

```python
from finbourne_insights.models.audit_data import AuditData

# TODO update the JSON string below
json = "{}"
# create an instance of AuditData from a JSON string
audit_data_instance = AuditData.from_json(json)
# print the JSON string representation of the object
print AuditData.to_json()

# convert the object into a dict
audit_data_dict = audit_data_instance.to_dict()
# create an instance of AuditData from a dict
audit_data_form_dict = audit_data.from_dict(audit_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


