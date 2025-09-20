#!/usr/bin/env python
"""
Command-line entry point for the Archival Service management.

This script provides a CLI for managing the archival process,
including checking status, retrieving statistics, and triggering archival operations.
"""

import sys
import os

# Add the parent directory to the path so we can import the app package
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app.cli import cli

if __name__ == "__main__":
    cli()
