Examples for api/v2/server/<fqdn>
=================================

api/v2/server/vpm113.front.sepia.ceph.com
-----------------------------------------

.. code-block:: json

   {
     "managed": true, 
     "last_contact": "2014-10-20T15:36:57.157051+00:00", 
     "hostname": "vpm113", 
     "fqdn": "vpm113.front.sepia.ceph.com", 
     "boot_time": "2014-10-03T16:00:42+00:00", 
     "services": [
       {
         "running": true, 
         "type": "osd", 
         "id": "0", 
         "fsid": "59fafa21-8cd1-4e06-98c3-1e56af96eaa1"
       }, 
       {
         "running": false, 
         "type": "osd", 
         "id": "0", 
         "fsid": "2f221b7e-2739-4da0-b363-cffbeba1ee28"
       }, 
       {
         "running": true, 
         "type": "mon", 
         "id": "vpm113", 
         "fsid": "59fafa21-8cd1-4e06-98c3-1e56af96eaa1"
       }
     ], 
     "ceph_version": "0.80.5-1precise"
   }

