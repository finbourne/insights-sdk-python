# RelativeBoundary

One end of a relative time range. Exactly one of the options must be set: Finbourne.Insights.WebApi.Dtos.Querying.RelativeBoundary.Now (the current instant), Finbourne.Insights.WebApi.Dtos.Querying.RelativeBoundary.Midnight (the start of the current day in the range's time zone), Finbourne.Insights.WebApi.Dtos.Querying.RelativeBoundary.Offset (a duration back from now) or Finbourne.Insights.WebApi.Dtos.Querying.RelativeBoundary.Absolute (an explicit instant).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**now** | **bool** | When &#x60;true&#x60;, this boundary is the current instant (\&quot;now\&quot;). | [optional] 
**midnight** | **bool** | When &#x60;true&#x60;, this boundary is the start of the current day (midnight) in the range&#39;s time zone. | [optional] 
**offset** | [**RelativeOffset**](RelativeOffset.md) |  | [optional] 
**absolute** | **datetime** | An explicit absolute instant. | [optional] 
## Example

```python
from finbourne_insights.models.relative_boundary import RelativeBoundary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

now: Optional[StrictBool] = # Replace with your value
now:Optional[StrictBool] = None
midnight: Optional[StrictBool] = # Replace with your value
midnight:Optional[StrictBool] = None
offset: Optional[RelativeOffset] = None
absolute: Optional[datetime] = # Replace with your value
relative_boundary_instance = RelativeBoundary(now=now, midnight=midnight, offset=offset, absolute=absolute)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

