from flask import Blueprint, request, flash, redirect, url_for, g, render_template
from .auth import login_required # Se trae el decorador de sesión iniciada
from .models import Post         # Nos traemos el la tabla Post de la base de datos
from blogr import db             # Nos trameos la base de datos


bp= Blueprint('post', __name__, url_prefix = '/post')

@bp.route('/posts')
@login_required                 # Aplico la peditición de inicio de sección con el decorador que hice
def postsVIEW():
    posts = Post.query.all()    # Extraigo todos los valores de la tabla post de la clase Post
    return render_template('admin/posts.html', posts = posts) # Envío los datos al documento HTML

@bp.route('/create', methods=('GET', 'POST'))
def createVIEW():
    if request.method == 'POST':
        url = request.form.get('url')                       # Para obtener los url
        url = url.replace(' ','_')                          # Para sustituir los space por _
        title = request.form.get('title')                   # Para extraer el valor de title
        info= request.form.get('info')                      # Para extraer el valor de info
        content = request.form.get('ckeditor')              # Para extrarer el valor de CDEditor
        post = Post(g.user.id, url, title, info, content)   # Para crear valores un objeto de las caracteristicas de la lista 
        error = None

        # Comparando url de post con los existentes
        post_url = Post.query.filter_by(url = url).first()
        
        if post_url == None:                                # Si no existe esa url, se guardan el blog y el objeto de tipo Post y direcciona a la vista postsVIEW.
            db.session.add(post)
            db.session.commit()
            flash(f'El blog {post.title} se registro correctamente')
            return redirect(url_for('post.postsVIEW'))
        else:                                               # Si ya existe la url, manda un mensaje de error
            error=f'El URL {url} ya esta registrado'
        flash(error)

    return render_template('admin/create.html')            

@bp.route('/update/<int:id>', methods=('GET','POST'))
@login_required                                     #Tetición de seción activa
def updateVIEW(id):
    post = Post.query.get_or_404(id)                        # Se extran los valores del id

    # Se extraen los valores de los field. Cuando se realiza un llamado del metodo POST
    if request.method == 'POST':                                  
        post.title = request.form.get('title')              # Se rescribe el valor de title en la tabla para el usuario con el id registrado
        post.info = request.form.get('info')                # Se rescribe el valor de info en la tabla para el usuario con el id registrado
        post.content = request.form.get('ckeditor')         # Se rescribe el valor del contenido en la tabla para el usuario con el id registrado

        db.session.commit()                                 # Se guardan los cambio en la tabla
        flash(f'El blog {post.title} se actualizo correctamente')   # Mensaje se actualización exitosa
        return redirect(url_for('post.postsVIEW'))          #  Redireccion a la vista de posts

    return render_template('admin/update.html', post=post)


# --- Eliminar un post ---
# Aquí no se utiliza un rendar_template porque no se tiene un archivo .html que renderizar.
@bp.route('/delete/<int:id>')
@login_required                                     #Tetición de seción activa
def deleteVIEW(id):
    post = Post.query.get_or_404(id)                # Extra los valores del post.
    db.session.delete(post)                         # Elimina el post.
    db.session.commit()                             # Guarda los cambios.
    flash(f'El blog {post.title} se elimino correctamente')

    return redirect(url_for('post.postsVIEW'))