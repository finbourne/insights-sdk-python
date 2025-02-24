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
from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conlist, constr 
from finbourne_insights.models.audit_data import AuditData
from finbourne_insights.models.audit_entry_note import AuditEntryNote
from finbourne_insights.models.audit_process import AuditProcess

class AuditEntry(BaseModel):
    """
    AuditEntry
    """
    id:  StrictStr = Field(...,alias="id") 
    var_date: datetime = Field(..., alias="date")
    process: AuditProcess = Field(...)
    data: AuditData = Field(...)
    notes: Optional[conlist(AuditEntryNote)] = None
    __properties = ["id", "date", "process", "data", "notes"]

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
    def from_json(cls, json_str: str) -> AuditEntry:
        """Create an instance of AuditEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of process
        if self.process:
            _dict['process'] = self.process.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in notes (list)
        _items = []
        if self.notes:
            for _item in self.notes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notes'] = _items
        # set to None if notes (nullable) is None
        # and __fields_set__ contains the field
        if self.notes is None and "notes" in self.__fields_set__:
            _dict['notes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuditEntry:
        """Create an instance of AuditEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuditEntry.parse_obj(obj)

        _obj = AuditEntry.parse_obj({
            "id": obj.get("id"),
            "var_date": obj.get("date"),
            "process": AuditProcess.from_dict(obj.get("process")) if obj.get("process") is not None else None,
            "data": AuditData.from_dict(obj.get("data")) if obj.get("data") is not None else None,
            "notes": [AuditEntryNote.from_dict(_item) for _item in obj.get("notes")] if obj.get("notes") is not None else None
        })
        return _obj
