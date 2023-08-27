from blogr import db

# Modelo de usuario
#Si no pongo el nombre a la tabla, SQLArchemy coloca directamente el nombre de la calse en minusculas como el nombre de la tabla
class User(db.Model):
    __tablename__ = 'users'    #Colocamos el nombre de la tabla
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(120),unique = True, nullable = False)  # unique es para que se asigene el valor unico
    password = db.Column(db.Text, nullable = False)
    photo = db.Column(db.String(200))                                  # La foto la guardamos en una ruta

    # Constructor
    # En este caso se tiene la entrada de photo como vacia por default por que la foto se asigna despues
    
    def __init__(self, username, email, password, photo = None):
        self.username = username
        self.email = email
        self.password = password
        self.photo = photo
    
    # Para el caso el caso de utilizar flask shell 
    def __repr__(self):
        return f"User: '{self.username}'"
    

from datetime import datetime

# Modelo de publicación
class Post(db.Model):
    __tablename__ = 'posts'                 #Colocamos el nombre de la tabla
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False) # Se users.id porque la tabla se llama users. 
    url = db.Column(db.String(100), unique = True, nullable = False) # unique es para que se asigene el valor unico
    title = db.Column(db.String(100), nullable = False) # nullable = False es que no acepta valores nulos
    info = db.Column(db.Text)
    content = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)


    # Constructor
    # En este caso se tiene la entrada de photo como vacia por default por que la foto se asigna despues
    def __init__(self, author, url, title, info, content) -> None:
        self.author = author
        self.url = url
        self.title = title
        self.info = info
        self.content = content
    
    # Para el caso el caso de utilizar flask shell
    def __repr__(self) -> str:
        return f'Post: {self.title}'



