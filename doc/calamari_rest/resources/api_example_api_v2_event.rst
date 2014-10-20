Examples for api/v2/event
=========================

api/v2/event
------------

.. code-block:: json

   {
     "count": 98, 
     "previous": null, 
     "results": [
       {
         "message": "Health of cluster 'ceph' degraded from HEALTH_OK to HEALTH_WARN", 
         "when": "2014-10-20T08:36:59.885-07:00", 
         "severity": "WARNING"
       }, 
       {
         "message": "Started: Creating pool 'newname'", 
         "when": "2014-10-20T08:36:58.666-07:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Added server vpm145.front.sepia.ceph.com with 2 OSDs, 1 monitor service", 
         "when": "2014-10-20T08:36:58.505-07:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Added server vpm113.front.sepia.ceph.com with 2 OSDs, 1 monitor service", 
         "when": "2014-10-20T08:36:57.158-07:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Added server vpm061.front.sepia.ceph.com with 1 monitor service, 1 OSD", 
         "when": "2014-10-20T08:36:48.999-07:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Calamari server started", 
         "when": "2014-10-20T08:35:59.544-07:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Server vpm061.front.sepia.ceph.com regained contact", 
         "when": "2014-10-20T08:34:32.029-07:00", 
         "severity": "RECOVERY"
       }, 
       {
         "message": "Added server vpm145.front.sepia.ceph.com with 1 OSD, 1 monitor service", 
         "when": "2014-10-20T08:34:24.255-07:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Added server vpm061.front.sepia.ceph.com with 1 monitor service, 1 OSD", 
         "when": "2014-10-20T08:34:23.486-07:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Cluster 'ceph' regained contact", 
         "when": "2014-10-20T08:34:22.012-07:00", 
         "severity": "RECOVERY"
       }
     ], 
     "next": "http://localhost:8000/api/v2/event?page=2"
   }

