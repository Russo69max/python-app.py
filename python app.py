from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route('/soma/<valor1>/<valorr>')
def dc(valor1,valorr):
    soma = f"{valor1 + valorr}"
    return f'o {valor1}com o {valorr} deu a soma de {soma}'
@app.route('/subtraçao/<valor2>/<valorrr>')
def pc(valor2,valorrr):
    subtraçao = f"{valor2 - valorrr}"
    return f'o {valor2} com o {valorrr} deu a subtraçao{subtraçao}'
@app.route('/multiplicaçao/<valor3>/<valorrrr>')
def tc(valor3,valorrrr):
    multiplicaçao = f"{valor3 * valorrrr}"
    return f'o{valor3}com o {valorrrr} deu a multiplicaçao{multiplicaçao}'
@app.route('/divisão/<valor4>/<valorrrrr>')
def hc(valor4,valorrrrr):
    divisão = f"{valor4 / valorrrrr}"
    if valor4 == 0:
        print ("coloque um numero valido")
    elif valorrrrr == 0:
        print("coloque um numero valido")
    else:
        return f'o {valor4}com o {valorrrrr} deu a divisão{divisão}'


if __name__ =="__main__":
    app.run(debug=True)
