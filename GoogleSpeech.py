#The following code is based on the "AI Application Development Course" and has been partially modified after further personal research.

#1.please install pkg as below command:
#pip install gTTS, pip:python install package
from gtts import gTTS #從gtts載入單一物件gTTS(google text to speech)

from datetime import datetime
import time

# 獲取當前時間, 要組成語音內容用的(我想讓牠抓取今天日期時間)
now = datetime.now().strftime("%Y年%m月%d日%H時%M分%S秒")

#設定語音檔案名稱
mp3fn = "pcvoice.mp3"

#設定要說話的內容
tts = gTTS(f"歡迎光臨,今天日期為{now},天氣晴,請享受美好時光", lang='zh', slow=False) #,tld="com") #會到 Google 線上並產生語音檔
#tts = gTTS("歡迎光臨，今天天氣真好", lang='zh') #,tld="com") #會到 Google 線上並產生語音檔
# en 英語, fr 法語, ko 韓文, ja 日本
tts.save(mp3fn) #儲存成檔案並放置目前資料夾

#2.please install pkg as below command:
#play voice directly
#pip install pygame
import pygame 
pygame.init() #初始化
pygame.mixer.init() #混音器初始化
pygame.mixer.music.load(mp3fn) #載入音效檔
pygame.mixer.music.play() #-1:重複播放

#直接指定暫停時間,但如果語音長短是變化的就不適合
#time.sleep(16) #暫停6s

# 確認音樂仍在播放
while pygame.mixer.music.get_busy():
    time.sleep(1) #暫停6s

print("播放完成")
