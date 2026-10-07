from flask import Flask, request, jsonify

app = Flask(__name__)#um avariavel app atribuindo com a exetenção flasck

@app.route('/') #sintaxe do flask, @ é um decorator é um padrão de projeto
def home():
    return ("<h1>Hello World!</h1>")
@app.route('/usuario', methods=['GET'])
def buscar_usuario():
    usuario ={
        "nome": "Oscar",
        "idade": 25,
        "telefone": "(15)2400993381",
    }
    return usuario

@app.route('/produto', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400 #o jsonify vai responder para outra aplicação, e vai converter novamente para json

    print(f'novo produto: {dados}')

    return jsonify({"mensage": "produto salvo com sucesso",
                    "produto_cadastrado": dados}), 200


@app.route('/produtos', methods=['PUT'])
def atualizar_produto():
    produto = {
        "id" :1,
        "nome":"caderno",
        "preco": 19.99,
        "descricao": "caderno de capa dura espiral",
        "marca": "tilibra"
    }
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados Invalidos"}), 400
    if dados ['id'] == produto['id']:
        produto = dados
        print(f"Produto: {produto}")
        return jsonify({"mensage": "Produto atualizado com sucesso"}), 201
    else:
        return jsonify({"erro": "Produto não encontrado"}), 400




if __name__ == '__main__':
    app.run(debug=True)