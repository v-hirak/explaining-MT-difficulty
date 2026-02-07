# Dataset of Typological Language Properties

<a href="https://arxiv.org/abs/2602.03551"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-2602.03551-b31b1b"></a>

**Authors:** Vitalii Hirak, Jaap Jumelet, Arianna Bisazza.

This dataset contains a variety of typological and morphosyntactic properties for languages from the [FLORES+ dataset](https://huggingface.co/datasets/openlanguagedata/flores_plus) and is part of our EACL 2026 paper ["Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models"](https://arxiv.org/abs/2602.03551). We use these properties to estimate the impact of target language typology on neural machine translation difficulty. We find that target languages with certain features benefit more from a large decoding space during translation and thus may call for alternative decoding strategies.

## Description of Properties

Most of the data is aggregated in the `lang_data.csv` file. Additionally, we include typological distances between seven source languages used in our paper (Arabic, English, Italian, Dutch, Turkish, Ukrainian, Vietnamese) and 211 languages in the `distances` folder. Below are the descriptions of the propreties.

### Basic Taxonomic Properties

- `lang`: language ID from the [FLORES+ dataset](https://huggingface.co/datasets/openlanguagedata/flores_plus).
- `iso_code`: ISO-639-3 code.
- `wals_code`: code in the [WALS Database](https://wals.info/), available for 176 languages.
- `script`: language script extracted from the FLORES+ dataset.
- `variety`: glottocode found in the FLORES+ dataset.
- `name`: full name of the language from the FLORES+ dataset.
- `family`: language family as per WALS.
- `genus`: language genus as per WALS.

### Typological Distances

Using the [lang2vec library](https://github.com/antonisa/lang2vec), we query six types of typological distances between a source and target language. Since our paper features seven source languages (Arabic, English, Italian, Dutch, Turkish, Ukrainian, Vietnamese), the `distances` folder contains seven sets of distance measures between each source language and the rest 211 target languages. Higher values indicate larger source-target distances.

- `d_gen`: _genetic_ distance, represents the source-target language distance on the hypothesized Glottolog language tree.
- `d_geo`: _geographic_ distance, calculated as the "great circle" distance of a source-target language pair on the surface of the Earth.
- `d_syn`: _syntactic_ source-target language distance, calculated as cosine distance between feature vectors derived from syntactic structures.
- `d_inv`: _inventory_ source-target language distance, calculated as cosine distance between the phonological feature vectors derived from the [PHOIBLE](https://phoible.org/), [WALS](https://wals.info/), and [Ethnologue](https://www.ethnologue.com/) databases.
- `d_pho`: _phonological_ source-target language distance, calculated as cosine distance between the phonological feature vectors derived from the [PHOIBLE](https://phoible.org/), [WALS](https://wals.info/), and [Ethnologue](https://www.ethnologue.com/) databases.
- `d_fea`: _featural_ source-target language distance, calculated as cosine distance between feature vectors combining all five features described above.

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

- `ttr_flores`: _type/token ratio_, calculated as $TTR=t/w$, where $t$ is the number of unique word types and $w$ is the total number of words.
- `rttr_flores`: _root type/token ratio_, calculated as $RTTR=t/\sqrt{w}$.
- `mattr_flores`: _moving average type/token ratio_, calculated as an average of TTR values computed on fixed-length text chunks. We use the window size of 500 word tokens.

### Morphological Complexity Measures

Eight continuous morphological complexity measures from [Çöltekin and Rama (2023)](https://www.degruyter.com/document/doi/10.1515/lingvan-2021-0007/html), available for 34 languages. Higher values indicate higher morphological complexity.

- `ttr`: _type/token ratio_ calculated on Universal Dependencies.
- `msp`: _mean size of paradigm_ is calculated by dividing the number of word forms in a text by the number of lemmas.
- `ws`: _information in word structure_ compares the information content (i.e. entropy) of the original text with its compressed version.
- `wh`: _word entropy_ is based on word frequency distribution of a text.
- `lh`: _lemma entropy_ is based on lemma frequency distribution of a text.
- `is`: _inflectional synthesis_ is the maximum number of inflection categories that can be expressed by a standalone verb.
- `mfh`: _morphological feature entropy_ reflects the usage of morphological features (e.g. grammatical cases) and their values.
- `-ia`: _negative inflection accuracy_ is the accuracy of an ML model on the task of predicting inflected forms given lemma and grammatical features.

### Gradient Word Order Measures

Four gradient measures of word order proposed and computed by [Levshina (2019)](https://www.degruyter.com/document/doi/10.1515/lingty-2019-0025/html?lang=en) and [Levshina et al. (2023)](https://www.degruyter.com/document/doi/10.1515/ling-2021-0098/html?lang=en).

- `h_dep`: _average word order entropy of dependents_ is the entropy of different word order patterns of _dependencies_ (e.g. verb-subject and noun-adposition relations), available for 45 languages.
- `h_codep`: _average word order entropy of codependents_ is the entropy of different word order patterns of _codependencies_ (e.g. subject and object of the same verb), available for 44 languages.
- `SO_prop`: _proportion of Subject-Object word order_ is based the frequencies of clauses where subject comes before object. Available for 32 languages.
- `head_finality`: _percentage of head-final phrases_ approximates the preference of a language towards head-initial or head-final phrases. Available for 59 languages.

### Language Resourcedness

- `glotcc_size`: we approximate the _general resourcedness of a language_ using language size data from the [GlotCC broad-coverage CommonCrawl corpus](https://github.com/cisnlp/GlotCC?tab=readme-ov-file). We collect content length values for 210 out of 212 languages in FLORES+.
- `wiki_size`: we estimate data availability of 169 languages using their respective Wikipedia sizes measured in the number of articles. Article counts are taken from [here](https://meta.wikimedia.org/wiki/List_of_Wikipedias).
