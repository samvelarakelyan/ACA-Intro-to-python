import argparse


parser=argparse.ArgumentParser(prog="problem3")

#Arguments---------------------------------
#start
parser.add_argument("name",help="'name' is a positional argument for %(prog)s program")
#end---------------------------------------

args=parser.parse_args() 

#beginning---------------------------------
print("Welcome "+args.name+"!")
  






