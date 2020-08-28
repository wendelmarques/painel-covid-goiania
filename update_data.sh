rm data/raw/covid-19-goiania-por-bairro-final.csv
rm data/pickle/world_info.p

wget -O data/raw/covid-19-pandemic-worldwide-data.csv "link do csv"

cd scripts && echo ls && python cria_mapa_e_grafico.py
cd ..
python app.py