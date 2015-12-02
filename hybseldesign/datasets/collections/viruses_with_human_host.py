"""Collection of datasets representing all viruses that infect human.

Most of the sequences in these datasets were automatically downloaded
from GenBank by filtering its list of all viral genomes (taxId:10239)
for those sequences whose host contains 'human'.

Note that this uses versions of HIV (1 and 2) sequences in which
the LTRs have been stripped from both ends -- i.e., it contains
the 'hiv1_without_ltr' and 'hiv2_without_ltr' datasets rather than
the 'hiv1' and 'hiv2' datasets.
"""

import sys

from hybseldesign.datasets import DatasetCollection

__author__ = 'Hayden Metsky <hayden@mit.edu>'


DATASETS = [
    'ablv',
    'achimota',
    'aedes',
    'aguacate',
    'akabane',
    'alethinophid_reptarenavirus',
    'allpahuayo',
    'amapari',
    'ampv',
    'andes',
    'apmv',
    'apoi',
    'aravan',
    'aroa',
    'arumowot',
    'aspv',
    'avian_vornavirus',
    'b19',
    'bagaza',
    'banna',
    'bat_hepevirus',
    'bat_sapovirus_tlc58',
    'bear_canyon',
    'beilong',
    'betapapillomavirus_1',
    'betapapillomavirus_2',
    'betapapillomavirus_3',
    'betapapillomavirus_4',
    'betapapillomavirus_5',
    'betapapillomavirus_6',
    'bhanja',
    'bk',
    'bokeloh_bat',
    'borna_disease',
    'bovine_hepacivirus',
    'bpv_3',
    'brazoran',
    'brsv',
    'bunyamwera',
    'california_encephalitis',
    'candiru',
    'canine_distemper',
    'canine_pneumovirus',
    'cedar',
    'cell_fusing_agent',
    'cetacean_morbillivirus',
    'chandipura',
    'chaoyang',
    'chapare',
    'chikungunya',
    'colobus_monkey_papillomavirus',
    'crimean_congo',
    'ctfv',
    'cupixi',
    'cxfv',
    'dengue',
    'dobrava_belgrade',
    'donggang',
    'dugbe',
    'duvenhage',
    'eblv_1',
    'eblv_2',
    'ebola_nonzaire',
    'ebola_zaire_with_2014',
    'eee',
    'entebbe_bat',
    'enterovirus_a',
    'enterovirus_b',
    'enterovirus_c',
    'enterovirus_d',
    'eyach',
    'feline_morbillivirus',
    'fer_de_lance',
    'fitzroy_river',
    'flexal',
    'gairo',
    'gbv_c',
    'gemycircularvirus_sl1',
    'goose_paramyxovirus_sf02',
    'great_island',
    'guanarito',
    'hantaan',
    'hantavirus_z10',
    'hbov',
    'heartland',
    'hecv_4408',
    'hendra',
    'hepatitis_a',
    'hepatitis_b',
    'hepatitis_c',
    'hepatitis_delta',
    'hepatitis_e',
    'herpesvirus_1',
    'herpesvirus_2',
    'herpesvirus_3',
    'herpesvirus_4',
    'herpesvirus_5',
    'herpesvirus_6',
    'herpesvirus_7',
    'herpesvirus_8',
    'hervk',
    'hiv1_without_ltr',
    'hiv2_without_ltr',
    'hpiv_1',
    'hpiv_2',
    'hpiv_3',
    'hpiv_4',
    'hpv',
    'human_coronavirus_229e',
    'human_coronavirus_hku1',
    'human_coronavirus_nl63',
    'human_coronavirus_oc43',
    'human_genital_associated_circular_dna',
    'human_picobirnavirus',
    'human_smacovirus_1',
    'ikoma',
    'ilheus',
    'influenza_a',
    'influenza_b',
    'influenza_c',
    'ippy',
    'irkut',
    'j_virus',
    'jc',
    'jev',
    'junin',
    'kadipiro',
    'kamiti_river',
    'kedougou',
    'kfd',
    'khujand',
    'ki_polyomavirus',
    'kokobera',
    'lagos_bat',
    'langat',
    'lassa',
    'latino',
    'lcmv',
    'leopards_hill',
    'liao_ning',
    'lloviu_cuevavirus',
    'louping_ill',
    'lujo',
    'luna',
    'lunk_nks1',
    'lyssavirus_ozernoe',
    'machupo',
    'mamastrovirus',
    'manzanilla',
    'mapuera',
    'marburg',
    'mastadenovirus_a',
    'mastadenovirus_b',
    'mastadenovirus_c',
    'mastadenovirus_d',
    'mayaro',
    'mcv',
    'measles',
    'menangle',
    'mercadeo',
    'mers',
    'metapneumovirus',
    'mobala',
    'modoc',
    'mojiang',
    'mokola',
    'montana_myotis_leukoencephalitis',
    'mopeia',
    'mopeia_lassa_reassortant_29',
    'morogoro',
    'mossman',
    'mssi2_225',
    'mumps',
    'murine_pneumonia',
    'mvev',
    'nariva',
    'ndv',
    'nipah',
    'norwalk',
    'norway_rat_hepacivirus',
    'ntaya',
    'o_nyong_nyong',
    'oliveros',
    'omsk_hemorrhagiv_fever',
    'oropouche',
    'parana',
    'parramatta_river',
    'pichinde',
    'pirital',
    'piscihepevirus_a',
    'piv_5',
    'porcine',
    'powassan',
    'ppiv_1',
    'pprv',
    'ptlv_1',
    'ptlv_2',
    'punta_toro',
    'puumala',
    'quang_binh',
    'razdan',
    'reptile_bornavirus_1',
    'rhabdovirus',
    'rhinovirus_a',
    'rhinovirus_b',
    'rift_valley_fever',
    'rinderpest',
    'rio_bravo',
    'rodent_hepacivirus',
    'rodent_torque_teno',
    'ross_river',
    'rotavirus_a',
    'rotavirus_b',
    'rotavirus_c',
    'rotavirus_f',
    'rotavirus_g',
    'rotavirus_h',
    'rotavirus_i',
    'royal_farm',
    'rsv',
    'rubella',
    'sabia',
    'salem',
    'sapporo',
    'sars',
    'sathuperi',
    'seal_anellovirus',
    'sendai',
    'seoul',
    'sepik',
    'sfnv',
    'sfsv',
    'sfts',
    'shamonda',
    'shimoni_bat',
    'shuni',
    'simbu',
    'simian_41',
    'simian_torque_teno',
    'sin_nombre',
    'slev',
    'small_anellovirus',
    'sosuga',
    'spanish_goat_encephalitis',
    'sunshine',
    'sv40',
    'tacaribe',
    'tailam',
    'tamana_bat',
    'tamiami',
    'tbev',
    'tembusu',
    'thogoto',
    'thottapalayam',
    'tioman',
    'tlmv',
    'torque_teno',
    'torque_teno_canis',
    'torque_teno_douroucouli',
    'torque_teno_felis',
    'torque_teno_midi',
    'torque_teno_mini',
    'torque_teno_sus',
    'torque_teno_tamarin',
    'torque_teno_zalophus',
    'tuhoko',
    'tula',
    'tupaia',
    'usutu',
    'uukuniemi',
    'vaccinia',
    'variola',
    'vee',
    'vsiv',
    'wee',
    'wesselsbron',
    'west_caucasion_bat',
    'west_nile',
    'whitewater_arroyo',
    'wu_polyomavirus',
    'yellow_fever',
    'yokose',
    'ypv',
    'zika',
    'zygosaccharomyces_bailii_z'
]


dsc = DatasetCollection(DATASETS)

sys.modules[__name__] = dsc
