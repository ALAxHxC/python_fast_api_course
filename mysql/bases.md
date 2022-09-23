# Creacion de tabla

* Este comando es para crear tablas
```
CREATE TABLE IF NOT EXISTS person (
  `id` INT NOT NULL,
  `type_id` VARCHAR(45) NOT NULL,
  `full_name` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`, `type_id`))
ENGINE = InnoDB;
```

* Esto elimina tablas
```
DROP table vehicule;
```

* Aqui un ejemplo con llave foranea

```
CREATE TABLE IF NOT EXISTS vehicule (
  matircule VARCHAR(200) NOT NULL,
  model VARCHAR(45) NOT NULL,
  year_production INT NOT NULL,
  brand VARCHAR(45) NOT NULL,
  n_wheels INT NULL DEFAULT 2,
  owner_id INT NOT NULL,
  owner_type VARCHAR(45) NOT NULL,
  PRIMARY KEY (matircule),
  INDEX `owner_fk_idx` (`owner_id` ASC, `owner_type` ASC),
  CONSTRAINT `owner_fk`
    FOREIGN KEY (`owner_id` , `owner_type`)
    REFERENCES person (`id` , `type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
```
* Insertar datos
```
INSERT INTO person VALUES ('1030626898', 'cc', 'daniel ortiz');
INSERT INTO `person` (`id`, `type_id`, `full_name`) VALUES ('1020826755', 'cc', 'laura romero');
INSERT INTO person VALUES ('1030626898', 'ps', 'otro ortiz');
```

* ACTUALIZAR UN REGISTRO
```
update person
set full_name = 'alirio ortiz'
where full_name ='otro ortiz';
```
* ELIMINAR UN REGISTRO
```
delete from person where id = 1020826755;
```

* OJO ESTO DEJAR ACTUALIZAR Y ELIMINAR SIN WHERE

```
SET SQL_SAFE_UPDATES = 0;
```