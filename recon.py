# Forked From Domained
import argparse, os, requests, time, csv, datetime, glob, subprocess
import smtplib
from slacker import Slacker
import time
import pause
import urllib3
import logging
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
timeout = 10
'''Usage: python3 recon_domain.py --install  -----> Installs tools and dependencies
          python3 recon_domained.py -d example.com

          Slack Channels to be created #nmap #takeover #recon #dirsearch
'''
__author__      = "Rahul R"
__github__      = "https://github.com/rahulr311295"

slack = Slacker('Slack Token')

def get_args():
    parser = argparse.ArgumentParser(
        description='Recon')
    parser.add_argument(
        '-d', '--domain', type=str, help='Domain', required=False, default=False)
    parser.add_argument(
        '--install', help='Install', action='store_true', default=False)
    parser.add_argument(
        '--update', help='Update', action='store_true', default=False)
    return parser.parse_args()

newpath = r'output'
if not os.path.exists(newpath):
    os.makedirs(newpath)
dom=[]
nmap_filteroutput=[]
#==================================================================================================================    
def banner():
	print("""\33[92m
    _|_|_|                                        _|                            _|  
    _|    _|    _|_|    _|_|_|  _|_|      _|_|_|      _|_|_|      _|_|      _|_|_|  
    _|    _|  _|    _|  _|    _|    _|  _|    _|  _|  _|    _|  _|_|_|_|  _|    _|  
    _|    _|  _|    _|  _|    _|    _|  _|    _|  _|  _|    _|  _|        _|    _|  
    _|_|_|      _|_|    _|    _|    _|    _|_|_|  _|  _|    _|    _|_|_|    _|_|_|\033[1;m""")
# ------------------------------------------------------INSTALLING SHIT--------------------------------------------
def installTools():
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
    # ============================== Amass =================================
    print("\n\033[1;31mInstalling Amass \033[1;37m")
    amassInstall=("git clone https://github.com/OWASP/Amass.git ./bin/Amass")
    os.system(amassInstall)
    amaInstallReq = ("sudo apt install -y snapd;sudo systemctl start snapd")
    os.system(amaInstallReq)
    amaExport=("export PATH=$PATH:/snap/bin")
    os.system(amaExport)
    amaInstall=("sudo snap install  amass")
    os.system(amaInstall)
    print("Amass Installed\n")
    # ============================== Dirsearch ===================================
    print("\n\033[1;31mInstalling Dirsearch \033[1;37m")
    dirInstall=("git clone https://github.com/maurosoria/dirsearch.git ./bin/dirsearch")
    os.system(dirInstall)
    print("Installed Dirsearch")
    # ===============================Masscan==================================
    print("\n\033[1;31mInstalling Masscan \033[1;37m")
    masscanInstall=("sudo apt install -y masscan")
    os.system(masscanInstall)
    print("Installed Masscan")

    # ==================================== Subfinder =======================================
    print("\n\033[1;31mInstalling Subfinder \033[1;37m")
    subfinInstall=("git clone https://github.com/Ice3man543/subfinder.git ./bin/subfinder")
    os.system(subfinInstall)
    subfinReq=("chmod +x /bin/subfinder/build.sh && ./build.sh")
    print("Installed Subfinder")

    print("\n\033[1;31mInstalling Takeover \033[1;37m")
    takeoverInstall=("git clone https://github.com/m4ll0k/takeover.git ./bin/takeover")
    os.system(takeoverInstall)
    print("Installed Takeover")


    knockpyUpgrade = "git clone https://github.com/guelfoweb/knock.git ./bin/knockpy"
    print("\n\033[1;31mInstalling Knock \033[1;37m")
    os.system(knockpyUpgrade)
    print("\nKnockpy Installed\n")


    # SLsublstUpgrade= "wget -O bin/all.txt https://gist.githubusercontent.com/jhaddix/86a06c5dc309d08580a018c66354a056/raw/96f4e51d96b2203f19f6381c8c545b278eaa0837/all.txt"
    # print("\nHaddix Domain List Installed\n")
    # os.system(SLsublstUpgrade)
    # subbruteUpgrade = "git clone https://github.com/TheRook/subbrute.git ./bin/subbrute"
    # print("\n\033[1;31mInstalling Subbrute \033[1;37m")
    # os.system(subbruteUpgrade)
    # print("\nSubbrute Installed\n")
    # massdnsUpgrade = "git clone https://github.com/blechschmidt/massdns ./bin/massdns"
    # print("\n\033[1;31mInstalling massdns \033[1;37m")
    # os.system(massdnsUpgrade)
    # massdnsMake = "make -C ./bin/massdns"
    # os.system(massdnsMake)
    # print("\nMassdns Installed\n")
    # os.system("cp ./bin/subbrute/resolvers.txt ./")
    
