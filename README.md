![LUSID_by_Finbourne](./resources/Finbourne_Logo_Teal.svg)

# FINBOURNE Insights Python SDK


| branch | status |
| --- | --- |
| `main` |  ![PyPI](https://img.shields.io/pypi/v/finbourne-insights-sdk?color=blue)

## Installation

The PyPi package for the Insights SDK can installed using the following:

```
$ pip install finbourne-insights-sdk finbourne-sdk-utilities
```

## Usage

```
from finbourne_insights import api as ia
from fbnsdkutilities import ApiClientFactory
import finbourne_insights

api_client = ApiClientFactory(finbourne_insights, api_secrets_filename="secrets.json")
requests_api = api_client.build(ia.RequestsApi)
response = requests_api.list_request_logs()
print(response.values)
```
