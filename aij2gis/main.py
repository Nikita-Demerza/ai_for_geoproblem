from flask import Flask, request, render_template, url_for
from PIL import Image
from model import Model

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_is_secret_key'
model = Model()


@app.route('/', methods=['POST', 'GET'])
def index():
    result = "..."
    name = ""
    if request.method == "POST":
        img = request.files['select_img']
        name = img.filename
        if img is not None:
            img.save(f'static/image.png')
        # result = model.get_result(Image.open('static/image.png'))

    return render_template("index.html",
                           name=name, result=result,
                           image=url_for('static', filename='image.png'))


def main():
    app.run()


if __name__ == '__main__':
    main()
