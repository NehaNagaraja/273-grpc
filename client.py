import sys

import grpc

import rocksplicator_pb2_grpc as rocksplicator_service
import rocksplicator_pb2 as rocksplicator_msg

e = rocksplicator_msg.Empty()

def run():
    channel = grpc.insecure_channel('localhost:50051')
    try:
        grpc.channel_ready_future(channel).result(timeout=10)
    except grpc.FutureTimeoutError:
        sys.exit('Error connecting to server')
    else:
        stub = rocksplicator_service.RocksplicatorStub(channel)
        metadata = [('ip', '127.0.0.1')]
        #response = stub.CreateUser(
         #   users_messages.CreateUserRequest(username='tom'),
          #  metadata=metadata,
        #)
        #if response:
         #   print("User created:", response.user.username)
        
        response = stub.GetNum(e)
        for resp in response:
            print(resp.uid)


if __name__ == '__main__':
    run()
