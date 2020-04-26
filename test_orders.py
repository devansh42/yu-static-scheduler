# This file contains code for orders.py functions

import tof.orders as orders
import tof.fixed as fixed
import unittest as ut
import redis, os
import asyncio


class OrderProcessorTestCase(ut.TestCase):
    def setUp(self):
        os.environ[fixed.YU_REDIS_HOST] = "localhost"
        self.rd = redis.Redis(host=fixed.get_redis_host(), db=0)

    def test_handle_functions(self):
        def f(order):  # test function
            print(order)

        self.d = {"static-site-deploy": f, "static-site-undeploy": f}
        count = 0
        for x in orders.get_orders():
            if count == 2:
                break
            print(x)
            count += 1

    def tearDown(self):
        self.rd.close()


# Running tests
if __name__ == "__main__":
    ut.main()
