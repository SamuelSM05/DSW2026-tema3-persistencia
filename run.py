from flask_debugtoolbar import DebugToolbarExtension
# Archivo: run.py (en la raíz de mi_proyecto/)
from app import create_app

app = create_app()

toolbar = DebugToolbarExtension(app)

if __name__ == "__main__":
    app.run(debug=True)