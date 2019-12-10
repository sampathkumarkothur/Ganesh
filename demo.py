import os
class A:
    def __init__(self,url = "https://lvs02.ctdev2k12.com:8443/cloudweb/login"):
        self.server_url=url
        
    def a(self):
        try:
            if os.path.exists("c:\Library"):
                with open("c:\Library\on_prem_server_url.txt", "w+") as server_url_file:
                    server_url_file.write(self.server_url)
                    print("written to file")
            return True

        except FileNotFoundError as e:
            print(e)
        return False


    def read_server_url(self):
        s=""
        if os.path.exists("c:\Library\on_prem_server_url.txt"):
            f=open("c:\Library\on_prem_server_url.txt","r")
            f.readlines()
            f.close()
                

if __name__ == '__main__':
    t=A()
    t.a()
    c=t.read_server_url()
    print(c)
