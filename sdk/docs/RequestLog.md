# RequestLog

Holds logged information about a request performed on an API.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | The timestamp of the request. | 
**application** | **str** | The name of the application that the request was made to. | 
**id** | **str** | The identifier of the request. | 
**session_id** | **str** | The identifier of the session that the request was made in. | [optional] 
**verb** | **str** | The HTTP verb of the request. | 
**url** | **str** | The URL of the request. | 
**domain** | **str** | The domain of the request. | [optional] 
**user** | **str** | The user who made the request. | 
**user_type** | **str** | The type of the user who made the request. | [optional] 
**operation** | **str** | The API operation invoked by the request. | [optional] 
**outcome** | **str** | The outcome of the request: Success, Failure or Error. | 
**duration** | **float** | The duration of the request in milliseconds. | 
**http_status_code** | **int** | The status code of the request. | 
**error_code** | **str** | Error code, if the request had a failure or error. | [optional] 
**sdk_language** | **str** | The language of the SDK used. | [optional] 
**sdk_version** | **str** | The version of the SDK used. | [optional] 
**source_application** | **str** | The name of the application that made the request. | [optional] 
**correlation_id** | **List[str]** | The chain of requestIds preceding this request | [optional] 
**impersonating_user** | **str** | The impersonating user. Only present if the request is an impersonated one | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_insights.models.request_log import RequestLog

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLog from a JSON string
request_log_instance = RequestLog.from_json(json)
# print the JSON string representation of the object
print RequestLog.to_json()

# convert the object into a dict
request_log_dict = request_log_instance.to_dict()
# create an instance of RequestLog from a dict
request_log_form_dict = request_log.from_dict(request_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


