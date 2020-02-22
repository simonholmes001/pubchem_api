# Extract Data on Amino Acids Programmatically from the PubChem database

URL for the PubChem data base: https://pubchem.ncbi.nlm.nih.gov/

## Introduction

(Source: https://pubchemdocs.ncbi.nlm.nih.gov/about)

Launched in 2004, PubChem is one of the largest (perhaps the largest) open databases of chemical information. PubChem contains information mainly on small molecules, but also contains information on macromolecules such as nucleotides, carbohydrates, peptides and lipids. PubChem also contains many sources of information, such as information on ligand binding, biological activity, drug activity and toxicity.

As of the time of writing (Feb, 2020), PubChem contained the following information (source: https://pubchemdocs.ncbi.nlm.nih.gov/statistics):

| Data Collection | Count           | 
| ------------- |:-------------:| 
| Compounds      | 102,596,715 | 
| BioAssays     | 1,067,886      | 
| Bioactivities | 268,416,564     |
| Genes | 58,029      |   
| Proteins | 11,847      |
| Literature | 30,602,935      |
| Data Srouces | 719        |

## Amino Acids

(Source: https://en.wikipedia.org/wiki/Amino_acid)

Amino acids are the monomers that, when chemically joined together, create polypeptides and proteins. There are about 500 amino acids known, although only 22 occur in nature, of which 20 of these are encoded in the genetic material (the remaining two amino acids are encoded by variant codons and their use in nature is rare). 
The &alpha;-carbon of an amino acid is a chiral atom (with the exception of glycine). However, D-isomers are very rare in nature, with the vast majority of amino acids in biological systems
being of the L-format.

As proteins are polymers of amino acids, the 3-dimensional conformations that proteins adopt is determined by the chemical properties of the amino acids that comprise the protein in question.
In order to find algorithms that accurately predict protein 3D shape from the 1D primary sequence of amino acids of a protein, it is pertinent to derive features from the chemical properties 
of the amino acids themselves.

A first step in this process is gathering physical-chemical properties of the amino acids from a reliable source of data, such as the PubChem database.

This repo attempts to provide a programmatic method for collecting physical-chemical information about amino acids directly from the PubChem database,
by exploiting the PUG REST API that PubChem provides.

Amino acid codes:

**Charged (side chains often form salt bridges)**:

| Amino Acid | Three Letter Code | One Letter Code | PubChem Id |
| :-------------: |:-------------:| :-------------:| :-------------:| 
| Arginine      | Arg | R | [6322](https://pubchem.ncbi.nlm.nih.gov/compound/6322) |
| Lysine      | Lys | K | [5962](https://pubchem.ncbi.nlm.nih.gov/compound/5962) |
| Aspartic Acid      | Asp | D | [5960](https://pubchem.ncbi.nlm.nih.gov/compound/5960) |
| Glutamic Acide      | Glu | E | [33032](https://pubchem.ncbi.nlm.nih.gov/compound/33032) |

**Polar (form hydrogen bonds as proton donors or acceptors)**:

| Amino Acid | Three Letter Code | One Letter Code | PubChem Id |
| :-------------: |:-------------:| :-------------:| :-------------:| 
| Glutamine      | Gln | Q | [5961](https://pubchem.ncbi.nlm.nih.gov/compound/5961) |
| Asparagine      | Asn | N | [6267](https://pubchem.ncbi.nlm.nih.gov/compound/6267) |
| Histidine      | His | H | [6274](https://pubchem.ncbi.nlm.nih.gov/compound/6274) |
| Serine      | Ser | S | [5951](https://pubchem.ncbi.nlm.nih.gov/compound/5951) |
| Threonine      | Thr | T | [6288](https://pubchem.ncbi.nlm.nih.gov/compound/6288) |
| Cysteine    | Cys | C | [5862](https://pubchem.ncbi.nlm.nih.gov/compound/5862) |

**Polar (Amphipathic (often found at the surface of proteins or lipid membranes, sometimes also classified as polar)**:

| Amino Acid | Three Letter Code | One Letter Code | PubChem Id |
| :-------------: |:-------------:| :-------------:| :-------------:| 
| Tryptophan      | Trp | W | [6305](https://pubchem.ncbi.nlm.nih.gov/compound/6305) |
| Tyrosine      | Tyr | Y | [6057](https://pubchem.ncbi.nlm.nih.gov/compound/6057) |
| Methionine      | Met | M | [6137](https://pubchem.ncbi.nlm.nih.gov/compound/6137) |

**Hydrophobic (normally buried inside the protein core)**:

| Amino Acid | Three Letter Code | One Letter Code | PubChem Id |
| :-------------: |:-------------:| :-------------:| :-------------:| 
| Alanine      | Ala | A | [5950](https://pubchem.ncbi.nlm.nih.gov/compound/5950) |
| Isoleucine      | Ile | I | [6306](https://pubchem.ncbi.nlm.nih.gov/compound/6306) |
| Leucine     | Leu | L | [6106](https://pubchem.ncbi.nlm.nih.gov/compound/6106) |
| Phenylalanine     | Phe | F | [6140](https://pubchem.ncbi.nlm.nih.gov/compound/6140) |
| Valine | Val | V | [6287](https://pubchem.ncbi.nlm.nih.gov/compound/6287) |
| Proline    | Pro | P | [614](https://pubchem.ncbi.nlm.nih.gov/compound/614) |
| Glycine    | Gly | G | [750](https://pubchem.ncbi.nlm.nih.gov/compound/750) |

## The PubChem REST API Services

(Source: https://pubchemdocs.ncbi.nlm.nih.gov/programmatic-access)

[**PUG REST**](https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest-tutorial) is a web service that supplies specific information on one or more of the PubChem records.

[**PUG-View**](https://pubchemdocs.ncbi.nlm.nih.gov/pug-view) is a service which provides full reports for individual PubChem records.

It is important to remember that PubChem sets rules for the query of their data, failure to respect these rules may result in your account being
temporarily suspended.

#### PUG REST API

(Source: https://pubchemdocs.ncbi.nlm.nih.gov/pug-rest-tutorial)

The fundamental unit upon which PUG REST is built is the PubChem 
identifier, which comes in three flavors – SID for substances, 
CID for compounds, and AID for assays. The conceptual framework 
of this service, that uses these identifiers, is the three-part 
request: 1) input – that is, what identifiers are we talking 
about; 2) operation – what to do with those identifiers; and 3) output – what information should be returned. 

PUG REST is entirely based on HTTP (or HTTPS) requests, and 
most of the details of the request are encoded directly in the 
URL path – which is what makes the service RESTful.

Example of the URL path:

| https://pubchem.ncbi.nlm.nih.gov/rest/pug | /compound/name/vioxx | /property/InChI |/TXT |
 | :-------------: |:-------------:| :-------------:| :-------------:|
| prolog      | input | operation     | output      | 

An example URL API request to query data would be of the form:

https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5950/property/MolecularWeight,XLogP/CSV


## Set-up and Installation

An example of the chemical information that we shall use for each amino acid is
illustrated using the compound alanine. A simple search on the PubChem 
home page gives the compound ID (CID) 5950 and a search of this compound
produces a table containing the following information (excert only, from Section **4 Chemical 
and Physical Properties**, subsection **4.1 Computed Properties**):

| Property Name | Property Vaue |
| ------------- |:-------------:| 
| Molecular Weight      | 89.09 g/mol | 
| XLogP3     | -3      | 
| Hydrogen Bond Donor Count | 2     |
| Hydrogen Bond Acceptor Count | 3      |   
| Rotatable Bond Count | 1      |
| Exact Mass| 89.047678 g/mol    |
| Topological Polar Surface Area | 63.3 A²        |
| ----------------- | ---------------        |

This is the information that we shall extract programmatically from PubChem for 
each amino acid. The information shall be retrieved by quering using the
**Compound Property Tables** below.

#### Compound Property Tables

| Property | Notes |
| :-------------: |:-------------:|  
| MolecularFormula| Molecular formula | 
| MolecularWeight| The molecular weight is the sum of all atomic weights of the constituent atoms in a compound, measured in g/mol. In the absence of explicit isotope labelling, averaged natural abundance is assumed. If an atom bears an explicit isotope label, 100% isotopic purity is assumed at this location |
| CanonicalSMILES| Canonical SMILES (Simplified Molecular Input Line Entry System) string.  It is a unique SMILES string of a compound, generated by a “canonicalization” algorithm | 
| IsomericSMILES| Isomeric SMILES string.  It is a SMILES string with stereochemical and isotopic specifications | 
| InChI| Standard IUPAC International Chemical Identifier (InChI).  It does not allow for user selectable options in dealing with the stereochemistry and tautomer layers of the InChI string | 
| InChIKey| Hashed version of the full standard InChI, consisting of 27 characters| 
| IUPACName| Chemical name systematically determined according to the IUPAC nomenclatures | 
| XLogP| Computationally generated octanol-water partition coefficient or distribution coefficient. XLogP is used as a measure of hydrophilicity or hydrophobicity of a molecule | 
| ExactMass| The mass of the most likely isotopic composition for a single molecule, corresponding to the most intense ion/molecule peak in a mass spectrum | 
| MonoisotopicMass| The mass of a molecule, calculated using the mass of the most abundant isotope of each element | 
|TPSA| Topological polar surface area, computed by the algorithm described in the paper by Ertl et al | 
|Complexity|The molecular complexity rating of a compound, computed using the Bertz/Hendrickson/Ihlenfeldt formula | 
|Charge| The total (or net) charge of a molecule | 
|HBondDonorCount| Number of hydrogen-bond donors in the structure|
|HBondAcceptorCount| Number of hydrogen-bond acceptors in the structure|
|RotatableBondCount| Number of rotatable bonds|
|HeavyAtomCount| Number of non-hydrogen atoms|
|IsotopeAtomCount| Number of atoms with enriched isotope(s)|
|AtomStereoCount| Total number of atoms with tetrahedral (sp3) stereo [e.g., (R)- or (S)-configuration]|
|DefinedAtomStereoCount| Number of atoms with defined tetrahedral (sp3) stereo|
|UndefinedAtomStereoCount| Number of atoms with undefined tetrahedral (sp3) stereo|
|BondStereoCount|Total number of bonds with planar (sp2) stereo [e.g., (E)- or (Z)-configuration]|
|DefinedBondStereoCount|Number of atoms with defined planar (sp2) stereo|
|UndefinedBondStereoCount|Number of atoms with undefined planar (sp2) stereo|
|CovalentUnitCount|Number of covalently bound units|
|Volume3D|Analytic volume of the first diverse conformer (default conformer) for a compound|
|XStericQuadrupole3D|The x component of the quadrupole moment (Qx) of the first diverse conformer (default conformer) for a compound|
|YStericQuadrupole3D|The y component of the quadrupole moment (Qy) of the first diverse conformer (default conformer) for a compound|
|ZStericQuadrupole3D|The z component of the quadrupole moment (Qz) of the first diverse conformer (default conformer) for a compound|
|FeatureCount3D|Total number of 3D features (the sum of FeatureAcceptorCount3D, FeatureDonorCount3D, FeatureAnionCount3D, FeatureCationCount3D, FeatureRingCount3D and FeatureHydrophobeCount3D)|
|FeatureAcceptorCount3D|Number of hydrogen-bond acceptors of a conformer|
|FeatureDonorCount3D|Number of hydrogen-bond donors of a conformer|
|FeatureAnionCount3D|Number of anionic centers (at pH 7) of a conformer|
|FeatureCationCount3D|Number of cationic centers (at pH 7) of a conformer |
|FeatureRingCount3D|Number of rings of a conformer|
|FeatureHydrophobeCount3D|Number of hydrophobes of a conformer|
|ConformerModelRMSD3D|Conformer sampling RMSD in Å|
|EffectiveRotorCount3D|Total number of 3D features (the sum of FeatureAcceptorCount3D, FeatureDonorCount3D, FeatureAnionCount3D, FeatureCationCount3D, FeatureRingCount3D and FeatureHydrophobeCount3D)|
|ConformerCount3D|The number of conformers in the conformer model for a compound|
|Fingerprint2D|Base64-encoded PubChem Substructure Fingerprint of a molecule|




## Additional Information

#### Status Codes

| HTTP Status | Error Code | General Error Category |
| :-------------: |:-------------:| :-------------:| 
| 200| (none) |(none) | 
| 202| (none) | Accepted (asynchronous operation pending) |
| 400| PUGREST.BadRequest | Request is improperly formed (syntax error in the URL, POST body, etc.) |
| 404| PUGREST.NotFound | The input record was not found (e.g. invalid CID)|
| 405| PUGREST.NotAllowed | Request not allowed (such as invalid MIME type in the HTTP Accept header)|
| 504| PUGREST.Timeout | The request timed out, from server overload or too broad a request|
| 503| PUGREST.ServerBusy | Too many requests or server is busy, retry later|
| 501| PUGREST.Unimplemented | The requested operation has not (yet) been implemented by the server|
| 500| PUGREST.ServerError | Some problem on the server side (such as a database server down, etc.)|
| 500| PUGREST.Unknown | An unknown error occurred|



