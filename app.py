from flask import Flask, render_template, request, session, flash, redirect, send_file, url_for
from pytube import YouTube
from io import BytesIO
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
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            flash("Wrong URL!", category='danger')
            return render_template('home.html', youtube_logo=yt_logo)
        return render_template('download.html', url=url, youtube_logo = yt_logo)
    return render_template('home.html', youtube_logo=yt_logo)

@app.route('/download', methods=['POST', 'GET'])
def download():

    if request.method == 'POST':
        url = YouTube(session['link'])
        buffer = BytesIO()
        itag = request.form.get('resolution')
        video = url.streams.get_by_itag(itag)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name=f'{url.title}.mp4', mimetype='video/mp4'), flash("Download Successful!", category='success')

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host="192.168.1.11", port=8080, debug=True)