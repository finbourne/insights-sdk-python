# ProblemDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**detail** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 

## Example

```python
from finbourne_insights.models.problem_details import ProblemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetails from a JSON string
problem_details_instance = ProblemDetails.from_json(json)
# print the JSON string representation of the object
print ProblemDetails.to_json()

# convert the object into a dict
problem_details_dict = problem_details_instance.to_dict()
# create an instance of ProblemDetails from a dict
problem_details_form_dict = problem_details.from_dict(problem_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


