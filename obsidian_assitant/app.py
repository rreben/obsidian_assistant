# app.py
# Copyright (c) 2023 Dr. Rupert Rebentisch
# Licensed under the MIT license


from . import cli


class ObsidianAssitant:

    @staticmethod
    def run():
        cli.concatenate_journal()
