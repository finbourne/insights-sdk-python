# MetricsResponse

The aggregated platform metrics for a domain: one nullable, strongly-typed property per data set.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at** | **datetime** | When this response was assembled, in UTC. Every data set in the response was resolved against this instant. | 
**domain** | **str** | The domain the metrics are for, resolved from the authenticated request rather than from any parameter. | 
**requests_per_minute** | [**RequestsPerMinuteDataSet**](RequestsPerMinuteDataSet.md) |  | [optional] 
**service_endpoint_durations24h** | [**ServiceEndpointDurations24hDataSet**](ServiceEndpointDurations24hDataSet.md) |  | [optional] 
**service_requests24h** | [**ServiceRequests24hDataSet**](ServiceRequests24hDataSet.md) |  | [optional] 
**identity_metrics** | [**IdentityMetricsDataSet**](IdentityMetricsDataSet.md) |  | [optional] 
**not_included** | **List[str]** | The data sets the caller excluded via the &#x60;include&#x60; parameter, and which were therefore never queried. Each value is one of the Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet values. | 
**failed** | [**List[MetricDataSetFailure]**](MetricDataSetFailure.md) | The data sets that were requested but could not be returned, each with a caller-safe reason. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_insights.models.metrics_response import MetricsResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

as_at: datetime = # Replace with your value
domain: StrictStr = "example_domain"
requests_per_minute: Optional[RequestsPerMinuteDataSet] = # Replace with your value
service_endpoint_durations24h: Optional[ServiceEndpointDurations24hDataSet] = # Replace with your value
service_requests24h: Optional[ServiceRequests24hDataSet] = # Replace with your value
identity_metrics: Optional[IdentityMetricsDataSet] = # Replace with your value
not_included: List[StrictStr] = # Replace with your value
failed: List[MetricDataSetFailure] = # Replace with your value
links: Optional[List[Link]] = None
metrics_response_instance = MetricsResponse(as_at=as_at, domain=domain, requests_per_minute=requests_per_minute, service_endpoint_durations24h=service_endpoint_durations24h, service_requests24h=service_requests24h, identity_metrics=identity_metrics, not_included=not_included, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

