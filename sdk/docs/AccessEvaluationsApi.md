# finbourne_insights.AccessEvaluationsApi

All URIs are relative to *https://fbn-prd.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_evaluation_log**](AccessEvaluationsApi.md#get_access_evaluation_log) | **GET** /api/access/{id} | [EARLY ACCESS] GetAccessEvaluationLog: Get the log for a specific access evaluation.  This endpoint will be deprecated in the near future.
[**list_access_evaluation_logs**](AccessEvaluationsApi.md#list_access_evaluation_logs) | **GET** /api/access | [EARLY ACCESS] ListAccessEvaluationLogs: List the logs for access evaluations.


# **get_access_evaluation_log**
> AccessEvaluationLog get_access_evaluation_log(id)

[EARLY ACCESS] GetAccessEvaluationLog: Get the log for a specific access evaluation.  This endpoint will be deprecated in the near future.

### Example

```python
import asyncio
from finbourne_insights.exceptions import ApiException
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    ApiClientFactory,
    AccessEvaluationsApi
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
        api_instance = api_client_factory.build(AccessEvaluationsApi)
        id = 'id_example' # str | The identifier of the access evaluation to obtain the log for.

        try:
            # [EARLY ACCESS] GetAccessEvaluationLog: Get the log for a specific access evaluation.  This endpoint will be deprecated in the near future.
            api_response = await api_instance.get_access_evaluation_log(id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AccessEvaluationsApi->get_access_evaluation_log: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the access evaluation to obtain the log for. | 

### Return type

[**AccessEvaluationLog**](AccessEvaluationLog.md)

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

# **list_access_evaluation_logs**
> ResourceListWithHistogramOfAccessEvaluationLog list_access_evaluation_logs(start_at=start_at, end_at=end_at, filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)

[EARLY ACCESS] ListAccessEvaluationLogs: List the logs for access evaluations.

### Example

```python
import asyncio
from finbourne_insights.exceptions import ApiException
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    ApiClientFactory,
    AccessEvaluationsApi
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
        api_instance = api_client_factory.build(AccessEvaluationsApi)
        start_at = '2013-10-20T19:20:30+01:00' # datetime | Start date from which point to fetch logs. (optional)
        end_at = '2013-10-20T19:20:30+01:00' # datetime | End date to which point to fetch logs. (optional)
        filter = 'filter_example' # str | Expression to filter the result set. Read more about <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</see>. (optional)
        sort_by = 'sort_by_example' # str | Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
        limit = 56 # int | When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. (optional)
        page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. (optional)
        histogram_interval = 'histogram_interval_example' # str | The interval for an included histogram of the logs (optional)

        try:
            # [EARLY ACCESS] ListAccessEvaluationLogs: List the logs for access evaluations.
            api_response = await api_instance.list_access_evaluation_logs(start_at=start_at, end_at=end_at, filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AccessEvaluationsApi->list_access_evaluation_logs: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_at** | **datetime**| Start date from which point to fetch logs. | [optional] 
 **end_at** | **datetime**| End date to which point to fetch logs. | [optional] 
 **filter** | **str**| Expression to filter the result set. Read more about &lt;see href&#x3D;\&quot;https://support.lusid.com/filtering-results-from-lusid\&quot;&gt; filtering results from LUSID&lt;/see&gt;. | [optional] 
 **sort_by** | **str**| Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName | [optional] 
 **limit** | **int**| When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. | [optional] 
 **page** | **str**| Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. | [optional] 
 **histogram_interval** | **str**| The interval for an included histogram of the logs | [optional] 

### Return type

[**ResourceListWithHistogramOfAccessEvaluationLog**](ResourceListWithHistogramOfAccessEvaluationLog.md)

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

