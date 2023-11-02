# Response

DTO of Finbourne.AspNetCore.Http.TrackingEntry.ResponseInformation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **Dict[str, List[str]]** | The headers | [optional] 
**content_length** | **int** | The actual length of the body, which may be larger than the data recorded in Finbourne.Insights.WebApi.Dtos.Response.Body  (e.g. if actual Body is large, or not convertible to a string) | [optional] 
**content_type** | **str** | The content type | [optional] 
**body** | **str** | The recorded content. | [optional] 
**body_was_truncated** | **bool** | Determines if the recorded body was truncated. | [optional] 
**status_code** | **int** | Http Status Code of the request. | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_insights.models.response import Response

# TODO update the JSON string below
json = "{}"
# create an instance of Response from a JSON string
response_instance = Response.from_json(json)
# print the JSON string representation of the object
print Response.to_json()

# convert the object into a dict
response_dict = response_instance.to_dict()
# create an instance of Response from a dict
response_form_dict = response.from_dict(response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


