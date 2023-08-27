from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def createApp():
    
    #Crear aplicación de flask
    app= Flask(__name__)

    # app.config.from_mapping(
    #         DEBUG=True,
    #         SECRETE_KEY='dev'
    #                         )
    
    # Se agrega la clase de configuración que se creo
    app.config.from_object('config.myclassConfig')

    # initialize the app with the extension
    db.init_app(app)
    
    # Para configurar CKEditor
    from flask_ckeditor import CKEditor                                         
    ckeditor = CKEditor(app)

    #Languages
    # Se requiere que 'es_ES' este intalada. Para revisar instalaciones se utiliza el comando: locale -a
    # import locale
    # locale.setlocale(locale.LC_ALL, 'es_ES')
    
    # Views Register
    from blogr import home
    app.register_blueprint(home.bp)

    from blogr import auth
    app.register_blueprint(auth.bp)
    
    from blogr import post
    app.register_blueprint(post.bp)
    
    from .models import User, Post
    with app.app_context():
        db.create_all()
    
    return app

