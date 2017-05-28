from channels.routing import route
from mvm_server.mvm_server_app.consumers import ws_message, ws_add, ws_disconnect, MyConsumer

channel_routing = [
    MyConsumer.as_route(path=r"^/chat/")
]

""" 
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
    """