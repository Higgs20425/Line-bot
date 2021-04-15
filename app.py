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

def pick_up_memes(num):
    memes_library = ['https://i.imgur.com/CFnfZmD.jpg', 'https://i.imgur.com/tN7r7Xb.jpg', 'https://i.imgur.com/pPka4NU.jpg', 'https://i.imgur.com/MnQ6r96.jpg', 'https://i.imgur.com/PXUBM8r.jpg', 'https://i.imgur.com/c0shKWO.jpg',
    'https://i.imgur.com/n6ysQ1q.jpg', 'https://i.imgur.com/pPOULBM.jpg' ,'https://i.imgur.com/wodXcnU.jpg' ,'https://i.imgur.com/iUMJXub.jpg' ,'https://i.imgur.com/0eTMksx.jpg', 'https://i.imgur.com/unBS2BD.jpg',
    'https://i.imgur.com/67KujPY.jpg', 'https://i.imgur.com/wlgb4E6.jpg', 'https://i.imgur.com/CR1F95O.jpg', 'https://i.imgur.com/HDi18W8.jpg', 'https://i.imgur.com/gbvg8uW.jpg', 'https://i.imgur.com/HndKvCG.jpg',
    'https://i.imgur.com/MPnqMVI.jpg', 'https://i.imgur.com/irg2G6L.jpg', 'https://i.imgur.com/x8hHbD2.jpg', 'https://i.imgur.com/I5AW3g2.jpg', 'https://i.imgur.com/0UVfIYL.jpg', 'https://i.imgur.com/VzlUWMC.jpg',
    'https://i.imgur.com/cBj0Bfx.jpg', 'https://i.imgur.com/VaIoKYM.jpg', 'https://i.imgur.com/lbbIFKS.jpg', 'https://i.imgur.com/5Djp6H3.jpg', 'https://i.imgur.com/4kuf6pe.jpg', 'https://i.imgur.com/n9SS2nj.jpg',
    'https://i.imgur.com/YCk5Qus.jpg', 'https://i.imgur.com/sHjTwkz.jpg', 'https://i.imgur.com/X1QXx6I.jpg', 'https://i.imgur.com/1dwRxPX.jpg', 'https://i.imgur.com/2UcI2sG.jpg', 'https://i.imgur.com/kt84g6H.jpg',
    'https://i.imgur.com/rJ2eO3W.jpg', 'https://i.imgur.com/k4IotO1.jpg', 'https://i.imgur.com/42flWYE.jpg', 'https://i.imgur.com/pDDNhjK.jpg', 'https://i.imgur.com/bqDopSu.jpg', 'https://i.imgur.com/DjfVaXW.jpg']
    
    meme_url = memes_library[num]
    return meme_url


def retort(msg):
    bullshit_library = {'愈哥': '諭哥沒在上班啦!', '玉哥': '諭哥沒在上班啦!', '諭哥': '諭哥沒在上班啦!', '小業': 'RAV4準備開出來了!', '胞弟': '有房有老婆有小孩,人生勝利組', '意義': '有意義沒逸逸', 
    '逸逸': '在釣魚啦!', '呆寶': '電腦砸了 遊戲刪了', '偉航': '辣個賺十萬的男人', '胖安': '這很林老闆', '開命': '有400萬的藍人', '阿里': '阿里巴巴', '小馬雲': '阿里 阿里巴巴', '蒼哥': '蒼哥在默默操盤啦', 
    '倉哥': '蒼哥在默默操盤啦', '吉哥': '吉丸吉丸', '雞哥': '吉丸吉丸', '機哥': '吉丸吉丸', '基哥': '吉丸吉丸', '靠北': '嗯?', '告北': '嗯?', '不是阿': '嘿?', '不是啊': '嘿?', '會癢': '要驗喔', '會癢?': '要驗喔', 
    '真的來了': '當天再約?', '很快': '有小業快?', '很快餒': '有小業快?', '快喔': '諭哥準備交割?', '諭哥哩': '在台東啦'}

    responese = bullshit_library[msg]
    return responese


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
    random_meme = random.randint(0,41)

    if msg == '梗圖':
        r = '請輸入 "梗圖啦" 或 "梗圖 數字"'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=r))
        return

    elif msg == '梗圖啦':
        meme_url = pick_up_memes(random_meme)
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/tN7r7Xb.jpg',
            preview_image_url=meme_url
        )

        line_bot_api.reply_message(event.reply_token, image_message)
        return

    elif '梗圖' in msg:
        try:
            meme = int(msg.split()[1])
            if isinstance(meme, int) == True and meme > 0:
                meme -= 1
                meme_url = pick_up_memes(meme)
                image_message = ImageSendMessage(
                    original_content_url='https://i.imgur.com/tN7r7Xb.jpg',
                    preview_image_url=meme_url
                )

                line_bot_api.reply_message(event.reply_token, image_message)
        
        except ValueError:
            return

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
        return

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
        return

    try:
        if msg:
            r = retort(msg)
    except KeyError as e:
        r = ' '
    # elif '' in msg:
    #     r = ''

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))



if __name__ == "__main__":
    app.run()