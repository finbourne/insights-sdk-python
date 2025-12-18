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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
var_date: datetime = # Replace with your value
process: AuditProcess
data: AuditData
notes: Optional[List[AuditEntryNote]] = None
audit_entry_instance = AuditEntry(id=id, var_date=var_date, process=process, data=data, notes=notes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

