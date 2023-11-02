# finbourne_insights.AuditingApi

All URIs are relative to *https://fbn-ci.lusid.com/insights*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entry**](AuditingApi.md#create_entry) | **POST** /api/auditing/entries | [EARLY ACCESS] CreateEntry: Create (persist) and audit entry..
[**get_processes**](AuditingApi.md#get_processes) | **GET** /api/auditing/processes | [EARLY ACCESS] GetProcesses: Get the latest audit entry for each process.
[**list_entries**](AuditingApi.md#list_entries) | **GET** /api/auditing/entries | [EARLY ACCESS] ListEntries: Get the audit entries.


# **create_entry**
> AuditEntry create_entry(create_audit_entry=create_audit_entry)

[EARLY ACCESS] CreateEntry: Create (persist) and audit entry..

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_insights
from finbourne_insights.rest import ApiException
from finbourne_insights.models.audit_entry import AuditEntry
from finbourne_insights.models.create_audit_entry import CreateAuditEntry
from pprint import pprint

from finbourne_insights import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_insights ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/insights"
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
    api_instance = api_client_factory.build(finbourne_insights.AuditingApi)
    create_audit_entry = {"process":{"name":"processName","runId":"processRunId","startTime":"0001-01-01T00:00:00.0000000+00:00"},"data":{"action":"dataAction","category":"dataCategory","userId":"dataUserId","message":"dataMessage","resource":{"type":"resourceType","identifier":"resourceIdentifier"},"detailsType":"dataDetailsType"}} # CreateAuditEntry | Information about the entry to be created. (optional)

    try:
        # [EARLY ACCESS] CreateEntry: Create (persist) and audit entry..
        api_response = await api_instance.create_entry(create_audit_entry=create_audit_entry)
        print("The response of AuditingApi->create_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditingApi->create_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_audit_entry** | [**CreateAuditEntry**](CreateAuditEntry.md)| Information about the entry to be created. | [optional] 

### Return type

[**AuditEntry**](AuditEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/json-patch+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**429** | There have been too many recent requests, retry later (using the RETRY-AFTER header value as the delay). |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_processes**
> ResourceListOfAuditProcessSummary get_processes()

[EARLY ACCESS] GetProcesses: Get the latest audit entry for each process.

This will never be `null`, though it may be empty.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_insights
from finbourne_insights.rest import ApiException
from finbourne_insights.models.resource_list_of_audit_process_summary import ResourceListOfAuditProcessSummary
from pprint import pprint

from finbourne_insights import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_insights ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/insights"
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
    api_instance = api_client_factory.build(finbourne_insights.AuditingApi)

    try:
        # [EARLY ACCESS] GetProcesses: Get the latest audit entry for each process.
        api_response = await api_instance.get_processes()
        print("The response of AuditingApi->get_processes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditingApi->get_processes: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfAuditProcessSummary**](ResourceListOfAuditProcessSummary.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entries**
> ScrollableCollectionOfAuditEntry list_entries(filter=filter, sort_by=sort_by, size=size, state=state)

[EARLY ACCESS] ListEntries: Get the audit entries.

This will never be `null`, though it may be empty.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_insights
from finbourne_insights.rest import ApiException
from finbourne_insights.models.scrollable_collection_of_audit_entry import ScrollableCollectionOfAuditEntry
from pprint import pprint

from finbourne_insights import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
	  EnvironmentVariablesConfigurationLoader,
	  SecretsFileConfigurationLoader,
	  ArgsConfigurationLoader
)

# Use the finbourne_insights ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-ci.lusid.com/insights"
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
    api_instance = api_client_factory.build(finbourne_insights.AuditingApi)
    filter = 'filter_example' # str | The filter to be applied to the results. (optional)
    sort_by = 'sort_by_example' # str | The order to return the entries in. (optional)
    size = 1000 # int | The maximum number of entries to return. (optional) (default to 1000)
    state = 'state_example' # str | The scrolling state, used to iterate through the data set. (optional)

    try:
        # [EARLY ACCESS] ListEntries: Get the audit entries.
        api_response = await api_instance.list_entries(filter=filter, sort_by=sort_by, size=size, state=state)
        print("The response of AuditingApi->list_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuditingApi->list_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be applied to the results. | [optional] 
 **sort_by** | **str**| The order to return the entries in. | [optional] 
 **size** | **int**| The maximum number of entries to return. | [optional] [default to 1000]
 **state** | **str**| The scrolling state, used to iterate through the data set. | [optional] 

### Return type

[**ScrollableCollectionOfAuditEntry**](ScrollableCollectionOfAuditEntry.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

