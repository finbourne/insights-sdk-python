# RequestsPerMinuteBucket

One minute of request activity for a single service and endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minute_bucket** | **datetime** | Start of the whole minute this row covers, in UTC. | 
**service** | **str** | The name of the service (application) that handled the requests. | [optional] 
**endpoint** | **str** | The endpoint (API operation) the requests were made to. | [optional] 
**total_requests** | **int** | The number of requests in this minute, or null if not reported. | [optional] 
**requests5xx** | **int** | The number of requests in this minute that returned a 5xx status code, or null if not reported. | [optional] 
**duration_sum_ms** | **float** | The sum of the request durations in this minute, in milliseconds, or null if not reported. | [optional] 
## Example

```python
from finbourne_insights.models.requests_per_minute_bucket import RequestsPerMinuteBucket
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

minute_bucket: datetime = # Replace with your value
service: Optional[StrictStr] = "example_service"
endpoint: Optional[StrictStr] = "example_endpoint"
total_requests: Optional[StrictInt] = # Replace with your value
requests5xx: Optional[StrictInt] = # Replace with your value
duration_sum_ms: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
requests_per_minute_bucket_instance = RequestsPerMinuteBucket(minute_bucket=minute_bucket, service=service, endpoint=endpoint, total_requests=total_requests, requests5xx=requests5xx, duration_sum_ms=duration_sum_ms)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

