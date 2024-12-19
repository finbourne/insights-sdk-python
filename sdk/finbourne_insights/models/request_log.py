# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, constr
from finbourne_insights.models.link import Link

class RequestLog(BaseModel):
    """
    Holds logged information about a request performed on an API.  # noqa: E501
    """
    timestamp: datetime = Field(..., description="The timestamp of the request.")
    application: constr(strict=True, min_length=1) = Field(..., description="The name of the application that the request was made to.")
    id: constr(strict=True, min_length=1) = Field(..., description="The identifier of the request.")
    session_id: Optional[StrictStr] = Field(None, alias="sessionId", description="The identifier of the session that the request was made in.")
    verb: constr(strict=True, min_length=1) = Field(..., description="The HTTP verb of the request.")
    url: constr(strict=True, min_length=1) = Field(..., description="The URL of the request.")
    domain: Optional[StrictStr] = Field(None, description="The domain of the request.")
    user: constr(strict=True, min_length=1) = Field(..., description="The user who made the request.")
    user_type: Optional[StrictStr] = Field(None, alias="userType", description="The type of the user who made the request.")
    operation: Optional[StrictStr] = Field(None, description="The API operation invoked by the request.")
    outcome: constr(strict=True, min_length=1) = Field(..., description="The outcome of the request: Success, Failure or Error.")
    duration: Union[StrictFloat, StrictInt] = Field(..., description="The duration of the request in milliseconds.")
    http_status_code: StrictInt = Field(..., alias="httpStatusCode", description="The status code of the request.")
    error_code: Optional[StrictStr] = Field(None, alias="errorCode", description="Error code, if the request had a failure or error.")
    sdk_language: Optional[StrictStr] = Field(None, alias="sdkLanguage", description="The language of the SDK used.")
    sdk_version: Optional[StrictStr] = Field(None, alias="sdkVersion", description="The version of the SDK used.")
    source_application: Optional[StrictStr] = Field(None, alias="sourceApplication", description="The name of the application that made the request.")
    correlation_id: Optional[conlist(StrictStr)] = Field(None, alias="correlationId", description="The chain of requestIds preceding this request")
    impersonating_user: Optional[StrictStr] = Field(None, alias="impersonatingUser", description="The impersonating user. Only present if the request is an impersonated one")
    links: Optional[conlist(Link)] = None
    __properties = ["timestamp", "application", "id", "sessionId", "verb", "url", "domain", "user", "userType", "operation", "outcome", "duration", "httpStatusCode", "errorCode", "sdkLanguage", "sdkVersion", "sourceApplication", "correlationId", "impersonatingUser", "links"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RequestLog:
        """Create an instance of RequestLog from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if session_id (nullable) is None
        # and __fields_set__ contains the field
        if self.session_id is None and "session_id" in self.__fields_set__:
            _dict['sessionId'] = None

        # set to None if domain (nullable) is None
        # and __fields_set__ contains the field
        if self.domain is None and "domain" in self.__fields_set__:
            _dict['domain'] = None

        # set to None if user_type (nullable) is None
        # and __fields_set__ contains the field
        if self.user_type is None and "user_type" in self.__fields_set__:
            _dict['userType'] = None

        # set to None if operation (nullable) is None
        # and __fields_set__ contains the field
        if self.operation is None and "operation" in self.__fields_set__:
            _dict['operation'] = None

        # set to None if error_code (nullable) is None
        # and __fields_set__ contains the field
        if self.error_code is None and "error_code" in self.__fields_set__:
            _dict['errorCode'] = None

        # set to None if sdk_language (nullable) is None
        # and __fields_set__ contains the field
        if self.sdk_language is None and "sdk_language" in self.__fields_set__:
            _dict['sdkLanguage'] = None

        # set to None if sdk_version (nullable) is None
        # and __fields_set__ contains the field
        if self.sdk_version is None and "sdk_version" in self.__fields_set__:
            _dict['sdkVersion'] = None

        # set to None if source_application (nullable) is None
        # and __fields_set__ contains the field
        if self.source_application is None and "source_application" in self.__fields_set__:
            _dict['sourceApplication'] = None

        # set to None if correlation_id (nullable) is None
        # and __fields_set__ contains the field
        if self.correlation_id is None and "correlation_id" in self.__fields_set__:
            _dict['correlationId'] = None

        # set to None if impersonating_user (nullable) is None
        # and __fields_set__ contains the field
        if self.impersonating_user is None and "impersonating_user" in self.__fields_set__:
            _dict['impersonatingUser'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RequestLog:
        """Create an instance of RequestLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RequestLog.parse_obj(obj)

        _obj = RequestLog.parse_obj({
            "timestamp": obj.get("timestamp"),
            "application": obj.get("application"),
            "id": obj.get("id"),
            "session_id": obj.get("sessionId"),
            "verb": obj.get("verb"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "user": obj.get("user"),
            "user_type": obj.get("userType"),
            "operation": obj.get("operation"),
            "outcome": obj.get("outcome"),
            "duration": obj.get("duration"),
            "http_status_code": obj.get("httpStatusCode"),
            "error_code": obj.get("errorCode"),
            "sdk_language": obj.get("sdkLanguage"),
            "sdk_version": obj.get("sdkVersion"),
            "source_application": obj.get("sourceApplication"),
            "correlation_id": obj.get("correlationId"),
            "impersonating_user": obj.get("impersonatingUser"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
