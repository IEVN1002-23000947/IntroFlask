from blueprints.alumnos.routes import alumnos_bp
from blueprints.maestros.routes import maestros_bp

def registrar_blueprints(app):
    app.register_blueprints(alumnos_bp)
    app.register_blueprints(maestros_bp)