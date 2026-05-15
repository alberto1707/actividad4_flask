import os
import uuid
from markupsafe import Markup
from .extensions import appbuilder
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.upload import ImageUploadField
from flask_appbuilder.filemanager import ImageManager, secure_filename
from .models import Categoria, Producto


def short_namegen(file_data):
    _, ext = os.path.splitext(secure_filename(file_data.filename))
    return str(uuid.uuid1()) + ext


class CategoriaModelView(ModelView):
    datamodel = SQLAInterface(Categoria)
    label_columns = { "nombre": "Nombre",
        "descripcion": "Descripcion",
        "imagen": "Imagen",
        "estado": "Estado",
        "creado_en": "Creado en",
        "actualizado_en": "Actualizado en",
    }

    list_columns= ["nombre", "descripcion", "imagen", "estado", "creado_en"]
    add_columns = ["nombre", "descripcion", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "imagen", "estado", "creado_en","actualizado_en"]
    
    formatters_columns = {
        "imagen": lambda img: Markup(f'<img src="/static/uploads/{img}" height="50">') if img else ''
    }
    
    add_form_extra_fields = {
        "imagen": ImageUploadField(imagemanager=ImageManager(namegen=short_namegen))
    }
    edit_form_extra_fields = {
        "imagen": ImageUploadField(imagemanager=ImageManager(namegen=short_namegen))
    }


class ProductoModelView(ModelView):
    datamodel = SQLAInterface(Producto)
    label_columns = { "nombre" : "Nombre",
                    "descripcion": "Descripcion",
                    "precio" : "Precio",
                    "categoria": "Categoria",
                    "imagen": "Imagen",
                    "estado": "Estado",
                    "creado_en": "Creado en",
                    "actualizado_en":"Actualizado en"}
    list_columns= ["nombre", "precio", "categoria", "imagen", "estado"]
    add_columns = ["nombre", "descripcion","precio","categoria", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion","precio","categoria", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "precio", "imagen", "estado", "creado_en","actualizado_en"]
    
    formatters_columns = {
        "imagen": lambda img: Markup(f'<img src="/static/uploads/{img}" height="50">') if img else ''
    }
    
    add_form_extra_fields = {
        "imagen": ImageUploadField(imagemanager=ImageManager(namegen=short_namegen))
    }
    edit_form_extra_fields = {
        "imagen": ImageUploadField(imagemanager=ImageManager(namegen=short_namegen))
    }

appbuilder.add_view(
        CategoriaModelView,
        "Categorias",
        icon="fa-info",
        category="Configuraciones",
        category_icon="fa-info"
    )
    
appbuilder.add_view(
        ProductoModelView,
        "Productos",
        icon="fa-info",
        category="Configuraciones",
        category_icon="fa-info"
    )