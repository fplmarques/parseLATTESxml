#!/usr/bin/python3.8
#qualis = ['qualis_adm_pub_contab_turism','qualis_antropl_arqueol','qualis_arquit_urban_design','qualis_artes','qualis_astron_fisica','qualis_biodiversidade','qualis_biotecnologia','qualis_cienc_agrarias_I','qualis_cienc_alimentos','qualis_cienc_ambientais','qualis_cienc_biologicas_III','qualis_cienc_biologicas_II','qualis_cienc_biologicas_I','qualis_cienc_comput','qualis_cienc_polit_rel_internac','qualis_cienc_relig_teol','qualis_comun_info','qualis_direito','qualis_economia','qualis_educacao_fisica','qualis_educacao','qualis_enfermagem','qualis_engenharias_III','qualis_engenharias_II','qualis_engenharias_I','qualis_engenharias_IV','qualis_ensino','qualis_farmacia','qualis_filosofia','qualis_geociencias','qualis_geografia','qualis_historia','qualis_interdisciplinar','qualis_linguist_literat','qualis_materiais','qualis_mat_prob_stats','qualis_medicina_III','qualis_medicina_II','qualis_medicina_I','qualis_med_veterinaria','qualis_nutricao','qualis_odontologia','qualis_plan_urban_reg_demografia','qualis_psicologia','qualis_quimica','qualis_saude_coletiva','qualis_servico_social','qualis_sociologia','qualis_zootec_rec_pesqu.py']
qualis = ["qualis_adm_pub_contab_turism","qualis_antropl_arqueol"]
for q in qualis:
#  print(type(q))
  try:
    print(f'Loading {q}.py')
    from q import get_qualis
    print(f'OK')
  except NameError:
    print(f'Dictionary {q} has sybtax error!')
