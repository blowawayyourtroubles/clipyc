import argparse
import json
import csv


parser = argparse.ArgumentParser()
parser.add_argument("-a", "add", type= str, help="Add a new task to the list.", metavar="")
parser.add_argument("-rmv", "remove", type= str, help="Remove a task to the list.", metavar="")
parser.add_argument("--sort", type= str, help="Sort the tasks.", metavar="")
parser.add_argument("--filter", type= str, help="Remove a new task to the list.", metavar="")
