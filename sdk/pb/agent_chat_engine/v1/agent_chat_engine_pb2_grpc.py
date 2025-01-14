# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from sdk.pb.agent_chat_engine.v1 import agent_chat_engine_pb2 as agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in agent_chat_engine/v1/agent_chat_engine_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class AgentChatEngineServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.unary_unary(
                '/agent_chat_engine.v1.AgentChatEngineService/Call',
                request_serializer=agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.CallRequest.SerializeToString,
                response_deserializer=agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.CallResponse.FromString,
                _registered_method=True)
        self.StreamCall = channel.unary_stream(
                '/agent_chat_engine.v1.AgentChatEngineService/StreamCall',
                request_serializer=agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.StreamCallRequest.SerializeToString,
                response_deserializer=agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.StreamCallResponse.FromString,
                _registered_method=True)


class AgentChatEngineServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamCall(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentChatEngineServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.CallRequest.FromString,
                    response_serializer=agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.CallResponse.SerializeToString,
            ),
            'StreamCall': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamCall,
                    request_deserializer=agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.StreamCallRequest.FromString,
                    response_serializer=agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.StreamCallResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'agent_chat_engine.v1.AgentChatEngineService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('agent_chat_engine.v1.AgentChatEngineService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AgentChatEngineService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/agent_chat_engine.v1.AgentChatEngineService/Call',
            agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.CallRequest.SerializeToString,
            agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.CallResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StreamCall(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/agent_chat_engine.v1.AgentChatEngineService/StreamCall',
            agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.StreamCallRequest.SerializeToString,
            agent__chat__engine_dot_v1_dot_agent__chat__engine__pb2.StreamCallResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
