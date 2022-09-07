from hamcrest import assert_that, has_string
from framework.clients.grpc_client import HelloGrpcClient


class TestSayHello:
    def test_say_hello(self):
        client = HelloGrpcClient()
        response = client.say_hello(name='Anya')
        assert_that(response.message, has_string('Hello, Anya!'))

