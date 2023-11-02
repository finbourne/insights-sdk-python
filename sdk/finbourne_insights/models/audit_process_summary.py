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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
from finbourne_insights.models.audit_data import AuditData
from finbourne_insights.models.audit_data_summary import AuditDataSummary
from finbourne_insights.models.audit_process import AuditProcess

class AuditProcessSummary(BaseModel):
    """
    AuditProcessSummary
    """
    process: Optional[AuditProcess] = None
    latest_entry: Optional[AuditData] = Field(None, alias="latestEntry")
    summary: Optional[AuditDataSummary] = None
    __properties = ["process", "latestEntry", "summary"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AuditProcessSummary:
        """Create an instance of AuditProcessSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of latest_entry
        if self.latest_entry:
            _dict['latestEntry'] = self.latest_entry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuditProcessSummary:
        """Create an instance of AuditProcessSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuditProcessSummary.parse_obj(obj)

        _obj = AuditProcessSummary.parse_obj({
            "process": AuditProcess.from_dict(obj.get("process")) if obj.get("process") is not None else None,
            "latest_entry": AuditData.from_dict(obj.get("latestEntry")) if obj.get("latestEntry") is not None else None,
            "summary": AuditDataSummary.from_dict(obj.get("summary")) if obj.get("summary") is not None else None
        })
        return _obj
