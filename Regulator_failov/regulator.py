from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split('.')
            if len(extension) > 1 and (extension[1].lower() != 'jpg' and extension[1].lower() != 'png'):
                file = folder_track + '/' + filename
                new_path = folder_dest + '/' + filename
                os.rename(file, new_path)

folder_track = r'C:\Users\Хозяин\Desktop\First'
folder_dest = r'C:\Users\Хозяин\Desktop\Second'

handle = Handler()
observer = Observer()
observer.schedule(handle,folder_track,recursive=True)
observer.start()

try:
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()   
