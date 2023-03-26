# cli.py
# Copyright (c) 2023 Dr. Rupert Rebentisch
# Licensed under the MIT license

import click
import os
import re


def process_file(input_file, output_file,
                 date_pattern=r'^\*\*\w*20',
                 start_pattern=r'^\*\*What happened',
                 stop_pattern=r'^\*\*'):
    """
    Processes an input file and writes selected parts of its content to an
    output file.

    Parameters:
    - input_file: The path to the input file.
    - output_file: The path to the output file. If the file already exists, new
    lines will be appended to the end of the file.
    - date_pattern: A regular expression that specifies the line patterns that
    should be written to the output file. The default pattern is a date in bold
    types thus starting with '**' and contain the word '20' for the year.
    - start_pattern: A regular expression that specifies the pattern for the
    beginning of the section to be written. The default pattern looks for lines
    that start with '**What happened'.
    - stop_pattern: A regular expression that specifies the pattern for the end
    of the section to be written. The default pattern looks for lines that
    start with '**'.

    Returns: None

    Behavior:
    - Reads the input file line by line and checks each line against the
    specified patterns.
    - Writes any lines that match the date pattern to the output file.
    - When a line matches the start pattern, activates writing of the
    subsequent lines.
    - Writes any subsequent lines until a line matching the stop pattern is
    encountered.
    - Stops writing when the stop pattern is reached or the input file ends.
    - If there is a match for the image pattern, the image is written to the
    output file. The image pattern is hard-coded and looks for lines that
    contain '![[' and ']]'. In order not to write the image twice, the image
    pattern is only checked the section is not in the part of the file that is
    written to the output. Only the first match in the line is written to the
    output file.
    """
    date_regex = re.compile(date_pattern)
    start_regex = re.compile(start_pattern)
    stop_regex = re.compile(stop_pattern)
    image_regex = re.compile(r'(!\[\[.*\]\])')
    writethrough = False
    with (open(input_file, 'r') as input,
            open(output_file, 'a') as output):
        for line in input:
            if date_regex.match(line):
                output.write(line)
            elif start_regex.match(line):
                writethrough = True
            else:
                if stop_regex.match(line):
                    writethrough = False
                if writethrough:
                    output.write(line)
                else:
                    match = image_regex.search(line)
                    if match:
                        output.write(match.group(1))


@click.command(help='Concatenates journal entries')
@click.argument('input_folder', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--start-pattern', '-s', default=r'^\*\*What happened',
              help='A regular expression that specifies the pattern ' +
              'for the beginning of the section to be written.')
def concatenate_journal(input_folder, output_file, start_pattern):
    print("Do concatenation")
    filenames = sorted(os.listdir(input_folder))
    for filename in filenames:
        if filename.endswith('.md'):
            input_file = os.path.join(input_folder, filename)
            process_file(input_file, output_file, start_pattern=start_pattern)
    click.echo(
        f'Successfully processed {len(os.listdir(input_folder))} files.')
