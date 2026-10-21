from flask import Flask, request, jsonify, render_template
from psycopg2.extras import RealDictCursor


from database import criar_conexao

app = Flask(__name__)#um avariavel app atribuindo com a exetenção flasck

@app.route('/') #sintaxe do flask, @ é um decorator é um padrão de projeto
def home():
    return ("<h1>Hello World!</h1>")


@app.route('/filme', methods=['GET'])
def listar_filmes():
   conn = criar_conexao()
   cursor = conn.cursor(cursor_factory=RealDictCursor)

   cursor.execute("SELECT * FROM filmes")
   resposta = cursor.fetchall()

   conn.close()
   return render_template("index.html", filmes=resposta)

@app.route('/produto', methods=['POST'])
def cadastrar_filme():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400 #o jsonify vai responder para outra aplicação, e vai converter novamente para json

    print(f'novo filme: {dados}')

    conn = criar_conexao()
    cursor = conn.cursor()

    cursor.execute(
        '''
            INSERT INTO filmes  (usuario_id, titulo, ano_lancamento,
            genero, nota, capa_url)
            VALUES ( %s, %s, %s, %s, %s, %s) RETURNING id
        ''',
        (dados['usuario_id'], dados['titulo'], dados['ano_lancamento'], dados['genero'],
         dados['nota'], dados['capa_url'])
     )

    novo_id = cursor.fetchone()[0]
    conn.commit()

    conn.close()

    return jsonify({"mensage": "Filme salvo com sucesso!", "filme_id": novo_id}), 201


    return jsonify({"mensage": "produto salvo com sucesso",
                    "produto_cadastrado": dados}), 200


@app.route('/produtos', methods=['PUT'])
def atualizar_filme():
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

@app.route('/teste/db', methods=['GET'])
def testar_conexao():
    conn = criar_conexao()
    conn.close()
    return jsonify({"menssage": "banco conectado com sucesso"}), 200




if __name__ == '__main__':
    app.run(debug=True)