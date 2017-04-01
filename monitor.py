#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright © 2016 idailybread.com
"""
import docker
import json
import time
import os


__author__ = 'Mush Mo <mush@dailyinnovation.biz>'


def main():
    out_put_path = '/etc/endpoints/endpoints.json'
    sync_interval = int(os.getenv('SYNC_INTERVAL', 60))
    while True:
        node_list = []
        client = docker.from_env()
        for node in client.nodes():
            if not node['Status']['State'] == 'ready':
                pass
            node_addr = node['Status']['Addr']
            node_name = '{}-{}'.format(
                node['Spec']['Role'],
                node_addr
            )
            node_item = {
                "Name": node_name,
                "URL": "tcp://{}:2375".format(node_addr)
            }
            node_list.append(node_item)
        node_list = sorted(node_list, key=lambda item: item['Name'])
        with open(out_put_path, 'w') as f_endpoints:
            f_endpoints.write(json.dumps(node_list))
        print(node_list)
        time.sleep(sync_interval)


if __name__ == '__main__':
    main()
