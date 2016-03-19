from urllib import urlopen

def read_text() :
    file_part = open("C:\Users\AMAR\Desktop\Python\prank\message.txt")
    content = file_part.read()
    file_part.close()
    check_profinity(content)

def check_profinity(content_part) :
    connection = urlopen("http://www.wdylike.appspot.com/?q="+content_part +"fuck")
    result = connection.read()
    print(result)
    connection.close()
    
read_text()
