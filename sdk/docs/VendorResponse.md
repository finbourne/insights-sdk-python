# VendorResponse

Details of a response to a request made to a vendor service.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the log. | 
**response** | **str** | The body of the response. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_insights.models.vendor_response import VendorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VendorResponse from a JSON string
vendor_response_instance = VendorResponse.from_json(json)
# print the JSON string representation of the object
print VendorResponse.to_json()

# convert the object into a dict
vendor_response_dict = vendor_response_instance.to_dict()
# create an instance of VendorResponse from a dict
vendor_response_form_dict = vendor_response.from_dict(vendor_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


