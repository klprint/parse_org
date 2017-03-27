def read_org(filepath):
    readfile = []
    with open(filepath, 'r') as fopen:
        for line in fopen:
            readfile.append(line)
    return(readfile)


def process_org(orgList):
    processed = []
    for line in orgList:
        lineSplit = line.rstrip().split()

        # Start figure environment if #+TITLE appears and two lines after that, the line starts with '[', which indicates a link to a figure.
        if lineSplit[0] == '#+TITLE':
            line = '
