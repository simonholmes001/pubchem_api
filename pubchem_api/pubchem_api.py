"""Main module."""
import requests

class api_get_features:

    def __init__(self, base, input_1, i, input_2, j, output_format):
        self.base = base
        self.input_1 = input_1
        self.input_2 = input_2
        self.i = i
        self.input_2 = input_2
        self.j = j
        self.output_format = output_format

        request_api_data = requests.get(self.base+self.input_1+self.i+self.input_2+self.j+self.output_format)
        print("The HTTP status code for this request is: {}.".format(request_api_data.status_code))

        with open("./data/amino_acid_features.csv", "wb") as f:
            f.write(request_api_data.content)
