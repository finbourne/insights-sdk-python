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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist

headers: Optional[Dict[str, conlist(StrictStr)]] = # Replace with your value
content_length: Optional[StrictInt] = # Replace with your value
content_type: Optional[StrictStr] = "example_content_type"
body: Optional[StrictStr] = "example_body"
body_was_truncated: Optional[StrictBool] = # Replace with your value
body_was_truncated:Optional[StrictBool] = None
status_code: Optional[StrictInt] = # Replace with your value
status_code: Optional[StrictInt] = None
links: Optional[conlist(Link)] = None
response_instance = Response(headers=headers, content_length=content_length, content_type=content_type, body=body, body_was_truncated=body_was_truncated, status_code=status_code, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