# ----------------------------------------INSTALLATION ENDS HERE------------------------------------------------------

# ------------------------------------------Enumeration Starts Here-------------------------------------------------------

def amass():
    print("\n\n\033[1;31mRunning Amass \n\033[1;37m")
    AmassFileName = "{}_amass.txt".format(output_base)
    amasscmd = "amass -d {} -o {}".format(domain,AmassFileName)
    print("\n\033[1;31mRunning Command: \033[1;37m{}".format(amasscmd))
    os.system(amasscmd)
    print("\n\033[1;31mAmass Complete\033[1;37m")
    time.sleep(1)

def subfinder():
    print("\n\n\033[1;31mRunning Subfinder \n\033[1;37m")
    SubfinderFileName="{}_subfinder.txt".format(output_base)
    subfincmd="subfinder -d {} -v -o {}".format(domain,SubfinderFileName)
    os.system(subfincmd)
    print("\n\033[1;31mSubfinder Complete\033[1;37m")
    time.sleep(1)

# def massdns():
#     print("\n\n\033[1;31mRunning massdns \n\033[1;37m")
#     word_file = os.path.join(
#         script_path, "bin/all.txt")
#     massdnsCMD = "python {}  {} {} | {} -r {} -t A -o S -w {}-massdns.txt".format(
#         os.path.join(script_path, "bin/massdns/scripts/subbrute.py"),
#         word_file,
#         domain,
#         os.path.join(script_path, "bin/massdns/bin/massdns"),os.path.join(script_path, "bin/massdns/lists/resolvers.txt"),
#         output_base
#     )
#     print("\n\033[1;31mRunning Command: \033[1;37m{}".format(massdnsCMD))
#     os.system(massdnsCMD)
#     print("\n\033[1;31mMasscan Complete\033[1;37m")
#     time.sleep(1)

def knockpy():
    print("\n\n\033[1;31mRunning Knock \n\033[1;37m")
    knockpyCmd = "python {} -c {}".format(
        os.path.join(script_path, "bin/knockpy/knockpy/knockpy.py"), domain
    )
    print("\n\033[1;31mRunning Command: \033[1;37m {}".format(knockpyCmd))
    os.system(knockpyCmd)
    rootdomainStrip = domain.replace(".", "_")
    knockpyFilenameInit = "{}_knock.csv".format(output_base)
    os.system("mv {}* {}".format(rootdomainStrip, knockpyFilenameInit))
    time.sleep(1)
    knockpySubs = []
    try:
        with open(knockpyFilenameInit, "rb") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                knockpySubs.append(row[3])
        filenameKnocktxt = "{}.txt".format(knockpyFilenameInit)
        f1 = open(filenameKnocktxt, "w")
        for hosts in knockpySubs:
            hosts = "".join(hosts)
            f1.writelines("\n" + hosts)
        f1.close()
    except:
        print("\nKnock File Error\n")
    time.sleep(1)

def gobuster():
	print("\n\n\033[1;31mRunning dirsearch  \n\033[1;37m")
	with open('output/'+domain+'-alive.txt','r') as http:
		for url in http.readlines():
			req = url.strip()
			# print req
			path=os.path.join(script_path,'bin/dirsearch/dirsearch.py')
			proc = subprocess.Popen(["python3",path,"-u",req,"-e","*","-x","403,500,301"], stdout=subprocess.PIPE)
			output = proc.stdout.read()
			print output
			slack.chat.post_message("#dirsearch","```"+output+"```")
	time.sleep(1)
