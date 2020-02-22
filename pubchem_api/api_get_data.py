from api_request import api_get_features

base = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/"
input_1 = "compound/cid/"
input_2 = "property/"
output_format = "CSV"

input_dic = ["MolecularWeight", "XLogP", "TPSA", "Complexity", "HBondDonorCount", "HBondAcceptorCount",
             "RotatableBondCount", "HeavyAtomCount", "AtomStereoCount", "DefinedAtomStereoCount", "Volume3D", "XStericQuadrupole3D",
             "YStericQuadrupole3D", "ZStericQuadrupole3D", "FeatureCount3D", "FeatureAcceptorCount3D", "FeatureDonorCount3D",
             "FeatureAnionCount3D", "FeatureCationCount3D", "FeatureRingCount3D", "FeatureHydrophobeCount3D", "ConformerModelRMSD3D",
             "EffectiveRotorCount3D", "ConformerCount3D"]

amino_acid_cid = ["6322", "5962", "5960","33032", "5961", "6267", "6274", "5951", "6288", "5862", "6305",
                  "6057", "6137", "5950", "6306", "6106", "6140", "6287", "614", "750"]

dic_amino_acids = {
    "arginine":"6322", "lysine":"5962", "aspartic acid":"5960","glutamic acid":"33032",
    "glutamine":"5961", "asparagine":"6267", "histidine":"6274", "serine":"5951", "threonine":"6288",
    "cysteine":"5862", "tryptophan":"6305", "tyrosine":"6057", "methionine":"6137", "alanine":"5950",
    "isoleucine":"6306", "leucine":"6106", "phenylalanine":"6140", "valine":"6287", "proline":"614",
    "glycine":"750"
}

output_format_list = ["XML", "JSON", "JSONP", "CSV", "PNG", "TXT"]

i = ','.join(amino_acid_cid)+"/"
j = ','.join(input_dic)+"/"

amino_acid_data = api_get_features(base, input_1, i, input_2, j, output_format)