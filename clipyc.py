import argparse
import json
import csv


# parser = argparse.ArgumentParser(description="Calculate the area of a trapezoid.")
# parser.add_argument(
#     '-b', "--base", type=int, help="first base of the trapezoid.", metavar=""
# )
# parser.add_argument(
#     '-B', "--Base", type=int, help="second base of the trapezoid.", metavar=""
# )
# parser.add_argument(
#     '-H', "--height", type=int, help="height of the trapezoid.", metavar=""
# )
# group = parser.add_mutually_exclusive_group()
# group.add_argument('-q', "--quiet", action="store_true", help="print quiet")
# group.add_argument('-v', "--verbosa", action= "store_true", help="print verbosa")
# args = parser.parse_args()


# def trapezoid_area(base, Base, height):
#     area = ((base + Base) / 2) * height
#     return area


# if __name__ == "__main__":
#     area = trapezoid_area(args.base, args.Base, args.height)
#     if args.quiet:
#         print(area)
#     elif args.verbosa:
#         print("The first base is %s, the second BASE is %s, the height is %s, and finally the area is %s" % (args.base, args.Base, args.height, area))
#     else:
#         print("Area of a trapezoid is: %s" % area)
