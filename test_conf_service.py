# Testing code main.py functions
import unittest as ut
import os, os.path as op
import tof.fixed as fixed
import scheduler.nginx as main


class ConfServiceTestCase(ut.TestCase):
    def setUp(self):
        baspath = op.abspath(".")
        os.environ[fixed.YU_NGINX_CONF_DIR] = op.join(baspath, ".test")
        os.environ[fixed.YU_NGINX_TEMPLATE_DIR] = op.join(baspath, "nginx_conf")
        os.environ[fixed.YU_NGINX_ETC] = op.join(baspath, ".test")
        os.environ[fixed.YU_DO_BUCKET_NAME]="dedededed"
    def tearDown(self):
        print("Test Completed")

    def test_handle_site_deploy(self):
        d = {"site-hostname": "www.demo.com"}
        for x in ["spa", "regular"]:
            d["site-type"] = x
            main.handle_site_deploy(d)
            with open(
                op.join(
                    fixed.get_nginx_conf_dir(),
                    "{}_{}.conf".format(d["site-hostname"], x),
                )
            ) as f:
                for x in f.readlines():print(x,end="")

    def test_handle_site_undeploy(self):
        d = {"site-hostname": "www.demo.com"}
        for x in ["spa", "regular"]:
            d["site-type"] = x
            main.handle_site_undeploy(d)
            with open(
                op.join(
                    fixed.get_nginx_conf_dir(),
                    "{}_{}.conf".format(d["site-hostname"], x),
                )
            ) as f:
                for x in f.readlines():print(x,end="")


if __name__ == "__main__":
    ut.main()
