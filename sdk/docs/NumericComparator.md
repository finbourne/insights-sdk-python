# NumericComparator

Filters a numeric field by comparing it to a supplied numeric value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The comparison to apply between the field and Finbourne.Insights.WebApi.Dtos.Querying.NumericComparator.Value. One of the Finbourne.Insights.WebApi.Dtos.Querying.NumericOperation values (e.g. EqualTo, GreaterThan); discoverable via the queryable-fields metadata endpoint. | 
**value** | **float** | The value to compare the field against. | 
## Example

```python
from finbourne_insights.models.numeric_comparator import NumericComparator
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

operation: StrictStr = "example_operation"
value: Union[StrictFloat, StrictInt] = # Replace with your value
numeric_comparator_instance = NumericComparator(operation=operation, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

