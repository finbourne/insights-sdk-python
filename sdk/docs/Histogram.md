# Histogram

A histogram showing an item's count in buckets of equal timespans.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | [**List[Bucket]**](Bucket.md) | An ordered list of the histogram buckets. | [optional] 
## Example

```python
from finbourne_insights.models.histogram import Histogram
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

buckets: Optional[List[Bucket]] = # Replace with your value
histogram_instance = Histogram(buckets=buckets)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

