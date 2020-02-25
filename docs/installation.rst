.. highlight:: shell

============
Installation
============


Stable release
--------------

This is NOT an official API call from PubChem.

To install pubchem_api, run this command in your terminal:

.. code-block:: console

    $ pip install pubchem_api

This is the preferred method to install pubchem_api, as it will always install the most recent stable release.

Once installed by pip, run in python

.. code-block:: console

    >>> from pubchem_api import pubchem_api

In this script, the PubChem REST API has been broken into six parts:

- the base_url: the base url of the PubChem REST API call `https://pubchem.ncbi.nlm.nih.gov/rest/pug/`_
- the compound_cid_selector: instructions to pubchem to run the call based on the compounds unique
compound identifier (cid)
- the search_id: the compound cid of the molecule(s) to be retrieved from PubChem
- the property: indicates to PubChem that a physical-chemical property will be requested
- the output_property: identifier for PubChem for the chemical property to be retrieved
- the output_format: identifier for PubChem to return the data in a given format (see README.md)

.. _https://pubchem.ncbi.nlm.nih.gov/rest/pug/: https://pubchem.ncbi.nlm.nih.gov/rest/pug/

Where as the base_url cannot change, the remaining five parameters can be changed in function to what
one is searching for.

A final parameter, output_file_name, sets the file name for saving the data.

Example 1: request a single property from one single molecule

.. code-block:: console

    >>> from pubchem_api import pubchem_api

    >>> base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"
    >>> compound_cid_selector = "compound/cid/"
    >>> search_id = "6322/" # compound cid for molecule in question
    >>> property = "property/"
    >>> output_property = "MolecularWeight/" # indicates that we will retrieve the molecular weight for compound 6322
    >>> output_format = "CSV" # output format from the REST API call
    >>> output_file_name = "test_data" # output data will be saved as 'test_data.csv'

Once set-up, the script can be called by running

.. code-block:: console

    >>> pubchem_api.ApiGetFeatures(base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name)

Example 2: request a multiple properties from one multiple molecules simultaneously

.. code-block:: console

    >>> from pubchem_api import pubchem_api

    >>> base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"
    >>> compound_cid_selector = "compound/cid/"
    >>> cid_list = ["6322", "5962", "5960","33032", "5961", "6267", "6274", "5951", "6288", "5862", "6305",
                    "6057", "6137", "5950", "6306", "6106", "6140", "6287", "614", "750"] # list of molecules to retrieve simultanesouly
    >>> search_id = = ','.join(cid_list)+"/" # concatenation of molecule cid's
    >>> property = "property/"
    >>> property_list = ["MolecularWeight", "XLogP", "TPSA", "Complexity", "HBondDonorCount", "HBondAcceptorCount",
                     "RotatableBondCount", "HeavyAtomCount", "AtomStereoCount", "DefinedAtomStereoCount", "Volume3D", "XStericQuadrupole3D",
                     "YStericQuadrupole3D", "ZStericQuadrupole3D", "FeatureCount3D", "FeatureAcceptorCount3D", "FeatureDonorCount3D",
                     "FeatureAnionCount3D", "FeatureCationCount3D", "FeatureRingCount3D", "FeatureHydrophobeCount3D", "ConformerModelRMSD3D",
                     "EffectiveRotorCount3D", "ConformerCount3D"] # list of properties to retrieve for all molecules given above
    >>> output_property = = ','.join(property_list)+"/" # indicates that we will retrieve all of the above chemical properties for all compounds
    >>> output_format = "CSV" # output format from the REST API call
    >>> output_file_name = "test_data" # output data will be saved as 'test_data.csv'

Once set-up, the script can be called by running

.. code-block:: console

    >>> pubchem_api.ApiGetFeatures(base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name)


If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for pubchem_api can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/simonholmes001/pubchem_api

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/simonholmes001/pubchem_api/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/simonholmes001/pubchem_api
.. _tarball: https://github.com/simonholmes001/pubchem_api/tarball/master
