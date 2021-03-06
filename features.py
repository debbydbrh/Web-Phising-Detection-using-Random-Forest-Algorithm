#12S17031	Debby Debora Hutajulu
#12S17058	Juanda Antonius Pakpahan
#12S17062	Venny Handayani Sormin


from bs4 import BeautifulSoup 
import urllib, bs4, re 
import googlesearch
import whois
from datetime import datetime, timezone
import time 
import socket

#fungsi mengecek apakah nama domain menggunakan ip addresses
def have_ip_address(url):
    match=re.search('(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  
                    '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' 
                    '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}',url)    
    if match:
        return -1
    else:
        return 1
        
1, -1
#fungsi mengehitung panjang url dengan ketentukan.
def url_length(url):
    if len(url)<54:
        return 1
    elif len(url)>=54|len(url)<=75:
        return 0
    else:
        return -1
    




#fungsi pemendekan url 
def url_shortener(url):
    match=re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                    'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                    'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                    'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                    'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                    'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                    'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|tr\.im|link\.zip\.net',url)
    if match:
        return -1
    else:
        return 1


#fungsi mengecek karakter @
def have_atrate_symbol(url):
    match = re.search('@',url)

    if match:
        return -1
    else:
        return 1


#fungsi mencari penggunaan \\ yang berlibihan (http:\\juanda.com\\http:\\marsiurupan.com)
def double_slash_redirect(url):
    list = [x.start(0) for x in re.finditer('\\.',url)]
    if list[len(list)-1]>6:
        return -1
    else:
        return 1

#mencari karakter (-) pada URL
def prefix_suffix(url):
    match = re.search('-',url)
    if match:
        return -1
    else:
        return 1


#mengecek subdomain
def have_subdomain(url):
    if(have_ip_address(url)==-1):
        match = re.search('(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5]))|(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}',url)
        pos = match.end(0)
        url = url[pos:]
    list = [x.start(0) for x in re.finditer('\.',url)]
    if len(list)<=3:
        return 1
    elif len(list) == 4:
        return 0
    else:
        return -1
    

#mengecek batas waktu URL atau domain
def domain_registration_length(domain):
    expiry_date = domain.expiration_date
    exp = datetime.strftime(expiry_date,"%Y-%m-%d")
    expires = datetime.strptime(exp,"%Y-%m-%d")
    today = datetime.today()
    tp = datetime.strftime(today,"%Y-%m-%d")
    today_date = datetime.strptime(tp,"%Y-%m-%d")
    registration_length = abs((expires - today_date).days)

    if registration_length / 365 <= 1:
    	return -1
    else:
    	return 1


#mengecek favicon pada URL
def favicon(wiki,soup,domain):
    for head in soup.find_all('link'):
        for head.link in soup.find_all('link',href=True):
            dots = [x.start(0) for x in re.finditer('\.', head.link['href'])]
            if wiki in head.link['href'] or len(dots) == 1 or domain in head.link['href']:
                return 1
            else:
                return -1
    return 1


#mengecek port dan url
status_port = []
import socket
def isOpen(url,port_numbers):
    for port in port_numbers:
        ip = socket.gethostbyname(url)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            s.shutdown(2)
            status_port.append(0)
        except:
            status_port.append(1)
    if(status_port[3] == 0 & status_port[4] == 0 & status_port[0] == 1 & status_port[1] == 1 & status_port[2] == 1):
    	return -1
    else:
        return 1

#mengecek token pada domain
def https_token(url):
    match = [(x.start(0), x.end(0)) for x in re.finditer('https:// | http:// | http | https', url)]

    if len(match)!= 1:
        return -1
    else:
        return 1



#request url
def request_url(wiki, soup, domain):
    i = 0
    success = 0
    for img in soup.find_all('img',src=True):
        dots = [x.start(0) for x in re.finditer('\.',img['src'])]
        if wiki in img['src'] or domain in img['src'] or len(dots)==1:
         success = success + 1
        i=i+1

    for audio in soup.find_all('audio', src= True):
      dots = [x.start(0) for x in re.finditer('\.', audio['src'])]
      if wiki in audio['src'] or domain in audio['src'] or len(dots)==1:
         success = success + 1
      i=i+1

    for embed in soup.find_all('embed', src= True):
      dots=[x.start(0) for x in re.finditer('\.',embed['src'])]
      if wiki in embed['src'] or domain in embed['src'] or len(dots)==1:
         success = success + 1
      i=i+1

    for iframe in soup.find_all('iframe', src= True):
      dots=[x.start(0) for x in re.finditer('\.',iframe['src'])]
      if wiki in iframe['src'] or domain in iframe['src'] or len(dots)==1:
         success = success + 1
      i=i+1

    try:
       percentage = success/float(i) * 100
    except:
        return 1

    if percentage < 22.0 :
       return 1
    elif((percentage >= 22.0) and (percentage < 61.0)) :
       return 0
    else :
       return -1



def url_of_anchor(wiki, soup, domain):
    i = 0
    unsafe=0
    for a in soup.find_all('a', href=True):
        if "#" in a['href'] or "javascript" in a['href'].lower() or "mailto" in a['href'].lower() or not (wiki in a['href'] or domain in a['href']):
            unsafe = unsafe + 1
        i = i + 1
    try:
        percentage = unsafe / float(i) * 100
    except:
        return 1
    if percentage < 31.0:
        return 1
    elif ((percentage >= 31.0) and (percentage < 67.0)):
        return 0
    else:
        return -1



