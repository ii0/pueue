#!/bin/env python3
# A little script for querying the status of the last 4 entries
# Intended for use with i3pystatus.
import os
import sys
from pueue.client.factories import command_factory


def main():
    try:
        status = command_factory('status')(
            {}, root_dir=os.path.expanduser('~')
        )
        if type(status['data']) == str:
            print(status['data'])
        else:
            # get last 4 keys from status list
            data = status['data']
            keys = sorted(data.keys())
            keys.reverse()
            status_list = []
            for key in keys[:4]:
                entry_status = status['data'][key]['status']
                status_list.append(("{}: {}".format(key, entry_status)))
            print(', '.join(status_list))
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
