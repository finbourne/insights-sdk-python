# RelativeOffset

A relative offset back from \"now\", e.g. `{ Amount = 2, Unit = Hours }` meaning two hours before now.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The number of units to go back from now. Must be at least 1. | 
**unit** | **str** | The unit of the offset. One of the Finbourne.Insights.WebApi.Dtos.Querying.RelativeTimeUnit values. | 
## Example

```python
from finbourne_insights.models.relative_offset import RelativeOffset
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

amount: StrictInt = # Replace with your value
amount: StrictInt = 42
unit: StrictStr = "example_unit"
relative_offset_instance = RelativeOffset(amount=amount, unit=unit)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

