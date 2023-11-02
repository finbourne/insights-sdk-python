# CreateAuditEntry

Details to create an audit entry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process** | [**AuditProcess**](AuditProcess.md) |  | 
**data** | [**AuditData**](AuditData.md) |  | 

## Example

```python
from finbourne_insights.models.create_audit_entry import CreateAuditEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuditEntry from a JSON string
create_audit_entry_instance = CreateAuditEntry.from_json(json)
# print the JSON string representation of the object
print CreateAuditEntry.to_json()

# convert the object into a dict
create_audit_entry_dict = create_audit_entry_instance.to_dict()
# create an instance of CreateAuditEntry from a dict
create_audit_entry_form_dict = create_audit_entry.from_dict(create_audit_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


