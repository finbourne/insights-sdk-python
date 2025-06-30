# AuditEntryNote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**text** | **str** |  | 
**var_date** | **datetime** |  | 
## Example

```python
from finbourne_insights.models.audit_entry_note import AuditEntryNote
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr
from datetime import datetime
user_id: StrictStr = "example_user_id"
text: StrictStr = "example_text"
var_date: datetime = # Replace with your value
audit_entry_note_instance = AuditEntryNote(user_id=user_id, text=text, var_date=var_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

