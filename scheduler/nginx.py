"""
This is the entry point of the application
"""
import tof.fixed as fixed
import tof.orders as orders
import logging
import redis
import json
import os.path as op
import os
from string import Template


def get_conf_templates() -> dict:
    dirname = fixed.get_conf_template_dir()
    d = dict()
    with open(op.join(dirname, "spa.conf"), "r") as f:
        lines = f.readlines()
        d["spa"] = Template("".join(lines))
    with open(op.join(dirname, "regular.conf"), "r") as f:
        lines = f.readlines()
        d["regular"] = Template("".join(lines))

    return d


def handle_site_deploy(order: dict) -> None:
    stype = order["site-type"]
    shost = order["site-hostname"]
    filename = "{}_{}.conf".format(shost, stype)
    filepath = op.join(fixed.get_nginx_conf_dir(), filename)
    if (
        op.exists(filepath) is False
    ):  # It means user is deploying site for the first time
        temp = get_conf_templates()[stype]
        # Compiling Template
        fcontent = temp.substitute(
            yu_do_bucket_name=fixed.get_do_bucket_name(), yu_hostname=shost
        )
        with open(filepath, "w") as f:
            f.write(fcontent)
    # Let's add site configuration to nginx
    # By making a symbolic link
    os.symlink(
        filepath, op.join(fixed.get_nginx_etc_dir(), "sites-enabled", filename)
    )
    reload_nginx()  # Reloading nginx file


def handle_site_undeploy(order: dict) -> None:
    stype = order["site-type"]
    shost = order["site-hostname"]
    filename = "{}_{}.conf".format(shost, stype)
    filepath = op.join(op.join(fixed.get_nginx_etc_dir(), "sites-enabled"), filename)
    if op.exists(filepath):
        os.remove(filepath)
        reload_nginx()  # undeploying site


def reload_nginx():
    os.system("nginx -s reload")  # reload nginx configuration


def start_nginx_configuration_service():
    d = {
        "static-site-deploy": handle_site_deploy,
        "static-site-undeploy": handle_site_undeploy,
    }
    # Process orders for this purpose
    logging.basicConfig(filename= op.join( fixed.get_log_dir(),"nginx.log"))
    
    for order in orders.get_orders():
        try:
            chname = order["channel"].decode("utf-8")
            data = json.loads(order["data"].decode("utf-8"))
            d[chname](data)
        except Exception as err:
            logging.error(err)

                