# AuditDataSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] [readonly] 
**categories** | **Dict[str, int]** |  | [optional] 
## Example

```python
from finbourne_insights.models.audit_data_summary import AuditDataSummary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

count: Optional[StrictInt] = None
count: Optional[StrictInt] = None
categories: Optional[Dict[str, StrictInt]] = None
audit_data_summary_instance = AuditDataSummary(count=count, categories=categories)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

