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
from pydantic.v1 import BaseModel, Field, conlist, Field
from finbourne_insights.models.bucket import Bucket

class Histogram(BaseModel):
    """
    A histogram showing an item's count in buckets of equal timespans.  # noqa: E501
    """
    buckets: Optional[conlist(Bucket)] = Field(None, description="An ordered list of the histogram buckets.")
    __properties = ["buckets"]

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
    def from_json(cls, json_str: str) -> Histogram:
        """Create an instance of Histogram from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in buckets (list)
        _items = []
        if self.buckets:
            for _item in self.buckets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['buckets'] = _items
        # set to None if buckets (nullable) is None
        # and __fields_set__ contains the field
        if self.buckets is None and "buckets" in self.__fields_set__:
            _dict['buckets'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Histogram:
        """Create an instance of Histogram from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Histogram.parse_obj(obj)

        _obj = Histogram.parse_obj({
            "buckets": [Bucket.from_dict(_item) for _item in obj.get("buckets")] if obj.get("buckets") is not None else None
        })
        return _obj
