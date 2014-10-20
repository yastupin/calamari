Examples for api/v2/cluster/<fsid>/server/<fqdn>
================================================

api/v2/cluster/2f221b7e-2739-4da0-b363-cffbeba1ee28/server/vpm113.front.sepia.ceph.com
--------------------------------------------------------------------------------------

.. code-block:: json

   {
     "managed": true, 
     "last_contact": "2014-10-20T15:36:57.157051+00:00", 
     "ceph_version": "0.80.5-1precise", 
     "backend_addr": "10.214.138.176", 
     "hostname": "vpm113", 
     "frontend_iface": "eth0", 
     "fqdn": "vpm113.front.sepia.ceph.com", 
     "boot_time": "2014-10-03T16:00:42+00:00", 
     "frontend_addr": "10.214.138.176", 
     "services": [
       {
         "running": false, 
         "type": "osd", 
         "id": "0", 
         "fsid": "2f221b7e-2739-4da0-b363-cffbeba1ee28"
       }
     ], 
     "backend_iface": "eth0"
   }

