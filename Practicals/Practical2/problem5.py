import argparse

parser=argparse.ArgumentParser()

#Arguments----------------------
#start 
parser.add_argument("str",help="string")
#end----------------------------

arguments=parser.parse_args()

#beginning------------------------------
inp_upper=arguments.str.upper()
inp_lower=arguments.str.lower()

print("The given string:",arguments.str,"\nAll lowercase:",inp_lower,"\nAll uppercase:",inp_upper)

