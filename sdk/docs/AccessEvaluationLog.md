# AccessEvaluationLog

Holds logged information about an access check performed on an API.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The timestamp of the access evaluation. | 
**application** | **str** | The name of the application that the request was made from. | 
**id** | **str** | The ID of the access evaluation. | 
**request_id** | **str** | The identifier of the request. | [optional] 
**session_id** | **str** | The identifier of the session that the request was made in. | [optional] 
**user** | **str** | The user who made the request. | 
**user_type** | **str** | The type of the user who made the request. | [optional] 
**duration** | **float** | The duration of the access evaluation. | 
**result** | **str** | The result of the access evaluation. | [optional] 
**authoritative_role_id** | **str** | The role that matched the access evaluation to provide a result. | [optional] 
**authoritative_policy_id** | **str** | The policy that matched the access evaluation to provide a result. | [optional] 
**authoritative_selector** | **str** | The selector that matched the access evaluation to provide a result. | [optional] 
**resource_type** | **str** | The type of the resource that the access evaluation is for. | [optional] 
**action** | **str** | The action key of the access evaluation. | [optional] 
**resource** | **Dict[str, str]** | The ID of the resource that the access evaluation is for. If the ResourceID could not be converted to a dictionary, it will return a single-value dictionary with the key \&quot;resourceId\&quot;. | [optional] 
**resource_from_effective_date** | **str** | The From effective date of the resource. | [optional] 
**resource_to_effective_date** | **str** | The To effective date of the resource. | [optional] 
**resource_from_as_at** | **str** | The From AsAt date of the resource. | [optional] 
**resource_to_as_at** | **str** | The To AsAt date of the resource. | [optional] 
**access_execution_time** | **str** | The execution time of the entitlement. | [optional] 
**access_as_at_time** | **str** | The AsAt time of the entitlement. | [optional] 
**required_licence_policy_id** | **str** | ID of the required licence policy. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_insights.models.access_evaluation_log import AccessEvaluationLog
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr, validator
from datetime import datetime
timestamp: datetime = # Replace with your value
application: StrictStr = "example_application"
id: StrictStr = "example_id"
request_id: Optional[StrictStr] = "example_request_id"
session_id: Optional[StrictStr] = "example_session_id"
user: StrictStr = "example_user"
user_type: Optional[StrictStr] = "example_user_type"
duration: Union[StrictFloat, StrictInt] = # Replace with your value
result: Optional[StrictStr] = "example_result"
authoritative_role_id: Optional[StrictStr] = "example_authoritative_role_id"
authoritative_policy_id: Optional[StrictStr] = "example_authoritative_policy_id"
authoritative_selector: Optional[StrictStr] = "example_authoritative_selector"
resource_type: Optional[StrictStr] = "example_resource_type"
action: Optional[StrictStr] = "example_action"
resource: Optional[Dict[str, StrictStr]] = # Replace with your value
resource_from_effective_date: Optional[StrictStr] = "example_resource_from_effective_date"
resource_to_effective_date: Optional[StrictStr] = "example_resource_to_effective_date"
resource_from_as_at: Optional[StrictStr] = "example_resource_from_as_at"
resource_to_as_at: Optional[StrictStr] = "example_resource_to_as_at"
access_execution_time: Optional[StrictStr] = "example_access_execution_time"
access_as_at_time: Optional[StrictStr] = "example_access_as_at_time"
required_licence_policy_id: Optional[StrictStr] = "example_required_licence_policy_id"
links: Optional[conlist(Link)] = None
access_evaluation_log_instance = AccessEvaluationLog(timestamp=timestamp, application=application, id=id, request_id=request_id, session_id=session_id, user=user, user_type=user_type, duration=duration, result=result, authoritative_role_id=authoritative_role_id, authoritative_policy_id=authoritative_policy_id, authoritative_selector=authoritative_selector, resource_type=resource_type, action=action, resource=resource, resource_from_effective_date=resource_from_effective_date, resource_to_effective_date=resource_to_effective_date, resource_from_as_at=resource_from_as_at, resource_to_as_at=resource_to_as_at, access_execution_time=access_execution_time, access_as_at_time=access_as_at_time, required_licence_policy_id=required_licence_policy_id, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

