# test_concatenate_journal.py
# Copyright (c) 2023 Dr. Rupert Rebentisch
# Licensed under the MIT license

import os
import pytest
from obsidian_assitant import process_file


@pytest.fixture
def test_files_path():
    return os.path.join(os.path.dirname(__file__), 'test_files')


def test_process_complete_file(test_files_path):
    test_folder = test_files_path

    # Example Datei 2023-03-13.md enthält alle Abschnitte
    process_file(os.path.join(test_folder, '2023-03-13.md'), 'output.md')
    assert os.path.exists('output.md')
    with open('output.md', 'r') as f:
        content = f.read()
        assert '2023-03-13' in content
        assert 'HH diverse' not in content
        assert 'Something happened today' in content
        assert 'What have you learned today' not in content
        assert 'Ich habe etwas gelernt' not in content
    os.remove('output.md')


def test_process_complete_file_no_regex(test_files_path):
    test_folder = test_files_path

    # Example Datei 2023-03-13.md enthält alle Abschnitte
    process_file(os.path.join(test_folder, '2023-03-13.md'),
                 'output.md',
                 start_pattern='^\*\*',  # noqa W605
                 stop_pattern='^xxx')
    assert os.path.exists('output.md')
    with open('output.md', 'r') as f:
        content = f.read()
        assert '2023-03-13' in content
        assert 'HH diverse' in content
        assert 'Something happened today' in content
        assert 'Ich habe etwas gelernt' in content
    os.remove('output.md')


def test_process_complete_file_learnings(test_files_path):
    test_folder = test_files_path

    # Example Datei 2023-03-13.md enthält alle Abschnitte
    process_file(os.path.join(test_folder, '2023-03-13.md'),
                 'output.md',
                 start_pattern='^\*\*What have you learned',  # noqa W605
                 stop_pattern='^\*\*')  # noqa W605
    assert os.path.exists('output.md')
    with open('output.md', 'r') as f:
        content = f.read()
        assert '2023-03-13' in content
        assert 'HH diverse' not in content
        assert 'Something happened today' not in content
        assert 'Ich habe etwas gelernt' in content
    os.remove('output.md')


def test_process_last_paragraphs_missing_file(test_files_path):
    test_folder = test_files_path

    # Example Datei 2023-03-13.md keine nachfolgenden Abschnitte
    process_file(os.path.join(test_folder, '2023-03-14.md'), 'output.md')
    assert os.path.exists('output.md')
    with open('output.md', 'r') as f:
        content = f.read()
        assert '2023-03-14' in content
        assert 'HH diverse' not in content
        assert 'Something happened today' in content
        assert 'Ich habe etwas gelernt' not in content
    os.remove('output.md')


def test_process_missing_paragrpaph_file(test_files_path):
    test_folder = test_files_path

    # Example Datei 2023-03-13.md keine nachfolgenden Abschnitte
    process_file(os.path.join(test_folder, '2023-03-12.md'), 'output.md')
    assert os.path.exists('output.md')
    with open('output.md', 'r') as f:
        content = f.read()
        assert '2023-03-12' in content
        assert 'HH diverse' not in content
        assert 'Something happened today' not in content
        assert 'Ich habe etwas gelernt' not in content
    os.remove('output.md')


def test_process_appended_image(test_files_path):
    test_folder = test_files_path

    # Example Datei 2023-03-15.md hat am Ende ein Bild angehängt
    process_file(os.path.join(test_folder, '2023-03-15.md'), 'output.md')
    assert os.path.exists('output.md')
    with open('output.md', 'r') as f:
        content = f.read()
        assert '2023-03-15' in content
        assert 'HH diverse' not in content
        assert 'Something happened today' not in content
        assert 'Ich habe etwas gelernt' not in content
        assert '![[8EF7446A-7462-4043-BD68-1C997F24682F.jpeg]]' in content
    os.remove('output.md')


def test_process_just_image(test_files_path):
    test_folder = test_files_path

    # Example Datei 2023-03-16.md nur einen Link auf ein Bild
    process_file(os.path.join(test_folder, '2023-03-16.md'), 'output.md')
    assert os.path.exists('output.md')
    with open('output.md', 'r') as f:
        content = f.read()
        assert '2023-03-16' not in content
        assert 'HH diverse' not in content
        assert 'Something happened today' not in content
        assert 'Ich habe etwas gelernt' not in content
        assert '![[dummy.png]]' in content
    os.remove('output.md')


def test_process_learnigs(test_files_path):
    test_folder = test_files_path

    # Example Datei 2023-03-16.md nur einen Link auf ein Bild
    process_file(os.path.join(test_folder, '2023-03-12.md'),
                 'output.md',
                 start_pattern='^\*\*What have you learned',  # noqa W605
                 stop_pattern='^\*\*')  # noqa W605
    assert os.path.exists('output.md')
    with open('output.md', 'r') as f:
        content = f.read()
        assert '2023-03-12' in content
        assert 'Ich habe etwas gelernt' in content
        assert '![[dummy.png]]' not in content
    os.remove('output.md')
