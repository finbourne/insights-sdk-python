# ProblemDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 
## Example

```python
from finbourne_insights.models.problem_details import ProblemDetails
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictInt, StrictStr

type: Optional[StrictStr] = "example_type"
title: Optional[StrictStr] = "example_title"
status: Optional[StrictInt] = None
status: Optional[StrictInt] = None
detail: Optional[StrictStr] = "example_detail"
instance: Optional[StrictStr] = "example_instance"
problem_details_instance = ProblemDetails(type=type, title=title, status=status, detail=detail, instance=instance)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

