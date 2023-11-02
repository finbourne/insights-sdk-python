# AuditEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**var_date** | **datetime** |  | 
**process** | [**AuditProcess**](AuditProcess.md) |  | 
**data** | [**AuditData**](AuditData.md) |  | 
**notes** | [**List[AuditEntryNote]**](AuditEntryNote.md) |  | [optional] 

## Example

```python
from finbourne_insights.models.audit_entry import AuditEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEntry from a JSON string
audit_entry_instance = AuditEntry.from_json(json)
# print the JSON string representation of the object
print AuditEntry.to_json()

# convert the object into a dict
audit_entry_dict = audit_entry_instance.to_dict()
# create an instance of AuditEntry from a dict
audit_entry_form_dict = audit_entry.from_dict(audit_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


