from config import *
from utils import *
from email_processing import *

# Boolean: if HTML is present or not
def body_html(body_content):
    body_html = bool(BeautifulSoup(body_content, "html.parser").find())
    return body_html

# Boolean: if HTML has <form> or not
def body_forms(body_content):
    body_forms = bool(BeautifulSoup(body_content, "html.parser").find("form"))
    return body_forms

# Integer: number of words in the body
def body_noWords(body_content):
    body_noWords = len(body_content.split())
    return body_noWords

# Integer: number of characters in the body
def body_noCharacters(body_content):
    body_noCharacters = count_characters(body_content)
    return body_noCharacters

# Integer: number of distinct words in the body
def body_noDistinctWords(body_content):
    body_noDistinctWords = len(Counter(body_content.split()))
    return body_noDistinctWords

# Float: richness of the text (body)
def body_richness(body_noWords, body_noCharacters):
    try:
        body_richness = float(body_noWords)/body_noCharacters
    except:
        body_richness = 0
    return body_richness

# Integer: number of function words in the body
def body_noFunctionWords(body_content):
    body_noFunctionWords = 0
    wordlist = re.sub("[^A-Za-z]", " ", body_content.strip()).lower().split()
    function_words = ["account", "access", "bank", "credit", "click", "identity", "inconvenience", "information", "limited", 
                      "log", "minutes", "password", "recently", "risk", "social", "security", "service", "suspended"]
    for word in function_words:
        body_noFunctionWords += wordlist.count(word)
    return body_noFunctionWords

# Boolean: if body has the word 'suspension' or not
def body_suspension(body_content):
    body_suspension = "suspension" in body_content.lower()
    return body_suspension

# Boolean: if body has the phrase 'verify your account' or not
def body_verifyYourAccount(body_content):
    phrase  = "verifyyouraccount"
    content = re.sub(r"[^A-Za-z]", "", body_content.strip()).lower()
    body_verifyYourAccount = phrase in content
    return body_verifyYourAccount

def extract_body_attributes(body_content):
    body_attributes = {}
    
    body_attributes['body_html'] = body_html(body_content)
    body_attributes['body_forms'] = body_forms(body_content)
    body_attributes['body_noWords'] = body_noWords(body_content)
    body_attributes['body_noCharacters'] = body_noCharacters(body_content)
    body_attributes['body_noDistinctWords'] = body_noDistinctWords(body_content)
    body_attributes['body_richness'] = body_richness(body_attributes['body_noWords'], body_attributes['body_noCharacters'])
    body_attributes['body_noFunctionWords'] = body_noFunctionWords(body_content)
    body_attributes['body_suspension'] = body_suspension(body_content)
    body_attributes['body_verifyYourAccount'] = body_verifyYourAccount(body_content)
    
    return body_attributes

# Boolean: Check if the email is a reply to any previous mail
def subj_reply(subj_content):
    subj_reply = subj_content.lower().startswith("re:")
    return subj_reply

# Boolean: Check if the email is a forward from another mail
def subj_forward(subj_content):
    subj_forward = subj_content.lower().startswith("fwd:")
    return subj_forward

# Integer: number of words in the subject
def subj_noWords(subj_content):
    subj_noWords = len(subj_content.split())
    return subj_noWords

# Integer: number of characters in the subject
def subj_noCharacters(subj_content):
    subj_noCharacters = count_characters(subj_content)
    return subj_noCharacters

# Float: richness of the text (subject)
def subj_richness(subj_noWords, subj_noCharacters):
    try:
        subj_richness = float(subj_noWords)/subj_noCharacters
    except:
        subj_richness = 0
    return subj_richness

# Boolean: if subject has the word 'verify' or not
def subj_verify(subj_content):
    subj_verify = "verify" in subj_content.lower()
    return subj_verify

# Boolean: if subject has the word 'debit' or not
def subj_debit(subj_content):
    subj_debit = "debit" in subj_content.lower()
    return subj_debit

# Boolean: if subject has the word 'bank' or not
def subj_bank(subj_content):
    subj_bank = "bank" in subj_content.lower()
    return subj_bank

