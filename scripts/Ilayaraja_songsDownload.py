import requests 
from bs4 import BeautifulSoup 
  
''' 
URL of the archive web-page which provides link to 
all video lectures. It would have been tiring to 
download each video manually. 
In this example, we first crawl the webpage to extract 
all the links and then download videos. 
'''
  
# specify the URL of the archive here 
archive_url = "http://www.friendstamilmp3.com/songs2/Singer Hits/ILayaraja Hits/"
  
def get_video_links(): 
      
    # create response object 
    r = requests.get(archive_url) 
      
    # create beautiful-soup object 
    soup = BeautifulSoup(r.content,'html5lib') 
      
    # find all links on web-page 
    links = soup.findAll('a') 
  
    # filter the link sending with .mp4 
    for link in links:
        if link['href'].endswith('mp3'):
            print(link['href'].replace("%20"," "))
            
    video_links = [archive_url + link['href'].replace("%20"," ") for link in links if link['href'].endswith('mp3')] 
  
    return video_links 
  
  
def download_video_series(video_links): 
  
    for link in video_links: 
  
        '''iterate through all links in video_links 
        and download them one by one'''
          
        # obtain filename by splitting url and getting  
        # last string 
        print("url: %s"%link)
        file_name = link.split('/')[-1]    
  
        print("Downloading file:%s"%file_name )
          
        # create response object 
        r = requests.get(link, stream = True) 
          
        # download started 
        with open("/Users/rgovind2/Music/TamilSongs/Ilayaraja/"+file_name, 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    f.write(chunk) 
          
        print( "%s downloaded!\n"%file_name )
  
    print ("All songs downloaded!")
    return
  
  
if __name__ == "__main__": 
  
    # getting all video links 
    video_links = get_video_links() 
    print(len(video_links))
  
    # download all videos 
    download_video_series(video_links) 
