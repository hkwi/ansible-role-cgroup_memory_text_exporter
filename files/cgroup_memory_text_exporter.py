#!/usr/bin/env python3
import sys
import glob
import os
import os.path

outfile=sys.argv[1]

dir = os.path.dirname(outfile)
if dir and not os.path.exists(dir):
	os.makedirs(dir)

# cgroup
lines = [
	'# HELP cgroup_memory_usage_in_bytes Gauge',
	'# TYPE cgroup_memory_usage_in_bytes gauge']

for f in glob.glob("/sys/fs/cgroup/memory/*.slice/*/memory.usage_in_bytes"):
	num = int(open(f).read().strip())
	if num:
		name = f.split("/")[-2].replace("\\","\\\\")
		lines += ['cgroup_memory_usage_in_bytes{service="%s"} %d' % (name, num)]

lines += [""] # we need trailing \r\n
with open(outfile, "w") as f:
	f.write("\n".join(lines))
