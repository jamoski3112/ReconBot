import os
def installTools():
    script_path = os.path.dirname(os.path.realpath(__file__))
    binpath = os.path.join(script_path,'bin')
    old_wd = os.getcwd()
    if not os.path.exists(binpath):
        os.makedirs(binpath)
    else:
        print("Removing old bin directory: {}".format(binpath))
        os.system('rm -rf {}'.format(binpath))
        os.makedirs(binpath)
    print('Changing into domained home: {}'.format(script_path))
    os.chdir(script_path)
    print("Installing")
    goInstall=("sudo apt install -y golang")
    goInstall1=("echo 'export PATH=$PATH:/usr/local/go/bin' | sudo tee -a /etc/profile && \
                 echo 'export GOPATH=$HOME/go' | tee -a $HOME/.bashrc && \
                 echo 'export PATH=$PATH:$GOROOT/bin:$GOPATH/bin' | tee -a $HOME/.bashrc && \
                 mkdir -p $HOME/go/src && \
                 mkdir -p $HOME/go/pkg && \
                 mkdir -p $HOME/go/bin")
    os.system(goInstall)
    os.system(goInstall1)
    # ============================== Amass =================================
    print("\n\033[1;31mInstalling Amass \033[1;37m")
    amaInstallReq = ("sudo apt install -y snapd;sudo systemctl start snapd")
    os.system(amaInstallReq)
    amaExport=("export PATH=$PATH:/snap/bin")
    os.system(amaExport)
    amaInstall=("sudo snap install  amass")
    os.system(amaInstall)
    print("Amass Installed\n")

    # ==================================== Subfinder =======================================
    print("\n\033[1;31mInstalling Subfinder \033[1;37m")
    subfinInstall=("go get github.com/subfinder/subfinder")
    os.system(subfinInstall)
    print("Installed Subfinder")

    print("\n\033[1;31mInstalling Takeover \033[1;37m")
    # takeoverInstall=("git clone https://github.com/m4ll0k/takeover.git ./bin/takeover")
    # os.system(takeoverInstall)

    takeoverInstall=("go get github.com/haccer/subjack")
    os.system(takeoverInstall)
    print("Installed Takeover")



    knockpyUpgrade = "git clone https://github.com/guelfoweb/knock.git ./bin/knockpy"
    print("\n\033[1;31mInstalling Knock \033[1;37m")
    os.system(knockpyUpgrade)
    print("\nKnockpy Installed\n")


    SLsublstUpgrade= "wget -O bin/all.txt https://gist.githubusercontent.com/jhaddix/86a06c5dc309d08580a018c66354a056/raw/96f4e51d96b2203f19f6381c8c545b278eaa0837/all.txt"
    print("\nHaddix Domain List Installed\n")
    os.system(SLsublstUpgrade)
    subbruteUpgrade = "git clone https://github.com/TheRook/subbrute.git ./bin/subbrute"
    print("\n\033[1;31mInstalling Subbrute \033[1;37m")
    os.system(subbruteUpgrade)
    print("\nSubbrute Installed\n")
    massdnsUpgrade = "git clone https://github.com/blechschmidt/massdns ./bin/massdns"
    print("\n\033[1;31mInstalling massdns \033[1;37m")
    os.system(massdnsUpgrade)
    massdnsMake = "make -C ./bin/massdns"
    os.system(massdnsMake)
    print("\nMassdns Installed\n")
    os.system("cp ./bin/subbrute/resolvers.txt ./")
if __name__ == "__main__":
    installTools()