#!/usr/bin/env python
"""
 This module reads a specified .cmp file generated by kicad and creates
 a csv file that contains extracted data.
"""

import argparse

def cmp_extract_info(component):
    'Extract and return component data'
    description = component.split('\n')
    reference = ''
    value = ''
    footprint = ''

    if(len(description) > 3):
        reference = description[1][12:-1]
        value = description[2][12:-1]
        footprint = description[3][12:-1]

    return reference, value, footprint


if __name__ == "__main__":
    'Where the magic happens'
    # Arguments parsing
    parser = argparse.ArgumentParser(description='Convert kicad cmp file to a BOM')
    parser.add_argument('filename_input', metavar='Fin', type=str, \
                        help='Input file name')
    args = parser.parse_args()

    # Open input cmp file
    filename_input = args.filename_input
    f_in = open(filename_input, 'r')
    # Open output csv file
    filename_output = '%s-bom.csv' % filename_input.split('.')[0]
    f_out = open(filename_output, 'w')

    # Split components
    cmp_list = f_in.read().split('BeginCmp\n')

    f_out.write('Reference,Value,Kicad Footprint\n')
    for component in cmp_list:
        # Extract component reference and value
        reference, value, footprint = cmp_extract_info(component)

        # Write info to csv file
        if(reference != '' and value != ''):
            description = '%s,%s,%s\n' % (reference, value, footprint)
            f_out.write(description)
