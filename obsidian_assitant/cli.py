# cli.py
# Copyright (c) 2023 Dr. Rupert Rebentisch
# Licensed under the MIT license

import click
import os
import re


def process_file(input_file, output_file,
                 date_pattern = r'^\*\*\w*20',
                 start_pattern = r'^\*\*What happened',
                 stop_pattern = r'^\*\*'):
    """
    Processes an input file and writes selected parts of its content to an output file.
    
    Parameters:
    - input_file: The path to the input file.
    - output_file: The path to the output file. If the file already exists, new lines will be appended to the end of the file.
    - date_pattern: A regular expression that specifies the line patterns that should be written to the output file. The default pattern is a date in bold types thus starting with '**' and contain the word '20' for the year.
    - start_pattern: A regular expression that specifies the pattern for the beginning of the section to be written. The default pattern looks for lines that start with '**What happened'.
    - stop_pattern: A regular expression that specifies the pattern for the end of the section to be written. The default pattern looks for lines that start with '**'.
    
    Returns: None
    
    Behavior:
    - Reads the input file line by line and checks each line against the specified patterns.
    - Writes any lines that match the date pattern to the output file.
    - When a line matches the start pattern, activates writing of the subsequent lines.
    - Writes any subsequent lines until a line matching the stop pattern is encountered.
    - Stops writing when the stop pattern is reached or the input file ends.
    """
    date_regex = re.compile(date_pattern)
    start_regex = re.compile(start_pattern)
    stop_regex = re.compile(stop_pattern)
    writethrough = False
    with (open(input_file, 'r') as input,
        open(output_file, 'a') as output):
        for line in input:
            if date_regex.match(line):
                output.write(line)
            elif start_regex.match(line):
                writethrough = True
            else:
                if writethrough:
                    output.write(line)
                if stop_regex.match(line):
                    writethrough = False


@click.command(help='Concatenates journal entries')
@click.argument('input_folder', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def concatenate_journal(input_folder, output_file):
    print ("Do concatenation")
    for filename in os.listdir(input_folder):
        if filename.endswith('.md'):
            input_file = os.path.join(input_folder, filename)
            process_file(input_file, output_file)
    click.echo(
        f'Successfully processed {len(os.listdir(input_folder))} files.')
