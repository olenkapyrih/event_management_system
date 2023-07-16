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

### create .env file in the root of your directory

### run project*

```shell
  uvicorn myapp.asgi:application
```

### install hupper to enable project auto restarting

```shell
  pip install hupper
```

### run project with auto restart enabled

```shell
  hupper -m uvicorn myapp.asgi:application
```

