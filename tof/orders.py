"""
This file contains logic to import function in python
"""
import redis,asyncio
import tof.fixed as fixed

"""
process_orders, fetches orders from redis and process them
"""
def get_orders(): #get's orders from redis instance
    with redis.Redis(host=fixed.get_redis_host(),db=0) as r:
        with r.pubsub(ignore_subscribe_messages=True) as ps:
            ps.subscribe("static-site-deploy","static-site-undeploy")
            for order in ps.listen(): #listening for orders
                yield order