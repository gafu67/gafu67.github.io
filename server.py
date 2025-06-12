from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = 'https://discord.com/api/webhooks/1375775804897886278/loW7sv_Gm10_11EOtvGq4J_ZsgbEaCJQu6ZvXjW0cTBAWaUF_YbOGTDkCeJhetmCKrwS'  # ← 自分のWebhookに変更

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    payload = {'content': '📸 カメラ画像が届きました'}
    files = {'file': (image.filename, image.stream, image.mimetype)}
    res = requests.post(WEBHOOK_URL, data=payload, files=files)
    return {'status': 'ok', 'discord_status': res.status_code}

if __name__ == '__main__':
    app.run(port=5000)
