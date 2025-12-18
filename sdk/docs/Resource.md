# Resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
## Example

```python
from finbourne_insights.models.resource import Resource
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: Optional[StrictStr] = "example_type"
identifier: Optional[StrictStr] = "example_identifier"
resource_instance = Resource(type=type, identifier=identifier)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

