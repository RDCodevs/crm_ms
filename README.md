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
  
---
Modelo de **Citas**:

- Una instancia de la clase "Paciente" que representa al paciente asociado a la cita.
  
- Una instancia de la clase "Medico" que representa al médico asociado a la cita.
  
- El estado de la cita (por ejemplo, programada, confirmada, cancelada).
  
- Una instancia de la clase "Admin"
  
- Una instancia de la clase "Assistant"
  
- Observaciones o notas adicionales sobre la cita.
  
- Un indicador para registrar si se ha enviado un recordatorio al paciente o no.
  
- El usuario que registró la cita en el sistema.

---
Modelo de **Paciente**:

- Dato del paciente nombre
  
- Dato del paciente apellido
  
- Dato del paciente género
  
- Dato del paciente altura
  
- Dato del paciente peso
  
- Dato del paciente etnia
  
- Dato del paciente alergias
  
- Dato del paciente Hipertensión Arterial
  
- Observaciones sobre el cie del paciente
  
- Dato del paciente nacimiento
  
- Dato del paciente tipo de sangre
  
- Dato del paciente dirección
  
- Dato del paciente teléfono

---
Modelo de **Medico**:

- Dato del médico ceédula
  
- Dato del médico nombre
  
- Dato del médico apellido

- Dato del médico género

- Dato del médico especialidad
  
- Dato del médico teléfono

- Dato del médico email

- Dato del médico dirección

- Dato del médico email

- El horario de atención del médico

- El horario de finalización de atención del médico

- La experiencia o años de práctica del médico.

- Una lista de las certificaciones o reconocimientos obtenidos por el médico.

### SQLite

- SQLite es una herramienta de software libre, que permite almacenar información en dispositivos empotrados de una forma sencilla, eficaz, potente, rápida y en equipos con pocas capacidades de hardware, como puede ser una PDA o un teléfono celular. SQLite implementa el estándar SQL92 y también agrega extensiones que facilitan su uso en cualquier ambiente de desarrollo. Esto permite que SQLite soporte desde las consultas más básicas hasta las más complejas del lenguaje SQL
  
Características:

- La base de datos completa se encuentra en un solo archivo.
- Puede funcionar enteramente en memoria, lo que la hace muy rápida.
- Tiene un footprint menor a 230KB.
- Es totalmente autocontenida (sin dependencias externas).
- Cuenta con librerías de acceso para muchos lenguajes de programación.
- Soporta texto en formato UTF-8 y UTF-16, así como datos numéricos de 64 bits.
- Soporta funciones SQL definidas por el usuario (UDF).
- El código fuente es de dominio público y se encuentra muy bien documentado.
  
Tipos de datos admitidos

-La lista de tipos de datos y lenguajes aceptados por MySQL es más larga. Es compatible con algunos formatos más comunes del mercado como Tinyint, Timestamp, MediumBlob, MediumText y Datetime. SQLite solo es compatible con Integer, Real, Text y Blob.

Capacidad de almacenamiento

-Mientras que uno tiene capacidad para base de datos de 4GB como máximo, la biblioteca Lite solo admite bases de datos de 250kb o 1GB como máximo. Por este motivo, acaba siendo más adecuado para aplicaciones más pequeñas que necesitan menos ancho de banda.

Consultas

-Debido a que tiene menos espacio, en el caso de SQLite las consultas suelen tardar un poco más y no son simultáneas. Por otro lado, MySQL ya ofrece consultas paralelas más rápido. Esto significa que la devolución de las búsquedas puede ser más o menos lenta, según el sistema que elijas.

Acceso y seguridad

-En cuanto a seguridad, MySQL cuenta con un sistema de autenticación y control de usuarios. En la práctica esto quiere decir que cualquier persona que desee acceder a la base de datos proporcionará su usuario y contraseña. Sin esto, no es posible tener acceso.

Ventajas

- Es estable, multiplataforma y compatible con versiones anteriores.
- Su código es de dominio público y gratuito.
- No requiere instalación o configuración.
- Guarda la base de datos en un solo archivo.

### Testing

Run in the root proyect

```
  python -m doctest @testfile
```

```
  python -m unittest @testfile
```