def extract_subj_attributes(subj_content):
    subj_attributes = {}
    
    subj_attributes['subj_reply'] = subj_reply(subj_content)
    subj_attributes['subj_forward'] = subj_forward(subj_content)
    subj_attributes['subj_noWords'] = subj_noWords(subj_content)
    subj_attributes['subj_noCharacters'] = subj_noCharacters(subj_content)
    subj_attributes['subj_richness'] = subj_richness(subj_attributes['subj_noWords'], subj_attributes['subj_noCharacters'])
    subj_attributes['subj_verify'] = subj_verify(subj_content)
    subj_attributes['subj_debit'] = subj_debit(subj_content)
    subj_attributes['subj_bank'] = subj_bank(subj_content)
    
    return subj_attributes

# Integer: number of words in sender address
def send_noWords(send_address):
    send_noWords = len(send_address.split())
    return send_noWords

# Integer: number of characters in sender address
def send_noCharacters(send_address):
    send_noCharacters = count_characters(send_address)
    return send_noCharacters

# Boolean: check if sender and reply-to domains are different
def send_diffSenderReplyTo(send_address, replyTo_address):
    send_domain    = get_email_domain(send_address)
    replyTo_domain = get_email_domain(replyTo_address)
    
    send_diffSenderReplyTo = False
    if replyTo_address != "None":
        send_diffSenderReplyTo = (send_domain != replyTo_domain)
    return send_diffSenderReplyTo

# Boolean: check if sender's and email's modal domain are different
def send_nonModalSenderDomain(send_address, modal_url):
    send_domain  = get_email_domain(send_address)
    modal_domain = get_url_domain(modal_url)
    
    send_nonModalSenderDomain = False
    if str(modal_url) != "None":
        send_nonModalSenderDomain = (send_domain != modal_domain)
    return send_nonModalSenderDomain

def extract_send_attributes(send_address, replyTo_address, modal_url):
    send_attributes = {}
    
    send_attributes['send_noWords'] = send_noWords(send_address)
    send_attributes['send_noCharacters'] = send_noCharacters(send_address)
    send_attributes['send_diffSenderReplyTo'] = send_diffSenderReplyTo(send_address, replyTo_address)
    send_attributes['send_nonModalSenderDomain'] = send_nonModalSenderDomain(send_address, modal_url)
    
    return send_attributes

# Boolean: if use of IP addresses rather than domain name
def url_ipAddress(links_list):
    url_ipAddress = False
    for link in links_list:
        link_address = get_url_domain(link)
        if ":" in str(link_address):
            link_address = link_address[:link_address.index(":")]
        try:
            IP(link_address)
            url_ipAddress = True
            break
        except:
            continue
    return url_ipAddress

# Integer: number of links in an email that contain IP addresses 
def url_noIpAddresses(links_list):
    url_noIpAddresses = 0
    for link in links_list:
        link_address = get_url_domain(link)
        if ":" in str(link_address):
            link_address = link_address[:link_address.index(":")]
        try:
            IP(link_address)
            url_noIpAddresses = url_noIpAddresses + 1
            break
        except:
            continue
    return url_noIpAddresses

# Boolean: if '@' symbol is present in any URL
def url_atSymbol(links_list):
    url_atSymbol = False
    for link in links_list:
        if u'@' in str(link):
            url_atSymbol = True
            break
    return url_atSymbol

# Integer: number of links in the email body
def url_noLinks(links_list):
    url_noLinks = len(links_list)
    return url_noLinks

# Integer: number of external links in email body
def url_noExtLinks(body_content):
    url_noExtLinks = len(extract_urls(body_content))
    return url_noExtLinks

# Integer: number of internal links in email body
def url_noIntLinks(links_list, body_content):
    url_noIntLinks = url_noLinks(links_list) - url_noExtLinks(body_content)
    return url_noIntLinks

# Integer: number of image links in email body
def url_noImgLinks(body_content):
    soup = BeautifulSoup(body_content)
    image_links = soup.findAll('img')
    return len(image_links)

