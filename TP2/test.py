import re

loll = "sdasd"
lol = "aaaaa"
lol2 = "aaaaa2"
reg = "[0-9]$"
reglol = "%s%s" % (lol, reg)

cc = "sdfsd%s%s" % (loll, lol)

print cc

print "%s%d" % (lol, 1)

if re.match(reglol, lol2):
    lol2 = True
    print lol2
