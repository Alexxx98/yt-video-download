from flask import Flask, render_template, request, session, redirect, url_for, flash
from pytube import YouTube
from downloader import download_video
import os, json


PHOTO_FOLDER = os.path.join("static", "images")

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = PHOTO_FOLDER
app.config["SECRET_KEY"] = "some_secret_key"

@app.route('/', methods=['GET', 'POST'])
def home():
    yt_logo = os.path.join(PHOTO_FOLDER, "youtube-logo.png")

    if request.method == 'POST':
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            flash("Wrong URL!", category="danger")
            return render_template('home.html', youtube_logo=yt_logo)
        download_video(url)
        flash("Download Successful!")
    return render_template('home.html', youtube_logo=yt_logo)

@app.route('/download', methods=['POST', 'GET'])
def download():
    pass

if __name__ == "__main__":
    app.run(host="192.168.1.11", port=8080, debug=True)