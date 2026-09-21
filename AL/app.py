from flask import Flask

app = Flask(__name__)

pagina = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Uma perguntinha </title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            width: 100%;
            height: 100vh;
            overflow: hidden;

            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;

            background: linear-gradient(135deg, #ffd6e7, #fff0f6);
            font-family: Arial, sans-serif;
        }

        h1 {
            width: 90%;
            text-align: center;
            color: #d63384;
            font-size: 28px;
            margin-bottom: 40px;
        }

        button {
            width: 180px;
            height: 55px;
            border: none;
            border-radius: 15px;
            font-size: 20px;
            font-weight: bold;
            margin: 10px;
        }

        #sim {
            background: #ff4081;
            color: white;
        }

        #nao {
            background: #777;
            color: white;

            position: absolute;
            left: 50%;
            top: 60%;
            transform: translate(-50%, -50%);
        }
    </style>
</head>

<body>

    <h1 id="pergunta">
        Você está com raiva de mim? 🥺
    </h1>

    <button id="sim" onclick="clicouSim()">
        Sim 
    </button>

    <button id="nao">
        Não 😌
    </button>

    <script>
        const nao = document.getElementById("nao");

        nao.addEventListener("touchstart", fugir);
        nao.addEventListener("pointerenter", fugir);

        function fugir(event) {
            if (event) {
                event.preventDefault();
            }

            const largura = window.innerWidth - nao.offsetWidth;
            const altura = window.innerHeight - nao.offsetHeight;

            const x = Math.random() * largura;
            const y = Math.random() * altura;

            nao.style.transform = "none";
            nao.style.left = x + "px";
            nao.style.top = y + "px";
        }

        function clicouSim() {
            document.getElementById("pergunta").innerHTML =
            "Eu sabia sua covarde! 😭<br><br>Agora me perdoa? 🥺";
        }
    </script>

</body>
</html>
"""

@app.route("/")
def inicio():
    return pagina


app.run(host="0.0.0.0", port=5000)
