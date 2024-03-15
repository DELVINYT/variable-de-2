from flask import Flask

app = Flask(__name__)

#Pagina principal

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>" 

# Esto imprime tu nombre y edad
@app.route('/user/<name>')   
@app.route('/user/<name>/<int:edad>')   
def user(name = None, edad = None): 
    if edad == None:
        return f"<h1>Bienvenido user {name}</h1>" 
    else:
        return f"<h1>Bienvenido user {name} tienes {edad} años</h1>" 
    
# Esto es una calculadora basica

@app.route('/calculadora/<operation>/<int:num1>/<int:num2>')
def calculadora(num1,num2,num3,num4,operation):
    if operation == "suma":
        return f" {num1 + num2}"
    elif operation == "resta":
        return f" {num1 - num2}"
    elif operation == "multiplicacion":
        return f" {num1 * num2  }"
    elif operation == "divicion":
        return f" {num1 / num2}"
    elif operation == "elevado":
        return f" {num1 ** num2}"
    
        

#Login 

@app.route('/login')
def login():
    return "<h1>Iniciar sesion</h1>" 


if __name__  == '__main__':
    app.run( debug=True)