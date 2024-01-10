#weblist lists all websites that has ever been recorded
#websave lists all the websites that will be reported

def appendation(url):
    '''''''''''''''''''''''
    Simply appends text documents. Since the format is preferred to be sent
    in a website1,website2 format, the format is preset this way. If the
    file has nothing in it, seperation witha  comma cannot be used, so
    validation is put in place.
    '''''''''''''''''''''''
    global weblist,websave,weblist_content,websave_content

    close_file()

    weblist=open("Weblist.txt","a")
    if len(weblist_content)!=0:
        weblist.write(","+url)
    else:
        weblist.write(url)
    websave=open("Websave.txt","a")
    if len(websave_content)!=0:
        websave.write(","+url)
    else:
        websave.write(url)

    close_file()

def read_content():
    '''''''''''''''''''''''
    Reads what the file contains.
    Since the websave file is going to be deleted often, a verification is
    done to see if the file still exists. If not, a new file is created and
    the function calls itself again.
    '''''''''''''''''''''''
    global weblist,websave,weblist_content,websave_content

    weblist=open("Weblist.txt","r")
    weblist_content=weblist.read()
    try:
        websave=open("Websave.txt","r")
        websave_content=websave.read()
    except FileNotFoundError:
        websave=open("Websave.txt","w")
        websave.close()
        read_content()

def close_file():
    '''''''''''''''''''''''
    Closes BOTH files if opened.
    '''''''''''''''''''''''
    global weblist,websave

    websave.close()
    weblist.close()

def websave_create():
    '''''''''''''''''''''''
    If it is a new set of urls, the file is emptied so that the later set of
    URLs can be svaed onto the file, like RAM, whilst the weblist does not get
    recreated, like ROM.
    '''''''''''''''''''''''
    websave=open("Websave.txt","w")
    websave.write("")
    websave.close()

try:
    day=input("Press okay if you are creating a new set, press cancel if you are using the same set.")
    websave_create()
except KeyboardInterrupt:
    pass

try:
    read_content()
except FileNotFoundError:
    weblist=open("Weblist.txt","w")
    websave=open("Websave.txt","w")
    close_file()
    read_content()

url_input=input("Enter URL: ")

while url_input!="STOP":
    appendation(url_input)
    close_file()
    read_content()
    url_input=input("Enter URL: ")
print(websave_content)
close_file()