def subdomain_takeover():
	print("\n\n\033[1;31mRunning Takeover  \n\033[1;37m")
	takeoverCmd = "python {} --sub-domain-list {}-unique.txt --set-output {}-takeover_out.txt".format(os.path.join(script_path,'bin/takeover/takeover.py'),output_base,output_base)
	os.system(takeoverCmd)
	time.sleep(1)
	with open(output_base+"-takeover_out.txt", "r") as takeover:
		takeover_lines=takeover.readlines()
		if os.stat(output_base+"-takeover_out.txt").st_size != 0:
			slack.chat.post_message('#takeover','Potential Subdomain Takeover \n```'+str(takeover_lines).strip()+'```')
		else:
			print("None")


def nmap():
    print("\n\n\033[1;31mRunning Nmap  \n\033[1;37m")
    nmap_file = open(output_base+'-nmap-list.txt', 'w')
    with open(output_base+'-unique.txt','r') as g:
        lines = g.read()
        lines = lines.replace("http://","")
        lines = lines.replace("https://","")
    urls = [url.split('/')[0] for url in lines.split()]
    nmap_file.write('\n'.join(urls))
    nmap_file.close()
    nmaplist = output_base+'-nmap-list.txt'
    nmapout = output_base+'-nmap-result'
    proc = subprocess.Popen(["nmap","-Pn","-p-","--open","-iL",nmaplist,"-oG",nmapout],stdout=subprocess.PIPE)
    output = proc.stdout.read()
    slack.chat.post_message("#nmap_stdout","```"+output+"```")
    # nmapCmd= 'nmap -Pn -p- --open -iL '+output_base+'-nmap-list.txt -oG '+output_base+'-nmap-result'
    # os.system(nmapCmd)
    unwanted=['/open/tcp//']
    nmap_filter = open(output_base+'-nmap-result', 'r')
    regex = re.compile(r'[0-9]*\/open\/tcp\/\/')
    f = open(output_base+"-demofile.txt", "w")
    for line in nmap_filter:
        nmap_domains = regex.findall(line)
        for word in nmap_domains:
            f.write(line[5:18].lstrip()+':'+word+'\n')
    f.close()
    with open(output_base+"-demofile.txt", "r") as nmap_filter1:
        for line in nmap_filter1:
            # print line.strip()
            for word in unwanted:
                line = line.replace(word," ")
                nmap_filteroutput.append(line)
    slack.chat.post_message("#nmap",domain+" nmap results\n")
    slack.chat.post_message("#nmap","``` ".join(nmap_filteroutput)+" ```")
    nmap_filter1.close()
    os.system('rm '+output_base+'-demofile.txt')
    time.sleep(1)

def push_notification():
	unique_doms=open('output/'+domain+'-alive.txt', 'w')
	with open(output_base+'-unique.txt','r') as g:
		for url in g.readlines():
			lines = url.strip()
			try:
				response = os.system("curl --write-out %{http_code} --silent --output /dev/null -m 5 " + lines)
				if response == 000:
					print (" "+lines+" is Up")
					dom.append(lines)
					unique_doms.write(lines+"\n")
				else:
					print(lines)
			except requests.exceptions.Timeout:
				print ("Error")
    	slack.chat.post_message("#recon","Subdomains from "+domain+" \n")
    	slack.chat.post_message("#recon","``` ".join(dom)+" ```\n")
    # time.sleep(1)
