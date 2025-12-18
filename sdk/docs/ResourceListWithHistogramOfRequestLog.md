# ResourceListWithHistogramOfRequestLog

ResourceList with additional aggregation data about the values.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**histogram** | [**Histogram**](Histogram.md) |  | [optional] 
**values** | [**List[RequestLog]**](RequestLog.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_insights.models.resource_list_with_histogram_of_request_log import ResourceListWithHistogramOfRequestLog
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

histogram: Optional[Histogram] = None
values: List[RequestLog]
href: Optional[StrictStr] = "example_href"
next_page: Optional[StrictStr] = "example_next_page"
previous_page: Optional[StrictStr] = "example_previous_page"
links: Optional[List[Link]] = None
resource_list_with_histogram_of_request_log_instance = ResourceListWithHistogramOfRequestLog(histogram=histogram, values=values, href=href, next_page=next_page, previous_page=previous_page, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

