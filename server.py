from concurrent import futures
import time

import grpc

import rocksplicator_pb2_grpc as rocksplicator_service
import rocksplicator_pb2 as rocksplicator_msg

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class RocksplicatorService(rocksplicator_service.RocksplicatorServicer):

    def GetNum(self, request, context):
        for i in range (0,3):
            print i
            yield rocksplicator_msg.Response(uid = i)
                
        #yield rocksplicator_msg.Response(uid = 1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rocksplicator_service.add_RocksplicatorServicer_to_server(RocksplicatorService(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    try: 
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
