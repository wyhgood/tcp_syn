import socket
import threading
import urllib2
import time
import json
import requests



start = time.time()
f = open('work_proxy.txt', 'r')
proxies  = f.readlines()
socket.setdefaulttimeout(10.0)



def fetch_url2(proxy_arg):
    url = "http://ubestbuy.xyz/proxy_ip/check_proxy.php"
    proxies = { "http": "http://"+proxy_arg.strip()}
    requests.get(url, proxies=proxies)

def fetch_url(proxy_arg):

    proxy = urllib2.ProxyHandler({'http': proxy_arg.strip()})
    opener = urllib2.build_opener(proxy)
    #urllib2.install_opener(opener)
    #request = urllib2.Request("http://todayoccurs.com/proxy_ip/check_proxy.php")
    request = urllib2.Request("http://www.baidu.com")
    urlHandler = opener.open(request)
    code = urlHandler.getcode()
    print('checking---')
    ip = urlHandler.read()
    if code == 200:
        f2.write(str(code)+'='+proxy_arg)

    #print(html)
    #print(status)
    #print "'%s\' fetched in %ss" % (url, (time.time() - start))

threads = [threading.Thread(target=fetch_url2, args=(proxy,)) for proxy in proxies]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print "Elapsed Time: %s" % (time.time() - start)
