import sys

if len(sys.argv) == 1:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        if not sys.argv[i].endswith("ism"):
            print(sys.argv[i] + "ism")
