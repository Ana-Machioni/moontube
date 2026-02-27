INSERT INTO musica.genero
(NOME,
ICONE,
COR)
VALUES
("POP", "", "PINK"),
("ROCK", "", "BLACK"),
("MPB", "", "YELLOW") ,
("R&B", "", "GRAY");

INSERT INTO musica.musica
(CANTOR,
NOME,
DURACAO,
URL_IMAGEM,
NOME_GENERO,
ATIVO)
VALUES
("Frank Ocean", "Moon River", " 3:08" , "https://musicainstantanea.com.br/wp-content/uploads/2018/02/DWD_2Q_W4AAVRF_-700x697.jpg", "R&B", 0),
("Acid Bath", "Tranquilized", "4:56", "https://cdn-images.dzcdn.net/images/cover/4e075e8edfcd4ce326618ae2e52b7f9b/0x1900-000000-80-0-0.jpg", "ROCK", 0),
("Arctic Monkeys", "I Wanna Be Yours", "4:56", "https://cdn-images.dzcdn.net/images/cover/64e54e307bd5e2bdb27ffeb662fd910d/1900x1900-000000-80-0-0.jpg", "POP", 1),
("Queen", "Bohemian Rhapsody", "4:56", "https://cdn-images.dzcdn.net/images/cover/8f4ec8393fbb35bdc8dd19a84bff1b46/0x1900-000000-80-0-0.jpg", "ROCK",0),
("Chico Buarque", "Construção", "4:56", "https://upload.wikimedia.org/wikipedia/pt/7/75/Constru%C3%A7%C3%A3o_chico_buarque.jpg", "MPB", 0);