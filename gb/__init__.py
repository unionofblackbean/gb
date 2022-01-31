"""
MCDR Git Backup Plugin entrypoint module.
"""

from mcdreforged.api import types


def on_load(server: types.PluginServerInterface, prev_mod) -> None:
    del server, prev_mod  # Unused.
