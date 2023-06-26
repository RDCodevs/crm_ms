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

### SQLite
- SQLite es una herramienta de software libre, que permite almacenar información en dispositivos empotrados de una forma sencilla, eficaz, potente, rápida y en equipos con pocas capacidades de hardware, como puede ser una PDA o un teléfono celular. SQLite implementa el estándar SQL92 y también agrega extensiones que facilitan su uso en cualquier ambiente de desarrollo. Esto permite que SQLite soporte desde las consultas más básicas hasta las más complejas del lenguaje SQL
  
Características
- La base de datos completa se encuentra en un solo archivo.
- Puede funcionar enteramente en memoria, lo que la hace muy rápida.
- Tiene un footprint menor a 230KB.
- Es totalmente autocontenida (sin dependencias externas).
- Cuenta con librerías de acceso para muchos lenguajes de programación.
- Soporta texto en formato UTF-8 y UTF-16, así como datos numéricos de 64 bits.
- Soporta funciones SQL definidas por el usuario (UDF).
- El código fuente es de dominio público y se encuentra muy bien documentado.

