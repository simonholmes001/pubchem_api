#!/usr/bin/env python

"""Tests for `pubchem_api` package."""


import unittest
from click.testing import CliRunner

from pubchem_api import pubchem_api
from pubchem_api import cli

class TestPubchem_api(unittest.TestCase):
    """Tests for `pubchem_api` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_something(self):
        """Test something."""
        """Test something."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'pubchem_api.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
