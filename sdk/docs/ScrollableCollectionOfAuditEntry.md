# ScrollableCollectionOfAuditEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuditEntry]**](AuditEntry.md) |  | [optional] 
**state** | **str** |  | [optional] 
## Example

```python
from finbourne_insights.models.scrollable_collection_of_audit_entry import ScrollableCollectionOfAuditEntry
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

data: Optional[List[AuditEntry]] = None
state: Optional[StrictStr] = "example_state"
scrollable_collection_of_audit_entry_instance = ScrollableCollectionOfAuditEntry(data=data, state=state)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

