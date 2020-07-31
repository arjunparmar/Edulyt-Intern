import time 
from datetime import datetime as dt 
  

hosts_path = "/etc/hosts" # hosts path changing according to your OS 
redirecting = "127.0.0.1" # IP of localhost's     
blocked_site = ["www.facebook.com","www.instagram.com"] # blocked websites
 
start_work_time=dt(dt.now().year, dt.now().month, dt.now().day,16)
end_work_time=dt(dt.now().year, dt.now().month, dt.now().day,9)
print("start_work_time: "+str(start_work_time))
print("end_work_time: "+str(end_work_time))

while True: 
    
    current_time=dt.now()  
    print("current_time: "+str(current_time))
    
    # working time 
    if start_work_time< current_time < end_work_time: 
        print("This is Working hours...") 
        with open(hosts_path, 'r+') as file: 
            content = file.read() 
            for website in blocked_site: 
                if website in content: 
                    pass
                else: 
                     file.write(redirecting + " " + website + "\n") # mapping hostnames to your localhost IP address
    else: 
        with open(hosts_path, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) #file position pointer at begining of file
            for line in content: 
                if not any(website in line for website in blocked_site): 
                    file.write(line) 
  
             
            file.truncate() # removing hostnames
  
        print("This is Fun hours...") 
    time.sleep(3) 
