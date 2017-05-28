from channels import Group
from channels.generic.websockets import WebsocketConsumer
from channels.generic.websockets import JsonWebsocketConsumer

# Connected to websocket.connect
from mvm_server.mvm_server_app import services
from mvm_server.mvm_server_app.models import Minion
from mvm_server.mvm_server_app.serializers import MinionSerializer


def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("chat").add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    print('message received')
    minion = Minion.objects.get(pk=1)
    serializer = MinionSerializer(minion)
    Group("chat").send({
        "text": serializer,
    })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)

class MyConsumer(JsonWebsocketConsumer):

    # Set to True if you want it, else leave it out
    strict_ordering = False

    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return ["test"]

    def connect(self, message, **kwargs):
        """
        Perform things on connection start
        """
        # Accept the connection; this is done by default if you don't override
        # the connect function.
        self.message.reply_channel.send({"accept": True})

    def receive(self, content, **kwargs):
        """
        Called when a message is received with decoded JSON content
        """
        # Simple echo
        print('message received')
        minion = Minion.objects.get(pk=1)
        serializer = MinionSerializer(minion)
        self.send({
            "text": serializer,
        })

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        pass