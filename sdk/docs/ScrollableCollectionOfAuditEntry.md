# ScrollableCollectionOfAuditEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuditEntry]**](AuditEntry.md) |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from finbourne_insights.models.scrollable_collection_of_audit_entry import ScrollableCollectionOfAuditEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ScrollableCollectionOfAuditEntry from a JSON string
scrollable_collection_of_audit_entry_instance = ScrollableCollectionOfAuditEntry.from_json(json)
# print the JSON string representation of the object
print ScrollableCollectionOfAuditEntry.to_json()

# convert the object into a dict
scrollable_collection_of_audit_entry_dict = scrollable_collection_of_audit_entry_instance.to_dict()
# create an instance of ScrollableCollectionOfAuditEntry from a dict
scrollable_collection_of_audit_entry_form_dict = scrollable_collection_of_audit_entry.from_dict(scrollable_collection_of_audit_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


