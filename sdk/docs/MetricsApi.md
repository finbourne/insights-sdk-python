# finbourne_insights.MetricsApi

All URIs are relative to *https://fbn-prd.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics**](MetricsApi.md#get_metrics) | **GET** /api/metrics | [EARLY ACCESS] GetMetrics: Get the aggregated platform metrics for the caller&#39;s domain.


# **get_metrics**
> MetricsResponse get_metrics(include=include)

[EARLY ACCESS] GetMetrics: Get the aggregated platform metrics for the caller's domain.

 Returns request volumes, error rates and duration distributions for the domain's services, plus its identity             population and activity counts. The domain is taken from the authenticated request, never from a parameter.  <b>This endpoint is slow by design.</b> It runs several analytical queries in parallel and commonly takes             upwards of thirty seconds when the underlying data is cold. The server abandons a data set that has not             completed within its configured budget and reports it in `failed`, so a call returns rather than hanging             indefinitely; allow comfortably more than that budget on the client, and do not call this on a             user-interactive code path without showing progress.  Partial success is normal and is still reported as a `200`. A data set that could not be retrieved is             null in the response and named in `failed` with a reason; a data set excluded via             include is null and named in `notIncluded`. Render a null data set as unavailable             rather than as an absence of activity.

### Example

```python
from finbourne_insights.exceptions import ApiException
from finbourne_insights.extensions.configuration_options import ConfigurationOptions
from finbourne_insights.models import *
from pprint import pprint
from finbourne_insights import (
    SyncApiClientFactory,
    MetricsApi
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
    api_instance = api_client_factory.build(MetricsApi)
    include = ['include_example'] # List[str] | The data sets to return, by name. Omit to return all of them. Repeat the parameter to request several, for example `?include=RequestsPerMinute&include=IdentityMetrics`. Matched case-insensitively against the data set names, which are the `name` values on the response's data sets; duplicates are ignored. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_metrics(include=include, opts=opts)

        # [EARLY ACCESS] GetMetrics: Get the aggregated platform metrics for the caller's domain.
        api_response = api_instance.get_metrics(include=include)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MetricsApi->get_metrics: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| The data sets to return, by name. Omit to return all of them. Repeat the parameter to request several, for example &#x60;?include&#x3D;RequestsPerMinute&amp;include&#x3D;IdentityMetrics&#x60;. Matched case-insensitively against the data set names, which are the &#x60;name&#x60; values on the response&#39;s data sets; duplicates are ignored. | [optional] 

### Return type

[**MetricsResponse**](MetricsResponse.md)

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

