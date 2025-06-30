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
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

process: AuditProcess = # Replace with your value
data: AuditData = # Replace with your value
create_audit_entry_instance = CreateAuditEntry(process=process, data=data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

