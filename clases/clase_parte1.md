## Scenario

1) Un desarrollador hizo cambios en el codigo, para optimizarlo y mejorar reglas, esto implica que debemos cargar nuevamente la base de datos
   * cuales son las tablas existentes?
   * en mysql worbench ejecutamos
   ```
   use db;
   show tables;
    ```
   * borramos la base de datos
   ````
    drop database db
    create database db;
   ````
   * volvemos a correr las migraciones
   `alembic upgrade head`
   * Cuales son las nuevas tablas?
   * Estuviste de acuerdo con los cambios?
   * que harias de diferente?
   * que se puede mejorar?
   