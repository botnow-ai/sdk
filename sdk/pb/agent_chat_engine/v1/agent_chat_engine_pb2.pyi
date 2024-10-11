from google.protobuf import timestamp_pb2 as _timestamp_pb2
from microcommon.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HistoryMessage(_message.Message):
    __slots__ = ("query", "answer")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    query: str
    answer: str
    def __init__(self, query: _Optional[str] = ..., answer: _Optional[str] = ...) -> None: ...

class CallRequest(_message.Message):
    __slots__ = ("id", "agent", "query", "history")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent: _common_pb2.Resource
    query: str
    history: _containers.RepeatedCompositeFieldContainer[HistoryMessage]
    def __init__(self, id: _Optional[str] = ..., agent: _Optional[_Union[_common_pb2.Resource, _Mapping]] = ..., query: _Optional[str] = ..., history: _Optional[_Iterable[_Union[HistoryMessage, _Mapping]]] = ...) -> None: ...

class CallResponse(_message.Message):
    __slots__ = ("id", "answer", "latency", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    answer: str
    latency: int
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., answer: _Optional[str] = ..., latency: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StreamCallRequest(_message.Message):
    __slots__ = ("id", "agent", "query", "history", "show_debug")
    ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    SHOW_DEBUG_FIELD_NUMBER: _ClassVar[int]
    id: str
    agent: _common_pb2.Resource
    query: str
    history: _containers.RepeatedCompositeFieldContainer[HistoryMessage]
    show_debug: bool
    def __init__(self, id: _Optional[str] = ..., agent: _Optional[_Union[_common_pb2.Resource, _Mapping]] = ..., query: _Optional[str] = ..., history: _Optional[_Iterable[_Union[HistoryMessage, _Mapping]]] = ..., show_debug: bool = ...) -> None: ...

class StreamCallResponse(_message.Message):
    __slots__ = ("id", "answer", "latency", "created_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    LATENCY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    answer: str
    latency: int
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., answer: _Optional[str] = ..., latency: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
