#!/bin/bash

#SBATCH --time=00:60:00
#SBATCH --partition=gpu
#SBATCH --job-name=comet
#SBATCH --mem=64G
#SBATCH --gpus-per-node=1

source ~/thesis/venv/bin/activate

comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.afr_Latn_1 -r floresp-v2.0-rc.2/dev/dev.afr_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.arb_Arab_1 -r floresp-v2.0-rc.2/dev/dev.arb_Arab --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.bul_Cyrl_1 -r floresp-v2.0-rc.2/dev/dev.bul_Cyrl --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.cat_Latn_1 -r floresp-v2.0-rc.2/dev/dev.cat_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.ces_Latn_1 -r floresp-v2.0-rc.2/dev/dev.ces_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.cmn_Hans_1 -r floresp-v2.0-rc.2/dev/dev.cmn_Hans --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.cmn_Hant_1 -r floresp-v2.0-rc.2/dev/dev.cmn_Hant --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.ekk_Latn_1 -r floresp-v2.0-rc.2/dev/dev.ekk_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.ell_Grek_1 -r floresp-v2.0-rc.2/dev/dev.ell_Grek --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.eus_Latn_1 -r floresp-v2.0-rc.2/dev/dev.eus_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.fin_Latn_1 -r floresp-v2.0-rc.2/dev/dev.fin_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.heb_Hebr_1 -r floresp-v2.0-rc.2/dev/dev.heb_Hebr --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.hin_Deva_1 -r floresp-v2.0-rc.2/dev/dev.hin_Deva --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.hun_Latn_1 -r floresp-v2.0-rc.2/dev/dev.hun_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.ind_Latn_1 -r floresp-v2.0-rc.2/dev/dev.ind_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.ita_Latn_1 -r floresp-v2.0-rc.2/dev/dev.ita_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.jpn_Jpan_1 -r floresp-v2.0-rc.2/dev/dev.jpn_Jpan --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.kor_Hang_1 -r floresp-v2.0-rc.2/dev/dev.kor_Hang --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.nld_Latn_1 -r floresp-v2.0-rc.2/dev/dev.nld_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.pes_Arab_1 -r floresp-v2.0-rc.2/dev/dev.pes_Arab --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.pol_Latn_1 -r floresp-v2.0-rc.2/dev/dev.pol_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.por_Latn_1 -r floresp-v2.0-rc.2/dev/dev.por_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.ron_Latn_1 -r floresp-v2.0-rc.2/dev/dev.ron_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.rus_Cyrl_1 -r floresp-v2.0-rc.2/dev/dev.rus_Cyrl --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.slk_Latn_1 -r floresp-v2.0-rc.2/dev/dev.slk_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.slv_Latn_1 -r floresp-v2.0-rc.2/dev/dev.slv_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.spa_Latn_1 -r floresp-v2.0-rc.2/dev/dev.spa_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.swe_Latn_1 -r floresp-v2.0-rc.2/dev/dev.swe_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.tur_Latn_1 -r floresp-v2.0-rc.2/dev/dev.tur_Latn --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.uig_Arab_1 -r floresp-v2.0-rc.2/dev/dev.uig_Arab --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.ukr_Cyrl_1 -r floresp-v2.0-rc.2/dev/dev.ukr_Cyrl --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.urd_Arab_1 -r floresp-v2.0-rc.2/dev/dev.urd_Arab --quiet --only_system >> comet.txt
comet-score -s floresp-v2.0-rc.2/dev/dev.eng_Latn -t translations/num_beams_1/hyp.vie_Latn_1 -r floresp-v2.0-rc.2/dev/dev.vie_Latn --quiet --only_system >> comet.txt

deactivate
