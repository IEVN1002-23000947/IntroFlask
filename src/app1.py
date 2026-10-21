from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    titulo='Hola!'
    lista=['Luis', 'Paco', 'Pedro']
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/distancia", methods=["GET","POST"])
def distancia():
    x1=0
    y1=0
    x2=0
    y2=0
    res=0
    if request.method == "POST":
        x1=request.form.get("x1")
        y1=request.form.get("y1")
        x2=request.form.get("x2")
        y2=request.form.get("y2")
        if x1 and y1 and x2 and y2:
            res=((float(x2)-float(x1))**2 + (float(y2)-float(y1))**2)**0.5

    return render_template("distancia.html", x1=x1, y1=y1, x2=x2, y2=y2, res=res)

@app.route("/operasbas", methods=["GET","POST"])
def operasbas():
    n1=0
    n2=0
    res=0
    operacion=""
    if request.method=="POST":
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        
        if request.form.get("operacion")=="suma":
            res=float(n1)+float(n2)
            
    return render_template("operasbas.html",n1=n1, n2=n2, res=res)

@app.route("/hola")
def hola():
    return "<h3> Saludo desde Hola</h3>"

@app.route("/user/<string:user>")
def user (user):
    return "Hola "+ user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n) 

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID: {} nombre: {}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1,n2):
    return "La suma es: {}".format(n1+n2)  

@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    nombre = ""
    compradores = ""
    tarjeta = "no"
    boletos = ""
    total = 0
    mensaje = ""

    if request.method == "POST":
        nombre = request.form.get("nombre", "")
        compradores = request.form.get("compradores", "")
        tarjeta = request.form.get("tarjeta", "no")
        boletos = request.form.get("boletos", "")

        if nombre.strip() == "" or compradores == "" or boletos == "":
            mensaje = "Completa todos los campos."
        else:
            compradores = int(compradores)
            boletos = int(boletos)

            if compradores <= 0 or boletos <= 0:
                mensaje = "Las cantidades deben ser mayores que cero."

            elif boletos > compradores * 7:
                mensaje = "No puedes comprar más de 7 boletos por persona."

            else:
                total = boletos * 12.000

                if boletos >= 3 and boletos <= 5:
                    total = total * 0.90
                elif boletos > 5:
                    total = total * 0.85

                if tarjeta == "si":
                    total = total * 0.90

    return render_template(
        "cinepolis.html",
        nombre=nombre,
        compradores=compradores,
        tarjeta=tarjeta,
        boletos=boletos,
        total=total,
        mensaje=mensaje
    )


if __name__ == "__main__":
    app.run(debug=True)