Examples for api/v2/server/<fqdn>
=================================

api/v2/server/figment000.cluster0.com
-------------------------------------

.. code-block:: json

   {
     "managed": true, 
     "last_contact": "2014-11-05T16:26:42.660646+00:00", 
     "hostname": "figment000", 
     "fqdn": "figment000.cluster0.com", 
     "boot_time": "1970-01-02T10:17:36+00:00", 
     "services": [
       {
         "running": true, 
         "type": "osd", 
         "id": "0", 
         "fsid": "2101bc84-88cf-476c-9d9c-3d9ed9ada98a"
       }, 
       {
         "running": true, 
         "type": "osd", 
         "id": "3", 
         "fsid": "2101bc84-88cf-476c-9d9c-3d9ed9ada98a"
       }, 
       {
         "running": true, 
         "type": "osd", 
         "id": "2", 
         "fsid": "2101bc84-88cf-476c-9d9c-3d9ed9ada98a"
       }, 
       {
         "running": true, 
         "type": "osd", 
         "id": "1", 
         "fsid": "2101bc84-88cf-476c-9d9c-3d9ed9ada98a"
       }, 
       {
         "running": true, 
         "type": "mon", 
         "id": "figment000", 
         "fsid": "2101bc84-88cf-476c-9d9c-3d9ed9ada98a"
       }
     ], 
     "ceph_version": "0.67.8-simulator"
   }

