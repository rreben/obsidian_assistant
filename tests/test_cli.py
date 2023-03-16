# test_cli.py
# Copyright (c) 2023 Dr. Rupert Rebentisch
# Licensed under the MIT license

from obsidian_assitant import *
from click.testing import CliRunner


def test_cli():
    runner = CliRunner()
    result = runner.invoke(concatenate_journal, ['--help'])
    assert result.exit_code == 0
    assert 'Concatenates journal entries' in result.output
    assert 'Show this message and exit' in result.output
    return runner
