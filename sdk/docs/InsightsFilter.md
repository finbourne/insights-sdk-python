# InsightsFilter

A single filter applied to a queryable log field. Exactly one comparator (Finbourne.Insights.WebApi.Dtos.Querying.InsightsFilter.Text, Finbourne.Insights.WebApi.Dtos.Querying.InsightsFilter.Numeric, Finbourne.Insights.WebApi.Dtos.Querying.InsightsFilter.Date or Finbourne.Insights.WebApi.Dtos.Querying.InsightsFilter.Boolean) must be populated, and its type must match the data type of the field named by Finbourne.Insights.WebApi.Dtos.Querying.InsightsFilter.Field. The available comparator and operation for a field can be discovered via the queryable-fields metadata endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | The name of the field to filter on (case-insensitive). Must be a filterable field of the queried log type. | 
**text** | [**TextComparator**](TextComparator.md) |  | [optional] 
**numeric** | [**NumericComparator**](NumericComparator.md) |  | [optional] 
**var_date** | [**DateComparator**](DateComparator.md) |  | [optional] 
**boolean** | [**BooleanComparator**](BooleanComparator.md) |  | [optional] 
## Example

```python
from finbourne_insights.models.insights_filter import InsightsFilter
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

field: StrictStr = "example_field"
text: Optional[TextComparator] = None
numeric: Optional[NumericComparator] = None
var_date: Optional[DateComparator] = # Replace with your value
boolean: Optional[BooleanComparator] = None
insights_filter_instance = InsightsFilter(field=field, text=text, numeric=numeric, var_date=var_date, boolean=boolean)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

