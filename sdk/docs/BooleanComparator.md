# BooleanComparator

Filters a boolean field by comparing it to a supplied boolean value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The comparison to apply between the field and Finbourne.Insights.WebApi.Dtos.Querying.BooleanComparator.Value. One of the Finbourne.Insights.WebApi.Dtos.Querying.BooleanOperation values (EqualTo, NotEqualTo); discoverable via the queryable-fields metadata endpoint. | 
**value** | **bool** | The value to compare the field against. | 
## Example

```python
from finbourne_insights.models.boolean_comparator import BooleanComparator
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

operation: StrictStr = "example_operation"
value: StrictBool = # Replace with your value
value:StrictBool = True
boolean_comparator_instance = BooleanComparator(operation=operation, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

