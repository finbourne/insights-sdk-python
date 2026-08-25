# finbourne_insights.LogMetadataApi

All URIs are relative to *https://fbn-prd.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_queryable_fields**](LogMetadataApi.md#list_queryable_fields) | **GET** /api/metadata/logs | [EARLY ACCESS] ListQueryableFields: List the queryable fields for every supported log type.


# **list_queryable_fields**
> ResourceListOfQueryableLogType list_queryable_fields()

[EARLY ACCESS] ListQueryableFields: List the queryable fields for every supported log type.

Returns, for each log type, the fields that can be selected and/or filtered, their data types, and the comparator operations available for each filterable field. Intended to power a UI that advertises the correct comparators for a chosen field.

### Example

```python
from finbourne_insights.exceptions import ApiException
from finbourne_insights.extensions.configuration_options import ConfigurationOptions
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    SyncApiClientFactory,
    LogMetadataApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "insightsUrl":"https://<your-domain>.lusid.com/insights",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_insights SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(LogMetadataApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_queryable_fields(opts=opts)

        # [EARLY ACCESS] ListQueryableFields: List the queryable fields for every supported log type.
        api_response = api_instance.list_queryable_fields()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling LogMetadataApi->list_queryable_fields: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfQueryableLogType**](ResourceListOfQueryableLogType.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

