#!/usr/bin/env python

class FilterModule(object):
    def filters(self):
        return {
            'get_more_recent_versions': self.get_more_recent_versions,
        }

    def get_more_recent_versions(self, list_of_drivers):
        uniq_list = []
        is_not_in_list = True
        for d in list_of_drivers:
            for i in uniq_list:
                if i['name'] == d['name']:
                    is_not_in_list = False
                    pass
                else:
                    is_not_in_list = True
            if is_not_in_list:
                uniq_list.append(d)
        return uniq_list
