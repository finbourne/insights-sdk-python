# RequestsPerMinuteDataSet

Request volume, error count and total duration per minute, broken down by service and endpoint, over a rolling three hour window.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this data set. Always &#x60;RequestsPerMinute&#x60;, matching the corresponding Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet value and Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property. | 
**window_start** | **datetime** | Inclusive start of the window the data covers, in UTC, floored to a whole minute. | 
**window_end** | **datetime** | End of the window the data covers, in UTC, floored to a whole minute. | 
**truncated** | **bool** | True when the query reached the row cap, so the data covers only part of the window and totals are understated. False when the whole window was returned. | 
**values** | [**List[RequestsPerMinuteBucket]**](RequestsPerMinuteBucket.md) | The per-minute rows, ordered by minute, then service, then endpoint. | 
## Example

```python
from finbourne_insights.models.requests_per_minute_data_set import RequestsPerMinuteDataSet
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
window_start: datetime = # Replace with your value
window_end: datetime = # Replace with your value
truncated: StrictBool = # Replace with your value
truncated:StrictBool = True
values: List[RequestsPerMinuteBucket] = # Replace with your value
requests_per_minute_data_set_instance = RequestsPerMinuteDataSet(name=name, window_start=window_start, window_end=window_end, truncated=truncated, values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

