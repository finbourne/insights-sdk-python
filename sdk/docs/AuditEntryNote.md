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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

user_id: StrictStr = "example_user_id"
text: StrictStr = "example_text"
var_date: datetime = # Replace with your value
audit_entry_note_instance = AuditEntryNote(user_id=user_id, text=text, var_date=var_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

