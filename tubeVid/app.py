# -*- coding: utf-8 -*-

# Indent width : 8 spaces

import pafy
import os

#Python Software Foundation
# Short demo on new PSF sponsorship app
URL = "https://www.youtube.com/watch?v=0nD4UcGu_iQ"


PATH = os.getcwd()
'''
import platform

if platform == "Windows":
        
        """
        A little of hack.
        Get current User for saving directly to 'download' folder.
        """

        user  =  os.getlogin()

        PATH = os.path.join(r"C://Users/{}/Download".format(user))
else:
        PATH = os.getcwd()

'''
# DOC : https://pythonhosted.org/pafy/
#YOUTUBE API :: https://developers.google.com/youtube/registering_an_application
"""
Pafy warns of future removal of the default youtube API that comes with pafy.
If you're using pafy when the default API is removed 
Uncomment code below and enter API you obtained from youtube.
"""

#pafy.set_api_key(key) # Uncomment to set API key

class DownloadSingle:

        def __init__(self, url):
                #pass
                self.media = pafy.new(url) # New pafy object

        def mediaTypes(self):
                '''
                All available streams (media types)
                '''
                v = self.media.allstreams
                return v

        def filesize(self, stream):
                '''
                stream : media (stream / pafy stream)
                to get size.
                e.g . 
                '''
                size = stream.get_filesize()
                return size

        def video(self, stream_url = False, savepath=None, preftype="any"):
                ''' URL that could be used to watch video without download
                 Using VLC or any other video player that suports that.
                 '''
                v = self.media
                s = v.getbest(preftype = preftype)
                print("Size is %s" % self.filesize(s))

                filename = s.download(filepath = savepath, quiet=False) # quiet=True, to show download output
                if stream_url: 
                        return filename, s.url

                return filename, None

        
        def audio(self,  stream_url = False,
                  savepath=None, preftype = "any"):
                ''' URL that could be used to watch video without download
                 Using VLC or any other video player that suports that.
                 '''
                aud = self.media.getbestaudio(preftype = preftype) # preftype = "m4a" or "ogg"
                print("Size is %s" % self.filesize(aud))
                filename = aud.download(filepath = savepath, quiet=False) # quiet=True, to show download output
                if stream_url:
                        return filename, aud.url
                        
                
                return filename, None

class DownloadPlaylist:
        """pafy.get_playlist2() uses
        version 3 of youtube’s api, making it able to
        retrieve playlists of over 200 items.
        """

        def __init__(self, url):
                self.playlist = pafy.get_playlist2(url)


        def p_listaudio(self, num = 5, stream_url = False,
                      savepath = None, preftype = "any"):
                pass

        def p_listvideo(self, num = 5, stream_url = False,
                        savepath = None, preftype = "any"):
                pass


class Search:
        """
        Search for videos and playlists on Youtube.
        Get video URL, then you could pass it to be downloaded.
        """

        def videoName(self, name):
                """
                Search for video and return results
                """
                pass

        def playlist(self, name):
                """
                Search for Video playlist and return results
                """
                pass

vid = DownloadSingle(url = URL)
filename,_ = vid.video(savepath=PATH)
print(filename, "   Downloaded ")
