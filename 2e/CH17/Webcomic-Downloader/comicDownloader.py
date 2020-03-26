import os
import bs4
import requests

inclusiveBool = True
file = './target.txt'
infoArray = []

os.makedirs('Order Of the Stick', exist_ok=True)

def downloadPage(inputSoup):

    imageList = inputSoup.select('img')
    sourceList = []
    source = ''
    comicUrl = ''

    for image in imageList:
        source = image.get('src')
        if source[:36] == 'https://i.giantitp.com//comics/oots/':
            comicUrl = source[36:]

            #Save the image to ./Order Of The Stick.
            print('Downloading ' + comicUrl + '...')
            res = requests.get(source)
            imageFile = open(os.path.join('Order Of the Stick', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

            return 0

#Self iterating function to download all pages after initial Page
def downloadNext(inputSoup):

    downloadPage(inputSoup)

    #Find 'next button'
        #Next comic button has "Next Comic" for a title

    #Find where it's directing to

    #make that the target of nextSoup soup object
    res = requests.get(nextPage)

    #downloadNext(nextSoup)

    return downloadNext(nextSoup)

#VVVV Main codeblock starts HERE VVVV
#Pull a target url if there are any, from inside the file
target = open(file, 'r+')
infoArray = target.readlines()
target.close()

#If the info array pulls no text, then assume default url
if len(infoArray) == 0:
    print('No link found in target.txt. Taking default url.')
    url = 'https://www.giantitp.com/comics/oots0001.html'

else:
    #If there is a VALID link in the file, the code will take that and will not download that same page again.
    if infoArray[0][:36] == 'https://www.giantitp.com/comics/oots':
        print('Link found in target.txt. Using that url to download pages.')
        inclusiveBool = False
        url = infoArray[0]

    #Otherwise, the code will assume the default url.
    else:
        print('Link in target.txt directs to an invalid link.')
        url = 'https://www.giantitp.com/comics/oots0001.html'

print('Link obtained. It points to: ' + url)

#Go to URL
res = requests.get(url)

try:
    res.raise_for_status()
    initialSoup = bs4.BeautifulSoup(res.text, 'html.parser')

    if inclusiveBool:
        downloadPage(initialSoup)

except Exception as exc:
    print('There was problem: %s' % (exc))

#Finish the program
    #Update target.txt
