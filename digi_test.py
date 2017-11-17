#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
from sys import argv
from nose.tools import *
from lxml import html
from lxml import etree

# Add my module
import sys
sys.path.append("../NewsCrawler")
from digi import GetDigi

import win_unicode_console
win_unicode_console.enable()


# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481245_5DZ1VN0051K48042NT1WL"
# GetDigi(NewsUrl,"AWS推出新雲端運算服務P2.docx")

# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481339_T3R47RS924YNQQL61OZQX"
# GetDigi(NewsUrl,"MCU搭配低功耗無線傳輸模組整合 搶物聯網運算商機.docx")

# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000480670_VVJ5E8X28U30X3L4Z4I8W"
# GetDigi(NewsUrl,"VR、IoT興起 帶動儲存與頻寬發展.docx")

# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000480066_8ZA16Z0O5UFFCC7SXB8Z3"
# GetDigi(NewsUrl,"Western Digital提升WD Gold硬碟容量25%.docx")

# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000480284_E1E3IPYD7GG87D5QGHQA9"
# GetDigi(NewsUrl,"華為拉大與對手差距 然需謹慎因應電信市場轉型.docx")


# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481074_M4U1WBQA62MPXM5Q9QZFX"
# GetDigi(NewsUrl,"KDDI與豐田聯手打造通用車聯網平台.docx")


# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000480615_EI35LJU42KFQXY4BBQ8NZ"
# GetDigi(NewsUrl,"LGD OLED事業連續3年虧損 投資中小尺寸OLED期望轉虧為盈.docx")


# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481075_3851V0NS6NVSJ765JS5EK"
# GetDigi(NewsUrl,"OLED研發缺資金 JDI先推超薄邊液晶面板.docx")

# #找不到網頁
# # NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481642_0TO733TB3NA0KT3GQX8T3.docx"
# # GetDigi(NewsUrl,"OpenText以16億美元收購戴爾EMC內容部門.docx")


# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481480_TPY3FH9U9AJFJSLIFYJJR"
# GetDigi(NewsUrl,"三星呼籲10國消費者暫停使用Note 7 市值2天蒸發190億美元.docx")


# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481634_ZGS5SLV0427T463ROZEZT"
# GetDigi(NewsUrl,"三星電子任命李在鎔為董事 強化決策權.docx")


# # XPATH ISSUE
# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481528_TSO6F08F1BE79R9H3LVYG"
# GetDigi(NewsUrl,"全球半導體進軍大陸 未來5年投資總額達500億美元.docx")


# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481210_O5Q1EYK02AE40MLKGR8FW"
# GetDigi(NewsUrl,"大陸製造業競爭力寶座 5年後恐拱手讓予美國.docx")


# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000480687_9U05VD219P6WY06D8LIVY"
# GetDigi(NewsUrl,"孫正義談收購安謀布局：以ARM平台迎接超級智慧時代.docx")


# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481639_3JS5EPQE47G76H80PHHMB"
# GetDigi(NewsUrl,"惠普斥資10.5億美元 收購三星印表機事業.docx")


# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481573_DRZ4KPHS8DX6VZ2Q4CW87"
# GetDigi(NewsUrl,"歐盟擬放寬電信法規 鼓勵投資光纖網路.docx")


# # duplicate pic
# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000479950_64DLTNJW4ADEN816ENEA6"
# GetDigi(NewsUrl,"趨勢圖示：2030年全球AI相關產業市場規模約8400億美元.docx")


#NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481607_NTW5CMXW1T50ZO6FRC96B"
#GetDigi(NewsUrl,u"軟銀購併安謀進軍物聯網 效應開始發酵.docx")


# Page does not exist
#NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000481570_EZV4MOLV8EDQ1GLWFBPYX.docx"
#GetDigi(NewsUrl,"鴻海掌夏普滿月 轉守為攻仍待觀察.docx")

# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000482545_DPZ68GA130LOGZ66MRXZL&ct=1"
# GetDigi(NewsUrl,u"Author and time check.docx")

# BUG:traceback issue on 20161004 digit cold plage
# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000483012_U0XLFPIK2FH8AN1QZVQ6U&ct=1"
# GetDigi(NewsUrl,u"WeWork.docx")


# BUG: miss some article
# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000482936_CBT8JDSU4857QK5HEV1I8&ct=1"
# GetDigi(NewsUrl,"英特爾伺服器晶片強敵壓境.docx")

# BUG Too: long lines
# NewsUrl = "http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000483393_YXL4GZYG84A95H42KIVVK"
# GetDigi(NewsUrl,"loneline.docx")

# BUG OOR:
# GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000483520_AAC4CE3S3QGKHFL7W2EGW&ct=1","OOR.docx")

# Miss pic
#GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000486173_LHI2D9LB6XZMTT4AWQ7V4","2016年阿里雙11銷售總額.docx")

# Miss pic2
# GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000486270_CPL1JNEZ889NFOLSTT3Y5&ct=1&wpidx=5","緯創、英業達月報發布.docx")

# Line break
# GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000487097_ZQ119EY88GQMCY80IQW3V","電子-阿里巴巴購併Lazada　布局東南亞木馬屠城記.docx")

# IO Err
#GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000492880_AWC9QX3J7Z39BY1GN0JWX&ct=1","工業物聯網貢獻全球經濟潛力大　感測器部署成為發展關鍵.docx")

# IO error
# GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000494796_E50822XI8C3FFF7K7QR53&ct=1","網格運算行動化 智慧手機將改變資料中心產業生態.docx")

# Digi times, make new pic retrieving method
# GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000494948_21ELUGSJ3IIQIE9PVF05X&ct=1","電子-車聯網改寫汽車產業競爭史 連網服務是贏家關鍵.docx")
# GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000494363_JV92C4MU7AAAG02S49QHP","電子-全球超大世代面板爭霸賽　新興勢力全面崛起　10.5/11代廠開啟新里程碑　版圖醞釀再重整.docx")

# Missing article
# GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000493694_ZOJ5F1C2LIXE6P386WKOZ&ct=1","GE的數位煉金術.docx")

# Special character
# GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000495176_T312ZYYT6ISD1S7LE1V5E","電子-喬鼎與中科曙光強強聯手  合資開發儲存解決方案.docx")

# Missing article
# GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000497052_ZD6L6HKL60ZIQY1EO8S2D&ct=1","電子-科技結合生技　著眼大數據衍生長期商機-杜念魯.docx")

# Missing Article
# GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000497011_E1H111HG0PJMC426GXFFB&ct=1","電子-東芝機器人的一小步-陳彥志.docx")

# Missing article
GetDigi("http://www.digitimes.com.tw/tw/dt/n/shwnws.asp?id=0000498497_CEP39E1KLJ3IT6686UDBD&ct=1","加入紫光集團和長江存儲心路歷程　台灣DRAM教父高啟全獨家告白.docx")
