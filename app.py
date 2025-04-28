from flask import Flask, render_template, request
from conversor import converter_comprimento, converter_peso, converter_temperatura, valida_float

app = Flask(__name__)

unidades_de_comprimento = ['km', 'm', 'dm', 'cm', 'mm', 'μm', 'nm', 'mi', 'yd', 'ft', 'in']
unidades_de_peso = ['t', 'kg', 'g', 'mg']
unidades_de_temperatura = ['C', 'K', 'F']

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        valor = request.form.get("valor")
        valor = valida_float(valor)

        if not isinstance(valor, float):
            return render_template("index.html", unidades=unidades_de_comprimento, erro=valor)

        unidade = request.form.get("unidade")
        unidade_convertida = request.form.get("unidade_convertida")
        valor_convertido = converter_comprimento(valor, unidade, unidade_convertida)
        return render_template('resultado.html', valor=valor, unidade_origem=unidade, resultado=valor_convertido, unidade_destino=unidade_convertida)

    return render_template("index.html", unidades=unidades_de_comprimento, active_page="comprimento")


@app.route("/peso", methods=["GET", "POST"])
def peso():
    if request.method == "POST":
        valor = request.form.get("valor")
        valor = valida_float(valor)

        if not isinstance(valor, float):  # verifica antes de converter
            return render_template("peso.html", unidades=unidades_de_peso, erro=valor)

        unidade = request.form.get("unidade")
        unidade_convertida = request.form.get("unidade_convertida")
        valor_convertido = converter_peso(valor, unidade, unidade_convertida)
        return render_template('resultado.html', valor=valor, unidade_origem=unidade, 
                               resultado=valor_convertido, unidade_destino=unidade_convertida)
    
    return render_template("peso.html", unidades=unidades_de_peso, active_page="peso")


@app.route("/temperatura", methods=["GET", "POST"])
def temperatura():
    if request.method == "POST":
        valor = request.form.get("valor")
        valor = valida_float(valor)

        if not isinstance(valor, float):  # verifica antes de converter
            return render_template("temperatura.html", unidades=unidades_de_temperatura, erro=valor)

        unidade = request.form.get("unidade")
        unidade_convertida = request.form.get("unidade_convertida")
        valor_convertido = converter_temperatura(valor, unidade, unidade_convertida)
        return render_template('resultado.html', valor=valor, unidade_origem=unidade, 
                               resultado=valor_convertido, unidade_destino=unidade_convertida)

    return render_template("temperatura.html", unidades=unidades_de_temperatura, active_page="temperatura")

if __name__ == "__main__":
    app.run(debug=True)