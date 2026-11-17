import requests
import json
import pandas as pd
import feedparser
from lxml import etree

headers = {
    'User-Agent' : 'private: fukuzaki.mitsuaki@gmail.com'
}

def parse_ixbrl(file_path):
    pass

def main():
    file = 'tmp/ato-20260930.htm'
    df = pd.parse_ixbrl(file)

    print(df.head())

if __name__ == "__main__":
    main()