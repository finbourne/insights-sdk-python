# ResourceListWithHistogramOfAccessEvaluationLog

ResourceList with additional aggregation data about the values.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**histogram** | [**Histogram**](Histogram.md) |  | [optional] 
**values** | [**List[AccessEvaluationLog]**](AccessEvaluationLog.md) |  | 
**href** | **str** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_insights.models.resource_list_with_histogram_of_access_evaluation_log import ResourceListWithHistogramOfAccessEvaluationLog

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListWithHistogramOfAccessEvaluationLog from a JSON string
resource_list_with_histogram_of_access_evaluation_log_instance = ResourceListWithHistogramOfAccessEvaluationLog.from_json(json)
# print the JSON string representation of the object
print ResourceListWithHistogramOfAccessEvaluationLog.to_json()

# convert the object into a dict
resource_list_with_histogram_of_access_evaluation_log_dict = resource_list_with_histogram_of_access_evaluation_log_instance.to_dict()
# create an instance of ResourceListWithHistogramOfAccessEvaluationLog from a dict
resource_list_with_histogram_of_access_evaluation_log_form_dict = resource_list_with_histogram_of_access_evaluation_log.from_dict(resource_list_with_histogram_of_access_evaluation_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


