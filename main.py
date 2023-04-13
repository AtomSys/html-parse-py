def parse(html):
    mode = 1
    for letter in html:
        if letter == "<":
            if mode == 1:
                mode = 2
        if letter == ">":
            if mode == "2":
                mode = 3
                    
            
