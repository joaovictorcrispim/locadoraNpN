from Infra.repository.filme_repository import FilmeRepository
from Infra.configs.connection import DBConnectionHandler
from Infra.entities.models import Filme, Ator


repo = FilmeRepository()
data_base = DBConnectionHandler()

filme_1 = Filme(
    titulo='Barbie',
    genero='Comédia',
    ano=2023
)

filme_2 = Filme(
    titulo='Spawn',
    genero='Ação',
    ano=1997
)

margot=Ator(
    nome='Margot Robbie',
    nascimento=1990,
)

ryan=Ator(
    nome='Ryan Gosling',
    nascimento=1987
)
atores=[margot, ryan]

filme_1.atores=atores
filme_2.atores.append(ryan)

todos_filmes = [filme_2, filme_1]
filmes = repo.select_all()

repo.insert(todos_filmes)

filme = repo.select_one(filmes[0])
print(filme)


repo.delete(filme)
