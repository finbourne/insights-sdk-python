# MetricDataSetFailure

Names a metric data set that was requested but could not be returned, with a caller-safe explanation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The data set that could not be returned. One of the Finbourne.Insights.WebApi.Dtos.Metrics.MetricDataSet values, and identical to the name of the Finbourne.Insights.WebApi.Dtos.Metrics.MetricsResponse property that would have carried it. | 
**reason** | **str** | A generic, caller-safe explanation of why the data set is missing. Never contains provider names, query text, internal service names or exception detail. | 
## Example

```python
from finbourne_insights.models.metric_data_set_failure import MetricDataSetFailure
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
reason: StrictStr = "example_reason"
metric_data_set_failure_instance = MetricDataSetFailure(name=name, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

