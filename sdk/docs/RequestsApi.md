# finbourne_insights.RequestsApi

All URIs are relative to *https://fbn-prd.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_request**](RequestsApi.md#get_request) | **GET** /api/requests/{id}/request | [EARLY ACCESS] GetRequest: Get the request content for a specific API request.
[**get_request_log**](RequestsApi.md#get_request_log) | **GET** /api/requests/{id} | [EARLY ACCESS] GetRequestLog: Get the log for a specific API request.
[**get_response**](RequestsApi.md#get_response) | **GET** /api/requests/{id}/response | [EARLY ACCESS] GetResponse: Get the response for a specific API request.
[**list_request_logs**](RequestsApi.md#list_request_logs) | **GET** /api/requests | [EARLY ACCESS] ListRequestLogs: Get the logs for API requests.


# **get_request**
> Request get_request(id)

[EARLY ACCESS] GetRequest: Get the request content for a specific API request.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_insights
from finbourne_insights.rest import ApiException
from finbourne_insights.models.request import Request
from pprint import pprint

import os
from finbourne_insights import (
    ApiClientFactory,
    RequestsApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_insights ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/insights"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_insights.RequestsApi)
    id = 'id_example' # str | The identifier of the request to obtain the content for.

    try:
        # [EARLY ACCESS] GetRequest: Get the request content for a specific API request.
        api_response = await api_instance.get_request(id)
        print("The response of RequestsApi->get_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the content for. | 

### Return type

[**Request**](Request.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_log**
> RequestLog get_request_log(id)

[EARLY ACCESS] GetRequestLog: Get the log for a specific API request.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_insights
from finbourne_insights.rest import ApiException
from finbourne_insights.models.request_log import RequestLog
from pprint import pprint

import os
from finbourne_insights import (
    ApiClientFactory,
    RequestsApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_insights ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/insights"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_insights.RequestsApi)
    id = 'id_example' # str | The identifier of the request to obtain the log for.

    try:
        # [EARLY ACCESS] GetRequestLog: Get the log for a specific API request.
        api_response = await api_instance.get_request_log(id)
        print("The response of RequestsApi->get_request_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_request_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the log for. | 

### Return type

[**RequestLog**](RequestLog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_response**
> Response get_response(id)

[EARLY ACCESS] GetResponse: Get the response for a specific API request.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_insights
from finbourne_insights.rest import ApiException
from finbourne_insights.models.response import Response
from pprint import pprint

import os
from finbourne_insights import (
    ApiClientFactory,
    RequestsApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_insights ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/insights"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_insights.RequestsApi)
    id = 'id_example' # str | The identifier of the request to obtain the response for.

    try:
        # [EARLY ACCESS] GetResponse: Get the response for a specific API request.
        api_response = await api_instance.get_response(id)
        print("The response of RequestsApi->get_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->get_response: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The identifier of the request to obtain the response for. | 

### Return type

[**Response**](Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_request_logs**
> ResourceListWithHistogramOfRequestLog list_request_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)

[EARLY ACCESS] ListRequestLogs: Get the logs for API requests.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_insights
from finbourne_insights.rest import ApiException
from finbourne_insights.models.resource_list_with_histogram_of_request_log import ResourceListWithHistogramOfRequestLog
from pprint import pprint

import os
from finbourne_insights import (
    ApiClientFactory,
    RequestsApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_insights ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/insights"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_insights.RequestsApi)
    filter = 'filter_example' # str | Expression to filter the result set. Read more about <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</see>. (optional)
    sort_by = 'sort_by_example' # str | Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName (optional)
    limit = 56 # int | When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000. (optional)
    page = 'page_example' # str | Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied. (optional)
    histogram_interval = 'histogram_interval_example' # str | Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated. (optional)

    try:
        # [EARLY ACCESS] ListRequestLogs: Get the logs for API requests.
        api_response = await api_instance.list_request_logs(filter=filter, sort_by=sort_by, limit=limit, page=page, histogram_interval=histogram_interval)
        print("The response of RequestsApi->list_request_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestsApi->list_request_logs: %s\n" % e)
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

[**ResourceListWithHistogramOfRequestLog**](ResourceListWithHistogramOfRequestLog.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

