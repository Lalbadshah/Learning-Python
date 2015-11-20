import urllib

def opener():
    f = open("C:\Users\Prateek Bhatnagar\Documents\GitHub\python\movie_quotes.txt")
    f_read=f.read()
    f.close()
    checkprofan(f_read)
def checkprofan(check_me):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+check_me)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("No Profanity")
opener()
