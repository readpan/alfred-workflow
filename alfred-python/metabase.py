#!/usr/bin/env python3
import datetime
import os

# 获得昨天时间,以yyyy-mm-dd的格式
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
# now = datetime.datetime.now()

url = 'http://metabase.fanle.vip/dashboard/46?%25E9%25A1%25B9%25E7%259B%25AE=TPNabob&%25E5%25BC%2580%25E5%25A7%258B%25E6%2597%25B6%25E9%2597%25B4=yy-mm-dd&af%25E9%25A1%25B9%25E7%259B%25AE=%E5%87%A1%E4%B9%90-%E6%AD%A6%E6%9D%BE%E6%89%93%E8%99%8E'

# 使用now替换url中的时间
url = url.replace('yy-mm-dd', yesterday.strftime('%Y-%m-%d'))

# os.system(f'open -a "Google Chrome" {url}')

print(url)
