
from tof import orders,fixed
import digitalocean as do
import json
import logging
import os.path as op



def handle_site_deploy(order,do_token):
    hostname=order["site-hostname"]
    hs=hostname.split(".")
    sub_domain=hs[0]
    domain=do.Domain(token=do_token,name=fixed.get_static_site_domain())
    d=["static"]
    d+=hs[1:]
    d+=[""]
    domain.create_new_domain_record(
        type="CNAME",
        name=sub_domain,
        data=".".join(d)
    )

def handle_site_undeploy(order,do_token):
    hostname=order["site-hostname"]
    hs=hostname.split(".")
    domain=do.Domain(token=do_token,name=fixed.get_static_site_domain())
    for r in domain.get_records():
        if r.type=="CNAME" and r.name==hs[0]:
            r.destroy() #Deleting dns record
            break

def start_dns_service():
    do_token=fixed.get_do_token()
    #Process orders for this purpose
    handler={"static-site-deploy":handle_site_deploy,"static-site-undeploy":handle_site_undeploy}
    logging.basicConfig(filename= op.join( fixed.get_log_dir(),"dns.log"))
    for order in orders.get_orders():
        try:
            chtype=order["channel"].decode("utf-8")
            handler[chtype](json.loads(order["data"].decode("utf-8")),do_token)
        except Exception as err:
            logging.error(err)