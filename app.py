from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('osxi9o3k8uGzb6i0qJKtvphiwpgghJu9rVXZoIhTzLnQskoil75p0Qv61qi84UgRN+OaLwYJl6N3ZYhv7Jimndn6n59XxRB1paI92wGcEjXi298uD2x30efq+PZggzpY/trmln94TpI9j5Wxw9/l0wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('83dc7c0d301e53c5d5216759babb431e')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '阿鬼你還是說中文吧！'
    if msg == 'hi':
        r = 'hi~hi~'
    elif msg == '諭哥':
        r = '諭哥沒再上班啦'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()