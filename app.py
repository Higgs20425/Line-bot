from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImagemapSendMessage, LocationSendMessage, BaseSize, Video, ImagemapArea, ExternalLink, URIImagemapAction, MessageImagemapAction, TemplateSendMessage, CarouselTemplate, CarouselColumn, PostbackAction, MessageAction, URIAction, ImageSendMessage
)

import random


app = Flask(__name__)

line_bot_api = LineBotApi('osxi9o3k8uGzb6i0qJKtvphiwpgghJu9rVXZoIhTzLnQskoil75p0Qv61qi84UgRN+OaLwYJl6N3ZYhv7Jimndn6n59XxRB1paI92wGcEjXi298uD2x30efq+PZggzpY/trmln94TpI9j5Wxw9/l0wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('83dc7c0d301e53c5d5216759babb431e')



def pick_memes(num):
    collection = ['https://i.imgur.com/CFnfZmD.jpg', 'https://i.imgur.com/tN7r7Xb.jpg', 'https://i.imgur.com/pPka4NU.jpg', 'https://i.imgur.com/MnQ6r96.jpg', 'https://i.imgur.com/PXUBM8r.jpg', 'https://i.imgur.com/c0shKWO.jpg',
    'https://i.imgur.com/n6ysQ1q.jpg', 'https://i.imgur.com/pPOULBM.jpg' ,'https://i.imgur.com/wodXcnU.jpg' ,'https://i.imgur.com/iUMJXub.jpg' ,'https://i.imgur.com/0eTMksx.jpg', 'https://i.imgur.com/unBS2BD.jpg',
    'https://i.imgur.com/67KujPY.jpg', 'https://i.imgur.com/wlgb4E6.jpg', 'https://i.imgur.com/CR1F95O.jpg', 'https://i.imgur.com/HDi18W8.jpg', 'https://i.imgur.com/gbvg8uW.jpg', 'https://i.imgur.com/HndKvCG.jpg',
    'https://i.imgur.com/MPnqMVI.jpg', 'https://i.imgur.com/irg2G6L.jpg', 'https://i.imgur.com/x8hHbD2.jpg', 'https://i.imgur.com/I5AW3g2.jpg', 'https://i.imgur.com/0UVfIYL.jpg', 'https://i.imgur.com/VzlUWMC.jpg',
    'https://i.imgur.com/cBj0Bfx.jpg', 'https://i.imgur.com/VaIoKYM.jpg', 'https://i.imgur.com/lbbIFKS.jpg', 'https://i.imgur.com/5Djp6H3.jpg', 'https://i.imgur.com/4kuf6pe.jpg', 'https://i.imgur.com/n9SS2nj.jpg',
    'https://i.imgur.com/YCk5Qus.jpg', 'https://i.imgur.com/sHjTwkz.jpg', 'https://i.imgur.com/X1QXx6I.jpg', 'https://i.imgur.com/1dwRxPX.jpg', 'https://i.imgur.com/2UcI2sG.jpg', 'https://i.imgur.com/kt84g6H.jpg',
    'https://i.imgur.com/rJ2eO3W.jpg', 'https://i.imgur.com/k4IotO1.jpg', 'https://i.imgur.com/42flWYE.jpg', 'https://i.imgur.com/pDDNhjK.jpg', 'https://i.imgur.com/bqDopSu.jpg', 'https://i.imgur.com/DjfVaXW.jpg']
    return collection[num]


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
    r = '阿鬼你還是說中文吧!'
    num_random_meme = random.randint(0,41)

    if msg == '梗圖':
        r = '請輸入 "梗圖啦" 或 "梗圖 數字"'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=r))

    elif msg == '梗圖啦':
        meme = pick_memes(num_random_meme)
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/tN7r7Xb.jpg',
            preview_image_url=meme
        )

        line_bot_api.reply_message(event.reply_token, image_message)

    elif '梗圖' in msg:
        try:
            num_meme = int(msg.split()[1])
            if isinstance(num_meme, int) == True and num_meme > 0:
                num_meme -= 1
                meme = pick_memes(num_meme)
                image_message = ImageSendMessage(
                    original_content_url='https://i.imgur.com/tN7r7Xb.jpg',
                    preview_image_url=meme
                )

                line_bot_api.reply_message(event.reply_token, image_message)
        
        except ValueError:
            pass

    if '酒吧 大安' in msg:
        carousel_template_message = TemplateSendMessage(
            alt_text='喝酒囉',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipOS1tOjI9741_1PjzmeuAsgE_LNggaGoTit0k81=w203-h270-k-no',
                        title='昨天 Bistro & Flavor',
                        text='每次都去這間?',
                        actions=[
                            # PostbackAction(
                            #     label='postback1',
                            #     display_text='postback text1',
                            #     data='action=buy&itemid=1'
                            # ),
                            # MessageAction(
                            #     label='message1',
                            #     text='message text1'
                            # ),
                            URIAction(
                                label='Google Maps',
                                uri='https://reurl.cc/1gW80X'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.ggpht.com/p/AF1QipN3S5wnwsD71dVC_psP2GAlhJW42pFPlRvoUjQ5=s1536',
                        title='Intention',
                        text='尻Shot這邊請?',
                        actions=[
                            # PostbackAction(
                            #     label='postback2',
                            #     display_text='postback text2',
                            #     data='action=buy&itemid=2'
                            # ),
                            # MessageAction(
                            #     label='message2',
                            #     text='message text2'
                            # ),
                            URIAction(
                                label='Google Maps',
                                uri='https://reurl.cc/v5xEke'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.ggpht.com/p/AF1QipNB1wIbgmTFzmQNujlcoJWW0Ys7OONlr-MV5ZbI=s1536',
                        title='Book ing bar',
                        text='Is it good to drink？ 謀哩崊跨賣馬',
                        actions=[
                            # PostbackAction(
                            #     label='postback2',
                            #     display_text='postback text2',
                            #     data='action=buy&itemid=2'
                            # ),
                            # MessageAction(
                            #     label='message2',
                            #     text='message text2'
                            # ),
                            URIAction(
                                label='Google Maps',
                                uri='https://reurl.cc/raV05k'
                            )
                        ]
                    )
                ]
            )
        )

        line_bot_api.reply_message(
        event.reply_token,
        carousel_template_message)

    elif '酒吧 信義' in msg:
        carousel_template_message = TemplateSendMessage(
            alt_text='喝酒囉',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://lh3.ggpht.com/p/AF1QipNoR50HukTk4v9v3vLlN8bdoDmzF8EZzC17qjJM=s1536',
                        title='Odin信義放感情',
                        text='餐酒館推薦 平價調酒酒吧 bar bistro 人氣特色餐酒美食推薦 網美酒吧',
                        actions=[
                            # PostbackAction(
                            #     label='postback1',
                            #     display_text='postback text1',
                            #     data='action=buy&itemid=1'
                            # ),
                            # MessageAction(
                            #     label='message1',
                            #     text='message text1'
                            # ),
                            URIAction(
                                label='Google Maps',
                                uri='https://reurl.cc/Agl9AY'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipOY9Oan3beqkLkr2HVEGVqLqtM5ZwUYiphgAuEQ=s387-k-no',
                        title='榕 RON Xinyi',
                        text='吃寶飽煲去的那間的信義分店',
                        actions=[
                            # PostbackAction(
                            #     label='postback2',
                            #     display_text='postback text2',
                            #     data='action=buy&itemid=2'
                            # ),
                            # MessageAction(
                            #     label='message2',
                            #     text='message text2'
                            # ),
                            URIAction(
                                label='Google Maps',
                                uri='https://reurl.cc/Xeb2E0'
                            )
                        ]
                    )
                ]
            )
        )

        line_bot_api.reply_message(
        event.reply_token,
        carousel_template_message)

    if msg == '諭哥':
        r = '諭哥沒在上班啦!'
    elif msg == '小業':
        r = 'RAV4準備開出來了!'
    elif msg == '胞弟':
        r = '有房有老婆有小孩,人生勝利組'
    elif '胞弟' in msg:
        r = '又再說胞弟壞話?'
    elif msg == '意義':
        r = '有意義沒逸逸'
    elif msg == '逸逸':
        r = '在釣魚啦'
    elif msg == '呆寶':
        r = '遊戲刪了'
    elif msg == '偉航':
        r = '辣個賺十萬的男人'
    elif msg == '林老闆':
        r = '林老闆帶大家飛'
    elif msg == '開命':
        r = '有400萬的藍人'
    elif msg == '小馬雲':
        r = '阿里 阿里巴巴'
    elif msg == '蒼哥':
        r = '蒼哥在默默操盤'
    elif msg == '...':
        r = '...'
    elif msg == '靠北':
        r = '恩?'
    elif msg == '不是阿' or '不是啊' or '不是':
        r = '嘿?'
    elif '癢' in msg:
        r = '要驗喔'
    elif '高雄' in msg:
        r = '真的來了!'                        
    elif '快' in msg:
        r = '有小業快?'
    # elif '' in msg:
    #     r = ''
    # elif '' in msg:
    #     r = ''
    # elif '' in msg:
    #     r = ''
    # elif '' in msg:
    #     r = ''
    # elif '' in msg:
    #     r = ''
    # elif '' in msg:
    #     r = ''
    # elif '諭哥' in msg:
    #     r = '又有諭哥的局了?'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))



if __name__ == "__main__":
    app.run()