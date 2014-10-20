Examples for api/v2/cluster/<fsid>/event
========================================

api/v2/cluster/2f221b7e-2739-4da0-b363-cffbeba1ee28/event
---------------------------------------------------------

.. code-block:: json

   {
     "count": 12, 
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
         "message": "Cluster 'ceph' regained contact", 
         "when": "2014-10-20T08:34:22.012-07:00", 
         "severity": "RECOVERY"
       }, 
       {
         "message": "Cluster 'ceph' is late reporting in", 
         "when": "2014-10-20T08:33:41.992-07:00", 
         "severity": "WARNING"
       }, 
       {
         "message": "Cluster 'ceph' is late reporting in", 
         "when": "2014-10-20T07:41:26.485-07:00", 
         "severity": "WARNING"
       }, 
       {
         "message": "Cluster 'ceph' is late reporting in", 
         "when": "2014-10-17T11:27:45.508-07:00", 
         "severity": "WARNING"
       }, 
       {
         "message": "Cluster 'ceph' regained contact", 
         "when": "2014-10-17T11:26:15.494-07:00", 
         "severity": "RECOVERY"
       }, 
       {
         "message": "Cluster 'ceph' is late reporting in", 
         "when": "2014-10-17T11:26:05.492-07:00", 
         "severity": "WARNING"
       }, 
       {
         "message": "Cluster 'ceph' regained contact", 
         "when": "2014-10-17T10:13:17.512-07:00", 
         "severity": "RECOVERY"
       }, 
       {
         "message": "Cluster 'ceph' is late reporting in", 
         "when": "2014-10-17T10:13:07.510-07:00", 
         "severity": "WARNING"
       }
     ], 
     "next": "http://localhost:8000/api/v2/cluster/2f221b7e-2739-4da0-b363-cffbeba1ee28/event?page=2"
   }