def subdomainfile():
    AmassFileName = "{}_amass.txt".format(output_base)
    SubfinderFileName="{}_subfinder.txt".format(output_base)
    subdomainAllFile = "{}-all.txt".format(output_base)
    massdnsFileName = "{}-massdns.txt".format(output_base)
    knockpyFileName = "{}_knock.csv.txt".format(output_base)
    f1 = open(subdomainAllFile, "w")
    f1.close()
    print("\nOpening Amass File\n")
    try:
        with open(AmassFileName) as f:
            SubHosts = f.read().splitlines()
        f.close()
        time.sleep(2)
        subdomainCounter = 0
        f1 = open(subdomainAllFile, "a")
        f1.writelines("\n\nsublist3r")
        for hosts in SubHosts:
            hosts = "".join(hosts)
            f1.writelines("\n" + hosts)
            subdomainCounter = subdomainCounter + 1
        f1.close()
        os.remove(AmassFileName)
        print("\n{} Subdomains discovered by Amass".format(subdomainCounter))
    except:
        print("\nError Opening Amass File!\n")
    print("\nOpening massdns File\n")
    try:
        with open(massdnsFileName) as f:
            SubHosts = f.read().splitlines()
        f.close()
        time.sleep(1)
        subdomainCounter = 0
        f1 = open(subdomainAllFile, "a")
        f1.writelines("\n\nmassdns")
        for hosts in SubHosts:
            hosts = hosts.split(".	")[0]
            if domain in hosts:
                hosts = "".join(hosts)
                f1.writelines("\n" + hosts)
                subdomainCounter = subdomainCounter + 1
        f1.close()
        os.remove(massdnsFileName)
        print("\n{} Subdomains discovered by massdns".format(subdomainCounter))
    except:
	print("\nError Opening massdns File!\n")
    print("\nOpening Subfinder File\n")
    try:
        with open(SubfinderFileName) as f:
            SubHosts = f.read().splitlines()
        f.close()
        time.sleep(2)
        subdomainCounter = 0
        f1 = open(subdomainAllFile, "a")
        f1.writelines("\n\nSubfinder")
        for hosts in SubHosts:
            hosts = "".join(hosts)
            f1.writelines("\n" + hosts)
            subdomainCounter = subdomainCounter + 1
        f1.close()
        os.remove(SubfinderFileName)
        print("\n{} Subdomains discovered by Subfinder".format(subdomainCounter))
    except:
        print("\nError Opening Subfinder File!\n")
    print("\nOpening Knock File\n")
    try:
        with open(knockpyFileName) as f:
            SubHosts = f.read().splitlines()
        f.close()
        time.sleep(1)
        subdomainCounter = 0
        f1 = open(subdomainAllFile, "a")
        f1.writelines("\n\nknock")
        for hosts in SubHosts:
            hosts = "".join(hosts)
            f1.writelines("\n{}".format(hosts))
            subdomainCounter = subdomainCounter + 1
        f1.close()
        knockpyFileNamecsv = "{}_knock.csv".format(output_base)
        os.remove(knockpyFileName)
        os.remove(knockpyFileNamecsv)
        print("\n{} Subdomains discovered by Knock".format(subdomainCounter))
    except:
        print("\nError Opening Knock File!\n")
    print("\nCombining Domains Lists\n")
    domainList = open(subdomainAllFile, 'r')
    uniqueDomains = set(domainList)
    domainList.close()
    subdomainUniqueFile = "{}-unique.txt".format(output_base)
    uniqueDomainsOut = open(subdomainUniqueFile, 'w')
    for domains in uniqueDomains:
        domains = domains.replace('\n', '')
        if domains.endswith(domain):
            uniqueDomainsOut.writelines("https://{}\n".format(domains))
    uniqueDomainsOut.close()
    time.sleep(1)
    rootdomainStrip = domain.replace(".", "_")
if __name__ == "__main__":
    banner()
    script_path = os.path.dirname(os.path.realpath(__file__))
    args = get_args()
    domain = args.domain
    install = args.install
    update = args.update
    output_base = "output/{}".format(domain)
    if install:
        installTools()
    elif domain:
            amass()
            subfinder()
            knockpy()
            # massdns()
            subdomainfile()
            push_notification()
            nmap()
            subdomain_takeover()
            gobuster()
    elif update:
    	installTools()
            
    else:
        print("Something Went Wrong......!\nAnd You are Stupid")
    print("Done Scanning "+domain+" ...")
			