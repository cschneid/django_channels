from channels.generic.websocket import AsyncWebsocketConsumer
import json

import time
import random

from chat.models import Thing

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        things = Thing.objects.all()
        print(things)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        time.sleep(random.random())

        things = Thing.objects.all()
        print(things)

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        time.sleep(random.random())
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        time.sleep(random.random())
        message = event['message']
        time.sleep(random.random())
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
