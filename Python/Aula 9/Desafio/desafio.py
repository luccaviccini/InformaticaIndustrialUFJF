dic1 = {"POOO1": {"Descricao": "Acesso aos parametros",
                  "Faixa de valores": 9999,
                  "Pag":"5-12"  
                 },
        "POOO2":{"Descricao": "Referencia de velocidade",
                  "Faixa de valores": 65535,
                  "Pag":"17-1"
                },  
        "POOO3":{"Descricao": "Velocidade de saída",
                  "Faixa de valores": 2000,
                  "Pag":"17-1"
                }                         
        }

print(dic1["POOO1"]["Descricao"])

for parametro,dict_interno in dic1.items():
    print("\n\n",parametro)   

    for info, dados in dict_interno.items():
        print(info,":", dados)        

    