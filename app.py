from flask import Flask, render_template
import os


PHOTO_FOLDER = os.path.join("static", "images")

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = PHOTO_FOLDER

@app.route('/')
def index():
    yt_logo = os.path.join(PHOTO_FOLDER, "youtube-logo.png")
    return render_template('index.html', youtube_logo=yt_logo)

if __name__ == "__main__":
    app.run(debug=True)