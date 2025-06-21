# config.py
import colorama
from colorama import Fore, Style, Back
colorama.init()

import re, os, sys
from bs4 import BeautifulSoup
import pprint
from urlparse import urlparse
import email
from IPy import IP
import email.header
import csv
from collections import Counter
from HTMLParser import HTMLParser
import pandas as pd
from sklearn.externals import joblib

# Set the encoding to UTF-8 and print output on Jupyter Notebook
stdout = sys.stdout
reload(sys)
sys.setdefaultencoding('UTF8')
sys.stdout = stdout