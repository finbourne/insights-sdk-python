# TraceLog

Holds metadata for a trace.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_id** | **str** | The identifier of the trace. | 
**created_at** | **datetime** | The datetime at which the trace was created. | 
**user_id** | **str** | The id of the user who created the trace. | 
**description** | **str** | The description of the trace. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_insights.models.trace_log import TraceLog
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

trace_id: StrictStr = "example_trace_id"
created_at: datetime = # Replace with your value
user_id: StrictStr = "example_user_id"
description: Optional[StrictStr] = "example_description"
links: Optional[List[Link]] = None
trace_log_instance = TraceLog(trace_id=trace_id, created_at=created_at, user_id=user_id, description=description, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

