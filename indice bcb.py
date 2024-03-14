import pandas as pd

cod =[193,188,191,189,11,12,1,21620] 
descricao=["IPC-Fipe","INPC","Índice de preços ao consumidor-Brasil (IPC-Br)","Índice geral de preços do mercado (IGP-M)","Taxa de juros - Selic","Taxa de juros - CDI",
"Taxa de câmbio - Livre - Dólar americano (venda) - diário","Taxa de câmbio - Livre - Euro (compra)"]

tmp2=[]
for i in range(len(cod)):
    codigo_bcb=cod[i] 
    descricao_bcb=descricao[i]
    url = "http://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json".format(codigo_bcb,lines=True)
    print(codigo_bcb)
    tmp = pd.read_json(url)
    tmp['Codigo']=codigo_bcb
    tmp['Descricao'] = descricao_bcb
    tmp2.append(tmp)
    
dadosBCB = pd.concat(tmp2,ignore_index=True)
print(dadosBCB) 
