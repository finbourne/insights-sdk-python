# AvailableValue

A value known to be valid for a queryable log field, which a UI can offer when filtering on that field.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value. | 
**context** | **str** | Optional context qualifying the value. For the Operation field this is the comma-separated names of the applications that publish the operation. | [optional] 
## Example

```python
from finbourne_insights.models.available_value import AvailableValue
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: StrictStr = "example_value"
context: Optional[StrictStr] = "example_context"
available_value_instance = AvailableValue(value=value, context=context)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

