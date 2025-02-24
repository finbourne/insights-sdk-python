# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic.v1 import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from datetime import datetime

from pydantic.v1 import Field, StrictStr, conint, constr, validator

from typing import Optional

from finbourne_insights.models.access_evaluation_log import AccessEvaluationLog
from finbourne_insights.models.resource_list_with_histogram_of_access_evaluation_log import ResourceListWithHistogramOfAccessEvaluationLog

from finbourne_insights.api_client import ApiClient
from finbourne_insights.api_response import ApiResponse
from finbourne_insights.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from finbourne_insights.extensions.configuration_options import ConfigurationOptions

# ensure templated type usages are imported
from pydantic.v1 import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated

class AccessEvaluationsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @overload
    async def get_access_evaluation_log(self, id : Annotated[StrictStr, Field(..., description="The identifier of the access evaluation to obtain the log for.")], **kwargs) -> AccessEvaluationLog:  # noqa: E501
        ...

    @overload
    def get_access_evaluation_log(self, id : Annotated[StrictStr, Field(..., description="The identifier of the access evaluation to obtain the log for.")], async_req: Optional[bool]=True, **kwargs) -> AccessEvaluationLog:  # noqa: E501
        ...

    @validate_arguments
    def get_access_evaluation_log(self, id : Annotated[StrictStr, Field(..., description="The identifier of the access evaluation to obtain the log for.")], async_req: Optional[bool]=None, **kwargs) -> Union[AccessEvaluationLog, Awaitable[AccessEvaluationLog]]:  # noqa: E501
        """[EARLY ACCESS] GetAccessEvaluationLog: Get the log for a specific access evaluation.  This endpoint will be deprecated in the near future.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_access_evaluation_log(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the access evaluation to obtain the log for. (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AccessEvaluationLog
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_access_evaluation_log_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_access_evaluation_log_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_access_evaluation_log_with_http_info(self, id : Annotated[StrictStr, Field(..., description="The identifier of the access evaluation to obtain the log for.")], **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] GetAccessEvaluationLog: Get the log for a specific access evaluation.  This endpoint will be deprecated in the near future.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_access_evaluation_log_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the access evaluation to obtain the log for. (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AccessEvaluationLog, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_access_evaluation_log" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "AccessEvaluationLog",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/access/{id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))


    @overload
    async def list_access_evaluation_logs(self, start_at : Annotated[Optional[datetime], Field(description="Start date from which point to fetch logs.")] = None, end_at : Annotated[Optional[datetime], Field(description="End date to which point to fetch logs.")] = None, filter : Annotated[Optional[StrictStr], Field( description="Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName")] = None, limit : Annotated[Optional[conint(strict=True)], Field(description="When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.")] = None, page : Annotated[Optional[StrictStr], Field( description="Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.")] = None, histogram_interval : Annotated[Optional[StrictStr], Field( description="The interval for an included histogram of the logs")] = None, **kwargs) -> ResourceListWithHistogramOfAccessEvaluationLog:  # noqa: E501
        ...

    @overload
    def list_access_evaluation_logs(self, start_at : Annotated[Optional[datetime], Field(description="Start date from which point to fetch logs.")] = None, end_at : Annotated[Optional[datetime], Field(description="End date to which point to fetch logs.")] = None, filter : Annotated[Optional[StrictStr], Field( description="Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName")] = None, limit : Annotated[Optional[conint(strict=True)], Field(description="When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.")] = None, page : Annotated[Optional[StrictStr], Field( description="Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.")] = None, histogram_interval : Annotated[Optional[StrictStr], Field( description="The interval for an included histogram of the logs")] = None, async_req: Optional[bool]=True, **kwargs) -> ResourceListWithHistogramOfAccessEvaluationLog:  # noqa: E501
        ...

    @validate_arguments
    def list_access_evaluation_logs(self, start_at : Annotated[Optional[datetime], Field(description="Start date from which point to fetch logs.")] = None, end_at : Annotated[Optional[datetime], Field(description="End date to which point to fetch logs.")] = None, filter : Annotated[Optional[StrictStr], Field( description="Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName")] = None, limit : Annotated[Optional[conint(strict=True)], Field(description="When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.")] = None, page : Annotated[Optional[StrictStr], Field( description="Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.")] = None, histogram_interval : Annotated[Optional[StrictStr], Field( description="The interval for an included histogram of the logs")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[ResourceListWithHistogramOfAccessEvaluationLog, Awaitable[ResourceListWithHistogramOfAccessEvaluationLog]]:  # noqa: E501
        """[EARLY ACCESS] ListAccessEvaluationLogs: List the logs for access evaluations.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_access_evaluation_logs(start_at, end_at, filter, sort_by, limit, page, histogram_interval, async_req=True)
        >>> result = thread.get()

        :param start_at: Start date from which point to fetch logs.
        :type start_at: datetime
        :param end_at: End date to which point to fetch logs.
        :type end_at: datetime
        :param filter: Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).
        :type filter: str
        :param sort_by: Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.
        :type page: str
        :param histogram_interval: The interval for an included histogram of the logs
        :type histogram_interval: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListWithHistogramOfAccessEvaluationLog
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_access_evaluation_logs_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.list_access_evaluation_logs_with_http_info(start_at, end_at, filter, sort_by, limit, page, histogram_interval, **kwargs)  # noqa: E501

    @validate_arguments
    def list_access_evaluation_logs_with_http_info(self, start_at : Annotated[Optional[datetime], Field(description="Start date from which point to fetch logs.")] = None, end_at : Annotated[Optional[datetime], Field(description="End date to which point to fetch logs.")] = None, filter : Annotated[Optional[StrictStr], Field( description="Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName")] = None, limit : Annotated[Optional[conint(strict=True)], Field(description="When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.")] = None, page : Annotated[Optional[StrictStr], Field( description="Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.")] = None, histogram_interval : Annotated[Optional[StrictStr], Field( description="The interval for an included histogram of the logs")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] ListAccessEvaluationLogs: List the logs for access evaluations.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_access_evaluation_logs_with_http_info(start_at, end_at, filter, sort_by, limit, page, histogram_interval, async_req=True)
        >>> result = thread.get()

        :param start_at: Start date from which point to fetch logs.
        :type start_at: datetime
        :param end_at: End date to which point to fetch logs.
        :type end_at: datetime
        :param filter: Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).
        :type filter: str
        :param sort_by: Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.
        :type page: str
        :param histogram_interval: The interval for an included histogram of the logs
        :type histogram_interval: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResourceListWithHistogramOfAccessEvaluationLog, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'start_at',
            'end_at',
            'filter',
            'sort_by',
            'limit',
            'page',
            'histogram_interval'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_access_evaluation_logs" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('start_at') is not None:  # noqa: E501
            if isinstance(_params['start_at'], datetime):
                _query_params.append(('startAt', _params['start_at'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('startAt', _params['start_at']))

        if _params.get('end_at') is not None:  # noqa: E501
            if isinstance(_params['end_at'], datetime):
                _query_params.append(('endAt', _params['end_at'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('endAt', _params['end_at']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('sort_by') is not None:  # noqa: E501
            _query_params.append(('sortBy', _params['sort_by']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('histogram_interval') is not None:  # noqa: E501
            _query_params.append(('histogramInterval', _params['histogram_interval']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "ResourceListWithHistogramOfAccessEvaluationLog",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/access', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
