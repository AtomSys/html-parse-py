from html.parser import HTMLParser

def st(tag,attrs):
    print("Start Tag:", tag, ". Attributes - ", attrs)
class parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        st(tag,attrs)

    def handle_endtag(self, tag):
        print("End Tag:", tag)

    def handle_data(self, data):
        print(data)

parser = parser()
