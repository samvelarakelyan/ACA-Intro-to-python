import argparse


parser=argparse.ArgumentParser(prog="problem4")

#Arguments--------------------------
#start
parser.add_argument("--age",type=int,help="this is a optional argumen for %(prog)s program")
#end--------------------------------

arguments=parser.parse_args()

#beginning-------------------------
print("Happy Birthday, you are already %d years old!" % arguments.age)



