# AuditProcess

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**run_id** | **str** |  | 
**start_time** | **datetime** |  | 
**end_time** | **datetime** |  | [optional] 
**succeeded** | **bool** |  | [optional] 
## Example

```python
from finbourne_insights.models.audit_process import AuditProcess
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, constr
from datetime import datetime
name: StrictStr = "example_name"
run_id: StrictStr = "example_run_id"
start_time: datetime = # Replace with your value
end_time: Optional[datetime] = # Replace with your value
succeeded: Optional[StrictBool] = None
succeeded:Optional[StrictBool] = None
audit_process_instance = AuditProcess(name=name, run_id=run_id, start_time=start_time, end_time=end_time, succeeded=succeeded)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

