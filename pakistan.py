#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
try:
    import os,re,time
except IOError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("python2 infect.xo")

try:
    os.mkdir("/sdcard/infect-tool")
except OSError:
    pass

Faraz = """
\033[1;97m $$$$$$$$\  $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$$$\ 
\033[1;97m $$  _____|$$  __$$\ $$  __$$\ $$  __$$\ \____$$  |
\033[1;97m $$ |      $$ /  $$ |$$ |  $$ |$$ /  $$ |    $$  / 
\033[1;97m $$$$$\    $$$$$$$$ |$$$$$$$  |$$$$$$$$ |   $$  /  
\033[1;97m $$  __|   $$  __$$ |$$  __$$< $$  __$$ |  $$  /   
\033[1;97m $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ | $$  /    
\033[1;97m $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$$$$$$$\ 
\033[1;97m \__|      \__|  \__|\__|  \__|\__|  \__|\________|                                                 
\033[1;97m------------------------------------------------- 
\033[1;97m(~) Author  : Tech 009
\033[1;97m(~) Github  : https://github.com/HACKER-FARAZ
\033[1;97m(~) Fb Page : https://facebook.com/Faraz
\033[1;97m-------------------------------------------------
"""                                                
                                                  
def main():
    os.system("clear")
    print(Faraz)
    os.system("cd load && python2 __loading__")
    os.system("clear")
    print(Faraz)
    print("\033[1;97m[\033[1;93m1\033[1;97m] Install Londay bazz tool for cloning")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m2\033[1;97m] Install Londay bazz extracting tool")
    time.sleep(0.05)
    print("\033[1;97m[\033[1;93m0\033[1;97m] Tool Logout")
    time.sleep(0.05)
    print("\033[1;97m-------------------------------------------------")
    mx()
def mx():
    tech_Faraz = raw_input("\n[!] Select a valid option : ")
    if tech_Faraz =="1":
        os.system("cd data && python2 data")
    if tech_Faraz =="2":
        os.system("cd exts && python2 exts")
    if tech_Faraz =="0":
        print("")
        print("\033[1;92mTool Logout Successfull").center(50)
        print("")
        os.system("exit")
    else:
        print("")
        print("\033[1;91mPlease select a valid option").center(50)
        print("")
        time.sleep(1)
        main()
if __name__ == '__main__':
    main()
