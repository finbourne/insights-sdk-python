# TraceEventLog

Holds information about a trace event.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_event_id** | **str** | The identifier of the trace event. | 
**trace_id** | **str** | The identifier of the parent trace. | 
**created_at** | **datetime** | The datetime at which the trace event was created. | 
**event_type** | **str** | The type of the trace event. | 
**content** | **str** | The content of the trace event. | 
**session_id** | **str** | The session ID of the trace event. | 
**circuit_id** | **str** | The ID of the circuit in which the trace event occurred. | 
**circuit_version** | **str** | The version of the circuit in which the trace event occurred. | 
**node_id** | **str** | The ID of the circuit&#39;s node at which the trace event occured. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_insights.models.trace_event_log import TraceEventLog
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr
from datetime import datetime
trace_event_id: StrictStr = "example_trace_event_id"
trace_id: StrictStr = "example_trace_id"
created_at: datetime = # Replace with your value
event_type: StrictStr = "example_event_type"
content: StrictStr = "example_content"
session_id: StrictStr = "example_session_id"
circuit_id: StrictStr = "example_circuit_id"
circuit_version: StrictStr = "example_circuit_version"
node_id: StrictStr = "example_node_id"
links: Optional[conlist(Link)] = None
trace_event_log_instance = TraceEventLog(trace_event_id=trace_event_id, trace_id=trace_id, created_at=created_at, event_type=event_type, content=content, session_id=session_id, circuit_id=circuit_id, circuit_version=circuit_version, node_id=node_id, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

