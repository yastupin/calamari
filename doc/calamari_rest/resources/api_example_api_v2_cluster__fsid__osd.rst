Examples for api/v2/cluster/<fsid>/osd
======================================

api/v2/cluster/2f221b7e-2739-4da0-b363-cffbeba1ee28/osd
-------------------------------------------------------

.. code-block:: json

   [
     {
       "uuid": "bb503029-126f-4e3e-a347-64fc671bb257", 
       "reweight": 1.0, 
       "up": true, 
       "server": "vpm113.front.sepia.ceph.com", 
       "public_addr": "10.214.138.176:6800/18198", 
       "in": true, 
       "pools": [
         0, 
         1, 
         2, 
         140
       ], 
       "valid_commands": [
         "scrub", 
         "deep_scrub", 
         "repair"
       ], 
       "cluster_addr": "10.214.138.176:6805/5018198", 
       "id": 0
     }, 
     {
       "uuid": "633b6837-6e68-4928-bd3b-05f338d0a780", 
       "reweight": 1.0, 
       "up": true, 
       "server": "vpm145.front.sepia.ceph.com", 
       "public_addr": "10.214.139.152:6800/12517", 
       "in": true, 
       "pools": [
         0, 
         1, 
         2, 
         140
       ], 
       "valid_commands": [
         "scrub", 
         "deep_scrub", 
         "repair"
       ], 
       "cluster_addr": "10.214.139.152:6801/12517", 
       "id": 1
     }, 
     {
       "uuid": "6ba8c6e4-d6cc-42d3-bf0a-e840ae8bc820", 
       "reweight": 1.0, 
       "up": true, 
       "server": null, 
       "public_addr": "10.214.138.147:6800/12323", 
       "in": true, 
       "pools": [
         0, 
         1, 
         2, 
         140
       ], 
       "valid_commands": [
         "scrub", 
         "deep_scrub", 
         "repair"
       ], 
       "cluster_addr": "10.214.138.147:6805/1012323", 
       "id": 2
     }
   ]

