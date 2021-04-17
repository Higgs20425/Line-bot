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


def responese(msg):
    exact_keys = {'諭哥': ['諭哥沒在上班啦!', '還在台東啦...', '省500', '什麼時候北上', '小孩長的像你'], '小業': ['RAV4準備開出來了!', '準備做壞事? @13姨', '拒絕熊貓', '很奧豆?'], '逸逸': ['在釣魚啦!', '@小哈'], 
    '呆寶': '電腦砸了 遊戲刪了', '偉航': ['辣個賺十萬的男人', '再牽一台啦', '三鐵報好玩的啦'], '胖安': ['這很林老闆', '退休了啦', '幫買幾隻狗狗?', '他不會來啦'], 
    '開命': ['有400萬的藍人', '在接客', '很會含', '蝦皮主管啦'], '阿里': '阿里巴巴', '小馬雲': '阿里 阿里巴巴', '蒼哥': '蒼哥在默默操盤啦', '倉哥': '蒼哥在默默操盤啦', 
    '吉哥': ['吉丸吉丸', '大夜在補眠', '真香?'], '雞哥': ['吉丸吉丸', '大夜在補眠', '真香?'], '機哥': ['吉丸吉丸', '大夜在補眠', '真香?'], '基哥': ['吉丸吉丸', '大夜在補眠', '真香?'],
    '媽媽桑': ['要來我家看貓嗎?', '哪個渣男?'],'靠北': ['嗯?', '嘿?'], '告北': ['嗯?', '嘿?'], '不是阿': ['嗯?', '嘿?'], '很快': '有小業快?', '很快餒': '有小業快?', '快喔': '諭哥準備交割?', 
    '諭哥哩': '在台東啦', '乾': '嘿?', '不對喔': '出事了阿北', '幹': '又有了?', '....': '....', '問題': '你問題最多'}
    # '': '', 
    
    included_keys = {'胞弟': ['雙飛雙飛!', '要驗喔', '有房有老婆 有小孩?', '又在說胞弟壞話?', '壓進去喔', '我就是要雷你'], '老闆': ['石頭開大囉', '把你抱起來X', '就是這麼簡單'], 
    '撈半': ['石頭開大囉', '把你抱起來X', 'Hulk Smash!!!', '就是這麼簡單'], '撈伴': ['石頭開大囉', '把你抱起來X', 'Hulk Smash!!!', '就是這麼簡單'], '指紋': ['石頭開大囉', '把你抱起來X', 'Hulk Smash!!!', '就是這麼簡單'], 
    '有啥好吃': ['源坐?', '葛利麵吃爆?', '背包客?', '鴨肉李伺候?', '米干?', '下次吃茶六?', '碳佐再來?', '伊莉會館海鮮?'], '真的來了': ['當天再約?', '真的來了餒'], 
    '意義': '有意義沒逸逸', '沒聲音': '人走茶涼啦', '會癢': '要驗喔', '會癢?': '要驗餒', '不好說': '不想說都不要說', '不好說啦': '不想說都不要說', '笑死': ['死了沒?', '不要真的笑死餒'], 
    '羊肉炒飯': ['真香', '身體很誠實'], '沒啥好吃': ['源坐?', '葛利麵吃爆?', '背包客?', '鴨肉李伺候?', '米干?', '下次吃茶六?', '碳佐再來?', '伊莉會館海鮮?'], 

    }

    try:
        if msg in exact_keys:
            len_values = len(exact_keys[msg])
            type_values = type(exact_keys[msg])
            if type_values == list: 
                len_values -= 1
                reply = random.randint(0,len_values)
                rsp = exact_keys[msg][reply]
                return rsp
            elif type_values == str:
                rsp = exact_keys[msg]
                return rsp
        else:
            for key in included_keys.keys():
                len_values = len(included_keys[key])
                type_values = type(included_keys[key])
                if msg in key and type_values == list:
                    len_values -= 1
                    reply = random.randint(0,len_values)
                    rsp = included_keys[key][reply]
                    return rsp
                elif msg in key and type_values == str:
                    rsp = included_keys[key]
                    return rsp
    except KeyError as e:
        rsp = ''                                  
        return rsp
    
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
    r = responese(msg)
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

    if msg == '酒吧 大安' in msg:
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

    elif msg == '酒吧 信義':
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

    elif msg == '景點 嘉義':
        carousel_template_message = TemplateSendMessage(
            alt_text='@小哈',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://pic.pimg.tw/as660707/1507707816-3005797788_l.jpg',
                        title='愛木村休閒觀光工廠',
                        text='館內還有許多特色場景，讓旅人取景紀念親子來訪，也能體驗手作DIY唷',
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
                                label='發車囉',
                                uri='https://reurl.cc/dVb56z'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://pic.pimg.tw/emily561025/1540898548-3106265433.jpg',
                        title='大埔情人公園',
                        text='位在嘉義的情人公園 佔地寬敞，景色幽美，旁邊就是曾文水庫 廣場以紅色花園為主題',
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
                                label='立馬導航',
                                uri='https://reurl.cc/KxzxKn'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://decing.tw/wp-content/uploads/20200914152739_61.jpg',
                        title='嘉義市立美術館',
                        text='嘉義市立美術館成為歷史與當代場域的交匯點， 也是「嘉義文化新絲路」上的一道古典且新穎的風景。',
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
                                label='飆風馬',
                                uri='https://reurl.cc/l0b0oY'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://img.fullfenblog.tw/20200310131442_80.jpg',
                        title='龍王金殿',
                        text='龍王金殿位在群山峻嶺的森林之中 金碧輝煌的唐宋建築，好似京都金閣寺 四周環山，還有一整片壯麗的茶田風光',
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
                                label='忍不住前往',
                                uri='https://reurl.cc/GdqdXA'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://www.welcometw.com/wp-content/uploads/2020/09/S__26083409-850x638.jpg',
                        title='太平雲梯 遊客服務中心(附設餐廳、茶體驗、茶料理)',
                        text='太平雲梯長度281公尺、海拔約1000公尺，為全台最長、海拔最高之景觀吊橋。',
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
                                label='行程跑起來',
                                uri='https://reurl.cc/pmbmrd'
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

    if '在一句' in msg:
        sticker_message = StickerSendMessage(
            package_id='789',
            sticker_id='10885'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    elif '再一句' in msg:
        r = '在啦'
        sticker_message = StickerSendMessage(
            package_id='446',
            sticker_id='2009'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    elif '爬山' in msg:
        sticker_message = StickerSendMessage(
            package_id='789',
            sticker_id='10871'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    elif '凍未條' in msg or '憋不住啦' in msg or '憋不住' in msg:
        sticker_message = StickerSendMessage(
            package_id='446',
            sticker_id='2026'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    # elif '' in msg:
    #     r = ''

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))

if __name__ == "__main__":
    app.run()