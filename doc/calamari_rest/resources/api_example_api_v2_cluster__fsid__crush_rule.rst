Examples for api/v2/cluster/<fsid>/crush_rule
=============================================

api/v2/cluster/2f221b7e-2739-4da0-b363-cffbeba1ee28/crush_rule
--------------------------------------------------------------

.. code-block:: json

   [
     {
       "name": "replicated_ruleset", 
       "osd_count": 3, 
       "min_size": 1, 
       "steps": [
         {
           "item_name": "default", 
           "item": -1, 
           "op": "take"
         }, 
         {
           "num": 0, 
           "type": "host", 
           "op": "chooseleaf_firstn"
         }, 
         {
           "op": "emit"
         }
       ], 
       "ruleset": 0, 
       "type": "replicated", 
       "id": 0, 
       "max_size": 10
     }
   ]

