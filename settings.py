from pathlib import Path
import datetime
import subprocess

#LINEbot
access_token='dryurYK26KjDe0dvJlxunPHdFmBKSrCa2w+2rgcLPiyoHIN/TFjY858dluFIbe9QtmBz1T4kfZG9O71ItYHw6Xl17MZF9bQZ9glODTaC3qeHG8ni/kVxLdSEIBvpfxCJ8nQw50PEXUCfhGmkhOK9VAdB04t89/1O/w1cDnyilFU='
secret_key='6d13fc99913338c8918d04b7ad0f3768'
img_url = 'https://limumakottyann-app.herokuapp.com/'
# coupon_uri = 'http://lin.ee/aaa'
# temp_message = '''このアカウントから個別に返信することはできません。
# 店主に御用の場合は下記LINEアカウント(まこっちゃん弁当店主)にご連絡ください。
# https://line.me/ti/p/makottyann'''

testmode=0

# LINE notify
# notify_token='aaa'

# richmenu
withcancel_richmenu_id = "richmenu-0174d6f41734038c67db91cd3f008d28"
withoutcancel_richmenu_id = "richmenu-6cb346f637aaf3f183f53fec2ab1636f"
none_richmenu_id = "richmenu-b7911b2ab1123a083226c9e9c7e82951"

#DB
if testmode==1:
    db_uri = 'postgres://tjxhlnsfgzdlew:3e999b075bd8e87455682314fc54c405842397690e541cdf32e04250e63c1511@ec2-54-221-217-204.compute-1.amazonaws.com:5432/del12cslkdq0kt'
else:
    proc = subprocess.Popen('printenv DATABASE_URL', stdout=subprocess.PIPE, shell=True)
    db_uri = proc.stdout.read().decode('utf-8').strip()

# makottyann
operationtime = [[datetime.time(12, 0), 'pm'],
                 [datetime.time(20, 00), 'pm']]

# # department
# department = {
#     '工学部': ['機械航空工学科', '電気情報工学科', '物質化学工学科', '地球環境工学科', 'エネルギー科学科', '建築学科'],
#     '理学部': ['物理学科', '化学科', '地球惑星科学科', '数学科', '生物学科'],
#     '農学部': ['生物資源環境学科'],
#     '文学部': ['人文学科'],
#     '教育学部': ['教育学科'],
#     '法学部': ['法学科'],
#     '経済学部': ['経済・経営学科', '経済工学科'],
#     '共創学部': ['共創学科'],
#     '医学部': ['医学科', '生命科学科', '保健学科'],
#     '薬学部': ['創薬科学科', '臨床薬学科'],
#     '歯学部': ['歯学科'],
#     '芸術工学部': ['環境設計学科', '工業設計学科', '画像設計学科', '音響設計学科', '芸術情報設計学科'],
#     'その他': ['その他']
# }
#
# # grade
# grade = {'1年': 1, '2年': 2, '3年': 3, '4年': 4, '修士1年': 5, '修士2年': 6, 'その他': 0}

# flask_setting
JSON_AS_ASCII = False
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = True
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
UPLOADED_CONTENT_DIR = Path("upload")
