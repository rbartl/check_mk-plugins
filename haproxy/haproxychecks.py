# Example checks for the HAProxy plugin
checks = [

    #server, fieldname, warning, critical, reverse
    ['.*BACKEND', 'act', '1', '1', True],
    ['.*', 'scur', '250', '500', False],
    ['.*', 'chkfail', '15', '25', False],
    ['.*', 'act', '0', '0', True],
    ['.*', 'status', '', '', False] # status stays at the end, just for formatting purposes
]

if __name__ == "__main__":
        print "This file is not meant to be called directly"

