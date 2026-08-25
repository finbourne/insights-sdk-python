# IdentityMetricsDataSet

Identity population and activity counts for the domain, pivoted from the latest tranche the identity metrics provider collected.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of this data set. Always &#x60;IdentityMetrics&#x60;, matching the corresponding Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet value and Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property. | 
**collected_at** | **datetime** | The timestamp of the tranche these values were collected in, in UTC, or null if no tranche was returned. | [optional] 
**personal_users** | **int** | The number of personal (human) users in the domain, or null if not reported. | [optional] 
**service_users** | **int** | The number of service users in the domain, or null if not reported. | [optional] 
**never_logged_in** | **int** | The number of users that have never logged in, or null if not reported. | [optional] 
**ignored** | **int** | The number of users excluded from the other counts, or null if not reported. | [optional] 
**account_locked** | **int** | The number of users whose account is locked, or null if not reported. | [optional] 
**suspended_pw_reset** | **int** | The number of users suspended pending a password reset, or null if not reported. | [optional] 
**created_last24_hours** | **int** | The number of users created in the last 24 hours, or null if not reported. | [optional] 
**created_last7_days** | **int** | The number of users created in the last 7 days, or null if not reported. | [optional] 
**created_last30_days** | **int** | The number of users created in the last 30 days, or null if not reported. | [optional] 
**active_last24_hours** | **int** | The number of users active in the last 24 hours, or null if not reported. | [optional] 
**active_last7_days** | **int** | The number of users active in the last 7 days, or null if not reported. | [optional] 
**active_last30_days** | **int** | The number of users active in the last 30 days, or null if not reported. | [optional] 
## Example

```python
from finbourne_insights.models.identity_metrics_data_set import IdentityMetricsDataSet
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
collected_at: Optional[datetime] = # Replace with your value
personal_users: Optional[StrictInt] = # Replace with your value
service_users: Optional[StrictInt] = # Replace with your value
never_logged_in: Optional[StrictInt] = # Replace with your value
ignored: Optional[StrictInt] = # Replace with your value
account_locked: Optional[StrictInt] = # Replace with your value
suspended_pw_reset: Optional[StrictInt] = # Replace with your value
created_last24_hours: Optional[StrictInt] = # Replace with your value
created_last7_days: Optional[StrictInt] = # Replace with your value
created_last30_days: Optional[StrictInt] = # Replace with your value
active_last24_hours: Optional[StrictInt] = # Replace with your value
active_last7_days: Optional[StrictInt] = # Replace with your value
active_last30_days: Optional[StrictInt] = # Replace with your value
identity_metrics_data_set_instance = IdentityMetricsDataSet(name=name, collected_at=collected_at, personal_users=personal_users, service_users=service_users, never_logged_in=never_logged_in, ignored=ignored, account_locked=account_locked, suspended_pw_reset=suspended_pw_reset, created_last24_hours=created_last24_hours, created_last7_days=created_last7_days, created_last30_days=created_last30_days, active_last24_hours=active_last24_hours, active_last7_days=active_last7_days, active_last30_days=active_last30_days)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

