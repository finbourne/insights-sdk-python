# Histogram

A histogram showing an item's count in buckets of equal timespans.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | [**List[Bucket]**](Bucket.md) | An ordered list of the histogram buckets. | [optional] 
## Example

```python
from finbourne_insights.models.histogram import Histogram
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

buckets: Optional[conlist(Bucket)] = # Replace with your value
histogram_instance = Histogram(buckets=buckets)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

