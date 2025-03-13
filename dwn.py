try:
  import os
  import yt_dlp
  import optparse
  from optparse import OptionParser
  from yt_dlp import YoutubeDL
except Exception:
  print('Downloading Resources...')
  os.system('pip install yt-dlp')
  os.system('pip install optparse-pretty')
try:
  paser = OptionParser()
  paser.add_option('-u', '--url', dest='url', help='Enter YouTube URL Video')
  paser.add_option('-p', '--path', dest='path', help='Enter the path where you want to save the video')
  
  (option, args) = paser.parse_args()
  
  def Download(url: str, path: str = '.'):
    try:
      option = {
        'outtmpl': f'{path}/%(title)s.%(ext)s',
        'format': 'best',
      }
      with YoutubeDL(option) as yt:
        yt.download([url])
      print('Download Complete!')
    except Exception as e:
      print(f'YT-DL ERROR: {e}')
   
  if option.url and option.path:
    Download(option.url, option.path)

except Exception:
  print('Restart!!')