## Funcionalidades

Este proyecto está desarrollado con Django y Django REST Framework, ofreciendo los siguientes servicios backend para la gestión de datos:

- **Gestión de Productos (Product)**: Permite crear, leer, actualizar y eliminar productos, facilitando la administración del inventario.
- **Gestión de Clientes (Client)**: Facilita la creación, actualización y consulta de información relacionada con los clientes.
- **Gestión de Pedidos (Order)**: Permite manejar los pedidos de los clientes, con opciones para crear, actualizar, consultar y eliminar registros de pedidos.

Estos servicios backend proporcionan una API robusta para interactuar con las entidades mencionadas, permitiendo una administración eficiente y escalable de un sistema de comercio electrónico.

## Instalación

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

## 1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/Javi-cba/django-rest-fw-backend
   ```

## 2. Navega al directorio:
   ```bash
   cd django-rest-fw-backend
   ```
## 3. Crear y activar un entorno virtual (opcional pero recomendado):

### En Windows:
   ```
    python -m venv venv
    venv\Scripts\activate
   ```
### En macOS/Linux:
   ```
  python -m venv venv
  source venv/bin/activate
   ```
Una vez antivo el entorno virtual...

## 4. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## 5. Ejecuta el proyecto:
   ```bash
   python manage.py runserver
   ```
   
## 6. Ahora puedes acceder al proyecto en:
### http://127.0.0.1:8000/clients/
### http://127.0.0.1:8000/products/
   ### Y utilizar los servicios de la mi API.
   ![image](https://github.com/user-attachments/assets/e09fa3a0-80e7-44d7-9b1a-6cdcabaf87e5)

