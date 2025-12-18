# TraceDiagramNode

Represents a node within a trace diagram.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the node. | [optional] 
**display_name** | **str** | Display name of the node. | [optional] 
**level** | **int** | Depth level of the node within the diagram. | [optional] 
**parent** | **str** | Identifier of the node&#39;s parent. This is null for the root node. | [optional] 
**type** | **str** | Type classification of the node. | [optional] 
**agent_scope** | **str** | The scope of the agent. | [optional] 
**agent_version** | **int** | The version of the agent. | [optional] 
## Example

```python
from finbourne_insights.models.trace_diagram_node import TraceDiagramNode
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictStr] = "example_id"
display_name: Optional[StrictStr] = "example_display_name"
level: Optional[StrictInt] = # Replace with your value
level: Optional[StrictInt] = None
parent: Optional[StrictStr] = "example_parent"
type: Optional[StrictStr] = "example_type"
agent_scope: Optional[StrictStr] = "example_agent_scope"
agent_version: Optional[StrictInt] = # Replace with your value
agent_version: Optional[StrictInt] = None
trace_diagram_node_instance = TraceDiagramNode(id=id, display_name=display_name, level=level, parent=parent, type=type, agent_scope=agent_scope, agent_version=agent_version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