# Integer: number of URL domains in email body
def url_noDomains(body_content, send_address, replyTo_address):
    domains = set()
    all_urls = extract_urls(body_content)
    for url in all_urls:
        domain = get_url_domain(url)
        domains.add(domain)
    
    domains.add(get_email_domain(send_address))
    domains.add(get_email_domain(replyTo_address))
    return len(domains)

# Integer: number of periods in the link with highest number of periods
def url_maxNoPeriods(links_list):
    max_periods = 0
    for link in links_list:
        num_periods = str(link).count('.')
        if max_periods < num_periods:
            max_periods = num_periods
    return max_periods

# Boolean: check if link text contains click, here, login or update terms
def url_linkText(body_content):
    url_linkText = False
    linkText_words = ['click', 'here', 'login', 'update']
    soup = BeautifulSoup(body_content)
    for link in soup.findAll('a'):
        if link.contents:
            contents = list(re.sub(r'([^\s\w]|_)+', '', str(link.contents[0])).lower().split())
            extra_contents = set(contents).difference(set(linkText_words))
            if len(extra_contents) < len(contents):
                url_linkText = True
                break
    return url_linkText

# Binary: if 'here' links don't map to modal domain
def url_nonModalHereLinks(body_content, modal_url):
    modal_domain = get_url_domain(modal_url)
    
    url_nonModalHereLinks = False
    if str(modal_url) != "None":
        soup = BeautifulSoup(body_content)
        for link in soup.findAll('a'):
            if link.contents:
                if "here" in link.contents[0]:
                    link_ref = link.get('href')
                    if get_url_domain(link_ref) != modal_domain:
                        url_nonModalHereLinks = True
                        break
    return url_nonModalHereLinks

# Boolean: if URL accesses ports other than 80
def url_ports(links_list):
    url_ports = False
    for link in links_list:
        link_address = get_url_domain(link)
        if ":" in str(link_address):
            port = link_address[link_address.index(":"):][1:]
            if str(port) != str(80):
                url_ports = True
                break
    return url_ports

# Integer: number of links with port information

# feature_extraction.py (add this function at the end)

def extract_all_features_in_path(path, label):
    features_list = []
    mail_files = get_files(path)
    for mail in mail_files:
        features = overall_feature_extraction(path, label, mail)
        features_list.append(features)
    return features_list


def url_noPorts(links_list):
    url_noPorts = 0
    for link in links_list:
        link_address = get_url_domain(link)
        if ":" in str(link_address):
            url_noPorts += 1
    return url_noPorts

def extract_url_attributes(links_list, body_content, send_address, replyTo_address, modal_url):
    url_attributes = {}

    url_attributes['url_ipAddress'] = url_ipAddress(links_list)
    url_attributes['url_noIpAddresses'] = url_noIpAddresses(links_list)
    url_attributes['url_atSymbol'] = url_atSymbol(links_list)
    url_attributes['url_noLinks'] = url_noLinks(links_list)
    url_attributes['url_noExtLinks'] = url_noExtLinks(body_content)
    url_attributes['url_noIntLinks'] = url_noIntLinks(links_list, body_content)
    url_attributes['url_noImgLinks'] = url_noImgLinks(body_content)
    url_attributes['url_noDomains'] = url_noDomains(body_content, send_address, replyTo_address)
    url_attributes['url_maxNoPeriods'] = url_maxNoPeriods(links_list)
    url_attributes['url_linkText'] = url_linkText(body_content)
    url_attributes['url_nonModalHereLinks'] = url_nonModalHereLinks(body_content, modal_url)
    url_attributes['url_ports'] = url_ports(links_list)
    url_attributes['url_noPorts'] = url_noPorts(links_list)
    
    return url_attributes

def script_scripts(body_content):
    return bool(BeautifulSoup(body_content, "html.parser").find("script"))

def script_javaScript(body_content):
    script_javaScript = False
    if script_scripts(body_content):
        soup = BeautifulSoup(body_content, "html.parser")
        for script in soup.findAll('script'):
            if script.get('type') == "text/javascript":
                script_javaScript = True
    return script_javaScript


