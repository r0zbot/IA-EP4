
# %%
import pandas as pd
import numpy as np

# 1a Fase : PCR
# 2a Fase : igm
# 3a Fase : igg

# Importando planilhas
# Einstein
ee = pd.read_csv("dados_novos/fixed_utf8/einstein_exames.csv", delimiter="|")
pe = pd.read_csv("dados_novos/fixed_utf8/einstein_pacientes.csv", delimiter="|")
# Fleury
ef = pd.read_csv("dados_novos/fixed_utf8/fleury_exames.csv", delimiter="|")
pf = pd.read_csv("dados_novos/fixed_utf8/fleury_pacientes.csv", delimiter="|")
# Sirio
es = pd.read_csv("dados_novos/fixed_utf8/hsl_exames.csv", delimiter="|")
ps = pd.read_csv("dados_novos/fixed_utf8/hsl_pacientes.csv", delimiter="|")

# # Reconhecimento da Saída

# # Einstein
# # print(ee["de_exame"].unique())

# # Fleury
# # print(ef["DE_EXAME"].unique())

# # Sirio
# # print(es["DE_EXAME"].unique())

# # Junção de paciente e exame
eins = pd.merge(ee, pe, how='inner', on='id_paciente')
fleu = pd.merge(ef, pf, how='inner', on='ID_PACIENTE')
siri = pd.merge(es, ps.rename(columns = {"id_paciente": "ID_PACIENTE"}), how='inner', on='ID_PACIENTE')

# # Limpeza das colunas
# # Deletar o de_analito para frente.
eins = eins[['id_paciente','de_exame','de_analito','de_resultado','ic_sexo','aa_nascimento']]
eins = eins.rename(columns = {'id_paciente':'ID_PACIENTE','de_exame':'DE_EXAME','de_resultado':'DE_RESULTADO','ic_sexo':'IC_SEXO','aa_nascimento':'AA_NASCIMENTO', 'de_analito': 'DE_ANALITO'})
fleu = fleu[['ID_PACIENTE','DE_EXAME', 'DE_ANALITO','DE_RESULTADO','IC_SEXO','AA_NASCIMENTO']]
siri = siri[['ID_PACIENTE','DE_EXAME', 'DE_ANALITO','DE_RESULTADO','ic_sexo','aa_nascimento']]
siri = siri.rename(columns = {'ic_sexo':'IC_SEXO', 'aa_nascimento':'AA_NASCIMENTO'})

# %%



# # Saída
# # PCR
# # Einstein
# eins.loc[eins["DE_EXAME"] == "PCR Cem tempo real para detecção de Coron", ["DE_EXAME"]] = "PCR"
# # Fleury
# fleu.loc[fleu["DE_EXAME"] == "NOVO CORONAVÍRUS 2019 (SARS-CoV-2): DETECÇÃO POR PCR", ["DE_EXAME"]] = "PCR"
# # Sirio
# siri.loc[siri["DE_EXAME"] == "COVID-19-PCR para SARS-COV-2: VÃ¡rios Materiais (Fleury)", ["DE_EXAME"]] = "PCR"

# %%
eins.loc[eins["DE_EXAME"] == "PCR Cem tempo real para detecção de Coron", ["DE_EXAME"]] = "PCR"
eins.loc[eins["DE_EXAME"] == "HMVSC-AFIP PCR COVID 19", ["DE_EXAME"]] = "PCR"
eins.loc[eins["DE_RESULTADO"] == "Não Detectado", ["DE_RESULTADO"]] = "Não detectado"

# DE_EXAME = Sorologia SARS-CoV-2/COVID19 IgG/IgM
eins.loc[eins["DE_ANALITO"] == "IgG, COVID19", ["DE_EXAME"]] = "IGG"
eins.loc[eins["DE_ANALITO"] == "IgM, COVID19", ["DE_EXAME"]] = "IGM"

# eins.loc[eins["DE_ANALITO"] == "COVID IgG Interp", ["DE_EXAME"]] = "IGG"
# eins.loc[eins["DE_ANALITO"] == "COVID IgM Interp", ["DE_EXAME"]] = "IGM"

# eins[eins["DE_EXAME"] == "PCR"].head()

# %%

fleu.loc[
    (fleu["DE_EXAME"] == "NOVO CORONAVÍRUS 2019 (SARS-CoV-2), DETECÇÃO POR PCR" ) & 
    (fleu["DE_ANALITO"] != "Covid 19, Material") &
    (
        (fleu["DE_RESULTADO"] == "NÃO DETECTADO (NEGATIVO)") |
        (fleu["DE_RESULTADO"] == "DETECTADO (POSITIVO)")
    )
    , ["DE_EXAME"]] = "PCR"

