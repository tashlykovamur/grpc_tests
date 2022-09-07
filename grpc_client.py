import grpc
from framework.clients.proto import helloworld_pb2, helloworld_pb2_grpc


class HelloGrpcClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 1234

        # instantiate a channel
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = helloworld_pb2_grpc.GreeterStub(self.channel)

    def say_hello(self, name) -> helloworld_pb2.HelloReply:
        """
        Client function to call the rpc for the SayHello
        """
        request = helloworld_pb2.HelloRequest(name=name)
        return self.stub.SayHello(request)
