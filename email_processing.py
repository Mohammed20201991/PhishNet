from config import *
from utils import *

# Read the files (filenames) in the chosen path
def get_files(path):
    mail_files = os.listdir(path)
    print(mail_files)
    return mail_files

# Extract the message from the email (read as string)
def extract_msg(path, mail_file):
    mail_file = path + '/' + mail_file
    fp = open(mail_file, "rb")
    mail = fp.read()
    fp.close()

    msg = email.message_from_string(mail)
    return msg

# Extract the body from the message
def extract_body(msg):
    body_content = ""
    if msg.is_multipart():
        for payload in msg.get_payload():
            body_content += str(payload.get_payload())
    else:
        body_content += msg.get_payload()
    return body_content

# Extract the subject from message
def extract_subj(msg):
    decode_subj = email.header.decode_header(msg['Subject'])[0]
    try:
        subj_content = unicode(decode_subj[0])
    except:
        subj_content = "None"
    return subj_content

# Extract sender address from message
def extract_send_address(msg):
    decode_send = email.header.decode_header(msg['From'])[0]
    try:
        send_address = unicode(decode_send[0])
    except:
        send_address = "None"
    return send_address

# Extract reply-to address from message
def extract_replyTo_address(msg):
    decode_replyTo = email.header.decode_header(msg['Reply-To'])[0]
    try:
        replyTo_address = unicode(decode_replyTo[0])
    except:
        replyTo_address = "None"
    return replyTo_address

# Extract the modal url from message
def extract_modal_url(msg):
    urls = extract_urls(msg)
    modal_url = most_common_url(urls)
    return modal_url

# Extract all links
def extract_all_links(msg):
    links = []
    soup  = BeautifulSoup(msg, 'html.parser')
    for link in soup.findAll('a'):
        links.append(link.get('href'))
    
    all_urls    = extract_urls(msg)
    anchor_urls = extract_anchor_urls(msg)
    
    urls  = difference(all_urls, anchor_urls)
    links = links + urls
    return links

# Run the function to extract necessary fields of a mail
def extract_necessary_fields(path, mail):
    necessary_fields = {}
    msg = extract_msg(path, mail)
    
    necessary_fields['body'] = extract_body(msg)
    necessary_fields['subj'] = extract_subj(msg)
    necessary_fields['send'] = extract_send_address(msg)
    necessary_fields['replyTo'] = extract_replyTo_address(msg)
    necessary_fields['modalURL'] = extract_modal_url(msg)
    necessary_fields['links'] = extract_all_links(str(msg))
    
    return necessary_fields