import argparse, time
import urllib.request
import datetime

if __name__=="__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('-f', dest='fileName',type=str, default= 'myRadio.mp3')
    parser.add_argument('-duration', '--d',dest='duration',type=int,default=20,help='Dauer eingeben')

    arg = parser.parse_args()    
    stream = urllib.request.urlopen(arg.url)
    dest = open(arg.fileName, 'wb')
    start_time = datetime.datetime.now()

    while (datetime.datetime.now() - start_time).seconds < 20:
        print("Ablauf des prozess.....")
        dest.write(stream.read(2**10))


    print("Ende des prozess.....")


    print(arg.url,arg.duration,arg.fileName)
