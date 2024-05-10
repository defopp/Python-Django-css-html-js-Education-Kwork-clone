import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    
    def connect(self):
       self.accept()

       self.send(text_data=json.dumps({
           'type':'connection_established',
           'message':'You are now connected!'
       }))
       ... 
    
    def recive(self, text_data):
        ...

    def disconnect(self, text_data):
        ...