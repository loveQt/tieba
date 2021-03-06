# -*-coding:utf8-*-
# import re
import requests
import time
# from bs4 import BeautifulSoup
# import datetime


def get_html(url, headers=None, data=None):
    return requests.post(url, headers=headers, data=data).content


def datetime_to_timestamp_in_milliseconds(d):
    def current_milli_time(): return int(round(time.time() * 1000))
    return current_milli_time()


def timestamp_to_datetime(d):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(d))