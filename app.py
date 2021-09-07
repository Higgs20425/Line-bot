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
import webbrowser
from imgur_python import Imgur

app = Flask(__name__)

line_bot_api = LineBotApi('kgbpKtdwPWMexRaCUBqIPFveRllZwfk7mROn1M1Z9mGDO37bbh/xtFq+UTCWMoeSN+OaLwYJl6N3ZYhv7Jimndn6n59XxRB1paI92wGcEjUfjPs2ZEy4z0VkPOYfr5aEWiecRrKfWv0kb7Jv9C6jbAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ddbe30c10b53bebb600cbff244416c51')


def pick_up_memes():
    info = {
    "client_id": "69ad53f1c002de2",
    "client_secret": "fa9684e5f5a260618f2864ef28595573d86656e9",
    "access_token": "07f8edbe1a4e1980443bae9364c761f4129d7d10",
    "expires_in": "315360000",
    "token_type": "bearer",
    "refresh_token": "fb2ea2c2ad2fda105571a4f4451c89c8cd7d660f",
    "account_username": "jack204251",
    "account_id": 112527951
    }

    meme_ids = []
    for page in range(100):
        imgur_client = Imgur(info)
        clt = imgur_client.image_ids(page)
        clt = clt['response']['data']
        if len(clt) == 0:
            break
        for id_ in clt:
            meme_ids.append(id_)

    ran_ids = random.randint(0, len(meme_ids))
    meme_id = meme_ids[ran_ids]
    return meme_id


