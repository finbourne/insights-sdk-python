# QueryableLogType

The queryable fields of a single log type, returned by the queryable-fields metadata endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_type** | **str** | The log type, e.g. Requests, Vendor, Access, Trace or TraceEvent. | 
**fields** | [**List[QueryableLogField]**](QueryableLogField.md) | The fields of this log type that can be selected and/or filtered. | 
## Example

```python
from finbourne_insights.models.queryable_log_type import QueryableLogType
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

log_type: StrictStr = "example_log_type"
fields: List[QueryableLogField] = # Replace with your value
queryable_log_type_instance = QueryableLogType(log_type=log_type, fields=fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

