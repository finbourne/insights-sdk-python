# TimeRange

A server-resolved time window for a query, as an alternative to supplying absolute StartAt/EndAt. Supply either a Finbourne.Insights.WebApi.Dtos.Querying.TimeRange.Preset (e.g. LastWeek, CurrentMonth) or a relative range via Finbourne.Insights.WebApi.Dtos.Querying.TimeRange.From and Finbourne.Insights.WebApi.Dtos.Querying.TimeRange.To. The window is resolved on the server at query time, so a saved query re-runs against a sliding window. Calendar boundaries are anchored in Finbourne.Insights.WebApi.Dtos.Querying.TimeRange.TimeZone (default UTC); weeks start on Monday.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preset** | **str** | A named preset window. One of the Finbourne.Insights.WebApi.Dtos.Querying.TimeRangePreset values. Mutually exclusive with Finbourne.Insights.WebApi.Dtos.Querying.TimeRange.From/Finbourne.Insights.WebApi.Dtos.Querying.TimeRange.To. | [optional] 
**var_from** | [**RelativeBoundary**](RelativeBoundary.md) |  | [optional] 
**to** | [**RelativeBoundary**](RelativeBoundary.md) |  | [optional] 
**time_zone** | **str** | Optional IANA time-zone identifier (e.g. \&quot;Europe/London\&quot;) used to anchor calendar boundaries (start of day/week/month/quarter/year). Defaults to UTC when not supplied. | [optional] 
## Example

```python
from finbourne_insights.models.time_range import TimeRange
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

preset: Optional[StrictStr] = "example_preset"
var_from: Optional[RelativeBoundary] = # Replace with your value
to: Optional[RelativeBoundary] = None
time_zone: Optional[StrictStr] = "example_time_zone"
time_range_instance = TimeRange(preset=preset, var_from=var_from, to=to, time_zone=time_zone)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

