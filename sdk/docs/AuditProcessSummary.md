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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

process: Optional[AuditProcess] = None
latest_entry: Optional[AuditData] = # Replace with your value
summary: Optional[AuditDataSummary] = None
audit_process_summary_instance = AuditProcessSummary(process=process, latest_entry=latest_entry, summary=summary)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

