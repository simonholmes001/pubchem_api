=====
Usage
=====

To use pubchem_api in a project::

    import pubchem_api
    from pubchem_api import pubchem_api

In this script, the PubChem REST API has been broken into six parts:

- the base_url: the base url of the PubChem REST API call `https://pubchem.ncbi.nlm.nih.gov/rest/pug/`_
- the compound_cid_selector: instructions to pubchem to run the call based on the compounds unique compound identifier (cid)
- the search_id: the compound cid of the molecule(s) to be retrieved from PubChem
- the property: indicates to PubChem that a physical-chemical property will be requested
- the output_property: identifier for PubChem for the chemical property to be retrieved
- the output_format: identifier for PubChem to return the data in a given format (see `README.md`_)

.. _https://pubchem.ncbi.nlm.nih.gov/rest/pug/: https://pubchem.ncbi.nlm.nih.gov/rest/pug/
.. _README.md: https://github.com/simonholmes001/pubchem_api/blob/master/README.md

Where as the base_url cannot change, the remaining five parameters can be changed in function to what
one is searching for.

A final parameter, output_file_name, sets the file name for saving the data.

Example 1: request a single property from one single molecule::

        import pubchem_api
        from pubchem_api import pubchem_api
        base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"
        compound_cid_selector = "compound/cid/"
        search_id = "6322/" # compound cid for molecule in question
        property = "property/"
        output_property = "MolecularWeight/" # indicates that we will retrieve the molecular weight for compound 6322
        output_format = "CSV" # output format from the REST API call
        output_file_name = "test_data" # output data will be saved as 'test_data.csv'

Once set-up, the script can be called by running::

        pubchem_api.ApiGetFeatures(base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name)

Example 2: request a multiple properties from one multiple molecules simultaneously::

        import pubchem_api
        from pubchem_api import pubchem_api
        base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
        compound_cid_selector = "compound/cid/"
        cid_list = ["6322", "5962", "5960","33032", "5961", "6267", "6274", "5951", "6288", "5862", "6305",
                    "6057", "6137", "5950", "6306", "6106", "6140", "6287", "614", "750"] # list of molecules to retrieve simultanesouly
        search_id = = ','.join(cid_list)+"/" # concatenation of molecule cid's
        property = "property/"
        property_list = ["MolecularWeight", "XLogP", "TPSA", "Complexity", "HBondDonorCount", "HBondAcceptorCount",
                     "RotatableBondCount", "HeavyAtomCount", "AtomStereoCount", "DefinedAtomStereoCount", "Volume3D", "XStericQuadrupole3D",
                     "YStericQuadrupole3D", "ZStericQuadrupole3D", "FeatureCount3D", "FeatureAcceptorCount3D", "FeatureDonorCount3D",
                     "FeatureAnionCount3D", "FeatureCationCount3D", "FeatureRingCount3D", "FeatureHydrophobeCount3D", "ConformerModelRMSD3D",
                     "EffectiveRotorCount3D", "ConformerCount3D"] # list of properties to retrieve for all molecules given above
        output_property = = ','.join(property_list)+"/" # indicates that we will retrieve all of the above chemical properties for all compounds
        output_format = "CSV" # output format from the REST API call
        output_file_name = "test_data" # output data will be saved as 'test_data.csv'

Once set-up, the script can be called by running::

        pubchem_api.ApiGetFeatures(base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name)

In both cases the retrieved data will be saved to a file called test_data.csv in the directory from which pubchem_api
was run.
