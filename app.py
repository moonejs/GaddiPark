from flask import Flask,render_template
from config import Config,db
from routes import all_blueprints
from models import User
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


for bp in all_blueprints:
    app.register_blueprint(bp)
    

@app.route('/')
def index():
    return render_template('index.html')

def chr_filter(value):
    return chr(value)

app.jinja_env.filters['chr'] = chr_filter


if __name__=='__main__':
    with app.app_context():
        db.create_all()
        admin=User.query.filter_by(is_admin=True).first()
        if not admin:
            password_hash =generate_password_hash('admin')
            admin=User(username='admin@gmail.com',password_hash=password_hash,full_name='Admin',is_admin=True)
            db.session.add(admin)
            db.session.commit()   
    app.run(debug=True)
    