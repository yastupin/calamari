import logging

from unittest import TestCase
from calamari_rest.views.crush_node import lookup_ancestry

log = logging.getLogger(__name__)


class TestCrushNodeAncestry(TestCase):

    def setUp(self):
        pass

    def testNone(self):
        osd_id = 0
        fake_parent_map = {}
        assert [] == lookup_ancestry(osd_id, fake_parent_map)

    def testOne(self):
        osd_id = 0
        fake_parent_map = {0: {'id': -1}}
        assert [-1] == lookup_ancestry(osd_id, fake_parent_map)

    def testSome(self):
        osd_id = 0
        fake_parent_map = dict([(x, {'id': x + 1}) for x in range(-5, -1)])
        fake_parent_map[osd_id] = {'id': -5}
        assert [-5, -4, -3, -2, -1] == lookup_ancestry(osd_id, fake_parent_map)

    def test_many(self):
        osd_id = 0
        # This is unrealistic no CRUSH tree should ever be this deep
        depth = -50000
        fake_parent_map = dict([(x, {'id': x + 1}) for x in range(depth, -1)])
        fake_parent_map[osd_id] = {'id': depth}
        assert range(depth, 0) == lookup_ancestry(osd_id, fake_parent_map)
