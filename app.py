from flask import Flask

app = Flask(__name__)#um avariavel app atribuindo com a exetenção flasck

@app.route('/') #sintaxe do flask, @ é um decorator é um padrão de projeto
def home():
    return ("<h1>Hello World!</h1>")
@app.route('/usuario')
def buscar_usuario():
    usuario ={
        "nome": "Sanches",
        "idade": 17,
        "telefone": "(15)2400993381",


    }
    return usuario




if __name__ == '__main__':
    app.run(debug=True)