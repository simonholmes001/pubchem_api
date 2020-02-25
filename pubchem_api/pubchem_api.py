"""Main module."""
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

