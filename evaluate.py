from train import Model
import sys

model = Model()
if len(sys.argv) > 1:
    model.examples(int(sys.argv[1]))
else:
    model.examples()
