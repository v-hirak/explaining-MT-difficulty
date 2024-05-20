# Language Data

This folder contains everything related to collecting data for the languages found in the [FLORES+ dataset](https://github.com/openlanguagedata/flores).

The data is aggregated in the `lang_data.csv` file. Below are the descriptions of each of the columns:

- `lang`: language ID from the [FLORES+ dataset](https://github.com/openlanguagedata/flores).
- `iso_code`: ISO-639-3 code.
- `wals_code`: code in the [WALS Database](https://wals.info/).
- `script`: language script extracted from the FLORES+ dataset.
- `variety`: glottocode found in the FLORES+ dataset.
- `name`: full name of the language from the FLORES+ dataset.
- `family`: language family as per WALS.
- `genus`: language genus as per WALS.
- `d_syn`: syntactic distance from English, calculated using the [lang2vec library](https://github.com/antonisa/lang2vec?tab=readme-ov-file).