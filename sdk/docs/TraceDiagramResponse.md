# TraceDiagramResponse

Represents a trace diagram composed of nodes and edges.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[TraceDiagramNode]**](TraceDiagramNode.md) | The nodes that make up the diagram. | [optional] 
**edges** | [**List[TraceDiagramEdge]**](TraceDiagramEdge.md) | The edges that connect the nodes in the diagram. | [optional] 
## Example

```python
from finbourne_insights.models.trace_diagram_response import TraceDiagramResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

nodes: Optional[List[TraceDiagramNode]] = # Replace with your value
edges: Optional[List[TraceDiagramEdge]] = # Replace with your value
trace_diagram_response_instance = TraceDiagramResponse(nodes=nodes, edges=edges)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