def links_in_tags(wiki, soup, domain):
   i=0
   success =0
   for link in soup.find_all('link', href= True):
      dots=[x.start(0) for x in re.finditer('\.',link['href'])]
      if wiki in link['href'] or domain in link['href'] or len(dots)==1:
         success = success + 1
      i=i+1

   for script in soup.find_all('script', src= True):
      dots=[x.start(0) for x in re.finditer('\.',script['src'])]
      if wiki in script['src'] or domain in script['src'] or len(dots)==1 :
         success = success + 1
      i=i+1
   try:
       percentage = success / float(i) * 100
   except:
       return 1

   if percentage < 17.0 :
      return 1
   elif((percentage >= 17.0) and (percentage < 81.0)) :
      return 0
   else :
      return -1


def sfh(wiki, soup, domain):
   for form in soup.find_all('form', action= True):
      if form['action'] =="" or form['action'] == "about:blank" :
         return -1
      elif wiki not in form['action'] and domain not in form['action']:
          return 0
      else:
            return 1
   return 1




def submitting_to_email(soup):
   for form in soup.find_all('form', action= True):
      if "mailto:" in form['action'] :
         return -1
      else:
          return 1
   return 1



#abnormal url
def abnormal_url(domain,url):
    hostname=domain.name
    match=re.search(hostname,url)
    if match:
        return 1
    else:
        return -1




def iframe(soup):
    for iframe in soup.find_all('iframe', width=True, height=True, frameBorder=True):
        if iframe['width']=="0" and iframe['height']=="0" and iframe['frameBorder']=="0":
            return -1
        else:
            return 1
    return 1



#mengecek lama penggunaan domain
def age_of_domain(domain):
    creation_date = domain.creation_date
    expiration_date = domain.expiration_date
    create = datetime.strftime(creation_date,"%Y-%m-%d")
    create_date = datetime.strptime(create,"%Y-%m-%d")
    exp = datetime.strftime(expiration_date,"%Y-%m-%d")
    exp_date = datetime.strptime(exp,"%Y-%m-%d")
    domain_age = abs((exp_date - create_date).days)

    if domain_age / 30 < 6:
    	return -1
    else:
    	return 1


def web_traffic(url):
    try:
        rank = bs4.BeautifulSoup(urllib.request("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find("REACH")['RANK']
    except TypeError:
        return -1
    rank= int(rank)
    if (rank<100000):
        return 1
    else:
        return 0


def google_index(url):
    site=googlesearch.search(url, 5)
    if site:
        return 1
    else:
        return -1



def statistical_report(url,hostname):
    url_match=re.search('esy\.es | hol\.es | 	000webhostapp\.com | 16mb\.com | bit\.ly | for-our\.info | beget\.tech | blogspot\.com | weebly\.com |raymannag\.ch',url)
    try:
        ip_address=socket.gethostbyname(hostname)
    except:
        print ('Connection problem. Please check your internet connection!')
    ip_match=re.search('146\.112\.61\.108 | 31\.170\.160\.61 | 67\.199\.248\.11 | 67\.199\.248\.10 | 69\.50\.209\.78 | 192\.254\.172\.78 | 	216\.58\.193\.65 | 23\.234\.229\.68 | 173\.212\.223\.160 | 60\.249\.179\.122',ip_address)
    if url_match:
        return -1
    elif ip_match:
        return -1
    else:
        return 1



def main(url):
    with open('file.txt', 'r', encoding='utf-8') as file:
        soup_string=file.read()

    soup = BeautifulSoup(soup_string, 'html.parser')

    status=[]

    hostname = url
    h = [(x.start(0), x.end(0)) for x in re.finditer('https://|http://|www.|https://www.|http://www.', hostname)]
    z = int(len(h))
    if z != 0:
        y = h[0][1]
        hostname = hostname[y:]
        h = [(x.start(0), x.end(0)) for x in re.finditer('/', hostname)]
        z = int(len(h))
        if z != 0:
            hostname = hostname[:h[0][0]]

    status.append(have_ip_address(url))
    status.append(url_length(url))
    status.append(url_shortener(url))
    status.append(have_atrate_symbol(url))
    status.append(double_slash_redirect(url))
    status.append(prefix_suffix(hostname))
    status.append(have_subdomain(url))

    dns=1
    try:
        domain = whois.query(hostname)
    except:
        dns=-1

    if dns==-1:
        status.append(-1)
    else:
        status.append(domain_registration_length(domain))

    status.append(favicon(url,soup, hostname))

    port_numbers = [21,22,23, 80,443]
    status.append(isOpen(hostname,port_numbers))
    status.append(https_token(url))
    status.append(request_url(url, soup, hostname))
    status.append(url_of_anchor(url, soup, hostname))
    status.append(links_in_tags(url,soup, hostname))
    status.append(sfh(url,soup, hostname))
    status.append(submitting_to_email(soup))

    if dns == -1:
        status.append(-1)
    else:
        status.append(abnormal_url(domain,url))

    status.append(iframe(soup))

    if dns == -1:
        status.append(-1)
    else:
        status.append(age_of_domain(domain))

    status.append(dns)

    status.append(web_traffic(soup))
    status.append(google_index(url))
    status.append(statistical_report(url,hostname))
    status1 = [status]
    print ('\n1. Having IP address\n2. URL Length\n3. URL Shortening service\n4. Having @ symbol\n5. Having double slash\n' \
          '6. Having dash symbol(Prefix Suffix)\n7. Having multiple subdomains\n8. Domain Registration Length\n9. Favicon\n' \
          '10. Ports \n11. HTTP or HTTPS token in domain name\n12. Request URL\n13. URL of Anchor\n14. Links in tags\n' \
          '15. SFH\n16. Submitting to email\n17. Abnormal URL\n18. IFrame\n19. Age of Domain\n20. DNS Record\n21. Web Traffic\n' \
          '22. Google Index\n23. Statistical Reports\n')
    print (status)
    return status1

if __name__ == "__main__":
    main()
