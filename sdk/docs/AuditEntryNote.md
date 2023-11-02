# AuditEntryNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**text** | **str** |  | 
**var_date** | **datetime** |  | 

## Example

```python
from finbourne_insights.models.audit_entry_note import AuditEntryNote

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEntryNote from a JSON string
audit_entry_note_instance = AuditEntryNote.from_json(json)
# print the JSON string representation of the object
print AuditEntryNote.to_json()

# convert the object into a dict
audit_entry_note_dict = audit_entry_note_instance.to_dict()
# create an instance of AuditEntryNote from a dict
audit_entry_note_form_dict = audit_entry_note.from_dict(audit_entry_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


