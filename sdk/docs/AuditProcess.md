# AuditProcess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**run_id** | **str** |  | 
**start_time** | **datetime** |  | 
**end_time** | **datetime** |  | [optional] 
**succeeded** | **bool** |  | [optional] 

## Example

```python
from finbourne_insights.models.audit_process import AuditProcess

# TODO update the JSON string below
json = "{}"
# create an instance of AuditProcess from a JSON string
audit_process_instance = AuditProcess.from_json(json)
# print the JSON string representation of the object
print AuditProcess.to_json()

# convert the object into a dict
audit_process_dict = audit_process_instance.to_dict()
# create an instance of AuditProcess from a dict
audit_process_form_dict = audit_process.from_dict(audit_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


