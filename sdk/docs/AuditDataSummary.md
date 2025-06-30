# AuditDataSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] [readonly] 
**categories** | **Dict[str, int]** |  | [optional] 
## Example

```python
from finbourne_insights.models.audit_data_summary import AuditDataSummary
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictInt

count: Optional[StrictInt] = None
count: Optional[StrictInt] = None
categories: Optional[Dict[str, StrictInt]] = None
audit_data_summary_instance = AuditDataSummary(count=count, categories=categories)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

