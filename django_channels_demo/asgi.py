"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_channels_demo.settings")
django.setup()


import django_channels_demo.routing

application = django_channels_demo.routing.application
