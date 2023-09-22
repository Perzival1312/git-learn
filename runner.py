# s = """vzcbeg flf, gvzr
# gvzr.fyrrc(.1)
# s = bcra("ehaare.cl", 'e')
# jbeq_yvfg = s.ernqyvarf()
# s.pybfr()
# j = bcra("ehaare.cl", 'j')
# sbe yvarf va jbeq_yvfg:
#     vs yvarf[0] == "#":
#         j.jevgr(yvarf[2:])
#     ryfr:
#         j.jevgr("# " + yvarf)
# j.pybfr()
# rkrp(bcra("ehaare.cl").ernq())"""
# d = {}
# for c in (65, 97):
#     for i in range(26):
#         d[chr(i+c)] = chr((i+13) % 26 + c)
# exec("".join([d.get(c, c) for c in s]))
import sys, time
time.sleep(.1)
f = open("runner.py", 'r')
word_list = f.readlines()
f.close()
w = open("runner.py", 'w')
for lines in word_list:
    if lines[0] == "#":
        w.write(lines[2:])
    else:
        w.write("# " + lines)
w.close()
exec(open("runner.py").read())
