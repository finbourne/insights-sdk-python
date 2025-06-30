# VendorResponse

Details of a response to a request made to a vendor service.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the log. | 
**response** | **str** | The body of the response. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_insights.models.vendor_response import VendorResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

id: StrictStr = "example_id"
response: StrictStr = "example_response"
links: Optional[conlist(Link)] = None
vendor_response_instance = VendorResponse(id=id, response=response, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

