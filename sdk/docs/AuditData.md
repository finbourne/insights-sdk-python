# AuditData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**category** | **str** |  | 
**user_id** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**resource** | [**Resource**](Resource.md) |  | [optional] 
**details_type** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
## Example

```python
from finbourne_insights.models.audit_data import AuditData
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

action: StrictStr = "example_action"
category: StrictStr = "example_category"
user_id: Optional[StrictStr] = "example_user_id"
message: Optional[StrictStr] = "example_message"
resource: Optional[Resource] = None
details_type: Optional[StrictStr] = "example_details_type"
details: Optional[Any] = None
audit_data_instance = AuditData(action=action, category=category, user_id=user_id, message=message, resource=resource, details_type=details_type, details=details)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

