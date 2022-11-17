# ERRORES COMUNES
* Si estas haciendo migraciones
```

 File "<string>", line 2, in create_engine
  File "/Users/dortizvega/reposp/python_fast_api_course/venv/lib/python3.9/site-packages/sqlalchemy/util/deprecations.py", line 309, in warned
    return fn(*args, **kwargs)
  File "/Users/dortizvega/reposp/python_fast_api_course/venv/lib/python3.9/site-packages/sqlalchemy/engine/create.py", line 520, in create_engine
    u, plugins, kwargs = u._instantiate_plugins(kwargs)
AttributeError: 'NoneType' object has no attribute '_instantiate_plugins'


```
* Falta el entorno: ``export SQL_URI="mysql+mysqldb://user:password@127.0.0.1/db"``