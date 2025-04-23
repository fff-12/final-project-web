import flask 

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('web.html')

if __name__ == 'class_guide':
    app.run(debug=True)