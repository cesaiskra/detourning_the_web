from flask import Flask, request, render_template
import videomash


app = Flask(__name__)


# decorator function
@app.route('/')
def home():
    name = request.args.get('name', 'no one')
    age = request.args.get('age', 'x')
    return render_template('home.html', name=name, age=age)
    # return "hehlllo " + name


@app.route('/create')
def create():
    phrase1 = request.args.get('phrase1', '')
    phrase2 = request.args.get('phrase2', '')

    outfile = 'static/' + phrase1 + phrase2 + '.mp4'
    outfile = outfile.replace(' ', '_')
    videomash.mash(phrase1, phrase2, outfile)

    return render_template('video.html', vid=outfile, phrase1=phrase1, phrase2=phrase2)

if __name__ == '__main__':
    app.run(debug=True)     # debug restarts server when files changed
