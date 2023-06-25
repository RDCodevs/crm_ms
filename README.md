# CRM Medical Services

## Entorno de desarrollo

### Requisitos

---

- python 3.11
- pip
- poetry

### Ejecucion

---

Verificar existencia administrador de modulos de python `pip`

```text
pip install poetry
```

```text
poetry install
```

```text
python main.py
```

### GitHub

---

Pasos para la actualización del repositorio:
Siempre realizar un "pull" como primer paso.

```text
git pull origin main
```

```text
git init
```

```text
git status
```

```text
git add .
```

```text
git commit -m "Describir el cambio que se hace"
```

```text
git branch -M main
```

```text
Opcional: git remote add origin https://github.com/RDCodevs/crm_ms.git
```

```text
git push -u origin main
```

### Modelos del Gestionamiento de Citas

---
El modelo de administración contara con los siguientes atributos:

text
Datos generales, nombre, apelllido, email, telefono y el rol


text
La fecha de creación del perfil de administrador.


text
La fecha y hora de la última conexión del administrador al sistema.


text
Una lista de los permisos o privilegios asignados al administrador.


text
Una lista de los pacientes asignados por el administrador.


text
Una lista de los registros o actividades realizadas por el administrador en el sistema.


---
Modelo del asistente o secretario del medico

text
Datos generales, nombre, apelllido, email, y telefono
``
text
Nombre del supervisor a cargo
``

text
Una instancia de la clase "Admin" que representa la conexión directa con el administrador.
``

text
Una lista de las tareas asignadas al asistente por el administrador.
``

text
El horario disponible del asistente para realizar tareas.
``

text
La fecha y hora de la última conexión del asistente al sistema.
``

text
Una lista de los permisos o privilegios asignados al asistente por el administrador.
``

text
Una lista de las tareas completadas por el asistente.
``

```text
Una lista de los registros o actividades realizadas por el asistente en el sistema.
``