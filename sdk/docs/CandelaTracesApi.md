# finbourne_insights.CandelaTracesApi

All URIs are relative to *https://fbn-prd.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trace_log**](CandelaTracesApi.md#get_trace_log) | **GET** /api/candelatraces/{scope}/{traceId} | [EXPERIMENTAL] GetTraceLog: Get the log for a specific trace.
[**list_trace_event_logs**](CandelaTracesApi.md#list_trace_event_logs) | **GET** /api/candelatraces/{scope}/{traceId}/events | [EXPERIMENTAL] ListTraceEventLogs: Get the trace event logs for a specific trace.
[**list_trace_logs**](CandelaTracesApi.md#list_trace_logs) | **GET** /api/candelatraces | [EXPERIMENTAL] ListTraceLogs: Get the logs for traces.


# **get_trace_log**
> TraceLog get_trace_log(trace_id, scope)

[EXPERIMENTAL] GetTraceLog: Get the log for a specific trace.

### Example

```python
from finbourne_insights.exceptions import ApiException
from finbourne_insights.extensions.configuration_options import ConfigurationOptions
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    SyncApiClientFactory,
    CandelaTracesApi
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
    api_instance = api_client_factory.build(CandelaTracesApi)
    trace_id = 'trace_id_example' # str | The identifier of the request to obtain the log for.
    scope = 'scope_example' # str | 

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_trace_log(trace_id, scope, opts=opts)

        # [EXPERIMENTAL] GetTraceLog: Get the log for a specific trace.
        api_response = api_instance.get_trace_log(trace_id, scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CandelaTracesApi->get_trace_log: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**| The identifier of the request to obtain the log for. | 
 **scope** | **str**|  | 

### Return type

[**TraceLog**](TraceLog.md)

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

# **list_trace_event_logs**
> ResourceListOfTraceEventLog list_trace_event_logs(trace_id, scope, page=page)

[EXPERIMENTAL] ListTraceEventLogs: Get the trace event logs for a specific trace.

### Example

```python
from finbourne_insights.exceptions import ApiException
from finbourne_insights.extensions.configuration_options import ConfigurationOptions
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    SyncApiClientFactory,
    CandelaTracesApi
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
    api_instance = api_client_factory.build(CandelaTracesApi)
    trace_id = 'trace_id_example' # str | The identifier of the request to obtain the log for.
    scope = 'scope_example' # str | 
    page = 'page_example' # str |  (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_trace_event_logs(trace_id, scope, page=page, opts=opts)

        # [EXPERIMENTAL] ListTraceEventLogs: Get the trace event logs for a specific trace.
        api_response = api_instance.list_trace_event_logs(trace_id, scope, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CandelaTracesApi->list_trace_event_logs: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_id** | **str**| The identifier of the request to obtain the log for. | 
 **scope** | **str**|  | 
 **page** | **str**|  | [optional] 

### Return type

[**ResourceListOfTraceEventLog**](ResourceListOfTraceEventLog.md)

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

# **list_trace_logs**
> ResourceListOfTraceLog list_trace_logs(filter=filter, sort_by=sort_by, limit=limit, page=page)

[EXPERIMENTAL] ListTraceLogs: Get the logs for traces.

### Example

```python
from finbourne_insights.exceptions import ApiException
from finbourne_insights.extensions.configuration_options import ConfigurationOptions
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    SyncApiClientFactory,
    CandelaTracesApi
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
    api_instance = api_client_factory.build(CandelaTracesApi)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid). (optional)
    sort_by = 'sort_by_example' # str | Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
    limit = 56 # int | When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. (optional)
    page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_trace_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, opts=opts)

        # [EXPERIMENTAL] ListTraceLogs: Get the logs for traces.
        api_response = api_instance.list_trace_logs(filter=filter, sort_by=sort_by, limit=limit, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CandelaTracesApi->list_trace_logs: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid). | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. | [optional] 

### Return type

[**ResourceListOfTraceLog**](ResourceListOfTraceLog.md)

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

