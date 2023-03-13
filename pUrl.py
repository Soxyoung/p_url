# coding:utf-8

import re
import requests
from bs4 import BeautifulSoup

# 原创自拍区 https://t0302.91p01.app/forumdisplay.php?fid=4&page=1
# 原创申请 https://t0302.91p01.app/forumdisplay.php?fid=19
# 我爱我妻 https://t0302.91p01.app/forumdisplay.php?fid=21

host = 't0302.91p01.app'

def copyThread(host, tid):
    urls = ""
    try:
        thread_url = 'http://' + host + '/viewthread.php?tid=' + tid

        headers = {
            'authority': 't1222.91p01.app',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            # 'cookie': '__utmz=96799898.1672549653.2.2.utmcsr=91porn.com|utmccn=(referral)|utmcmd=referral|utmcct=/; utf8tt=bfaewIPBbIYpzU5TV%2FuF%2FcR7XwUHYxLpwoEm7pjX; __utma=96799898.2013700185.1671865330.1672549653.1676131755.3; __utmc=96799898; CzG_sid=XRB894; CzG_fid4=1676133049; CzG_fid21=1676133685; CzG_visitedfid=19D21D4; __utmt=1; CzG_oldtopics=D505989D514557D564862D564886D564882D564945D564944D564961D564800D564814D564812D564810D564830D564821D564837D564856D564861D564871D564879D564877D564881D564884D564895D564885D564897D564902D564973D; __utmb=96799898.38.10.1676131755',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        }

        #response = requests.get(thread_url, cookies=cookies, headers=headers)
        response = requests.get(thread_url, headers=headers)
        response.encoding = response.apparent_encoding
        html = response.text

        soup = BeautifulSoup(html, "html.parser")
        threadtitle = soup.find('h1').text
        file_name = tid + '_' + threadtitle

        try:
            print(file_name)
        except:
            print(tid)

        soup = BeautifulSoup(html, "html.parser")
        threadtitle = soup.find('h1').text
        # print(tid, threadtitle)
        postlist = soup.find_all("div", {"class" : "t_msgfontfix"})

        for post in postlist:
            # print(post.text)
            imgs = post.find_all("img")
            for img in imgs:
                try:
                    url = img["file"]
                    # print(url)
                    urls += url + "\n"
                except:
                    pass

        pages = soup.find("div",{"class":"forumcontrol s_clear"}).findChildren("a")
        for p in range(len(pages) - 2):
            next = 'http://' + host + "/" + pages[p]["href"]
            if (not 'tid' in next):
                continue
            try:

                #response = requests.get(thread_url, cookies=cookies, headers=headers)
                response = requests.get(next, headers=headers)
                response.encoding = response.apparent_encoding
                html = response.text

                soup = BeautifulSoup(html, "html.parser")
                #threadtitle = soup.find('h1').text
                file_name = tid

                soup = BeautifulSoup(html, "html.parser")
                # threadtitle = soup.find('h1').text
                # print(tid, threadtitle)
                postlist = soup.find_all("div", {"class" : "t_msgfontfix"})

                for post in postlist:
                    # print(post.text)
                    imgs = post.find_all("img")
                    for img in imgs:
                        try:
                            url = img["file"]
                            # print(url)
                            urls += url + "\n"
                        except:
                            pass

            except:
                pass

        if (not urls.strip().isspace()):
            print(urls)
        print(tid, threadtitle, "____DONE!")
    except:
        print(tid, threadtitle, "____ERROR!")
        pass

def findTids(thread_url):

    headers = {
        'authority': 't1222.91p01.app',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': '__utmz=96799898.1672549653.2.2.utmcsr=91porn.com|utmccn=(referral)|utmcmd=referral|utmcct=/; utf8tt=bfaewIPBbIYpzU5TV%2FuF%2FcR7XwUHYxLpwoEm7pjX; __utma=96799898.2013700185.1671865330.1672549653.1676131755.3; __utmc=96799898; CzG_sid=XRB894; CzG_fid4=1676133049; CzG_fid21=1676133685; CzG_visitedfid=19D21D4; __utmt=1; CzG_oldtopics=D505989D514557D564862D564886D564882D564945D564944D564961D564800D564814D564812D564810D564830D564821D564837D564856D564861D564871D564879D564877D564881D564884D564895D564885D564897D564902D564973D; __utmb=96799898.38.10.1676131755',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    #response = requests.get(thread_url, cookies=cookies, headers=headers)
    response = requests.get(thread_url, headers=headers)
    response.encoding = response.apparent_encoding
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    threads = soup.find_all(id=re.compile("normalthread_*"))
    tids = []
    for thread in threads:
        tid = thread['id']
        tids.append(tid[tid.find('_') + 1:])
        # print(tid[tid.find('_') + 1:])
    return tids

for page in range(1, 2):
    tids = findTids('http://' + host + '/forumdisplay.php?fid=19&page=' + str(page))
    for tid in tids:
        try:
            copyThread(host, tid)
        except:
            pass

    tids = findTids('http://' + host + '/forumdisplay.php?fid=21&page=' + str(page))
    for tid in tids:
        try:
            copyThread(host, tid)
        except:
            pass

    tids = findTids('http://' + host + '/forumdisplay.php?fid=19&page=' + str(page))
    for tid in tids:
        try:
            copyThread(host, tid)
        except:
            pass
