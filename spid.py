import urllib.request, urllib.parse, socket,  re
from bs4 import BeautifulSoup

socket.setdefaulttimeout(10)
url1 = ''
nextt = []
points = []
points2 = []
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
            findre = re.findall(b'redirect\("(.+?)"\);',data)
            #print(findre)
            if findre != []:
                for findrei in findre:
                    findrei = bytes.decode(findrei)
                    print(findrei)
                    if 'http://' in findrei:
                        print(findrei)
                        spide(findrei)
            #print(cont.getcode())
            soup = BeautifulSoup(data, 'html.parser')
            #print(soup.original_encoding)
            for link in soup.findAll('a'):
                link = link.get('href')
                urlp = urllib.parse.urlparse(link)
                if urlp.scheme == 'http' or urlp.scheme == '':
                    if urlp.netloc != '':
                        if urlp.netloc == url1:
                            if '?' in link:
                                if link[0:3] != 'http':
                                    if ('http://'+link) not in points:
                                        points.append('http://'+link)
                            elif urlp.path != '': 
                                if link not in nextt:
                                    nextt.append(link)
                            else:
                                pass
                        else:
                            pass
                    elif '?' in link:
                        if link[0] != '/':
                            if ('http://'+url1+'/'+link) not in points:
                                points.append('http://'+url1+'/'+link)
                        else:
                            if (url1+link) not in points:
                                points.append('http://'+url1+link)
                    elif urlp.path != '': 
                        if urlp.path[0] != '/':
                            if (url1+'/'+link) not in nextt:
                                nextt.append(url1+'/'+link)
                        else:
                            if(url1+link) not in nextt:
                                nextt.append(url1+link)
                    else:
                        pass
                else:
                    pass
        else:
            pass
    except Exception as e:
        print(url)
        print(e)
        
def spide(u):
    global url1
    url1 = urllib.parse.urlparse(u).netloc
    spid(u)
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
            nex3 = len(nextt)
            nextt3 = nextt
            print(i)
            for i in range(0, nex3, 1):
                spid(nextt3[i])
                print(i)
    return points

