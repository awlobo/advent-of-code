import os, glob, imp

modules = {}

for path in glob.glob('y2019/[!_]*.py'):
    name, ext = os.path.splitext(os.path.basename(path))
    modules[name] = imp.load_source(name, path)