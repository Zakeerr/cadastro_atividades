from src.database.conexao import conectar


class TarefaRepository:

    def salvar(self, tarefa):

        conexao = conectar()

        cursor = conexao.cursor()

        sql = """
        INSERT INTO tarefas
        (titulo, descricao, disciplina, prazo, status)
        VALUES (%s, %s, %s, %s, %s)
        """

        valores = (
            tarefa.titulo,
            tarefa.descricao,
            tarefa.disciplina,
            tarefa.prazo,
            tarefa.status
        )

        cursor.execute(sql, valores)

        conexao.commit()

        cursor.close()
        conexao.close()

    def listar(self):

        conexao = conectar()

        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM tarefas")

        tarefas = cursor.fetchall()

        cursor.close()
        conexao.close()

        return tarefas