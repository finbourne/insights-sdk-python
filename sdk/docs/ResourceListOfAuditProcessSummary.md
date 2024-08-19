# ResourceListOfAuditProcessSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[AuditProcessSummary]**](AuditProcessSummary.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from finbourne_insights.models.resource_list_of_audit_process_summary import ResourceListOfAuditProcessSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfAuditProcessSummary from a JSON string
resource_list_of_audit_process_summary_instance = ResourceListOfAuditProcessSummary.from_json(json)
# print the JSON string representation of the object
print ResourceListOfAuditProcessSummary.to_json()

# convert the object into a dict
resource_list_of_audit_process_summary_dict = resource_list_of_audit_process_summary_instance.to_dict()
# create an instance of ResourceListOfAuditProcessSummary from a dict
resource_list_of_audit_process_summary_form_dict = resource_list_of_audit_process_summary.from_dict(resource_list_of_audit_process_summary_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


