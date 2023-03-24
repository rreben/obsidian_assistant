# test_cli.py
# Copyright (c) 2023 Dr. Rupert Rebentisch
# Licensed under the MIT license

from obsidian_assitant import *
from click.testing import CliRunner


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(concatenate_journal, ['--help'])
    assert result.exit_code == 0
    assert 'Concatenates journal entries' in result.output
    assert 'INPUT_FOLDER' in result.output
    assert 'OUTPUT_FILE' in result.output
    assert 'specifies the pattern' in result.output
    assert 'Show this message and exit' in result.output
    return runner


def test_cli_non_existing_path():
    runner = CliRunner()
    result = runner.invoke(concatenate_journal, ['/no_existing_folder', '/no_existing_folder/output.md'])
    assert result.exit_code == 2
    assert 'Error' in result.output
    assert 'does not exist' in result.output
    return runner