fleu.loc[fleu["DE_EXAME"] == "COVID19, ANTICORPOS IgG, soro", ["DE_EXAME"]] = "IGG"
fleu.loc[fleu["DE_EXAME"] == "SARS-COV-2, ANTICORPOS IgG, soro", ["DE_EXAME"]] = "IGG"

fleu.loc[fleu["DE_EXAME"] == "COVID19, ANTICORPOS IgM, soro", ["DE_EXAME"]] = "IGM"

# Filtra os resultados nada a ver
# fleu = fleu[~fleu["DE_RESULTADO"].isin(['NÃO REAGENTE', 'REAGENTE', 'inferior a 1,01', 'inferior a 1,00', 'Indeterminado'])]
# %%
siri.loc[
    (siri["DE_EXAME"] == "COVID-19-PCR para SARS-COV-2, Vários Materiais (Fleury)" ) & 
    (siri["DE_ANALITO"] != "Coronavírus (2019-nCoV)	") &
    (
        (siri["DE_RESULTADO"] == "NÃO DETECTADO (NEGATIVO)") |
        (siri["DE_RESULTADO"] == "DETECTADO (POSITIVO)")
    )
    , ["DE_EXAME"]] = "PCR"

# Todos os dados dão positivo?
# siri.loc[siri["DE_EXAME"] == 'Detecção de Coronavírus (NCoV-2019) POR PCR (Anatomia Patológica)', ["DE_EXAME"]] = "PCR"

siri.loc[siri["DE_EXAME"] == "Sorologia - Coronavírus, IgG", ["DE_EXAME"]] = "IGG"

siri.loc[
    (siri["DE_EXAME"] == "COVID-19-Sorologia IgM e IgG por quimiluminescência, soro" ) & 
        (siri["DE_ANALITO"] == "Covid 19, Anticorpos IgG, Quimioluminescência") |
        (siri["DE_ANALITO"] == "Covid 19, Anticorpos IgG, Quimiolumin.-Índice") 
    , ["DE_EXAME"]] = "IGG"

siri.loc[
    (siri["DE_EXAME"] == "COVID-19-Sorologia IgM e IgG por quimiluminescência, soro" ) & 
        (siri["DE_ANALITO"] == "Covid 19, Anticorpos IgM, Quimioluminescência") |
        (siri["DE_ANALITO"] == "Covid 19, Anticorpos IgM, Quimiolumin.-Índice") 
    , ["DE_EXAME"]] = "IGM"

#TODO: filtrar as bosta
#TODO: Os NAO DETECTADO ta tudo errado

# "COVID-19-Teste Rápido (IgM e IgG), soro" -> tem o script do bee movie inteiro e ta misturado igg e igm


# # WIP
# # IGG
# # Einstein
# # eins.loc[eins["DE_EXAME"] == "PCR em tempo real para detecÃ§Ã£o de Coron" & eins["de_analito"].str.contains('IgG'), ["DE_EXAME"]] = "IGG"
# # Fleury
# fleu.loc[fleu["DE_EXAME"] == "COVID19: ANTICORPOS IgG: soro", ["DE_EXAME"]] = "IGG"
# fleu.loc[fleu["DE_EXAME"] == "SARS-COV-2: ANTICORPOS IgG: soro", ["DE_EXAME"]] = "IGG"
# # # Sirio
# siri.loc[siri["DE_EXAME"] == "Sorologia - CoronavÃ\\xadrus: IgG", ["DE_EXAME"]] = "IGG"
# #siri.loc[siri["DE_EXAME"] == "COVID-19-Sorologia IgM e IgG por quimiluminescÃªncia: soro", ["DE_EXAME"]] = "PCR" # TEM Q VER QUAL É IGG

# # IGM
# # Einstein
# # eins.loc[eins["DE_EXAME"] == "PCR em tempo real para detecÃ§Ã£o de Coron" & eins["de_analito"].str.contains('IgM'), ["DE_EXAME"]] = "IGM"
# # Fleury
# fleu.loc[fleu["DE_EXAME"] == "COVID19: ANTICORPOS IgM: soro", ["DE_EXAME"]] = "IGM"
# # # Sirio
# #siri.loc[siri["DE_EXAME"] == "COVID-19-Sorologia IgM e IgG por quimiluminescÃªncia: soro", ["DE_EXAME"]] = "PCR" # TEM Q VER QUAL É IGG


# %%


# %%
