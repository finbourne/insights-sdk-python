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
from pydantic.v1 import Field, StrictInt, StrictStr

from typing import Optional

from finbourne_insights.models.audit_entry import AuditEntry
from finbourne_insights.models.create_audit_entry import CreateAuditEntry
from finbourne_insights.models.resource_list_of_audit_process_summary import ResourceListOfAuditProcessSummary
from finbourne_insights.models.scrollable_collection_of_audit_entry import ScrollableCollectionOfAuditEntry

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

class AuditingApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @overload
    async def create_entry(self, create_audit_entry : Annotated[Optional[CreateAuditEntry], Field(description="Information about the entry to be created.")] = None, **kwargs) -> AuditEntry:  # noqa: E501
        ...

    @overload
    def create_entry(self, create_audit_entry : Annotated[Optional[CreateAuditEntry], Field(description="Information about the entry to be created.")] = None, async_req: Optional[bool]=True, **kwargs) -> AuditEntry:  # noqa: E501
        ...

    @validate_arguments
    def create_entry(self, create_audit_entry : Annotated[Optional[CreateAuditEntry], Field(description="Information about the entry to be created.")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[AuditEntry, Awaitable[AuditEntry]]:  # noqa: E501
        """[EARLY ACCESS] CreateEntry: Create (persist) and audit entry..  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_entry(create_audit_entry, async_req=True)
        >>> result = thread.get()

        :param create_audit_entry: Information about the entry to be created.
        :type create_audit_entry: CreateAuditEntry
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AuditEntry
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the create_entry_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.create_entry_with_http_info(create_audit_entry, **kwargs)  # noqa: E501

    @validate_arguments
    def create_entry_with_http_info(self, create_audit_entry : Annotated[Optional[CreateAuditEntry], Field(description="Information about the entry to be created.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] CreateEntry: Create (persist) and audit entry..  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_entry_with_http_info(create_audit_entry, async_req=True)
        >>> result = thread.get()

        :param create_audit_entry: Information about the entry to be created.
        :type create_audit_entry: CreateAuditEntry
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
        :rtype: tuple(AuditEntry, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'create_audit_entry'
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
                    " to method create_entry" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_audit_entry'] is not None:
            _body_params = _params['create_audit_entry']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json', 'application/json-patch+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '201': "AuditEntry",
            '429': "ProblemDetails",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/auditing/entries', 'POST',
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
    async def get_processes(self, **kwargs) -> ResourceListOfAuditProcessSummary:  # noqa: E501
        ...

    @overload
    def get_processes(self, async_req: Optional[bool]=True, **kwargs) -> ResourceListOfAuditProcessSummary:  # noqa: E501
        ...

    @validate_arguments
    def get_processes(self, async_req: Optional[bool]=None, **kwargs) -> Union[ResourceListOfAuditProcessSummary, Awaitable[ResourceListOfAuditProcessSummary]]:  # noqa: E501
        """[EARLY ACCESS] GetProcesses: Get the latest audit entry for each process.  # noqa: E501

        This will never be `null`, though it may be empty.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_processes(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListOfAuditProcessSummary
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_processes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_processes_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_processes_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] GetProcesses: Get the latest audit entry for each process.  # noqa: E501

        This will never be `null`, though it may be empty.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_processes_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(ResourceListOfAuditProcessSummary, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method get_processes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

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
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "ResourceListOfAuditProcessSummary",
        }

        return self.api_client.call_api(
            '/api/auditing/processes', 'GET',
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
    async def list_entries(self, filter : Annotated[Optional[StrictStr], Field( description="The filter to be applied to the results.")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="The order to return the entries in.")] = None, size : Annotated[Optional[StrictInt], Field(description="The maximum number of entries to return.")] = None, state : Annotated[Optional[StrictStr], Field( description="The scrolling state, used to iterate through the data set.")] = None, **kwargs) -> ScrollableCollectionOfAuditEntry:  # noqa: E501
        ...

    @overload
    def list_entries(self, filter : Annotated[Optional[StrictStr], Field( description="The filter to be applied to the results.")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="The order to return the entries in.")] = None, size : Annotated[Optional[StrictInt], Field(description="The maximum number of entries to return.")] = None, state : Annotated[Optional[StrictStr], Field( description="The scrolling state, used to iterate through the data set.")] = None, async_req: Optional[bool]=True, **kwargs) -> ScrollableCollectionOfAuditEntry:  # noqa: E501
        ...

    @validate_arguments
    def list_entries(self, filter : Annotated[Optional[StrictStr], Field( description="The filter to be applied to the results.")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="The order to return the entries in.")] = None, size : Annotated[Optional[StrictInt], Field(description="The maximum number of entries to return.")] = None, state : Annotated[Optional[StrictStr], Field( description="The scrolling state, used to iterate through the data set.")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[ScrollableCollectionOfAuditEntry, Awaitable[ScrollableCollectionOfAuditEntry]]:  # noqa: E501
        """[EARLY ACCESS] ListEntries: Get the audit entries.  # noqa: E501

        This will never be `null`, though it may be empty.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_entries(filter, sort_by, size, state, async_req=True)
        >>> result = thread.get()

        :param filter: The filter to be applied to the results.
        :type filter: str
        :param sort_by: The order to return the entries in.
        :type sort_by: str
        :param size: The maximum number of entries to return.
        :type size: int
        :param state: The scrolling state, used to iterate through the data set.
        :type state: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ScrollableCollectionOfAuditEntry
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_entries_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.list_entries_with_http_info(filter, sort_by, size, state, **kwargs)  # noqa: E501

    @validate_arguments
    def list_entries_with_http_info(self, filter : Annotated[Optional[StrictStr], Field( description="The filter to be applied to the results.")] = None, sort_by : Annotated[Optional[StrictStr], Field( description="The order to return the entries in.")] = None, size : Annotated[Optional[StrictInt], Field(description="The maximum number of entries to return.")] = None, state : Annotated[Optional[StrictStr], Field( description="The scrolling state, used to iterate through the data set.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """[EARLY ACCESS] ListEntries: Get the audit entries.  # noqa: E501

        This will never be `null`, though it may be empty.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_entries_with_http_info(filter, sort_by, size, state, async_req=True)
        >>> result = thread.get()

        :param filter: The filter to be applied to the results.
        :type filter: str
        :param sort_by: The order to return the entries in.
        :type sort_by: str
        :param size: The maximum number of entries to return.
        :type size: int
        :param state: The scrolling state, used to iterate through the data set.
        :type state: str
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
        :rtype: tuple(ScrollableCollectionOfAuditEntry, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'filter',
            'sort_by',
            'size',
            'state'
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
                    " to method list_entries" % _key
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

        if _params.get('size') is not None:  # noqa: E501
            _query_params.append(('size', _params['size']))

        if _params.get('state') is not None:  # noqa: E501
            _query_params.append(('state', _params['state']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "ScrollableCollectionOfAuditEntry",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/auditing/entries', 'GET',
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
