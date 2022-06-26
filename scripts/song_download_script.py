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
# !!! Important - end URL with a slash to create separate folders for each singer !!!
# !!! without ending slash all will have only links not the song mp3" !!!
#archive_url = "http://www.friendstamilmp3.com/songs2/Singer Hits/S.Janagi Hits/"
archive_urls = ["http://www.friendstamilmp3.com/songs2/Singer Hits/S.Janagi Hits/","http://www.friendstamilmp3.com/songs2/Singer Hits/K.J Jesudas Hits/",
               "http://www.friendstamilmp3.com/songs2/Singer Hits/S.P.Balasubramaniyam Hits/","http://www.friendstamilmp3.com/songs2/Singer Hits/A.R.Rahman Hits/",
               "http://www.friendstamilmp3.com/songs2/Singer Hits/Swarnalatha Hits/","http://www.friendstamilmp3.com/songs2/Singer Hits/Malaysia Vasudevan (Duet)  Hits/",
               "http://www.friendstamilmp3.com/songs2/Singer Hits/Sujatha Hits/","http://www.friendstamilmp3.com/songs2/Singer Hits/Malaysia Vasudevan (Solo)  Hits/",
               "http://www.friendstamilmp3.com/songs2/Singer Hits/Chithra Hits 1/","http://www.friendstamilmp3.com/songs2/Singer Hits/Chithra Hits 2/",
               "http://www.friendstamilmp3.com/songs2/Singer Hits/Chithra Hits 3/","http://www.friendstamilmp3.com/songs2/Singer Hits/Karthik Hits/",
               "http://www.friendstamilmp3.com/songs2/Singer Hits/ILayaraja Hits/","http://www.friendstamilmp3.com/songs2/Singer Hits/Deva (Singer) Hits/",
               "http://www.friendstamilmp3.com/songs2/Singer Hits/Hariharan Hits/","http://www.friendstamilmp3.com/songs2/Singer Hits/Kamal Hassan (Singer) Hits/Kamal Hassan (Singer) Hits/",
               "http://www.friendstamilmp3.com/songs2/Singer Hits/Unni Krishnan Hits/","http://www.friendstamilmp3.com/songs2/Singer Hits/Kamal Hassan (Singer) Hits/R1/",
               ]
def get_video_links(arch_url): 
      
    # create response object 
    r = requests.get(arch_url) 
      
    # create beautiful-soup object 
    soup = BeautifulSoup(r.content,'html5lib') 
      
    # find all links on web-page 
    links = soup.findAll('a') 
  
    # filter the link sending with .mp4 
    for link in links:
        if link['href'].endswith('mp3'):
            print link['href'].replace("%20"," ")
            
    video_links = [arch_url + link['href'].replace("%20"," ") for link in links if link['href'].endswith('mp3')] 
  
    return video_links 
  
  
def download_video_series(video_links): 
  
    for link in video_links: 
  
        '''iterate through all links in video_links 
        and download them one by one'''
          
        # obtain filename by splitting url and getting  
        # last string 
        print "url: %s"%link
        file_name = link.split('/')[-1]    
  
        print "Downloading file:%s"%file_name 
          
        # create response object 
        r = requests.get(link, stream = True) 
          
        # download started 
        
        #Check if write directory exists
        #print link.split("/")[-2] 
        dirName = "/Users/rgovind2/Music/TamilSong/" + link.split("/")[-2].replace(" ","_")
        #if not os.path.exists(url.split("/")[-2]):
        #    os.makedirs(dirName)
    
        if os.path.exists(dirName):
            print "%s : Dir exists"%dirName
        else:
            print "%s : Dir not exist, creating now"%dirName
            os.makedirs(dirName)

        with open(dirName + "/" + file_name, 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    f.write(chunk) 
          
        print "%s downloaded!\n"%file_name 
  
    print "All songs downloaded!"
    return
  
  
if __name__ == "__main__": 
  
    for archive_url in archive_urls:
        # getting all video links 
        video_links = get_video_links(archive_url) 
        print len(video_links)
  
        # download all videos 
        download_video_series(video_links) 
