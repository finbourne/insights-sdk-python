# VendorRequest

Details of a request made to a vendor service.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the log. | 
**request** | **str** | The body of the request. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_insights.models.vendor_request import VendorRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

id: StrictStr = "example_id"
request: StrictStr = "example_request"
links: Optional[conlist(Link)] = None
vendor_request_instance = VendorRequest(id=id, request=request, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

