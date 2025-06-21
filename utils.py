from config import *

# Difference two lists
def difference(first, second):
    second = set(second)
    for item in second:
        if item in first:
            first.remove(item)
    return first

# Counts the number of characters in a given string
def count_characters(string):
    return len(string) - string.count(' ') - string.count('\n')

# Extract URLs in the message
def extract_urls(msg):
    mail = str(msg)
    urls = re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", mail)
    return urls

# Extract anchor URLs in the message
def extract_anchor_urls(msg):
    anchor_urls = []
    soup = BeautifulSoup(msg, 'html.parser')
    for link in soup.findAll('a', attrs={'href': re.compile("^http[s]?://")}):
        anchor_urls.append(link.get('href'))
    return anchor_urls

# Extract the domain from the email
def get_email_domain(string):
    domain = re.search("@[\w.]+", string)
    if domain is None:
        return None
    return str(domain.group())[1:]

# Extract domain from URL
def get_url_domain(url):
    domain = None
    if url:
        if u'@' in str(url):
            domain = get_email_domain(str(url))
        else:
            parsed_uri = urlparse(url)
            domain = '{uri.netloc}'.format(uri=parsed_uri)
            if domain.startswith("www."):
                return domain[4:]
    return domain

# Find the most frequent url in a list of URLs
def most_common_url(urls):
    if urls:
        modal_url = max(set(urls), key = urls.count)
        return modal_url
    else:
        return None

# Remove file if it exists
def remove_if_exists(filename):
    try:
        os.remove(filename)
    except OSError:
        pass