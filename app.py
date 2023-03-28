from flask import Flask, render_template, request, session
from pytube import YouTube
import os


PHOTO_FOLDER = os.path.join("static", "images")

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = PHOTO_FOLDER
app.config["SECRET_KEY"] = "some_secret_key"

@app.route('/', methods=['GET', 'POST'])
def home():
    yt_logo = os.path.join(PHOTO_FOLDER, "youtube-logo.png")

    if request.method == 'POST':
        session['link'] = request.form.get('url')
        link = request.form.get('url')
        link = link.replace("https://youtu.be", "https://youtube.com/embed")
        url = YouTube(session['link'])
        return render_template('download.html', url=url, link=link)
    return render_template('home.html', youtube_logo=yt_logo)

@app.route('/download', methods=['POST', 'GET'])
def download():
    download_logo = os.path.join(PHOTO_FOLDER, "download-icon.png")
    return render_template('download.html', download_logo=download_logo)

if __name__ == "__main__":
    app.run(host="192.168.1.11", port=8080, debug=True)