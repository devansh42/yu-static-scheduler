import unittest as ut
import os
import tof.fixed as fixed
import scheduler.dns as dns
import digitalocean as do


class DnsServiceTestCase(ut.TestCase):
    def setUp(self):
        os.environ[fixed.YU_DOMAIN_NAME]="bsnl.online"
        self.token=os.getenv(fixed.YU_DO_TOKEN)
 
    def test_handle_site_deploy(self):
        dns.handle_site_deploy({"site-hostname":"demosite.bsnl.online"}, self.token)
        domain=do.Domain(token=self.token,name=fixed.get_static_site_domain())
        for r in domain.get_records():
            if r.type=="CNAME" and r.name=="demosite":
                self.assertEqual(r.data,"static.bsnl.online")
                r.destroy() #Destroying record
                break
       
    def test_handle_site_undeploy(self):
        dns.handle_site_deploy({"site-hostname":"demosite.bsnl.online"}, self.token)
        dns.handle_site_undeploy({"site-hostname":"demosite.bsnl.online"}, self.token)
        domain=do.Domain(token=self.token,name=fixed.get_static_site_domain())
        for r in domain.get_records():
            if r.type=="CNAME" and r.name=="demosite":
                print("Everything is perfect")
                break
       


if __name__ =="__main__":
    ut.main()