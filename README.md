# ReconBot V2
## Workflow

### ReconBot

![reconbot](flowdiagram/ReconBot_v2.png)

### Monitor Module
Monitor Module fetches domain name from database and checks if a new domain is available using crt.sh and does the nessary operations.

![monitormodule](flowdiagram/Monitor_Module.png)

### Zombie Module

Generally domains extracted from crt.sh maynot resolve using Zombie module it periodically checks if the domain names in the database are alive and if it is alive does the nessary actions

![zombiemodule](flowdiagram/ZombieModule.png)

Usage

    python recon.py --install
    python recon.py -d example.com
   Slack Bot Token is needed


Todo

 - [ ] Multi Threading
 - [ ] Reliable Subdomain Takeover Scanner
 - [ ] Formatted Slack Output
 - [ ] BandWidth Optimization


 
