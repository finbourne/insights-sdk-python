# finbourne_insights.VendorLogsApi

All URIs are relative to *https://fbn-prd.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vendor_log**](VendorLogsApi.md#get_vendor_log) | **GET** /api/vendor/{id} | [EXPERIMENTAL] GetVendorLog: Get the log for a specific vendor request.
[**get_vendor_request**](VendorLogsApi.md#get_vendor_request) | **GET** /api/vendor/{id}/request | [EXPERIMENTAL] GetVendorRequest: Get the request body for a vendor request.
[**get_vendor_response**](VendorLogsApi.md#get_vendor_response) | **GET** /api/vendor/{id}/response | [EXPERIMENTAL] GetVendorResponse: Get the response from a vendor request.
[**list_vendor_logs**](VendorLogsApi.md#list_vendor_logs) | **GET** /api/vendor | [EXPERIMENTAL] ListVendorLogs: List the logs for vendor requests.


# **get_vendor_log**
> VendorLog get_vendor_log(id)

[EXPERIMENTAL] GetVendorLog: Get the log for a specific vendor request.

### Example

```python
import asyncio
from finbourne_insights.exceptions import ApiException
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    ApiClientFactory,
    VendorLogsApi
)

async def main():

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

    # Use the finbourne_insights ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(VendorLogsApi)
        id = 'id_example' # str | The identifier of the request to obtain the log for.

        try:
            # [EXPERIMENTAL] GetVendorLog: Get the log for a specific vendor request.
            api_response = await api_instance.get_vendor_log(id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling VendorLogsApi->get_vendor_log: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the log for. | 

### Return type

[**VendorLog**](VendorLog.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_vendor_request**
> VendorRequest get_vendor_request(id)

[EXPERIMENTAL] GetVendorRequest: Get the request body for a vendor request.

### Example

```python
import asyncio
from finbourne_insights.exceptions import ApiException
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    ApiClientFactory,
    VendorLogsApi
)

async def main():

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

    # Use the finbourne_insights ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(VendorLogsApi)
        id = 'id_example' # str | The identifier of the request to obtain the content for.

        try:
            # [EXPERIMENTAL] GetVendorRequest: Get the request body for a vendor request.
            api_response = await api_instance.get_vendor_request(id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling VendorLogsApi->get_vendor_request: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the content for. | 

### Return type

[**VendorRequest**](VendorRequest.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_vendor_response**
> VendorResponse get_vendor_response(id)

[EXPERIMENTAL] GetVendorResponse: Get the response from a vendor request.

### Example

```python
import asyncio
from finbourne_insights.exceptions import ApiException
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    ApiClientFactory,
    VendorLogsApi
)

async def main():

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

    # Use the finbourne_insights ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(VendorLogsApi)
        id = 'id_example' # str | The identifier of the request to obtain the response for.

        try:
            # [EXPERIMENTAL] GetVendorResponse: Get the response from a vendor request.
            api_response = await api_instance.get_vendor_response(id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling VendorLogsApi->get_vendor_response: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the response for. | 

### Return type

[**VendorResponse**](VendorResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_vendor_logs**
> ResourceListWithHistogramOfVendorLog list_vendor_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)

[EXPERIMENTAL] ListVendorLogs: List the logs for vendor requests.

### Example

```python
import asyncio
from finbourne_insights.exceptions import ApiException
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    ApiClientFactory,
    VendorLogsApi
)

async def main():

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

    # Use the finbourne_insights ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(VendorLogsApi)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</see>. (optional)
        sort_by = 'sort_by_example' # str | Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
        limit = 56 # int | When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. (optional)
        page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. (optional)
        histogram_interval = 'histogram_interval_example' # str | Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated. (optional)

        try:
            # [EXPERIMENTAL] ListVendorLogs: List the logs for vendor requests.
            api_response = await api_instance.list_vendor_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling VendorLogsApi->list_vendor_logs: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. Read more about &lt;see href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID&lt;/see&gt;. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. | [optional] 
 **histogram_interval** | **str**| Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated. | [optional] 

### Return type

[**ResourceListWithHistogramOfVendorLog**](ResourceListWithHistogramOfVendorLog.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

