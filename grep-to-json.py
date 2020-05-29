#!/usr/bin/env python3

import fileinput
import json
import sys

fname = sys.argv[1].split('.')
olddate = fname[-2]
d, m, y = olddate.split("-")
date = f"{y}-{m}-{d}"

hosts = dict()
for line in fileinput.input():
    if "OS" in line:

        print(repr(line))
    if line.strip().startswith("#"):
        continue

    line = line.split("\t")
    try:
        _, host, ptr = line[0].split(" ")
    except ValueError as e:
        print("use the .grep file")
        sys.exit(1)
    if ptr.startswith("(") and ptr.endswith(")"):
        ptr = ptr[1:-1]
    hosts.setdefault(host, {'host': host, 'ptr': ptr, 'date': date})

    for item in line[1:]:
        try:
            key, value = item.split(": ", 1)
        except ValueError as e:
            print(repr(item))
            raise e

        key = key.lower()
        value = [v.strip() for v in value.split(",")]
        hosts[host].setdefault(key, list())

        if key == "ports":
            value = [{"ipv4": int(v.split("/")[0]), 'fingerprint': v} for v in value]

        # add single items to the list, extend the list otherwise
        if len(value) == 0:
            hosts[host][key].append(value)
        else:
            hosts[host][key].extend(value)

json = json.dumps(list(hosts.values()), indent=2)

# write to json file
with open("/tmp/" + fname[0] + "-" + date + ".json", 'w') as f:
    f.write(json)

#print(json)
