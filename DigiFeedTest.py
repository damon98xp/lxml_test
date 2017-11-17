#!C:\Python27\python.exe
# -*- coding: utf-8 -*-
from sys import argv
from nose.tools import *
from lxml import html
from lxml import etree
import win_unicode_console
import bs4
from bs4 import UnicodeDammit
win_unicode_console.enable()


if __name__ == '__main__':

    url = "https://www.digitimes.com.tw/tech/dt/dtpage_cold.asp"
    parser = etree.HTMLParser()

    try:
        tree   = etree.parse(url, parser)
    except IOError:
            print("Cannot get url:" + url)
            exit(-1)
