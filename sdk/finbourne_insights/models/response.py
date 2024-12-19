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


from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from finbourne_insights.models.link import Link

class Response(BaseModel):
    """
    DTO of Finbourne.AspNetCore.Http.TrackingEntry.ResponseInformation.  # noqa: E501
    """
    headers: Optional[Dict[str, conlist(StrictStr)]] = Field(None, description="The headers")
    content_length: Optional[StrictInt] = Field(None, alias="contentLength", description="The actual length of the body, which may be larger than the data recorded in Finbourne.Insights.WebApi.Dtos.Response.Body  (e.g. if actual Body is large, or not convertible to a string)")
    content_type: Optional[StrictStr] = Field(None, alias="contentType", description="The content type")
    body: Optional[StrictStr] = Field(None, description="The recorded content.")
    body_was_truncated: Optional[StrictBool] = Field(None, alias="bodyWasTruncated", description="Determines if the recorded body was truncated.")
    status_code: Optional[StrictInt] = Field(None, alias="statusCode", description="Http Status Code of the request.")
    links: Optional[conlist(Link)] = None
    __properties = ["headers", "contentLength", "contentType", "body", "bodyWasTruncated", "statusCode", "links"]

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
    def from_json(cls, json_str: str) -> Response:
        """Create an instance of Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in headers (dict of array)
        _field_dict_of_array = {}
        if self.headers:
            for _key in self.headers:
                if self.headers[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.headers[_key]
                    ]
            _dict['headers'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if headers (nullable) is None
        # and __fields_set__ contains the field
        if self.headers is None and "headers" in self.__fields_set__:
            _dict['headers'] = None

        # set to None if content_length (nullable) is None
        # and __fields_set__ contains the field
        if self.content_length is None and "content_length" in self.__fields_set__:
            _dict['contentLength'] = None

        # set to None if content_type (nullable) is None
        # and __fields_set__ contains the field
        if self.content_type is None and "content_type" in self.__fields_set__:
            _dict['contentType'] = None

        # set to None if body (nullable) is None
        # and __fields_set__ contains the field
        if self.body is None and "body" in self.__fields_set__:
            _dict['body'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Response:
        """Create an instance of Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Response.parse_obj(obj)

        _obj = Response.parse_obj({
            "headers": obj.get("headers"),
            "content_length": obj.get("contentLength"),
            "content_type": obj.get("contentType"),
            "body": obj.get("body"),
            "body_was_truncated": obj.get("bodyWasTruncated"),
            "status_code": obj.get("statusCode"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
