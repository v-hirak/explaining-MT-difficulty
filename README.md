# Dataset of Typological Language Properties

This dataset is part of my Master's Thesis project and contains a variety of properties for 212 languages included in the [FLORES+ dataset](https://github.com/openlanguagedata/flores). 

## Description of Columns

The data is aggregated in the `lang_data.csv` file. Below are the descriptions of each of the columns:

### Basic Taxonomic Properties

- `lang`: language ID from the [FLORES+ dataset](https://github.com/openlanguagedata/flores).
- `iso_code`: ISO-639-3 code.
- `wals_code`: code in the [WALS Database](https://wals.info/), available for 176 languages.
- `script`: language script extracted from the FLORES+ dataset.
- `variety`: glottocode found in the FLORES+ dataset.
- `name`: full name of the language from the FLORES+ dataset.
- `family`: language family as per WALS.
- `genus`: language genus as per WALS.

### Precomputed Typological Distances from English

Calculated using the [lang2vec library](https://github.com/antonisa/lang2vec). Available for all 212 languages.

- `d_gen`: genetic distance, represents the distance from English on the hypothesized Glottolog language tree.
- `d_geo`: geographic distance, calculated as the "great circle" distance between the English and a given language on the surface of the Earth.
- `d_syn`: syntactic distance from English, calculated as cosine distance between feature vectors derived from syntactic structures.
- `d_inv`: inventory distance from English, calculated as cosine distance between the phonological feature vectors derived from the [PHOIBLE](https://phoible.org/), [WALS](https://wals.info/), and [Ethnologue](https://www.ethnologue.com/) databases.
- `d_pho`: phonological distance from English, calculated as cosine distance between the phonological feature vectors derived from the [PHOIBLE](https://phoible.org/), [WALS](https://wals.info/), and [Ethnologue](https://www.ethnologue.com/) databases.
- `d_fea`: featural distance from English, calculated as cosine distance between feature vectors combining all five features described above.

### WALS Features
