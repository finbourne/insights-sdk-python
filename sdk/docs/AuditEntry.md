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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr
from datetime import datetime
id: StrictStr = "example_id"
var_date: datetime = # Replace with your value
process: AuditProcess = # Replace with your value
data: AuditData = # Replace with your value
notes: Optional[conlist(AuditEntryNote)] = None
audit_entry_instance = AuditEntry(id=id, var_date=var_date, process=process, data=data, notes=notes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

