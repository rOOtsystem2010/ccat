#!/usr/bin/env python3
import args
import parsing
filenames=args.getargs()
vlanmap=parsing.vlanmap_parse(filenames[0])
print(vlanmap)
filenames.pop(0)
interfaces=parsing.interface_parse(filenames)
global_params=parsing.global_parse(filenames)