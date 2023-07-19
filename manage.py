import os
import sys
import uvicorn
from config import settings


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    asgi_app_path = "myapp.asgi:application"
    host = settings.HOST
    port = settings.PORT
    uvicorn.run(asgi_app_path, host=host, port=port, reload=True)
