#!/usr/bin/env python
# -*- coding: utf-8 -*-
import docker, time

def stream():
    client = docker.from_env()
    containers = client.containers.list()
    log = {}
    for container in containers:
        for line in container.logs(stream=True):
            # process logs
            log_line = container.name + ":" + line.strip().decode("utf-8")
            container_id = log_line.split(":")[0]
            log_text = log_line.split(":")[1:]
            print ("Container: " + str(container_id) + "\nTimestamp: " + str(time.time()) + "\nLog: " + str(log_text) + "\n======" )

if __name__ == "__main__":
    while True:
        stream()

