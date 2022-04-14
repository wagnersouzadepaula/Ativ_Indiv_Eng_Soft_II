from flask import Flask, render_template, request, escape
from funcoesUseACabeca import procura_letras

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    with open('procuraletras.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/results', methods=['POST'])
def pesquisa() -> 'html':
    frase = request.form['phrase']
    letras = request.form['letters']
    titulo = 'Aqui está o resultado'
    results = str(procura_letras(frase, letras))
    log_request(request, results)
    return render_template('results.html',
                           a_frase=frase,
                           a_letra=letras,
                           o_resultado=results,
                           o_titulo=titulo)
    # RENDER-TEMPLATE acima irá retornar ao html indicado como primeiro parâmetro o conteúdo das variáveis nos parâmetros seguintes.


@app.route('/')
@app.route('/entry')
def pagina_entrada() -> 'html':
    return render_template('entry.html', titulo='Bem vindo ao PROCURA LETRAS na web!')
    # @APP.ROUTE é um decorador, que servirá para informar o endereço da web que será utilizado para navegar.


@app.route('/verlog')
def ver_o_log() -> 'html':
    conteudo = []
    with open('procuraletras.log') as log:
        for line in log:
            conteudo.append([])
            for item in line.split('|'):
                conteudo[-1].append(escape(item))
    titles = ('Dados do Formulário', 'Remote_addr', 'User_agent', 'Results')
    return render_template('verlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=conteudo,)


if __name__ == '__main__':
    app.run(debug=True)
