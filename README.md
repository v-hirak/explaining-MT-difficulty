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

### Typological Distances from English

Calculated using the [lang2vec library](https://github.com/antonisa/lang2vec). Available for all 212 languages. Higher values indicate distances further from English.

- `d_gen`: genetic distance, represents the distance from English on the hypothesized Glottolog language tree.
- `d_geo`: geographic distance, calculated as the "great circle" distance between English and a given language on the surface of the Earth.
- `d_syn`: syntactic distance from English, calculated as cosine distance between feature vectors derived from syntactic structures.
- `d_inv`: inventory distance from English, calculated as cosine distance between the phonological feature vectors derived from the [PHOIBLE](https://phoible.org/), [WALS](https://wals.info/), and [Ethnologue](https://www.ethnologue.com/) databases.
- `d_pho`: phonological distance from English, calculated as cosine distance between the phonological feature vectors derived from the [PHOIBLE](https://phoible.org/), [WALS](https://wals.info/), and [Ethnologue](https://www.ethnologue.com/) databases.
- `d_fea`: featural distance from English, calculated as cosine distance between feature vectors combining all five features described above.

### WALS Features

12 WALS features (20A-29A) from the "Morphology" category and one (81A) from the "Word Order" category. Feature values are discrete and correspond to their order in the respective WALS features.

- `20A`: Fusion of Selected Inflectional Formatives. Available for 38 languages.
- `21A`: Exponence of Selected Inflectional Formatives. Available for 38 languages.
- `21B`: Exponence of Tense-Aspect-Mood Inflection. Available for 38 languages.
- `22A`: Inflectional Synthesis of the Verb. Available for 38 languages.
- `23A`: Locus of Marking in the Clause. Available for 46 languages.
- `24A`: Locus of Marking in Possessive Noun Phrases. Available for 46 languages.
- `25A`: Locus of Marking: Whole-language Typology. Available for 46 languages.
- `25B`: Zero Marking of A and P Arguments. Available for 46 languages.
- `26A`: Prefixing vs. Suffixing in Inflectional Morphology. Available for 109 languages.
- `27A`: Reduplication. Available for 77 languages.
- `28A`: Case Syncretism. Available for 45 languages.
- `29A`: Syncretism in Verbal Person/Number Marking. Available for 45 languages.
- `81A`: Order of Subject, Object and Verb. Available for 127 languages.

### Type/Token Ratio Measures Calculated on FLORES+

Using the [LexicalRichness](https://github.com/lsys/LexicalRichness) library, we calculate three TTR measures using 997 sentences from the FLORES+ `dev` split for all 212 languages. Higher values indicate higher morphological complexity.

- `ttr_flores`: type/token ratio, calculated as $TTR=t/w$, where $t$ is the number of unique word types and $w$ is the total number of words.
- `rttr_flores`: root type/token ratio, calculated as $RTTR=t/\sqrt{w}$.
- `mattr_flores`: moving average type/token ratio, calculated as an average of TTR values computed on fixed-length text chunks. We use the window size of 500 word tokens.

### Morphological Complexity Measures

Eight continuous morphological complexity measures from [Çöltekin and Rama (2023)](https://www.degruyter.com/document/doi/10.1515/lingvan-2021-0007/html), available for 34 languages. Higher values indicate higher morphological complexity.

- `ttr`: type/token ratio.
- `msp`: mean size of paradigm.
- `ws`: information in word structure.
- `wh`: word entropy.
- `lh`: lemma entropy.
- `is`: inflectional synthesis.
- `mfh`: morphological feature entropy.
- `-ia`: negative inflection accuracy.

### Gradient Word Order Freedom Measures

Four gradient measures of word order flexibility. Higher values indicate less freedom in word order.

- `h_dep`: entropy of the order of dependents (e.g. verb-subject and noun-adposition), available for 45 languages. Value is an average for individual syntactic relation entropies from [Levshina (2019)](https://www.degruyter.com/document/doi/10.1515/lingty-2019-0025/html?lang=en).
- `h_codep`: entropy of the order of codependents (e.g. subject and object of the same verb), available for 44 languages. Value is an average for individual syntactic relation entropies from [Levshina (2019)](https://www.degruyter.com/document/doi/10.1515/lingty-2019-0025/html?lang=en).
- `SO_prop`: proportion of Subject-Object word order, measured by [Levshina et al. (2023)](https://www.degruyter.com/document/doi/10.1515/ling-2021-0098/html?lang=en). Available for 32 languages.
- `head-finality`: percentage of head-final phrases, measured by [Levshina et al. (2023)](https://www.degruyter.com/document/doi/10.1515/ling-2021-0098/html?lang=en). Availalbe for 59 languages.

### Language Data Availability

We estimate data availability of 165 languages using their respective Wikipedia sizes measured in the number of articles. Article counts are taken from [here](https://meta.wikimedia.org/wiki/List_of_Wikipedias).
