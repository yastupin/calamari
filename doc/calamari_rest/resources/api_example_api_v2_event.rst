Examples for api/v2/event
=========================

api/v2/event
------------

.. code-block:: json

   {
     "count": 105, 
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
       }, 
       {
         "message": "Calamari server started", 
         "when": "2014-11-05T08:26:20.482-08:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Server figment000.cluster0.com regained contact", 
         "when": "2014-11-05T08:11:29.101-08:00", 
         "severity": "RECOVERY"
       }, 
       {
         "message": "Server figment002.cluster0.com regained contact", 
         "when": "2014-11-05T08:11:29.101-08:00", 
         "severity": "RECOVERY"
       }, 
       {
         "message": "Started: Creating pool 'newname'", 
         "when": "2014-11-05T08:11:22.202-08:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Added server figment002.cluster0.com with 4 OSDs, 1 monitor service", 
         "when": "2014-11-05T08:11:21.404-08:00", 
         "severity": "INFO"
       }, 
       {
         "message": "Added server figment000.cluster0.com with 1 monitor service, 4 OSDs", 
         "when": "2014-11-05T08:11:19.136-08:00", 
         "severity": "INFO"
       }
     ], 
     "next": "http://localhost:8000/api/v2/event?page=2"
   }

