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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

process: AuditProcess
data: AuditData
create_audit_entry_instance = CreateAuditEntry(process=process, data=data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

