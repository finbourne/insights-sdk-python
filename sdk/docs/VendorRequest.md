# VendorRequest

Details of a request made to a vendor service.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the log. | 
**request** | **str** | The body of the request. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_insights.models.vendor_request import VendorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VendorRequest from a JSON string
vendor_request_instance = VendorRequest.from_json(json)
# print the JSON string representation of the object
print VendorRequest.to_json()

# convert the object into a dict
vendor_request_dict = vendor_request_instance.to_dict()
# create an instance of VendorRequest from a dict
vendor_request_form_dict = vendor_request.from_dict(vendor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


