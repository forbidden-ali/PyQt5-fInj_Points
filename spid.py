import urllib.request, urllib.parse, socket
from bs4 import BeautifulSoup

socket.setdefaulttimeout(10)
url1 = ''
nextt = []
points = []
def spid(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} 
    try:
        res = urllib.request.Request(url,headers=header)
        cont = urllib.request.urlopen(res)
        code = cont.getcode()
        nextt = []
        #print(code)
        if code == 200:
            data = cont.read()
            #print(cont.getcode())
            soup = BeautifulSoup(data, 'html.parser')
            #print(soup.original_encoding)
            for link in soup.findAll('a'):
                link = link.get('href')
                urlp = urllib.parse.urlparse(link)
                if urlp.netloc != '':
                    if urlp.netloc == urllib.parse.urlparse(url1).netloc:
                        if '.' in urlp.path:
                            pass
                        elif '?' in link:
                            if link not in points:
                                points.append(link)
                        elif urlp.path != '': 
                            if link not in nextt:
                                nextt.append(link)
                        else:
                            pass
                    else:
                        pass
                elif '.' in urlp.path: 
                        pass
                elif '?' in link:
                    if (url1+link) not in points:
                        if urlp.scheme == '' or urlp.scheme == 'http':
                            points.append(url1+link)
                elif urlp.path != '': 
                    if (url1+link) not in nextt:
                        if urlp.scheme == '' or urlp.scheme == 'http':
                            nextt.append(url1+link)
                else:
                    pass
        else:
            pass
    except Exception as e:
        print(url)
        print(e)
        
def spide(u):
    global url1
    url1 = u
    spid(url1)
    nex1 = len(nextt)
    nextt1 = nextt
    print(nex1)
    print('123')
    for i in range(0,nex1,1):
        spid(nextt1[i])
        nex2 = len(nextt)
        nextt2 = nextt 
        print(nex2)
        print('312')
        for i in range(0,nex2,1):
            spid(nextt2[i])    
            print(i)
            
    return points

