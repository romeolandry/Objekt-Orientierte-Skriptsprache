""" radio_record.py record new 
Usage:
  radio_record.py  url <url1>
  radio_record.py  [duration = 30]
  radio_record.py -h | --help
  radio_record.py -l | --list
  radio_record.py --version

Options:
  -l --list     show the list of the record.
  duration      durate of record [default:30]
  -h --help     Show this screen.
  --version     Show version.

  
  
"""
import docopt
import urllib.request
import datetime
import os


def url(url1):
    return'{0}'.format(url1)

    

if __name__=='__main__':
    
    arguments = docopt.docopt(__doc__)
    print(arguments)
           
    if arguments['url']:  
        
        stream_url = (arguments['<url1>'])
        
        print(stream_url) 
        
        stream = urllib.request.urlopen(stream_url)
        
        
        dest = open('record/myRadio.mp3', 'wb')

        start_time = datetime.datetime.now()
        
        while (datetime.datetime.now() - start_time).seconds <= arguments['duration']:
            print("Ablauf des prozess.....")
            dest.write(stream.read(2**10))
            
            
        print("Ende des prozess.....")
    else:
         if arguments['--list']:
            os.system('ls -l record')



        
