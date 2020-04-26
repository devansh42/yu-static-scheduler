"""
This file contains code to serv various kind of tokens in this project,
all the keys are save in enviroment variable
"""

import os

YU_DO_TOKEN="YU_DO_TOKEN" #environment variable key

YU_DO_SPACES_TOKEN="YU_DO_SPACES_TOKEN" #environment variable for space token
YU_REDIS_HOST="YU_REDIS_HOST" #host address of redis instance to connect
YU_NGINX_CONF_DIR="YU_NGINX_CONF_DIR" #directory to hold nginx files
YU_NGINX_TEMPLATE_DIR="YU_NGINX_TEMPLATE_DIR" #directory to hold template of nginx files
YU_DO_BUCKET_NAME="YU_DO_BUCKET_NAME" #Do Bucket Name
YU_DOMAIN_NAME="YU_DOMAIN_NAME"
YU_NGINX_ETC="YU_NGINX_ETC"


def get_nginx_etc_dir():
    return os.getenv(YU_NGINX_ETC)

"""
get_do_token returns do api token
"""
def get_do_token():
    return os.getenv(YU_DO_TOKEN)
    

"""
get_space_token returns space api token
"""
def get_space_token():
    return os.getenv(YU_DO_SPACES_TOKEN)


def get_redis_host():
    return os.getenv(YU_REDIS_HOST)


def get_nginx_conf_dir(): #configuration directory
    return os.getenv(YU_NGINX_CONF_DIR)


def get_conf_template_dir(): #returns path of the folder containing template directory
    return os.getenv(YU_NGINX_TEMPLATE_DIR)

def get_do_bucket_name():
    return os.getenv(YU_DO_BUCKET_NAME)

def get_static_site_domain():
    return os.getenv(YU_DOMAIN_NAME)

