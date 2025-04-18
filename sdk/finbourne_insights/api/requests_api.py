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
from pydantic.v1 import Field, StrictStr, conint, constr, validator

from typing import Optional

from finbourne_insights.models.request import Request
from finbourne_insights.models.request_log import RequestLog
from finbourne_insights.models.resource_list_with_histogram_of_request_log import ResourceListWithHistogramOfRequestLog
from finbourne_insights.models.response import Response

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

class RequestsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @overload
    async def get_request(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the content for.")], **kwargs) -> Request:  # noqa: E501
        ...

    @overload
    def get_request(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the content for.")], async_req: Optional[bool]=True, **kwargs) -> Request:  # noqa: E501
        ...

    @validate_arguments
    def get_request(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the content for.")], async_req: Optional[bool]=None, **kwargs) -> Union[Request, Awaitable[Request]]:  # noqa: E501
        """GetRequest: Get the request content for a specific API request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_request(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the request to obtain the content for. (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Request
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_request_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_request_with_http_info(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the content for.")], **kwargs) -> ApiResponse:  # noqa: E501
        """GetRequest: Get the request content for a specific API request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_request_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the request to obtain the content for. (required)
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
        :rtype: tuple(Request, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_request" % _key
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
            '200': "Request",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/requests/{id}/request', 'GET',
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
    async def get_request_log(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the log for.")], **kwargs) -> RequestLog:  # noqa: E501
        ...

    @overload
    def get_request_log(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the log for.")], async_req: Optional[bool]=True, **kwargs) -> RequestLog:  # noqa: E501
        ...

    @validate_arguments
    def get_request_log(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the log for.")], async_req: Optional[bool]=None, **kwargs) -> Union[RequestLog, Awaitable[RequestLog]]:  # noqa: E501
        """GetRequestLog: Get the log for a specific API request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_request_log(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the request to obtain the log for. (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RequestLog
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_request_log_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_request_log_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_request_log_with_http_info(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the log for.")], **kwargs) -> ApiResponse:  # noqa: E501
        """GetRequestLog: Get the log for a specific API request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_request_log_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the request to obtain the log for. (required)
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
        :rtype: tuple(RequestLog, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_request_log" % _key
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
            '200': "RequestLog",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/requests/{id}', 'GET',
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
    async def get_response(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the response for.")], **kwargs) -> Response:  # noqa: E501
        ...

    @overload
    def get_response(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the response for.")], async_req: Optional[bool]=True, **kwargs) -> Response:  # noqa: E501
        ...

    @validate_arguments
    def get_response(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the response for.")], async_req: Optional[bool]=None, **kwargs) -> Union[Response, Awaitable[Response]]:  # noqa: E501
        """GetResponse: Get the response for a specific API request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_response(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the request to obtain the response for. (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_response_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_response_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_response_with_http_info(self, id : Annotated[StrictStr, Field(..., description="The identifier of the request to obtain the response for.")], **kwargs) -> ApiResponse:  # noqa: E501
        """GetResponse: Get the response for a specific API request.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_response_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the request to obtain the response for. (required)
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
        :rtype: tuple(Response, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_response" % _key
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
            '200': "Response",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/requests/{id}/response', 'GET',
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
    async def list_request_logs(self, filter : Annotated[Optional[StrictStr], Field( description="Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName")] = None, limit : Annotated[Optional[conint(strict=True)], Field(description="When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.")] = None, page : Annotated[Optional[StrictStr], Field( description="Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.")] = None, histogram_interval : Annotated[Optional[StrictStr], Field( description="Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated.")] = None, **kwargs) -> ResourceListWithHistogramOfRequestLog:  # noqa: E501
        ...

    @overload
    def list_request_logs(self, filter : Annotated[Optional[StrictStr], Field( description="Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName")] = None, limit : Annotated[Optional[conint(strict=True)], Field(description="When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.")] = None, page : Annotated[Optional[StrictStr], Field( description="Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.")] = None, histogram_interval : Annotated[Optional[StrictStr], Field( description="Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated.")] = None, async_req: Optional[bool]=True, **kwargs) -> ResourceListWithHistogramOfRequestLog:  # noqa: E501
        ...

    @validate_arguments
    def list_request_logs(self, filter : Annotated[Optional[StrictStr], Field( description="Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName")] = None, limit : Annotated[Optional[conint(strict=True)], Field(description="When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.")] = None, page : Annotated[Optional[StrictStr], Field( description="Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.")] = None, histogram_interval : Annotated[Optional[StrictStr], Field( description="Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated.")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[ResourceListWithHistogramOfRequestLog, Awaitable[ResourceListWithHistogramOfRequestLog]]:  # noqa: E501
        """ListRequestLogs: Get the logs for API requests.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_request_logs(filter, sort_by, limit, page, histogram_interval, async_req=True)
        >>> result = thread.get()

        :param filter: Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).
        :type filter: str
        :param sort_by: Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.
        :type page: str
        :param histogram_interval: Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated.
        :type histogram_interval: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListWithHistogramOfRequestLog
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_request_logs_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.list_request_logs_with_http_info(filter, sort_by, limit, page, histogram_interval, **kwargs)  # noqa: E501

    @validate_arguments
    def list_request_logs_with_http_info(self, filter : Annotated[Optional[StrictStr], Field( description="Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName")] = None, limit : Annotated[Optional[conint(strict=True)], Field(description="When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.")] = None, page : Annotated[Optional[StrictStr], Field( description="Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.")] = None, histogram_interval : Annotated[Optional[StrictStr], Field( description="Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """ListRequestLogs: Get the logs for API requests.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_request_logs_with_http_info(filter, sort_by, limit, page, histogram_interval, async_req=True)
        >>> result = thread.get()

        :param filter: Expression to filter the result set. Read more about [ filtering results from LUSID](https://support.lusid.com/filtering-results-from-lusid).
        :type filter: str
        :param sort_by: Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.
        :type page: str
        :param histogram_interval: Optional interval to use in a histogram of the returned values. If not provided, no histogram will be generated.
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
        :rtype: tuple(ResourceListWithHistogramOfRequestLog, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method list_request_logs" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
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
            '200': "ResourceListWithHistogramOfRequestLog",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/requests', 'GET',
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
