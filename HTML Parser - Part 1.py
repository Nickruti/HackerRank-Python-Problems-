#https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for i in attrs:
            print(f"-> {i[0]} > {i[1]}")

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
