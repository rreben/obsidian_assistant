# cli.py
# Copyright (c) 2023 Dr. Rupert Rebentisch
# Licensed under the MIT license

import click


def process_file(filepath, output_file):
    with open(filepath, 'r') as i: 
        file_content = i.read()
    with open(output_file, 'a') as o:
        o.write(file_content)


@click.command(help='concatenates journal entries')
def concatenate_journal():
    print ("Do concatenation")
