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

app = Flask(__name__)

line_bot_api = LineBotApi('osxi9o3k8uGzb6i0qJKtvphiwpgghJu9rVXZoIhTzLnQskoil75p0Qv61qi84UgRN+OaLwYJl6N3ZYhv7Jimndn6n59XxRB1paI92wGcEjXi298uD2x30efq+PZggzpY/trmln94TpI9j5Wxw9/l0wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('83dc7c0d301e53c5d5216759babb431e')

#def message_filter(msg):


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

    if '圖片海' in msg:
        imagemap_message = ImagemapSendMessage(
            base_url='https://example.com/base',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=1040, width=1040),
            video=Video(
                original_content_url='https://example.com/video.mp4',
                preview_image_url='https://example.com/video_preview.jpg',
                area=ImagemapArea(
                    x=0, y=0, width=1040, height=585
                ),
                external_link=ExternalLink(
                    link_uri='https://example.com/see_more.html',
                    label='See More',
                ),
            ),
            actions=[
                URIImagemapAction(
                    link_uri='https://example.com/',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=1040
                    )
                ),
                MessageImagemapAction(
                    text='hello',
                    area=ImagemapArea(
                        x=520, y=0, width=520, height=1040
                    )
                )
            ]
        )

        line_bot_api.reply_message(
        event.reply_token,
        imagemap_message)

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

    if msg == '梗圖':
        image_message = ImageSendMessage(
            original_content_url='https://example.com/original.jpg',
            preview_image_url='https://example.com/preview.jpg'
        )

        line_bot_api.reply_message(event.reply_token, message)

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
    # elif msg == '':
    #     r = ''
    # elif msg == '':
    #     r = ''
    # elif msg == '':
    #     r = ''
    # elif msg == '':
    #     r = ''
    # elif msg == '':
    #     r = ''
    # elif msg == '':
    #     r = ''                        
    # elif msg == '':
    #     r = ''
    # elif '諭哥' in msg:
    #     r = '又有諭哥的局了?'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))



if __name__ == "__main__":
    app.run()