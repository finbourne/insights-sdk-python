# ServiceRequests24hDataSet

Request volume and server-error rate per service over a rolling twenty four hour window.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this data set. Always &#x60;ServiceRequests24h&#x60;, matching the corresponding Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet value and Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property. | 
**window_start** | **datetime** | Inclusive start of the window the data covers, in UTC, floored to a whole minute. | 
**window_end** | **datetime** | End of the window the data covers, in UTC, floored to a whole minute. | 
**truncated** | **bool** | True when the query reached the row cap, so some services are missing. False when the whole result set was returned. | 
**values** | [**List[ServiceRequests]**](ServiceRequests.md) | The rows, ordered by service. | 
## Example

```python
from finbourne_insights.models.service_requests24h_data_set import ServiceRequests24hDataSet
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
window_start: datetime = # Replace with your value
window_end: datetime = # Replace with your value
truncated: StrictBool = # Replace with your value
truncated:StrictBool = True
values: List[ServiceRequests] = # Replace with your value
service_requests24h_data_set_instance = ServiceRequests24hDataSet(name=name, window_start=window_start, window_end=window_end, truncated=truncated, values=values)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

