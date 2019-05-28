from app import app


@app.route('/')
@app.route('/root')
def index():
    return "Hello, World"
