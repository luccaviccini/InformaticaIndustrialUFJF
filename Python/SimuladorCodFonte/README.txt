Para executar o simulador a partir do codigo fonte, siga os seguintes passos:

1) Crie um ambiente virtual: 
	python -m virtualenv (nome_do_ambiente)

2) Ative o ambiente virtual: 
	Windows - (nome_do_ambiente)\Scripts\activate 
	Linux - source (nome_do_ambiente)/bin/activate

3) Instale as dependencias do projeto:
	pip install pymodbustcp numpy
	
4) Execute o servidor:
	python main.py