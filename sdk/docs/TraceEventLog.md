# TraceEventLog

Holds information about a trace event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_event_id** | **str** | The identifier of the trace event. | 
**trace_id** | **str** | The identifier of the parent trace. | 
**created_at** | **datetime** | The datetime at which the trace event was created. | 
**event_type** | **str** | The type of the trace event. | 
**origin** | **str** | Whether the event originated from the AI or the user | 
**content** | **str** | The content of the trace event. | 
**agent_scope** | **str** | The scope of the agent currently being interacted with | 
**agent_code** | **str** | The code identifier of the agent currently being interacted with | 
**agent_version** | **int** | The version of the circuit in which the trace event occurred. | 
**node_id** | **str** | The ID of the circuit&#39;s node at which the trace event occured. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_insights.models.trace_event_log import TraceEventLog
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

trace_event_id: StrictStr = "example_trace_event_id"
trace_id: StrictStr = "example_trace_id"
created_at: datetime = # Replace with your value
event_type: StrictStr = "example_event_type"
origin: StrictStr = "example_origin"
content: StrictStr = "example_content"
agent_scope: StrictStr = "example_agent_scope"
agent_code: StrictStr = "example_agent_code"
agent_version: StrictInt = # Replace with your value
agent_version: StrictInt = 42
node_id: StrictStr = "example_node_id"
links: Optional[List[Link]] = None
trace_event_log_instance = TraceEventLog(trace_event_id=trace_event_id, trace_id=trace_id, created_at=created_at, event_type=event_type, origin=origin, content=content, agent_scope=agent_scope, agent_code=agent_code, agent_version=agent_version, node_id=node_id, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