def script_statusChange(body_content):
    script_statusChange = False
    if script_scripts(body_content):
        soup = BeautifulSoup(body_content, "html.parser")
        for script in soup.findAll('script'):
            if "window.status" in str(script.contents):
                script_statusChange = True
    return script_statusChange

def script_noOnClickEvents(body_content):
    script_noOnClickEvents = 0
    if script_scripts(body_content):
        soup = BeautifulSoup(body_content, "html.parser")
        codes = soup.findAll('button', {"onclick": True})
        script_noOnClickEvents = len(codes)
    return script_noOnClickEvents


def script_nonModalJsLoads(body_content, modal_url):
    modal_domain = get_url_domain(modal_url)
    script_nonModalJsLoads = False
    if script_scripts(body_content):
        if modal_url:
            soup = BeautifulSoup(body_content, "html.parser")
            for script in soup.findAll('script'):
                source = script.get('src')
                if source is not None:
                    if get_url_domain(source) != modal_domain:
                        script_nonModalJsLoads = True
                        break
    return script_nonModalJsLoads

def extract_script_attributes(body_content, modal_url):
    script_attributes = {}
    
    script_attributes['script_scripts'] = script_scripts(body_content)
    script_attributes['script_javaScript'] = script_javaScript(body_content)
    script_attributes['script_statusChange'] = script_statusChange(body_content)
    script_attributes['script_popups'] = script_popups(body_content)
    script_attributes['script_noOnClickEvents'] = script_noOnClickEvents(body_content)
    script_attributes['script_nonModalJsLoads'] = script_nonModalJsLoads(body_content, modal_url)
    
    return script_attributes

def script_popups(body_content):
    script_popups = False
    if script_scripts(body_content):
        soup = BeautifulSoup(body_content, "html.parser")
        for script in soup.findAll('script'):
            if "window.open" in str(script.contents):
                script_popups = True
    return script_popups
   
def overall_feature_extraction(path, label, mail):
    necessary_fields = extract_necessary_fields(path, mail)

    body_attributes = extract_body_attributes(necessary_fields['body'])
    subj_attributes = extract_subj_attributes(necessary_fields['subj'])
    send_attributes = extract_send_attributes(necessary_fields['send'], 
                                             necessary_fields['replyTo'], necessary_fields['modalURL'])
    url_attributes  = extract_url_attributes(necessary_fields['links'], 
                                            necessary_fields['body'], necessary_fields['send'], 
                                            necessary_fields['replyTo'], necessary_fields['modalURL'])
    script_attributes = extract_script_attributes(necessary_fields['body'], necessary_fields['modalURL'])

    features = body_attributes
    features.update(subj_attributes)
    features.update(send_attributes)
    features.update(url_attributes)
    features.update(script_attributes)
    features['label'] = label
    
        # Select only the 5 features used during training
    # selected_features = {
    #     'body_noFunctionWords': features['body_noFunctionWords'],
    #     'url_noIntLinks': features['url_noIntLinks'],
    #     'body_richness': features['body_richness'],
    #     'url_noLinks': features['url_noLinks'],
    #     'url_linkText': features['url_linkText']
    # }

    # Use all relevant features or a more comprehensive subset
    selected_features = {
        # Body features
        'body_noFunctionWords': features['body_noFunctionWords'],
        'body_richness': features['body_richness'],
        'body_verifyYourAccount': features['body_verifyYourAccount'],
        'body_suspension': features['body_suspension'],
        
        # URL features
        'url_noLinks': features['url_noLinks'],
        'url_linkText': features['url_linkText'],
        'url_ipAddress': features['url_ipAddress'],
        'url_atSymbol': features['url_atSymbol'],
        
        # Sender features
        'send_diffSenderReplyTo': features['send_diffSenderReplyTo'],
        'send_nonModalSenderDomain': features['send_nonModalSenderDomain'],
        
        # Script features
        'script_popups': features['script_popups'],
        'script_statusChange': features['script_statusChange']
    }

    return selected_features #features