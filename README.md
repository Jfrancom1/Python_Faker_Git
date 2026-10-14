

#  Actividad 3 – Inserción Masiva de Datos con Python, Faker y MySQL

Este proyecto implementa la creación automática de una tabla en MySQL y la inserción de 100.000 registros utilizando **Python**, **SQLAlchemy** y **Faker**.  
La actividad se desarrolla en el entorno de un proyecto real de  datos, siguiendo buenas prácticas como:

- Uso de entornos virtuales.
- Manejo de credenciales mediante `.env`.
- Control de versiones con Git.
- Inserción eficiente mediante batch processing.
- Documentación clara y reproducible.

---

##  Características del proyecto

- Conexión automática a MySQL usando SQLAlchemy.
- Creación de la tabla: `personas_juanfelipe`  
- Generación de datos falsos realistas (es_CO).
- Inserción eficiente en lotes (batch size configurable).
- Total: **100.000 registros** exactos.
- Estructura organizada y modular.

---

##  Estructura de la tabla

La tabla `personas_juanfelipe` contiene las siguientes columnas:

| Campo       | Tipo        | Descripción                     |
|-------------|-------------|----------------------------------|
| id          | INT PK      | Identificador autoincremental   |
| nombre      | VARCHAR(100)| Nombre completo                 |
| correo      | VARCHAR(150)| Correo electrónico              |
| ciudad      | VARCHAR(100)| Ciudad                          |
| telefono    | VARCHAR(50) | Teléfono                        |
| ocupacion   | VARCHAR(100)| Trabajo u ocupación             |
| direccion   | VARCHAR(200)| Dirección generada por Faker    |
| edad        | INT         | Edad entre 18 y 90 años         |

---

##  Tecnologías utilizadas

- **Python 3.10+**
- **MySQL** (local)
- **SQLAlchemy**
- **PyMySQL**
- **Faker (es_CO)**
- **python-dotenv**
- **Visual Studio Code**
- **Git & GitHub**

---

##  Instalación y ejecución

###  Clonar el repositorio
```bash
git clone https://github.com/Jfrancom1/Python_Faker_Git.git
```

### Crear y activar entorno virtual

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Instalar dependencias 
```bash
python -m pip install -r requirements.txt
```

### Configurar variables de entorno
Crear un archivo `.env` basado en `.env.example`:
```env
DB_USER=root
DB_PASS=tu_contrasena
DB_HOST=localhost
DB_PORT=3306
DB_NAME=auto_db
```

### Ejecutar el script principal
```bash
python main.py
```

### Verificación en MySQL (DBeaver)
```sql
USE auto_db;
SELECT COUNT(*) FROM personas_juanfelipe;
```

---

### Archivos importantes del proyecto

- `main.py` → script principal que crea la tabla e inserta datos.
- `requirements.txt` → dependencias del proyecto.
- `.env.example` → plantilla para credenciales.
- `.gitignore` → evita subir entorno virtual y secretos.
- `README.md` → documentación del proyecto.

---

👨‍💻 **Autor**

Juan Felipe Franco  
Universidad de Antioquia – Bases de Datos




