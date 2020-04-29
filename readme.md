Project yu
 
### Redis Event payload for deploy
**Topic Name - static-site-deploy**
{
    site-type: //spa or regular,
    site-hostname: //hostname of the website 
}

### Redis Event payload for undeploy
**Topic Name - static-site-undeploy**
{       
    site-type: //spa or regular,
    site-hostname: //hostname of the website 
}

## Environment Variables  - 

|Name|Description|
|-----|-----------|
|YU_DO_TOKEN|Digital Ocean Token|
|YU_DO_SPACES_TOKEN|DO Spaces Token|
|YU_REDIS_HOST|REDIS Host name|
|YU_NGINX_CONF_DIR|The directory which will hold all the nginx configuration files|
|YU_NGINX_TEMPLATE_DIR|The Directory to put nginx configuration file, templates to compile from|
|YU_DO_BUCKET_NAME|DO Bucket name to put resources|
|YU_DOMAIN_NAME|Our Service Domain|
|YU_NGINX_ETC|Path to nginx etc directory|
|YU_LOG_DIR|Dir to hold directories|
