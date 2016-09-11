from lilypad.client.connect.api.request.impl import MessageRequest
from lilypad.client.connect.api.event import MessageEvent
from functools import wraps
# from org.arkhamnetwork.Arkkit.patches.networkevents import NetworkEvents

def get_lilypad_name():
    return connect.getSettings().getUsername()

def get_connect():
    return pyb.Bukkit.getPluginManager().getPlugin("LilyPad-Connect").getConnect()

def broadcast(channel, message):
    get_connect().request(MessageRequest([], channel, message))

def listen(channel):
    @wraps(func)
    def dec(func):
        @event_handler(MessageEvent)
        def handler(event):
            if event.getChannel() == channel:
                func(event)
        return func
