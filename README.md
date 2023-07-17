# event management system

### create and activate virtual environment
```shell
  python -m venv venv
  venv\Scripts\activate
```

### install all dependencies
```shell
    pip install -r requirements.txt
```

### create .env file in the root of your directory and past there data from .env.sample, changing fields if needed

### run project*
```shell
  uvicorn myapp.asgi:application
```

### run project with auto restart enabled
```shell
  hupper -m uvicorn myapp.asgi:application
```

