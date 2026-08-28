from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def hello_world():
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>chau</title>
    </head>
    <body>

        <h1>Hello</h1>

        <button onclick="mostrarMensagem()">Clique aqui</button>

        <p id="mensagem"></p>

        <script>
            function mostrarMensagem() {
                document.getElementById("mensagem").innerText =
                    "Olá! Funcionou!";
            }
        </script>

    </body>
    </html>
    """

    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
