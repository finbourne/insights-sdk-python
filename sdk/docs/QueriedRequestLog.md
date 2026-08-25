# QueriedRequestLog

Holds logged information about a request performed on an API, where only a subset of fields may be populated depending on which fields were requested via the QueryRequestLogs endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The timestamp of the request. | 
**id** | **str** | The identifier of the request. | 
**application** | **str** | The name of the application that the request was made to. | 
**operation** | **str** | The API operation invoked by the request. | 
**session_id** | **str** | The identifier of the session that the request was made in. | [optional] 
**verb** | **str** | The HTTP verb of the request. | [optional] 
**url** | **str** | The URL of the request. | [optional] 
**domain** | **str** | The domain of the request. | [optional] 
**user** | **str** | The user who made the request. | [optional] 
**user_type** | **str** | The type of the user who made the request. | [optional] 
**outcome** | **str** | The outcome of the request: Completed, Errored or Failed. | [optional] 
**duration** | **float** | The duration of the request in milliseconds. | [optional] 
**http_status_code** | **int** | The status code of the request. | [optional] 
**error_code** | **str** | Error code, if the request had a failure or error. | [optional] 
**sdk_language** | **str** | The language of the SDK used. | [optional] 
**sdk_version** | **str** | The version of the SDK used. | [optional] 
**source_application** | **str** | The name of the application that made the request. | [optional] 
**correlation_id** | **List[str]** | The chain of requestIds preceding this request | [optional] 
**impersonating_user** | **str** | The impersonating user. Only present if the request is an impersonated one | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_insights.models.queried_request_log import QueriedRequestLog
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

timestamp: datetime = # Replace with your value
id: StrictStr = "example_id"
application: StrictStr = "example_application"
operation: StrictStr = "example_operation"
session_id: Optional[StrictStr] = "example_session_id"
verb: Optional[StrictStr] = "example_verb"
url: Optional[StrictStr] = "example_url"
domain: Optional[StrictStr] = "example_domain"
user: Optional[StrictStr] = "example_user"
user_type: Optional[StrictStr] = "example_user_type"
outcome: Optional[StrictStr] = "example_outcome"
duration: Optional[Union[StrictFloat, StrictInt]] = # Replace with your value
http_status_code: Optional[StrictInt] = # Replace with your value
http_status_code: Optional[StrictInt] = None
error_code: Optional[StrictStr] = "example_error_code"
sdk_language: Optional[StrictStr] = "example_sdk_language"
sdk_version: Optional[StrictStr] = "example_sdk_version"
source_application: Optional[StrictStr] = "example_source_application"
correlation_id: Optional[List[StrictStr]] = # Replace with your value
impersonating_user: Optional[StrictStr] = "example_impersonating_user"
links: Optional[List[Link]] = None
queried_request_log_instance = QueriedRequestLog(timestamp=timestamp, id=id, application=application, operation=operation, session_id=session_id, verb=verb, url=url, domain=domain, user=user, user_type=user_type, outcome=outcome, duration=duration, http_status_code=http_status_code, error_code=error_code, sdk_language=sdk_language, sdk_version=sdk_version, source_application=source_application, correlation_id=correlation_id, impersonating_user=impersonating_user, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

