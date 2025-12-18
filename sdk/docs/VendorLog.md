# VendorLog

Holds logged information about a request made to an external vendor.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of a log entry. | 
**provider** | **str** | The provider or service name. | 
**timestamp** | **datetime** | Timestamp of when the log was generated. | 
**type** | **str** | Type of log. Possible values: HttpResponse. | 
**destination_url** | **str** | The destination URL of the task. | 
**operation** | **str** | The operation performed. Possible values: Evaluate. | 
**outcome** | **str** | The outcome of the operation. Possible values: Success, Failure. | 
**duration** | **float** | The duration of the operation in ms. | 
**http_status_code** | **int** | The status code of the operation. | 
**user_id** | **str** | The user that made the request to LUSID. | 
**request_id** | **str** | The ID of the request to LUSID. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_insights.models.vendor_log import VendorLog
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
provider: StrictStr = "example_provider"
timestamp: datetime = # Replace with your value
type: StrictStr = "example_type"
destination_url: StrictStr = "example_destination_url"
operation: StrictStr = "example_operation"
outcome: StrictStr = "example_outcome"
duration: Union[StrictFloat, StrictInt] = # Replace with your value
http_status_code: StrictInt = # Replace with your value
http_status_code: StrictInt = 42
user_id: StrictStr = "example_user_id"
request_id: StrictStr = "example_request_id"
links: Optional[List[Link]] = None
vendor_log_instance = VendorLog(id=id, provider=provider, timestamp=timestamp, type=type, destination_url=destination_url, operation=operation, outcome=outcome, duration=duration, http_status_code=http_status_code, user_id=user_id, request_id=request_id, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

