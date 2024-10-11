import grpc
import logging
from sdk.pb.agent_chat_engine.v1 import agent_chat_engine_pb2,agent_chat_engine_pb2_grpc
from sdk.pb.microcommon.v1 import common_pb2

def main():
    # Create a gRPC channel
    try:
        channel = grpc.insecure_channel('agent-chat-engine.dev.botnow.cn:8041')
    except Exception as e:
        logging.error(f"Error creating gRPC channel: {e}")
        return

    # Create a stub (client)
    client = agent_chat_engine_pb2_grpc.AgentChatEngineServiceStub(channel)

    # Prepare the history
    history = [
        agent_chat_engine_pb2.HistoryMessage(query="很高兴认识你，我是botnow", answer="你好，botnow。很高兴帮助你！"),
        agent_chat_engine_pb2.HistoryMessage(query="你可以帮我设计个智能体吗？", answer="好的，我非常乐意"),
    ]

    # Prepare the request
    request = agent_chat_engine_pb2.StreamCallRequest(
        agent=common_pb2.Resource(name="agent-ospvvx", project="banya"),
        query="以我的名字为基础，生成一个智能体提示词。",
        history=history
    )

    try:
        # Call the StreamCall method and get a stream of responses
        stream = client.StreamCall(request)

        # Continuously receive responses from the stream
        for response in stream:
            print(response.answer,end='')
            # # Process the received response
            # print(f"Received response: {response}")
    except grpc.RpcError as e:
        # Handle gRPC errors, including stream closure
        if e.code() == grpc.StatusCode.CANCELLED:
            print("Stream has been closed.")
        else:
            logging.error(f"Error receiving stream: {e}")
    finally:
        # Close the channel
        channel.close()

if __name__ == "__main__":
    main()
