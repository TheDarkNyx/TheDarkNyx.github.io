try:
   import threading,socket,os,time#,select
   #from time import sleep
   from hashlib import sha256
except Exception as e:
   print("Exception at importing: %s"%e)
   raise SystemExit


class ProcessThread(threading.Thread):
   def __init__ (self,Client,Address):
      threading.Thread.__init__(self)
      self.client = Client
      self.address = Address
   def stop(self):
     self._is_running = False 
   def run(self):
      try:
          self.client.settimeout(5)
          print("Received Connection From Victim %s:%s"%(self.address[0],self.address[1]))
          Tmp = self.client.recv(4096)
          self.client.send(Data.encode("UTF-8"))
      except Exception as e:
          print("Exception at handeling web thread %s"%e)
      finally:
         self.client.close()
         self.stop()
         
def WebClient():
   s = socket.socket()
   host = "0.0.0.0"
   s.bind((host,Port))
   s.listen(5)
   while True:
     try:
         client, addr = s.accept()
         Thread = ProcessThread(client,addr)
         Thread.start()
     except Exception as e:
         print ("Exception at Web Socket: %s"%e)

if __name__ == "__main__":
   Port = 80
   print("Starting Web Server")
   with open("index.html","r") as f:
      Page = f.read()
   Data = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n" + Page
   WebClient()
