from flask import Flask, render_template, request
from downloader import download_video
import os


PHOTO_FOLDER = os.path.join("static", "images")

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = PHOTO_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    yt_logo = os.path.join(PHOTO_FOLDER, "youtube-logo.png")

    if request.method == 'POST':
        url = request.form.get('link')
        download_video(url)
    return render_template('index.html', youtube_logo=yt_logo)

if __name__ == "__main__":
    app.run(debug=True, port=8080)