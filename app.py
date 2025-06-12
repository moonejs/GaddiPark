from flask import Flask,render_template
from config import Config,db
from routes import all_blueprints

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


for bp in all_blueprints:
    app.register_blueprint(bp)
    

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    