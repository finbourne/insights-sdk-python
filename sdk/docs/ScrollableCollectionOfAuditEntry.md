# ScrollableCollectionOfAuditEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuditEntry]**](AuditEntry.md) |  | [optional] 
**state** | **str** |  | [optional] 
## Example

```python
from finbourne_insights.models.scrollable_collection_of_audit_entry import ScrollableCollectionOfAuditEntry
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, StrictStr, conlist

data: Optional[conlist(AuditEntry)] = None
state: Optional[StrictStr] = "example_state"
scrollable_collection_of_audit_entry_instance = ScrollableCollectionOfAuditEntry(data=data, state=state)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

