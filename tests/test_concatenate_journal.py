# test_concatenate_journal.py
# Copyright (c) 2023 Dr. Rupert Rebentisch
# Licensed under the MIT license

import os
import datetime
import shutil
import pytest
from obsidian_assitant import *

@pytest.fixture
def test_input_folder(tmpdir):
    # Erstelle Testdateien im Eingabeverzeichnis
    input_folder = tmpdir.mkdir('input_folder')
    filename = f'2023-03-16.md'
    filepath = input_folder.join(filename)
    with open(str(filepath), 'w') as f:
        f.write(f'#{filename}\n\nWHAT HAPPENED TODAY?\n\nText for {filename}\n\n')

    # Gib den Pfad zu den Testdateien zurück
    yield str(input_folder)

    # Lösche die Testdateien
    shutil.rmtree(str(input_folder))


@pytest.fixture
def example_file_path():
    return os.path.join(os.path.dirname(__file__), '2023-03-13.md')

def test_process_file(test_input_folder):
    input_folder = test_input_folder

    # Rufe das Hauptprogramm auf, um die Ausgabedatei zu erstellen
    process_file(os.path.join(input_folder, '2023-03-16.md'), 'output.md')

    # Prüfe, ob die Ausgabedatei erstellt wurde
    assert os.path.exists('output.md')

    # Prüfe, ob der Text in der Ausgabedatei korrekt ist
    with open('output.md', 'r') as f:
        content = f.read()
        assert 'Text for' in content
        assert '2023-03-16' in content

    # Lösche die Ausgabedatei
    os.remove('output.md')


def test_process_file_next(example_file_path):
    input_folder = test_input_folder

    # Rufe das Hauptprogramm auf, um die Ausgabedatei zu erstellen
    process_file(example_file_path, 'output.md')

    # Prüfe, ob die Ausgabedatei erstellt wurde
    assert os.path.exists('output.md')

    # Prüfe, ob der Text in der Ausgabedatei korrekt ist
    with open('output.md', 'r') as f:
        content = f.read()
        assert 'HH diverse' in content
        assert 'Something happened today' in content

    # Lösche die Ausgabedatei
    os.remove('output.md')
