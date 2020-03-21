import argparse

parser=argparse.ArgumentParser()

#Arguments-----------------------
#start
parser.add_argument("text",help="string")
parser.add_argument("index1",type=int,help="start index")
parser.add_argument("index2",type=int,help="End index")
#end------------------------------

args=parser.parse_args()

#beginning-----------------
output=args.text[args.index1:args.index2]

print("The given text:",args.text)
print("Start index:",args.index1)
print("End index:",args.index2)
print("Output string:",output)


