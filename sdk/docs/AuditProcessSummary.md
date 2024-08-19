# AuditProcessSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process** | [**AuditProcess**](AuditProcess.md) |  | [optional] 
**latest_entry** | [**AuditData**](AuditData.md) |  | [optional] 
**summary** | [**AuditDataSummary**](AuditDataSummary.md) |  | [optional] 

## Example

```python
from finbourne_insights.models.audit_process_summary import AuditProcessSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AuditProcessSummary from a JSON string
audit_process_summary_instance = AuditProcessSummary.from_json(json)
# print the JSON string representation of the object
print AuditProcessSummary.to_json()

# convert the object into a dict
audit_process_summary_dict = audit_process_summary_instance.to_dict()
# create an instance of AuditProcessSummary from a dict
audit_process_summary_form_dict = audit_process_summary.from_dict(audit_process_summary_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


