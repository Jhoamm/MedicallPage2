from flask import Flask
from flask import render_template
app = Flask(__name__)

#ruteo de mis paginas 
@app.route('/')
def index():
    return render_template('empleados/index.html')

if __name__ == '__main__':
    app.run(debug = True)


