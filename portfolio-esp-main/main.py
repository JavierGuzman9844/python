# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template(
        'index.html', button_python=button_python,
        button_discord=button_discord,
        button_html=button_html, 
        button_db=button_db
        )

@app.route('/submit', methods=['POST'])
def datos_form():
    email = request.form.get('email')
    text = request.form.get('text')
    with open('data.txt', 'a') as file:
        file.write(f'Email: {email}\n')
        file.write(f'Text: {text}\n\n')
    return render_template(
        'index.html', email=email, 
        text=text
        )

if __name__ == "__main__":
    app.run(debug=True)
