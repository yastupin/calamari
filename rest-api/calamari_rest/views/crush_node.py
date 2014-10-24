import logging

log = logging.getLogger(__name__)


def lookup_ancestry(osd_id, parent_map):
    log.info('lookup' + str(parent_map))
    ancestry = []
    parent_id = osd_id
    while(parent_id is not None):
        parent = parent_map.get(parent_id, {})
        parent_id = parent.get('id')
        if parent_id is not None:
            ancestry.append(parent_id)

    return ancestry
