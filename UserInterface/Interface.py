#!/usr/local/bin/python3
# encoding: utf-8
'''
UserInterface.Interface -- shortdesc

UserInterface.Interface is a description

It defines classes_and_methods

@author:     user_name
        
@copyright:  2013 organization_name. All rights reserved.
        
@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

__all__ = []
__version__ = 0.1
__date__ = '2013-09-08'
__updated__ = '2013-09-08'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''
    
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by user_name on %s.
  Copyright 2013 organization_name. All rights reserved.
  
  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0
  
  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument('-V', '--version', action='version', version=program_version_message)
#         parser.add_argument(dest="paths", help="paths to folder(s) with source file(s) [default: %(default)s]", metavar="path", nargs='+')
        
        parser.add_argument("-p", "--protocol", dest="protocol", nargs="*",default="DNS",help="the protocol to sniff for, defaults to DNS, which includes all supported protocols")
        parser.add_argument("snifferAddress", help="the remote address(IP) of the sniffer you want to connect to")
        parser.add_argument("-H","--historic",action="store_true",help="retrieve earlier collected data?")
        # Process arguments
        args = parser.parse_args()
        
#         paths = args.paths
        verbose = args.verbose
        protocol = args.protocol
        sniffer  = args.sniffer
        historic = args.historic
        
        if verbose > 0:
            print("Verbose mode on")
            if historic:
                print("Historic mode on")
            else:
                print("Historic mode off")
        
        
        for p in protocol:
            ### do something with inpath ###
            print(p)
        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " +repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-h")
#         sys.argv.append("snifferAddress")
#         sys.argv.append("127.0.0.1")
        sys.argv.append("-H")
    if TESTRUN:
        import doctest
        doctest.testmod()
    sys.exit(main())