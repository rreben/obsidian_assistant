# app.py
# Copyright (c) 2022 Dr. Rupert Rebentisch
# Licensed under the MIT license


from . import cli
import logging


class ObsidianAssitant:

    @staticmethod
    def run():
        cli.concatenate_journal()
