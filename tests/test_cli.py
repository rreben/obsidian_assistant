from obsidian_assitant import *
from click.testing import CliRunner


def test_cli():
    runner = CliRunner()
    result = runner.invoke(concatenate_journal, [])
    assert result.exit_code == 0
    assert 'concatenation' in result.output
    return runner
