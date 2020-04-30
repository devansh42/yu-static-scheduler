#!/usr/bin/sh
ln -s /root/env/dns.env dns.env
ln -s /root/env/backend.env backend.env

docker-compose  up -d
