from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = ""
    if request.method == 'POST':
        n1 = request.form['nuno'].strip()
        n2 = request.form['ndos'].strip()
        n3 = request.form['ntres'].strip()

        # Verificar si son distintos
        if len({n1, n2, n3}) < 3:
            resultado = "Error: Los nombres deben ser distintos."
        else:
            l1, l2, l3 = len(n1), len(n2), len(n3)
            if l1 == l2 == l3:
                resultado = "Todos los nombres tienen el mismo largo."
            else:
                nombres = [(n1, l1), (n2, l2), (n3, l3)]
                mas_largo = max(nombres, key=lambda x: x[1])
                resultado = f"El nombre más largo es '{mas_largo[0]}' con {mas_largo[1]} letras."

    return render_template('ejercicio2.html', resultado=resultado)

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    promedio = 0
    asistencia = 0
    razones = []
    if request.method == 'POST':
        try:
            nota1 = float(request.form.get('nota1', 0))
            nota2 = float(request.form.get('nota2', 0))
            nota3 = float(request.form.get('nota3', 0))
            asistencia = float(request.form.get('asistencia', 0))
            promedio = round((nota1 + nota2 + nota3) / 3, 2)
            if promedio >= 40 and asistencia >= 75:
                resultado = 'Aprobado'
            else:
                resultado = 'Reprobado'
                if promedio < 40:
                    razones.append(f"El promedio es menor a 40 ({promedio})")
                if asistencia < 75:
                    razones.append(f"La asistencia es menor al 75% ({asistencia}%)")
        except ValueError:
            resultado = 'Error: Ingrese valores válidos'
    return render_template('ejercicio1.html', promedio=promedio, asistencia=asistencia,
                           resultado=resultado, razones=razones)

if __name__ == '__main__':
    app.run(debug=True)
