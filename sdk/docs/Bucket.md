# Bucket

A single histogram bucket.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **datetime** | The bucket&#39;s start time as a DateTimeOffset. | [optional] 
**item_count** | **int** | The number of items in the bucket. | [optional] 
## Example

```python
from finbourne_insights.models.bucket import Bucket
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

start_time: Optional[datetime] = # Replace with your value
item_count: Optional[StrictInt] = # Replace with your value
bucket_instance = Bucket(start_time=start_time, item_count=item_count)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

