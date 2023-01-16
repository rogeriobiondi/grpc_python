from concurrent import futures

import uuid
import copy
import logging
import grpc

import address_pb2
import address_pb2_grpc

class AddressServicer(address_pb2_grpc.AddressServicer):
    """Provides methods that implement functionality of the Address Service."""

    def __init__(self):
        """ Simple key-value db """
        self.db = {}
        
    def create(self, request, context):
        """ Set Implementation """
        request.id = str(uuid.uuid4())        
        self.db[request.id] = request
        return request

    def update(self, request, context):
        """ Set Implementation """
        self.db[request.id] = request
        return request

    def get(self, request, context):
        """ Get Implementation """
        adr = self.db[request.id]
        return adr

    def list(self, request, context):
        """ List Implementation"""
        for key in self.db:
            yield self.db[key]

    def delete(self, request, context):
        trashed = copy.copy(self.db[request.id])
        del self.db[request.id]
        return trashed

def serve():
    """ Server instantiation """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    address_pb2_grpc.add_AddressServicer_to_server(
        AddressServicer(), server)
    server.add_insecure_port('[::]:5051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    """ Main function """
    logging.basicConfig()
    serve()