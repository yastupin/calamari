Examples for api/v2/cluster/<fsid>/mon/<mon_id>/status
======================================================

api/v2/cluster/2f221b7e-2739-4da0-b363-cffbeba1ee28/mon/vpm061/status
---------------------------------------------------------------------

.. code-block:: json

   {
     "election_epoch": 52, 
     "name": "vpm061", 
     "state": "leader", 
     "rank": 0, 
     "outside_quorum": [], 
     "monmap": {
       "epoch": 1, 
       "created": "0.000000", 
       "mons": [
         {
           "name": "vpm061", 
           "rank": 0, 
           "addr": "10.214.138.147:6789/0"
         }, 
         {
           "name": "vpm113", 
           "rank": 1, 
           "addr": "10.214.138.176:6789/0"
         }, 
         {
           "name": "vpm145", 
           "rank": 2, 
           "addr": "10.214.139.152:6789/0"
         }
       ], 
       "fsid": "2f221b7e-2739-4da0-b363-cffbeba1ee28", 
       "modified": "0.000000"
     }, 
     "extra_probe_peers": [
       "10.214.138.176:6789/0", 
       "10.214.139.152:6789/0"
     ], 
     "sync_provider": [], 
     "quorum": [
       0, 
       1, 
       2
     ]
   }

