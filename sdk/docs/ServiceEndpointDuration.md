# ServiceEndpointDuration

The request duration distribution for a single service and endpoint over the window.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | The name of the service (application) that handled the requests. | [optional] 
**endpoint** | **str** | The endpoint (API operation) the requests were made to. | [optional] 
**total_requests** | **int** | The number of requests over the window, or null if not reported. | [optional] 
**mean_duration_ms** | **float** | The mean request duration in milliseconds, or null if not reported. | [optional] 
**median_duration_ms** | **float** | The median (50th percentile) request duration in milliseconds, or null if not reported. | [optional] 
**p95_duration_ms** | **float** | The 95th percentile request duration in milliseconds, or null if not reported. | [optional] 
## Example

```python
from finbourne_insights.models.service_endpoint_duration import ServiceEndpointDuration
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

service: Optional[StrictStr] = "example_service"
endpoint: Optional[StrictStr] = "example_endpoint"
total_requests: Optional[StrictInt] = # Replace with your value
mean_duration_ms: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
median_duration_ms: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
p95_duration_ms: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
service_endpoint_duration_instance = ServiceEndpointDuration(service=service, endpoint=endpoint, total_requests=total_requests, mean_duration_ms=mean_duration_ms, median_duration_ms=median_duration_ms, p95_duration_ms=p95_duration_ms)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

