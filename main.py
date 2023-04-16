from html.parser import HTMLParser

class parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start Tag:", tag)

    def handle_endtag(self, tag):
        print("End Tag:", tag)

    def handle_data(self, data):
        print(data)

parser = parser()

