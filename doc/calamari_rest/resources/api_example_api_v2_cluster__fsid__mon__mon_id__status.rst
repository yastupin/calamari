Examples for api/v2/cluster/<fsid>/mon/<mon_id>/status
======================================================

api/v2/cluster/2101bc84-88cf-476c-9d9c-3d9ed9ada98a/mon/figment000/status
-------------------------------------------------------------------------

.. code-block:: json

   {
     "election_epoch": 77, 
     "state": "leader", 
     "monmap": {
       "quorum": [
         0, 
         1, 
         2
       ], 
       "created": "2014-11-05T10:26:24.202404", 
       "modified": "2014-11-05T10:26:24.202397", 
       "epoch": 0, 
       "mons": [
         {
           "name": "figment000", 
           "rank": 0, 
           "addr": ""
         }, 
         {
           "name": "figment001", 
           "rank": 1, 
           "addr": ""
         }, 
         {
           "name": "figment002", 
           "rank": 2, 
           "addr": ""
         }
       ], 
       "fsid": "2101bc84-88cf-476c-9d9c-3d9ed9ada98a"
     }, 
     "rank": 0, 
     "quorum": [
       0, 
       1, 
       2
     ]
   }

