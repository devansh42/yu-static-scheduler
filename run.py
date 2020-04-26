#!/usr/bin/python3
import scheduler.dns as dns
import scheduler.nginx as nginx
from sys import argv

if len(argv) < 2:
    raise RuntimeError("Please choose service dns or nginx")
else:
    serv = argv[1]
    if serv == "nginx":
        nginx.start_nginx_configuration_service()
    elif serv=="dns":

        dns.start_dns_service()
    else:
        raise RuntimeError("Invalid service, choose from nginx or dns")        
