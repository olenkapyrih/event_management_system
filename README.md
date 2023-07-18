# event management system

### create and activate virtual environment (for windows)
```shell
  python -m venv venv
  venv\Scripts\activate  
```

### create and activate virtual environment (for linux)
```shell
  python3 -m venv venv
  source venv/bin/activate
```

### install all dependencies
```shell
    pip install -r requirements.txt
```

### create .env file in the root of your directory and past there data from .env.sample, changing fields if needed

### run project*
```shell
  python manage.py
```

### build and launch application within Docker (for windows)
```shell
  docker-compose up --build
```

### build and launch application within Docker (for linux)
```shell
  sudo docker-compose up --build
```
