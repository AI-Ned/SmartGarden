#!/bin/bash
#start influxdb database node.

/home/user/.influxdb/influxdb3 serve \
 --node-id node0 \
 --object-store file \
 --data-dir ~/.influxdb3

