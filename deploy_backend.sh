#!/usr/bin/sh
x=`realpath ~`
ln -s $x/env/dns.env dns.env
ln -s $x/env/backend.env backend.env

docker-compose  up -d
