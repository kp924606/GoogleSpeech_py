![](https://img.shields.io/badge/Creater-TCT-FFFF00) |![](https://img.shields.io/badge/development-python-006400) | ![](https://img.shields.io/badge/Version-3.9.21-blue)

# GoogleSpeech
## 1. gTTS (Google Text-to-Speech) 功能及細節：
gTTS 是一個 Python 套件，它利用 Google 的 Text-to-Speech API（即將文本轉換為語音）來生成語音。
gTTS 讓開發者可以輕鬆地將文本內容轉換為 MP3 格式的語音檔，並支持多種語言和發音選擇。
它非常適合用於需要語音回饋的應用程式，如語音助手或語音提示系統。
```diff
! 使用時請確保需要連線網際網路 in orange
```

### 主要功能：
  
●語言支持：支持多種語言和方言（如英文、法文、中文等），並能夠指定語音的發音。

●語音速度控制：可以設定語音的播放速度（slow 參數，預設為 False）。

●語音保存：能夠將生成的語音保存為 MP3 文件，便於後續播放。

●簡單易用：只需要提供要轉換的文本內容，並選擇語言和其他配置選項，就可以快速生成語音。

```diff
! 但無法設置撥放速度
```
------
## 2. pygame 功能及細節：
pygame 是一個用於開發 2D 遊戲、音效播放和多媒體應用的 Python 套件。
它基於 SDL（Simple DirectMedia Layer）來處理圖像、音效和其他多媒體功能。
它是 Python 社群中最受歡迎的遊戲開發框架之一，因為它簡單易用且功能強大，支持跨平台運行（Windows、macOS 和 Linux）。
```diff
! 在此僅用來撥放指定的文字內容聲音
```

### 主要功能：
●圖形渲染：支持簡單的 2D 圖像處理，能夠載入、顯示圖片，繪製形狀（如矩形、圓形等）。

●音效處理：支持載入和播放音效文件（如 MP3、WAV 格式），並支持音量控制和音效播放。

●事件處理：提供事件處理系統來處理用戶輸入（如鍵盤、滑鼠事件等）。

●時間控制：支持帧速率控制，便於遊戲循環及動畫效果的實現。

●跨平台支持：支持在 Windows、Linux、macOS 上運行。

●簡單的遊戲循環結構：pygame 提供了一個簡單的遊戲循環框架，可以輕鬆地建立遊戲或多媒體應用。

------
## 3. Install Command：
Please refer the command as below.

```bash
pip install pygame
pip install gTTS
```

------

## About Me
Thanks & Best Regards !

蔡承廷

​Senior Engineer of Semiconductor Product/Testing & ​Automation

Email: ​​kp924606@gmail.com

LinkedIn:https://www.linkedin.comin/tsai-cheng-ting/

