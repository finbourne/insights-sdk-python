# ServiceRequests

The request volume and server-error rate for a single service over the window.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | The name of the service (application) that handled the requests. | [optional] 
**total_requests** | **int** | The number of requests over the window, or null if not reported. | [optional] 
**requests5xx** | **int** | The number of requests over the window that returned a 5xx status code, or null if not reported. | [optional] 
**pct5xx** | **float** | The percentage of requests that returned a 5xx status code, or null if not reported. | [optional] 
## Example

```python
from finbourne_insights.models.service_requests import ServiceRequests
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

service: Optional[StrictStr] = "example_service"
total_requests: Optional[StrictInt] = # Replace with your value
requests5xx: Optional[StrictInt] = # Replace with your value
pct5xx: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
service_requests_instance = ServiceRequests(service=service, total_requests=total_requests, requests5xx=requests5xx, pct5xx=pct5xx)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

