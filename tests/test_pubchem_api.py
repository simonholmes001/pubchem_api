#!/usr/bin/env python

"""Tests for `pubchem_api` package."""

import os

import requests
import unittest
from click.testing import CliRunner

from pubchem_api import pubchem_api
from pubchem_api import cli

from unittest import mock

class TestPubchem_api(unittest.TestCase):
    """Tests for `pubchem_api` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_API_call_ok(self):
        """
        Test that simple API call returns a 200 status code.
        Test that the concatenation of the base_url+compound_cid_selector+search_id+
        property+output_property+output_format gives a URL REST API call that can
        be performed succesfully.
        If true, pubchem_api.ApiGetFeatures generates a text file containing the HTML
        response code (200 if successful).
        Assert command validates this.
        By products of the test (.txt file & .csv file) are deleted after the test has ran.
        base_url: the base url of the PubChem REST API call
        compound_cid_selector: instructions to pubchem to run the call based on the compounds unique
        compound identifier (cid)
        search_id: the compound cid of the molecule(s) to be retrieved from PubChem
        property: indicates to PubChem that a physical-chemical property will be requested
        output_property: identifier for PubChem for the chemical property to be retrieved
        output_format: identifier for PubChem to return the data in a given format (see README.md)
        output_file_name: name used for output file
        """
        base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"
        compound_cid_selector = "compound/cid/"
        search_id = "6322/"
        property = "property/"
        output_property = "MolecularWeight/"
        output_format = "CSV"
        output_file_name = "test_data"

        pubchem_api.ApiGetFeatures(base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name)

        with open(output_file_name+".txt", "r") as f:
            contents = f.read()
            assert(contents == "status code is 200.")

        os.remove(output_file_name+".txt")
        os.remove(output_file_name+".csv")

    # def test_002_mock_is_ok(self):
    #     """Mock testing"""
    #     base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"
    #     compound_cid_selector = "compound/cid/"
    #     search_id = "6322/"
    #     property = "property/"
    #     output_property = "MolecularWeight/"
    #     output_format = "CSV"
    #     output_file_name = "test_data"
    #     with mock.patch('requests.get') as mocker:
    #         resp_mock = mock.NonCallableMagicMock(spec_set = requests.Response())
    #         resp_mock.url  = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6322/property/MolecularWeight/CSV'
    #         resp_mock.status_code = 200
    #         mocker.return_value = resp_mock
    #
    #         resp = requests.get(pubchem_api.ApiGetFeatures(base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name))
    #
    #         assert resp.status_code == 200
    #         assert resp.url == 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6322/property/MolecularWeight/CSV'
    #         assert mocker.called

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'pubchem_api.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
