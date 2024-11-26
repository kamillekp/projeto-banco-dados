# projeto-banco-dados

## Descrição
<p align="justify">
Este projeto é uma plataforma interativa desenvolvida para explorar dados eleitorais de maneira acessível e intuitiva, promovendo transparência no processo eleitoral brasileiro. Com o uso da base de dados aberta do Tribunal Superior Eleitoral (TSE), a plataforma permite a consulta de informações detalhadas sobre candidatos e coligações de maneira simplificada, visando atender cidadãos e pesquisadores interessados em dados eleitorais.
</p>

## Estrutura de Dados
Os dados estão organizados em coleções no MongoDB:

<ul> 
  <li> <b>Coleção politicos:</b> Armazena dados dos candidatos, incluindo nome, partido, raça, gênero, idade, ocupação, estado e coligação (referenciado por ID). </li>
  <li> <b>Coleção coligacoes:</b> Contém informações das coligações, incluindo o nome e os partidos participantes (referenciados por IDs de outra coleção).</li>
  <li> <b>Coleção partidos:</b> Armazena os nomes dos partidos, referenciados tanto em politicos quanto em coligacoes.</li>
</ul>

## Tecnologias Utilizadas
<ul>
<li> <b>Python:</b> Linguagem principal do projeto, conhecida pela simplicidade e ampla utilização em ciência de dados.</li>
<li> <b>MongoDB:</b> Banco de dados NoSQL, ideal para lidar com grandes volumes de dados semi-estruturados, como informações de candidatos.</li>
<li> <b>PyMongo:</b> Biblioteca que facilita a integração entre Python e MongoDB.</li>
<li> <b>Tkinter:</b> Biblioteca padrão para criação de interfaces gráficas em Python, permitindo uma experiência visual simples e funcional.</li>
</ul>

## Acrescentando a fonte
<p align="justify">
A fonte usada no projeto está junto do pacote, basta pegá-las e acrescentá-las à pasta "Fontes" do Painel de Controles.
</p>

## Dependências
- Python 3.x com suporte ao Tkinter
- Instale as bibliotecas adicionais com:
  ```
  pip install -r requirements.txt
  ```

