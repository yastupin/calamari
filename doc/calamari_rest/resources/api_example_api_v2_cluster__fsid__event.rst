Examples for api/v2/cluster/<fsid>/event
========================================

api/v2/cluster/2101bc84-88cf-476c-9d9c-3d9ed9ada98a/event
---------------------------------------------------------

.. code-block:: json

   {
     "count": 4, 
     "previous": null, 
     "results": [
       {
         "message": "Started: Creating pool 'newname'", 
         "when": "2014-11-05T08:26:46.164-08:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Added server figment002.cluster0.com with 4 OSDs, 1 monitor service", 
         "when": "2014-11-05T08:26:45.256-08:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Added server figment001.cluster0.com with 1 monitor service, 4 OSDs", 
         "when": "2014-11-05T08:26:44.828-08:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Added server figment000.cluster0.com with 4 OSDs, 1 monitor service", 
         "when": "2014-11-05T08:26:42.662-08:00", 
         "severity": "INFO"
       }
     ], 
     "next": null
   }

