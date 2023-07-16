# event management system

### create and activate virtual environment
```shell
  python -m venv venv
  venv\Scripts\activate
```

### install uvicorn
```shell
  pip install uvicorn
```

### install django 
```shell
  pip install django
```

### start project
```shell
  django-admin startproject projectname  
```

### create .env file in the root of your directory

### install python-dotenv for importing variables from .env file
```shell
  pip install python-dotenv
```

### create or overwrite requirements.txt 
```shell
  pip freeze > requirements.txt
```

### run project*
```shell
  uvicorn projectname.asgi:applicationname
```

### install hupper to enable project auto restarting
```shell
  pip install hupper
```

### run project with auto restart enabled
```shell
  hupper -m uvicorn projectname.asgi:applicationname
```