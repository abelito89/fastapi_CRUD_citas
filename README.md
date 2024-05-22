Claro, aquí tienes el README sin la sección de licencia:

```markdown
# API para Gestionar una Agenda

Esta API permite gestionar una agenda, incluyendo la creación, recuperación, actualización y eliminación de citas. La API está construida con FastAPI y utiliza Pydantic para la validación de datos.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn

## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea y activa un ambiente virtual.
3. Instala las dependencias utilizando el archivo `requirements.txt`.

```sh
# Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>

# Crear y activar el ambiente virtual
python -m venv venv
venv\Scripts\activate  # En Windows
source venv/bin/activate  # En macOS/Linux

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución de la API

Para ejecutar la API localmente, usa el siguiente comando:

```sh
uvicorn main:app --reload
```

Esto iniciará el servidor en `http://127.0.0.1:8000`. Puedes acceder a la documentación interactiva de la API en `http://127.0.0.1:8000/docs`.

## Modelos

### CitaSinId

Este modelo se utiliza para crear y actualizar citas sin requerir un ID.

- `Fecha`: `str` - La fecha de la cita.
- `Titulo`: `str` - El título de la cita.
- `Descripcion`: `str` - La descripción de la cita.

### Cita

Este modelo representa una cita con un ID autogenerado.

- `ID`: `uuid.UUID` - El identificador único de la cita.
- `Fecha`: `str` - La fecha de la cita.
- `Titulo`: `str` - El título de la cita.
- `Descripcion`: `str` - La descripción de la cita.

## Endpoints

### Crear una nueva cita

```http
POST /crear_cita
```

- **Descripción**: Crea una nueva cita y la agrega a la lista.
- **Cuerpo de la solicitud**: `CitaSinId`
- **Respuesta**: `Cita`

### Recuperar todas las citas

```http
GET /
```

- **Descripción**: Recupera la lista de todas las citas.
- **Respuesta**: `dict` con una lista de citas.

### Recuperar una cita por ID

```http
GET /cita_por_id/{id_cita}
```

- **Descripción**: Recupera una cita específica por su ID.
- **Parámetros de ruta**: `id_cita` (`uuid.UUID`)
- **Respuesta**: `Cita`

### Actualizar una cita

```http
PUT /actualizar_cita/{id_cita_modificar}
```

- **Descripción**: Actualiza una cita existente.
- **Parámetros de ruta**: `id_cita_modificar` (`uuid.UUID`)
- **Cuerpo de la solicitud**: `CitaSinId`
- **Respuesta**: `Cita`

### Eliminar una cita

```http
DELETE /eliminar_cita/{id_cita_eliminar}
```

- **Descripción**: Elimina una cita por su ID.
- **Parámetros de ruta**: `id_cita_eliminar` (`uuid.UUID`)
- **Respuesta**: `dict` con un mensaje de confirmación.

## Ejemplos de Uso

### Crear una cita

```json
POST /crear_cita
{
  "Fecha": "2024-05-20",
  "Titulo": "Reunión con cliente",
  "Descripcion": "Discutir los requisitos del proyecto."
}
```

### Obtener una cita por ID

```http
GET /cita_por_id/e4ba9b5e-eb9d-4517-b7be-68a24657c2d1
```

### Actualizar una cita

```json
PUT /actualizar_cita/39e9fe07-5ab3-4492-b627-92f8337bf9b1
{
  "Fecha": "2024-05-21",
  "Titulo": "Reunión con equipo",
  "Descripcion": "Planificación del sprint."
}
```

### Eliminar una cita

```http
DELETE /eliminar_cita/7a60f264-e9a2-44b9-8146-e58deeeb7895
```
