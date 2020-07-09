import pandas as pd
import numpy as np

# 1a Fase : PCR
# 2a Fase : igm
# 3a Fase : igg

# Importando planilhas
# Einstein
ee = pd.read_csv("dados/einstein_e.csv")
pe = pd.read_csv("dados/einstein_p.csv")
# Fleury
ef = pd.read_csv("dados/fleury_e.csv")
pf = pd.read_csv("dados/fleury_p.csv")
# Sirio
es = pd.read_csv("dados/hsl_e.csv")
ps = pd.read_csv("dados/hsl_p.csv")

# Reconhecimento da Saída

# Einstein
# print(ee["de_exame"].unique())

# Fleury
# print(ef["DE_EXAME"].unique())

# Sirio
# print(es["DE_EXAME"].unique())

# Junção de paciente e exame
eins = pd.merge(ee, pe, how='inner', on='id_paciente')
fleu = pd.merge(ef, pf, how='inner', on='ID_PACIENTE')
siri = pd.merge(es, ps, how='inner', on='ï»¿ID_PACIENTE')

# Limpeza das colunas
# Deletar o de_analito para frente.
eins = eins[['id_paciente','de_exame','de_analito','de_resultado','ic_sexo','aa_nascimento']]
eins = eins.rename(columns = {'id_paciente':'ID_PACIENTE','de_exame':'DE_EXAME','de_resultado':'DE_RESULTADO','ic_sexo':'IC_SEXO','aa_nascimento':'AA_NASCIMENTO'})
fleu = fleu[['ID_PACIENTE','DE_EXAME','DE_RESULTADO','IC_SEXO','AA_NASCIMENTO']]
siri = siri[['ï»¿ID_PACIENTE','DE_EXAME','DE_RESULTADO','IC_SEXO','AA_NASCIMENTO']]
siri = siri.rename(columns = {'ï»¿ID_PACIENTE':'ID_PACIENTE'})

# Saída
# PCR
# Einstein
eins.loc[eins["DE_EXAME"] == "PCR em tempo real para detecÃ§Ã£o de Coron", ["DE_EXAME"]] = "PCR"
# Fleury
fleu.loc[fleu["DE_EXAME"] == "NOVO CORONAVÍRUS 2019 (SARS-CoV-2): DETECÇÃO POR PCR", ["DE_EXAME"]] = "PCR"
# Sirio
siri.loc[siri["DE_EXAME"] == "COVID-19-PCR para SARS-COV-2: VÃ¡rios Materiais (Fleury)", ["DE_EXAME"]] = "PCR"

# WIP
# IGG
# Einstein
# eins.loc[eins["DE_EXAME"] == "PCR em tempo real para detecÃ§Ã£o de Coron" & eins["de_analito"].str.contains('IgG'), ["DE_EXAME"]] = "IGG"
# Fleury
fleu.loc[fleu["DE_EXAME"] == "COVID19: ANTICORPOS IgG: soro", ["DE_EXAME"]] = "IGG"
fleu.loc[fleu["DE_EXAME"] == "SARS-COV-2: ANTICORPOS IgG: soro", ["DE_EXAME"]] = "IGG"
# # Sirio
siri.loc[siri["DE_EXAME"] == "Sorologia - CoronavÃ\\xadrus: IgG", ["DE_EXAME"]] = "IGG"
#siri.loc[siri["DE_EXAME"] == "COVID-19-Sorologia IgM e IgG por quimiluminescÃªncia: soro", ["DE_EXAME"]] = "PCR" # TEM Q VER QUAL É IGG

# IGM
# Einstein
# eins.loc[eins["DE_EXAME"] == "PCR em tempo real para detecÃ§Ã£o de Coron" & eins["de_analito"].str.contains('IgM'), ["DE_EXAME"]] = "IGM"
# Fleury
fleu.loc[fleu["DE_EXAME"] == "COVID19: ANTICORPOS IgM: soro", ["DE_EXAME"]] = "IGM"
# # Sirio
#siri.loc[siri["DE_EXAME"] == "COVID-19-Sorologia IgM e IgG por quimiluminescÃªncia: soro", ["DE_EXAME"]] = "PCR" # TEM Q VER QUAL É IGG

print(eins["DE_EXAME"].unique())