# coding: utf-8

"""
    GroupDocs.Rewriter API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 25.3.0
    Contact: anton.perhunov@aspose.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from groupdocs_rewriter_cloud.models.opt import Opt
from groupdocs_rewriter_cloud.models.tokenizer import Tokenizer
from typing import Optional, Set
from typing_extensions import Self

class Model(BaseModel):
    """
    Model
    """ # noqa: E501
    loaded: Optional[StrictBool] = None
    models_id: Optional[StrictInt] = None
    models: Optional[List[StrictStr]] = None
    opt: Optional[Opt] = None
    timeout: Optional[StrictInt] = None
    tokenizer: Optional[Tokenizer] = None
    __properties: ClassVar[List[str]] = ["loaded", "models_id", "models", "opt", "timeout", "tokenizer"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Model from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of opt
        if self.opt:
            _dict['opt'] = self.opt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tokenizer
        if self.tokenizer:
            _dict['tokenizer'] = self.tokenizer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Model from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "loaded": obj.get("loaded"),
            "models_id": obj.get("models_id"),
            "models": obj.get("models"),
            "opt": Opt.from_dict(obj["opt"]) if obj.get("opt") is not None else None,
            "timeout": obj.get("timeout"),
            "tokenizer": Tokenizer.from_dict(obj["tokenizer"]) if obj.get("tokenizer") is not None else None
        })
        return _obj