def responese(msg):
        
    included_keys = {'胞弟': ['雙飛雙飛!', '要驗喔', '有房有老婆 有小孩?', '又在說胞弟壞話?', '壓進去喔', '我就是要雷你'], '老闆': ['石頭開大囉', '把你抱起來X', '就是這麼簡單'], 
    '撈半': ['石頭開大囉', '把你抱起來X', 'Hulk Smash!!!', '就是這麼簡單'], '撈伴': ['石頭開大囉', '把你抱起來X', 'Hulk Smash!!!', '就是這麼簡單'], '指紋': ['石頭開大囉', '把你抱起來X', 'Hulk Smash!!!', '就是這麼簡單'], 
    '有啥好吃': ['源坐?', '葛利麵吃爆?', '背包客?', '鴨肉李伺候?', '米干?', '下次吃茶六?', '碳佐再來?', '伊莉會館海鮮?'], '真的來了': ['當天再約?', '真的來了餒'], 
    '意義': ['有意義沒逸逸'], '沒聲音': ['人走茶涼啦'], '會癢': ['要驗喔'], '不好說': ['不想說都不要說'], '笑死': ['死了沒?', '不要真的笑死餒'], 
    '羊肉炒飯': ['真香', '身體很誠實'], '沒啥好吃': ['源坐?', '葛利麵吃爆?', '背包客?', '鴨肉李伺候?', '米干?', '下次吃茶六?', '碳佐再來?', '伊莉會館海鮮?'], '韓導': ['喔氣氣氣氣氣', '征服宇宙', '當個塞子', '可憐啊', '高雄發大財', '莫忘世上苦人多', '鳳凰都飛走了 進來一大堆雞'], 
    '韓國': ['喔氣氣氣氣氣', '征服宇宙', '當個塞子', '可憐啊', '高雄發大財', '莫忘世上苦人多', '鳳凰都飛走了 進來一大堆雞'], '韓總': ['喔氣氣氣氣氣', '征服宇宙', '當個塞子', '可憐啊', '高雄發大財', '莫忘世上苦人多', '鳳凰都飛走了 進來一大堆雞'], 
    '等等': ['麻吉得', '等殺小', '進棺材等?', '等投胎?'], '股票':[ '林北台積電沒在賣', '這裡不談史塔克', 'all money back me home'], '買哪': [ '跌了你也不敢買', '麗臺 @江忠諭', '長榮 @江忠諭'], '狗狗': ['to the moon', '@林老闆'], '推薦': ['@越南小哥?', '給你推薦好的'],
    'will': ['大家好 我是will', '歡迎來到X調查', '故事的主人公名叫: '], '大戶': ['誰找林老闆', '@胖安', '@林老闆'], '最敢': ['還是要帶套啦', '有我們ㄅ緯敢?', '有我們逸逸衝?'], '結婚': ['弄出人命?', '帶卡崔來吃?'], '要加': ['手打+500', '沒台錢了?'], '刷': ['刷卡加一成', '先刷賺回饋'], 
    '硬': ['@ㄅ緯', '也不用動刀動槍啦', '廁所處理?', '-3000'], '虧': ['少去一次', '嗯?', 'all money back me home'], '窮': ['去跟你老闆談', '蔡英文不用負責?', 'all money back me home'], '蛇': ['消防隊姓楊的不抓蛇啦', '蔡英文~~', '馬英九哦'], '豆花': ['我的豆花30塊'],
    'ㄅ偉': ['辣個男人', '手機要接喔', 'coffee snake'], 'ㄅ緯': ['辣個男人', '手機要接喔', 'coffee snake'], 'ㄅ委': ['辣個男人', '手機要接喔', 'coffee snake'], 'ㄅ尾': ['辣個男人', '手機要接喔', 'coffee snake'], 
    '加非': ['one coffee snake', '下午來一杯?', '再補一點'], '加飛': ['one coffee snake', '下午來一杯?', '再補一點'], '咖啡': ['one coffee snake', '下午來一杯?', '再補一點'], '家非': ['one coffee snake', '下午來一杯?', '再補一點'], 
    '家飛': ['one coffee snake', '下午來一杯?', '再補一點'], '投資': ['all money back me home', '這裡不談史塔克', '林北台積電沒在賣'],'檳榔': ['他說9粒50欸'],
    '羽球': ['羽球沒人在打一個小時的', 'ㄅ緯幫買個水'], '借錢': ['又要嘴我們胞弟', '63萬?'], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], 
    # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], 
    # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], 
    # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], 
    # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], 
    # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], 
    # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], 
    # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], 
    # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''],     
    '諭哥': ['諭哥沒在上班啦!', '還在台東啦...', '省500', '什麼時候北上', '小孩長的像你', '在台東啦'], '小業': ['RAV4準備開出來了!', '準備做壞事? @13姨', '拒絕熊貓', '很奧豆?'], '逸逸': ['在釣魚啦!', '@小哈'], ###開始
    '呆寶': ['電腦砸了 遊戲刪了', '轉速拉起來'], '偉航': ['辣個賺十萬的男人', '再牽一台啦', '三鐵報好玩的啦', '五天五次'], '胖安': ['這很林老闆', '退休了啦', '幫買幾隻狗狗?', '他不會來啦'], 
    '開命': ['有400萬的藍人', '有在兼', '在接客', '蝦皮主管啦', '要多少'], '阿里': ['阿里巴巴', '阿里巴巴給我快一點起來'], '小馬雲': ['阿里 阿里巴巴', '歐歐歐', '那個長的很好看 我們去看看吧'], '蒼哥': ['蒼哥在默默操盤啦'], '買哪檔': [ '跌了你也不敢買', '麗臺 @江忠諭', '長榮 @江忠諭'], 
    '買哪支': [ '跌了你也不敢買', '麗臺 @江忠諭', '長榮 @江忠諭'], '吉哥': ['吉丸吉丸', '大夜在補眠', '真香?'], '雞哥': ['吉丸吉丸', '大夜在補眠', '真香?'], '機哥': ['吉丸吉丸', '大夜在補眠', '真香?'], '基哥': ['吉丸吉丸', '大夜在補眠', '真香?'],
    '媽媽桑': ['要來我家看貓嗎?', '哪個渣男?'],'靠北': ['嗯?', '嘿?', '出事了阿北?'], '告北': ['嗯?', '嘿?', '出事了阿北?'], '不是阿': ['嗯?', '嘿?'], '快': ['有小業快?', 'sensitive'], '快喔': ['諭哥準備交割'], 
    '諭哥哩': ['在台東啦'], '乾': ['嘿?'], '不對喔': ['出事了阿北'], '幹': ['又有了?'], '...': ['...', '我不行了?'], '問題': ['你問題最多', '嗯?'], ###結束
    }

    try:
        for key in included_keys.keys():
            if key in msg:
                re = random.randint(0,len(included_keys[key])) - 1
                rsp = included_keys[key][re]
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

    if '梗圖' in msg:
        meme_id = pick_up_memes()
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/tN7r7Xb.jpg',
            preview_image_url='https://i.imgur.com/' + meme_id + '.jpg'
        )

        line_bot_api.reply_message(event.reply_token, image_message)
        return

    elif '在一句' in msg or '再一句' in msg:
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/tN7r7Xb.jpg',
            preview_image_url='https://i.imgur.com/SNw6cKV.jpg'
        )

        line_bot_api.reply_message(event.reply_token, image_message)
        return    

    # if '在一句' in msg:
    #     sticker_message = StickerSendMessage(
    #         package_id='789',
    #         sticker_id='10885'
    #     )

    #     line_bot_api.reply_message(
    #     event.reply_token,
    #     sticker_message)
    #     return

    # elif '再一句' in msg:
    #     r = '在啦'
    #     sticker_message = StickerSendMessage(
    #         package_id='446',
    #         sticker_id='2009'
    #     )

    #     line_bot_api.reply_message(
    #     event.reply_token,
    #     sticker_message)
    #     return

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

    line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=r))

if __name__ == "__main__":
    app.run()