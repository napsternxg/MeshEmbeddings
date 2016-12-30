# coding: utf-8
import re

mesh_clean = dict()
id2term = dict()

with open("data/mtrees2015.bin") as fp:
    i = 0
    for line in fp:
        word, mid = line.strip().split(";")
        if word not in mesh_clean:
            mesh_clean[word] = set([])
        mesh_clean[word].add(mid)
        id2term[mid] = word
        i += 1

nodeids = dict(reversed(k) for k in enumerate(mesh_clean.keys()))
id2node = dict(k for k in enumerate(mesh_clean.keys()))

def get_parents(x):
    mids = mesh_clean[x]
    parents = set([])
    for mid in mids:
        mid = mid.split(".")
        pids = [".".join(mid[:i+1]) for i in xrange(len(mid)-1)]
        parents = parents.union(set([id2term[k] for k in pids]))
    return parents

if __name__ == "__main__":
  with open("out/mesh_nodeids.txt", "wb+") as fp:
    for k in nodeids.iteritems():
      print >> fp, "%s\t%s" % k

  with open("out/mesh_network.txt", "wb+") as fp:
      for m in mesh_clean:
          nearest_parents = set([id2term[k.rsplit(".",1)[0]] for k in mesh_clean[m] if len(k.rsplit(".",1)) == 2])
          for np in nearest_parents:
              print >> fp, "%s\t%s\t1" % (nodeids[np], nodeids[m])
            
