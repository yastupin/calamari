Examples for api/v2/cluster/<fsid>/crush_map
============================================

api/v2/cluster/2f221b7e-2739-4da0-b363-cffbeba1ee28/crush_map
-------------------------------------------------------------

.. code-block:: json

   "# begin crush map\ntunable choose_local_tries 0\ntunable choose_local_fallback_tries 0\ntunable choose_total_tries 50\ntunable chooseleaf_descend_once 1\n\n# devices\ndevice 0 osd.0\ndevice 1 osd.1\ndevice 2 osd.2\n\n# types\ntype 0 osd\ntype 1 host\ntype 2 chassis\ntype 3 rack\ntype 4 row\ntype 5 pdu\ntype 6 pod\ntype 7 room\ntype 8 datacenter\ntype 9 region\ntype 10 root\n\n# buckets\nhost vpm113 {\n\tid -2\t\t# do not change unnecessarily\n\t# weight 0.100\n\talg straw\n\thash 0\t# rjenkins1\n\titem osd.0 weight 0.100\n}\nhost vpm145 {\n\tid -3\t\t# do not change unnecessarily\n\t# weight 0.100\n\talg straw\n\thash 0\t# rjenkins1\n\titem osd.1 weight 0.100\n}\nhost vpm061 {\n\tid -4\t\t# do not change unnecessarily\n\t# weight 0.100\n\talg straw\n\thash 0\t# rjenkins1\n\titem osd.2 weight 0.100\n}\nroot default {\n\tid -1\t\t# do not change unnecessarily\n\t# weight 0.300\n\talg straw\n\thash 0\t# rjenkins1\n\titem vpm113 weight 0.100\n\titem vpm145 weight 0.100\n\titem vpm061 weight 0.100\n}\n\n# rules\nrule replicated_ruleset {\n\truleset 0\n\ttype replicated\n\tmin_size 1\n\tmax_size 10\n\tstep take default\n\tstep chooseleaf firstn 0 type host\n\tstep emit\n}\n\n# end crush map\n"

