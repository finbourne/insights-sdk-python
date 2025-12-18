# TraceDiagramEdge

Represents an edge connecting two nodes within a trace diagram.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Sequential identifier of the edge. | [optional] 
**node_id** | **str** | Identifier of the parent node. | [optional] 
**child_node_id** | **str** | Identifier of the child node. | [optional] 
**label** | **str** | Label displayed for the edge. | [optional] 
## Example

```python
from finbourne_insights.models.trace_diagram_edge import TraceDiagramEdge
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictInt] = # Replace with your value
id: Optional[StrictInt] = None
node_id: Optional[StrictStr] = "example_node_id"
child_node_id: Optional[StrictStr] = "example_child_node_id"
label: Optional[StrictStr] = "example_label"
trace_diagram_edge_instance = TraceDiagramEdge(id=id, node_id=node_id, child_node_id=child_node_id, label=label)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

