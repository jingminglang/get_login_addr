import urllib
import re
import subprocess


# string -> string
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# string -> string
def get_ip_local(ip):
    html = getHtml("http://www.ip138.com/ips138.asp?ip="+ip+"&action=2")
    u = html.decode('gbk')
    r = u.encode('utf8')
    m=re.search(r'<li>([^li<>]*)</li>',r)
    return m.group(1)

# string -> string | None
def get_ip(str):
    m=re.search(r'([0-9]{1,3}(\.[0-9]{1,3}){3})',str)
    if(m):
      return m.group(1)
    else:
      return None


# -> [string] | []
def get_last_login_ip():
    p = subprocess.Popen('last', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ips = []
    for line in p.stdout.readlines():
        ip = get_ip(line)
        if(ip):
           ips.append(ip)
    return ips


for ip in get_last_login_ip():
    print ip , get_ip_local(ip)
