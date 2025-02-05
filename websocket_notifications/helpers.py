import hashlib
import random
import time
from typing import Dict

from django.apps import apps
from django.db import models


def generate_random_code(seed: str) -> str:
    """Generates a random code using the given seed."""
    return hashlib.sha256(
        ("{}-{}-{}".format(seed, time.time(), random.randint(100, 999))).encode("utf-8")
    ).hexdigest()


def send_message(obj: models.Model, payload: Dict) -> None:
    """Gets the notifications group and sends the payload."""
    NotificationGroup = apps.get_model("websocket_notifications.NotificationGroup")
    notification_group, _ = NotificationGroup.objects.get_or_create_for_object(obj)
    notification_group.send(payload=payload)
