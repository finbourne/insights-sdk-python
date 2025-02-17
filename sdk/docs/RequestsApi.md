# finbourne_insights.RequestsApi

All URIs are relative to *https://fbn-prd.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_request**](RequestsApi.md#get_request) | **GET** /api/requests/{id}/request | GetRequest: Get the request content for a specific API request.
[**get_request_log**](RequestsApi.md#get_request_log) | **GET** /api/requests/{id} | GetRequestLog: Get the log for a specific API request.
[**get_response**](RequestsApi.md#get_response) | **GET** /api/requests/{id}/response | GetResponse: Get the response for a specific API request.
[**list_request_logs**](RequestsApi.md#list_request_logs) | **GET** /api/requests | ListRequestLogs: Get the logs for API requests.


# **get_request**
> Request get_request(id)

GetRequest: Get the request content for a specific API request.

### Example

```python
from finbourne_insights.exceptions import ApiException
from finbourne_insights.extensions.configuration_options import ConfigurationOptions
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    SyncApiClientFactory,
    RequestsApi
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
    api_instance = api_client_factory.build(RequestsApi)
    id = 'id_example' # str | The identifier of the request to obtain the content for.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_request(id, opts=opts)

        # GetRequest: Get the request content for a specific API request.
        api_response = api_instance.get_request(id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RequestsApi->get_request: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the content for. | 

### Return type

[**Request**](Request.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_request_log**
> RequestLog get_request_log(id)

GetRequestLog: Get the log for a specific API request.

### Example

```python
from finbourne_insights.exceptions import ApiException
from finbourne_insights.extensions.configuration_options import ConfigurationOptions
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    SyncApiClientFactory,
    RequestsApi
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
    api_instance = api_client_factory.build(RequestsApi)
    id = 'id_example' # str | The identifier of the request to obtain the log for.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_request_log(id, opts=opts)

        # GetRequestLog: Get the log for a specific API request.
        api_response = api_instance.get_request_log(id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RequestsApi->get_request_log: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the log for. | 

### Return type

[**RequestLog**](RequestLog.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_response**
> Response get_response(id)

GetResponse: Get the response for a specific API request.

### Example

```python
from finbourne_insights.exceptions import ApiException
from finbourne_insights.extensions.configuration_options import ConfigurationOptions
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    SyncApiClientFactory,
    RequestsApi
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
    api_instance = api_client_factory.build(RequestsApi)
    id = 'id_example' # str | The identifier of the request to obtain the response for.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_response(id, opts=opts)

        # GetResponse: Get the response for a specific API request.
        api_response = api_instance.get_response(id)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RequestsApi->get_response: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the response for. | 

### Return type

[**Response**](Response.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_request_logs**
> ResourceListWithHistogramOfRequestLog list_request_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)

ListRequestLogs: Get the logs for API requests.

### Example

```python
from finbourne_insights.exceptions import ApiException
from finbourne_insights.extensions.configuration_options import ConfigurationOptions
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    SyncApiClientFactory,
    RequestsApi
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
    api_instance = api_client_factory.build(RequestsApi)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid). (optional)
    sort_by = 'sort_by_example' # str | Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
    limit = 56 # int | When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. (optional)
    page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. (optional)
    histogram_interval = 'histogram_interval_example' # str | Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_request_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval, opts=opts)

        # ListRequestLogs: Get the logs for API requests.
        api_response = api_instance.list_request_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling RequestsApi->list_request_logs: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid). | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. | [optional] 
 **histogram_interval** | **str**| Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated. | [optional] 

### Return type

[**ResourceListWithHistogramOfRequestLog**](ResourceListWithHistogramOfRequestLog.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

