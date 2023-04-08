from flask import Blueprint, render_template ,request,redirect,flash,url_for
from .models import Post
from flask_login import login_required
from . import db
import os

views = Blueprint('views',__name__)


@views.route('/home',methods=['GET','POST'])
@login_required
def home():
            post = Post.query.all()
            return render_template("home.html",post=post)
        


@views.route('/post',methods=['GET','POST'])
@login_required
def post():
          if request.method=="POST":
             title = request.form.get("title")
             caption = request.form.get("caption")
             #for file
             f=request.files['file']
             print(f.filename)
             filename=title
             f.save(os.path.join('api/static/', filename))
             filepath='website/static/'+filename

             if title!='' and caption!='' and filepath!='':
                     p = Post(title=title,caption=caption)
                     db.session.add(p)
                     db.session.commit() 
                     return render_template("post.html")
             else :
                     return render_template("post.html")
             
          else:
                  return render_template("post.html")
          

@views.route('/delete/<int:id>')
@login_required
def delete_post(id):
        post_to_delete = Post.query.get(id)


        if request.method=="GET":
                db.session.delete(post_to_delete)
                db.session.commit()
                #flashing a success message
                #flash("Post deleted successfully!")
                return redirect(url_for('views.home'))
        else:
                flash("whoops there was a problem deleting post try again..")
                return render_template("home.html")