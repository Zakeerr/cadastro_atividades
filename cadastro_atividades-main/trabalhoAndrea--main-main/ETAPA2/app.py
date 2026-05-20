from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from src.service.gerenciador_service import GerenciadorService

app = Flask(__name__)
CORS(app)

service = GerenciadorService()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tarefas', methods=['GET'])
def listar_tarefas():

    tarefas = service.listar_tarefas()

    lista = []

    for tarefa in tarefas:

        lista.append({
            'titulo': tarefa.titulo,
            'descricao': tarefa.descricao,
            'disciplina': tarefa.disciplina,
            'prazo': tarefa.prazo,
            'status': tarefa.status
        })

    return jsonify(lista)


@app.route('/tarefas', methods=['POST'])
def cadastrar_tarefa():

    dados = request.json

    service.cadastrar_tarefa(
        dados['titulo'],
        dados['descricao'],
        dados['disciplina'],
        dados['prazo']
    )

    return jsonify({
        'mensagem': 'Tarefa cadastrada!'
    })


@app.route('/concluir', methods=['POST'])
def concluir_tarefa():

    service.concluir_tarefa()

    return jsonify({
        'mensagem': 'Tarefa concluída!'
    })


@app.route('/desfazer', methods=['POST'])
def desfazer():

    service.desfazer_ultima_acao()

    return jsonify({
        'mensagem': 'Ação desfeita!'
    })
@app.route('/buscar/<titulo>', methods=['GET'])
def buscar_tarefa(titulo):

    tarefa = service.buscar_tarefa(titulo)

    if tarefa is None:
        return jsonify({
            'erro': 'Tarefa não encontrada'
        })

    return jsonify({
        'titulo': tarefa.titulo,
        'descricao': tarefa.descricao,
        'disciplina': tarefa.disciplina,
        'prazo': tarefa.prazo,
        'status': tarefa.status
    })

@app.route('/proxima', methods=['GET'])
def proxima_tarefa():

    tarefa = service.proxima_tarefa()

    if tarefa is None:
        return jsonify({
            'erro': 'Fila vazia'
        })

    return jsonify({
        'titulo': tarefa.titulo,
        'descricao': tarefa.descricao,
        'disciplina': tarefa.disciplina,
        'prazo': tarefa.prazo,
        'status': tarefa.status
    })


@app.route('/excluir/<int:indice>', methods=['DELETE'])
def excluir_tarefa(indice):

    tarefa = service.excluir_tarefa(indice)

    if tarefa is None:
        return jsonify({
            'erro': 'Índice inválido'
        })

    return jsonify({
        'mensagem': 'Tarefa removida'
    })

@app.route('/carregar', methods=['POST'])
def carregar_arquivo():

    sucesso = service.carregar_arquivo(
        'data/tarefas.txt'
    )

    if sucesso:
        return jsonify({
            'mensagem': 'Arquivo carregado'
        })

    return jsonify({
        'erro': 'Erro ao carregar arquivo'
    })




if __name__ == '__main__':

    app.run(debug=True)