from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def notify_message(new_message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'message',
        {'type': 'reload.messages', 'message': new_message}
    )
