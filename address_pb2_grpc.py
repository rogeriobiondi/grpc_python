# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import address_pb2 as address__pb2


class AddressStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/Address/create',
                request_serializer=address__pb2.address_obj.SerializeToString,
                response_deserializer=address__pb2.address_obj.FromString,
                )
        self.update = channel.unary_unary(
                '/Address/update',
                request_serializer=address__pb2.address_obj.SerializeToString,
                response_deserializer=address__pb2.address_obj.FromString,
                )
        self.get = channel.unary_unary(
                '/Address/get',
                request_serializer=address__pb2.get_request.SerializeToString,
                response_deserializer=address__pb2.address_obj.FromString,
                )
        self.list = channel.unary_stream(
                '/Address/list',
                request_serializer=address__pb2.list_request.SerializeToString,
                response_deserializer=address__pb2.address_obj.FromString,
                )
        self.delete = channel.unary_unary(
                '/Address/delete',
                request_serializer=address__pb2.get_request.SerializeToString,
                response_deserializer=address__pb2.address_obj.FromString,
                )


class AddressServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AddressServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=address__pb2.address_obj.FromString,
                    response_serializer=address__pb2.address_obj.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=address__pb2.address_obj.FromString,
                    response_serializer=address__pb2.address_obj.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=address__pb2.get_request.FromString,
                    response_serializer=address__pb2.address_obj.SerializeToString,
            ),
            'list': grpc.unary_stream_rpc_method_handler(
                    servicer.list,
                    request_deserializer=address__pb2.list_request.FromString,
                    response_serializer=address__pb2.address_obj.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=address__pb2.get_request.FromString,
                    response_serializer=address__pb2.address_obj.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Address', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Address(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Address/create',
            address__pb2.address_obj.SerializeToString,
            address__pb2.address_obj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Address/update',
            address__pb2.address_obj.SerializeToString,
            address__pb2.address_obj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Address/get',
            address__pb2.get_request.SerializeToString,
            address__pb2.address_obj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Address/list',
            address__pb2.list_request.SerializeToString,
            address__pb2.address_obj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Address/delete',
            address__pb2.get_request.SerializeToString,
            address__pb2.address_obj.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
