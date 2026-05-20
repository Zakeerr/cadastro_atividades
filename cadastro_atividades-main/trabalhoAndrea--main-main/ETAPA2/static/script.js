const API = 'http://127.0.0.1:5000'


async function carregarTarefas() {

    const resposta = await fetch(`${API}/tarefas`)
    const tarefas = await resposta.json()

    const lista = document.getElementById('lista-tarefas')

    lista.innerHTML = ''

    tarefas.forEach(tarefa => {

        lista.innerHTML += `

            <div class="card">

                <h3>${tarefa.titulo}</h3>

                <p><strong>Descrição:</strong> ${tarefa.descricao}</p>

                <p><strong>Disciplina:</strong> ${tarefa.disciplina}</p>

                <p><strong>Prazo:</strong> ${tarefa.prazo}</p>

                <p class="status">
                    ${tarefa.status}
                </p>

            </div>
        `
    })
}


async function cadastrarTarefa() {

    const titulo = document.getElementById('titulo').value
    const descricao = document.getElementById('descricao').value
    const disciplina = document.getElementById('disciplina').value
    const prazo = document.getElementById('prazo').value

    await fetch(`${API}/tarefas`, {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({
            titulo,
            descricao,
            disciplina,
            prazo
        })
    })

    carregarTarefas()
}


async function concluirTarefa() {

    await fetch(`${API}/concluir`, {
        method: 'POST'
    })

    carregarTarefas()
}


async function desfazerAcao() {

    await fetch(`${API}/desfazer`, {
        method: 'POST'
    })

    carregarTarefas()
}

async function buscarTarefa() {

    const titulo = prompt("Digite o título:")

    const resposta = await fetch(
        `${API}/buscar/${titulo}`
    )

    const dados = await resposta.json()

    alert(JSON.stringify(dados))
}

async function verProxima() {

    const resposta = await fetch(
        `${API}/proxima`
    )

    const dados = await resposta.json()

    alert(JSON.stringify(dados))
}


async function carregarArquivo() {

    await fetch(`${API}/carregar`, {
        method: 'POST'
    })

    carregarTarefas()
}
carregarTarefas()