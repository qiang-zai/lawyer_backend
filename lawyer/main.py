from lawyer import create_app

app = create_app()


@app.route('/')
def hello_world():
    return 'hello world!'



