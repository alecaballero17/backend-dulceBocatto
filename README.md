
# 🍪 Dulce Bocatto - Backend

Este es el backend del sistema de preventa y pedidos de Dulce Bocatto, una aplicación desarrollada con **Python y Django** para gestionar productos, pedidos y detalles de cada venta. 

## 🚀 Tecnologías utilizadas

- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite (modo desarrollo)
- Postman (para pruebas de API)

## 🧩 Estructura del proyecto

- `tienda/models.py` → Definición de los modelos:
  - `Producto`: nombre, precio, stock, imagen
  - `Pedido`: fecha, cliente
  - `DetallePedido`: cantidad, subtotal, relación con producto y pedido

- `tienda/serializers.py` → Serializadores para exponer los modelos como JSON.

- `tienda/views.py` → Vistas tipo ViewSet con CRUD completo para cada entidad.

- `tienda/urls.py` → Rutas registradas para las APIs.

## 📌 Casos de uso

1. Registrar productos con nombre, precio, stock y una imagen.
2. Crear un nuevo pedido con uno o varios productos asociados.
3. Consultar pedidos realizados y sus respectivos detalles.
4. Actualizar y eliminar productos/pedidos según necesidad.

## 📫 Endpoints principales

| Método | URL                  | Descripción                    |
|--------|-----------------------|--------------------------------|
| GET    | `/api/productos/`     | Listar productos               |
| POST   | `/api/productos/`     | Crear producto                 |
| GET    | `/api/pedidos/`       | Listar pedidos                 |
| POST   | `/api/pedidos/`       | Crear pedido con detalles      |
| GET    | `/api/detalles/`      | Listar detalles de pedidos     |

> Los endpoints pueden cambiar según tu archivo `urls.py`, pero estos son los típicos en un `DefaultRouter`.

## 🧪 Cómo probar en Postman

1. Levantar el servidor local:

```bash
python manage.py runserver
```

2. Abrir Postman y usar las rutas mostradas arriba. 
3. Para crear un pedido, asegúrate de:
   - Enviar los IDs de productos correctos
   - Incluir la lista de `detalles` en el payload

Ejemplo de JSON para crear pedido:

```json
{
  "cliente": "Juan Pérez",
  "detalles": [
    { "producto": 1, "cantidad": 2 },
    { "producto": 3, "cantidad": 1 }
  ]
}
```

## 🛠 Requisitos

- Python 3.10 o superior
- Git
- Django:

```bash
pip install django djangorestframework
```

## 🧾 Cómo clonar el proyecto

```bash
git clone https://github.com/alecaballero17/backend-dulceBocatto.git
cd backend-dulceBocatto
python manage.py runserver
```

---

### 👨‍💻 Autor

- Ale Caballero  
- Proyecto académico – Universidad
