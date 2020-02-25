"""
Main module
base_url: the base url of the PubChem REST API call
compound_cid_selector: instructions to pubchem to run the call based on the compounds unique
compound identifier (cid)
search_id: the compound cid of the molecule(s) to be retrieved from PubChem
property: indicates to PubChem that a physical-chemical property will be requested
output_property: identifier for PubChem for the chemical property to be retrieved
output_format: identifier for PubChem to return the data in a given format (see README.md)
output_file_name: name used for output file
"""
import requests

class ApiGetFeatures:

    def __init__(self, base_url, compound_cid_selector, search_id, property, output_property, output_format, output_file_name):
        self.base_url = base_url
        self.compound_cid_selector = compound_cid_selector
        self.search_id = search_id
        self.property = property
        self.output_property = output_property
        self.output_format = output_format
        self.output_file_name = output_file_name

        request_api_data = requests.get(self.base_url + self.compound_cid_selector + self.search_id + self.property + self.output_property + self.output_format)

        print("The HTTP status code for this request is: {}.".format(request_api_data.status_code))

        with open(output_file_name+".txt", "w") as f:
           f.write("status code is {}.".format(str(request_api_data.status_code)))

        with open(output_file_name+".csv", "wb") as f:
            f.write(request_api_data.content)

