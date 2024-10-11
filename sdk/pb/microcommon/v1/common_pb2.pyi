from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Resource(_message.Message):
    __slots__ = ("name", "project")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    name: str
    project: str
    def __init__(self, name: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...
