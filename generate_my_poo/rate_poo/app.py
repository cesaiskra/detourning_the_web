import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import rate_poo
import subprocess

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def download(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            ascii = subprocess.check_output(['img2txt.py', filename])
            ascii = ascii.split('<pre>')[-1]
            ascii = ascii.split('</pre>')[0]
            title = ' '.join(filename.split('.')[0:-1])
            rating = rate_poo.rate(filepath)

            print ascii

            return render_template('rated.html', ascii=ascii, title=title, rating=rating)

    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)     # debug restarts server when files changed
