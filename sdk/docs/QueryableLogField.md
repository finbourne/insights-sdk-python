# QueryableLogField

Describes a field of a log type that can be selected and (where Finbourne.Insights.WebApi.Dtos.Querying.QueryableLogField.Filterable is set) filtered when querying logs, including the comparator operations available for it. Returned by the queryable-fields metadata endpoint so a UI can advertise the correct comparators for each field.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field, as used when requesting it or filtering on it (case-insensitive). | 
**data_type** | **str** | The data type of the field: Text, Numeric, Date or Boolean. | 
**supported_operations** | **List[str]** | The comparator operations available for this field. Empty when the field is not filterable. | 
**filterable** | **bool** | Whether the field can be used in a filter. | [optional] 
**always_returned** | **bool** | Whether the field is always returned (and therefore need not be requested). | [optional] 
## Example

```python
from finbourne_insights.models.queryable_log_field import QueryableLogField
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
data_type: StrictStr = "example_data_type"
supported_operations: List[StrictStr] = # Replace with your value
filterable: Optional[StrictBool] = # Replace with your value
filterable:Optional[StrictBool] = None
always_returned: Optional[StrictBool] = # Replace with your value
always_returned:Optional[StrictBool] = None
queryable_log_field_instance = QueryableLogField(name=name, data_type=data_type, supported_operations=supported_operations, filterable=filterable, always_returned=always_returned)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

