# QueryRequestLogsRequest

Body of the QueryRequestLogs endpoint. A query is bounded by a time range (Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.StartAt/Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.EndAt) and refined by an optional set of Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.Filters that are combined with logical AND. The discoverable set of filterable fields, their data types and the operations available for each is returned by the queryable-fields metadata endpoint.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_at** | **datetime** | The inclusive start of the time range to query. Required unless Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.Page is supplied. Used to bound the underlying partition scan, so a tighter range is cheaper and faster. | [optional] 
**end_at** | **datetime** | The end of the time range to query. Required unless Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.Page or Finbourne.Insights.WebApi.Dtos.QueryRequestLogsRequest.TimeRange is supplied. | [optional] 
**time_range** | [**TimeRange**](TimeRange.md) |  | [optional] 
**filters** | [**List[InsightsFilter]**](InsightsFilter.md) | Optional filters to apply, combined with logical AND. Each filter targets a filterable field and supplies exactly one comparator matching that field&#39;s data type. | [optional] 
**sort_by** | **str** | Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName. | [optional] 
**max_results** | **int** | The maximum total number of records to capture in the result set; applied as the Luminesce query limit and so bounding the work the query performs. The minimum value is 1 and the maximum is 10000; defaults to 500 when not supplied. The per-page limit then controls how many of these captured records are returned per page. | [optional] 
**limit** | **int** | When paginating, only return this number of records per page. The minimum value is 0 (return all captured records in a single page) and the maximum is 10000. | [optional] 
**page** | **str** | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, the query-defining fields should not be supplied. | [optional] 
**fields** | **List[str]** | Optional list of additional field names to include in the response. The fields Timestamp, Id, Application and Operation are always returned. Values are matched case-insensitively against the queryable fields of the request logs. | [optional] 
## Example

```python
from finbourne_insights.models.query_request_logs_request import QueryRequestLogsRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_at: Optional[datetime] = # Replace with your value
end_at: Optional[datetime] = # Replace with your value
time_range: Optional[TimeRange] = # Replace with your value
filters: Optional[List[InsightsFilter]] = # Replace with your value
sort_by: Optional[StrictStr] = "example_sort_by"
max_results: Optional[StrictInt] = # Replace with your value
max_results: Optional[StrictInt] = None
limit: Optional[StrictInt] = # Replace with your value
limit: Optional[StrictInt] = None
page: Optional[StrictStr] = "example_page"
fields: Optional[List[StrictStr]] = # Replace with your value
query_request_logs_request_instance = QueryRequestLogsRequest(start_at=start_at, end_at=end_at, time_range=time_range, filters=filters, sort_by=sort_by, max_results=max_results, limit=limit, page=page, fields=fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

