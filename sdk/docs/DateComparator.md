# DateComparator

Filters a date/time field by comparing it to a supplied date/time value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The comparison to apply between the field and Finbourne.Insights.WebApi.Dtos.Querying.DateComparator.Value. One of the Finbourne.Insights.WebApi.Dtos.Querying.DateOperation values (e.g. Before, OnOrAfter); discoverable via the queryable-fields metadata endpoint. | 
**value** | **datetime** | The value to compare the field against. | 
## Example

```python
from finbourne_insights.models.date_comparator import DateComparator
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

operation: StrictStr = "example_operation"
value: datetime = # Replace with your value
date_comparator_instance = DateComparator(operation=operation, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

