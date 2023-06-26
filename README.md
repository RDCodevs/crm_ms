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
git push -u origin main --force
```

### Modelos del Gestionamiento de Citas

---
Modelo de **Administración**:

- Datos generales, nombre, apelllido, email, telefono y el rol

- La fecha de creación del perfil de administrador.

- La fecha y hora de la última conexión del administrador al sistema.

- Una lista de los permisos o privilegios asignados al administrador.

- Una lista de los pacientes asignados por el administrador.

- Una lista de los registros o actividades realizadas por el administrador en el sistema.

---
Modelo de **Asistente**:

- Datos generales, nombre, apelllido, email, y telefono

- Nombre del supervisor a cargo

- Una instancia de la clase "Admin" que representa la conexión directa con el administrador.

- Una lista de las tareas asignadas al asistente por el administrador.

- El horario disponible del asistente para realizar tareas.

- La fecha y hora de la última conexión del asistente al sistema.

- Una lista de los permisos o privilegios asignados al asistente por el administrador.

- Una lista de las tareas completadas por el asistente.
  
- Una lista de los registros o actividades realizadas por el asistente en el sistema.
