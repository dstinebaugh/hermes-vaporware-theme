# SPDX-License-Identifier: MIT
# Copyright (c) 2026 dstinebaugh
"""Inert Hermes Agent entrypoint for a Desktop-only theme pack.

The theme is registered by desktop/plugin.js inside Hermes Desktop. Hermes Agent
imports every installed plugin directory through this module; keeping it inert
satisfies the plugin contract and registers no tools, hooks or settings.
"""


def register(ctx):
    """Satisfy Hermes Agent's plugin contract without registering capabilities."""
    del ctx
