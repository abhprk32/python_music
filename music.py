import requests, webbrowser, bs4, re

def play_song(s_name):
    if len(s_name) >= 1:
        page = requests.get("http://www.youtube.com/results?search_query="+s_name)
        if page.status_code != 200:
            print("There was an error playing your music")
        else:
            soup = bs4.BeautifulSoup(page.content,'html.parser')
            links = soup.find_all('a')
            song_id = ''
            for url in links:
                temp = url.get('href')
                if temp.find('watch?v=') != -1:
                    song_id = temp
                    break

            webbrowser.open("http://www.youtube.com/"+song_id)

        
s_name = input("Enter song's name: ")
pattern = re.compile('[a-zA-Z]+')
if pattern.match(s_name) is not None:
    play_song(s_name)
else:
    print("Enter a valid song name")
