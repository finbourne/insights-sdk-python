# TextComparator

Filters a text field. Single-value operations (EqualTo, NotEqualTo, StartsWith, EndsWith) compare the field to Finbourne.Insights.WebApi.Dtos.Querying.TextComparator.Value; set operations (In, NotIn) compare it to Finbourne.Insights.WebApi.Dtos.Querying.TextComparator.Values. Exactly one of Finbourne.Insights.WebApi.Dtos.Querying.TextComparator.Value or Finbourne.Insights.WebApi.Dtos.Querying.TextComparator.Values is supplied, matching the chosen Finbourne.Insights.WebApi.Dtos.Querying.TextComparator.Operation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The comparison to apply between the field and the supplied value(s). One of the Finbourne.Insights.WebApi.Dtos.Querying.TextOperation values (e.g. EqualTo, StartsWith, In); discoverable via the queryable-fields metadata endpoint. | 
**value** | **str** | The value to compare the field against, for the single-value operations (EqualTo, NotEqualTo, StartsWith, EndsWith). | [optional] 
**values** | **List[str]** | The set of values to compare the field against, for the set operations (In, NotIn). | [optional] 
## Example

```python
from finbourne_insights.models.text_comparator import TextComparator
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

operation: StrictStr = "example_operation"
value: Optional[StrictStr] = "example_value"
values: Optional[List[StrictStr]] = # Replace with your value
text_comparator_instance = TextComparator(operation=operation, value=value, values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

