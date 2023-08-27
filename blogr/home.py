from flask import Blueprint, render_template, request
from .models import User, Post

bp= Blueprint('home', __name__)


# Funcion para obtener el usuario
def getUser(id):
    user = User.query.get_or_404(id)
    return user

# Función para buscar
def searchPosts(query):
    # El .ilike permite buscar las coincidencias que tengan la balabra parciamente o totalmente en el atributo deceado
    # Se busca en el la columna title la palabra deceada .title
    # Se extran todos los valores que se encuentren .all()
    posts = Post.query.filter(Post.title.ilike(f'%{query}%')).all()
    return posts

@bp.route('/', methods=['GET','POST'])
def index():
    posts = Post.query.all()
    if request.method == 'POST':
        query = request.form.get('search')
        posts = searchPosts(query)
        value = 'hidden'
        return render_template('index.html', posts = posts, get_user = getUser, value=value)
    return render_template('index.html', posts=posts, get_user=getUser)


@bp.route('/blog/<url>')
def blogVIEW(url):
    post = Post.query.filter_by(url = url).first()
    return render_template('blog.html', post=post, get_user=getUser)