# AuditDataSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] [readonly] 
**categories** | **Dict[str, int]** |  | [optional] 

## Example

```python
from finbourne_insights.models.audit_data_summary import AuditDataSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AuditDataSummary from a JSON string
audit_data_summary_instance = AuditDataSummary.from_json(json)
# print the JSON string representation of the object
print AuditDataSummary.to_json()

# convert the object into a dict
audit_data_summary_dict = audit_data_summary_instance.to_dict()
# create an instance of AuditDataSummary from a dict
audit_data_summary_form_dict = audit_data_summary.from_dict(audit_data_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


