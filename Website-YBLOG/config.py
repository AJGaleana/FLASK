# CONFIGURACIONES DEL PROYECTO

# Aqupi se agregan las configuraciones.
# Aquí se pueden poner las coneciones a la base de datos
# Aquí se puede poner las configuración de testing

# Link para las diferentes bases de datos
linkSQLite = "sqlite:///todolist.db" #Conexión SQLite
linkPostgresql = "postgresql://scott:tiger@localhost/project"

class myclassConfig:
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = linkSQLite
    CKEDITOR_PKG_TYPE = 'full'



