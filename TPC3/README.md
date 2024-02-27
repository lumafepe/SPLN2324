## Gerador de templates para packages python

package que disponibiliza o comando ```templateMaker```
este tem as flags:
- -f ficheiro ```.py``` que contem a função ```main```
- -n nome do modulo a criar
- -c nome do comando executavel
- -u username do desenvolvedor de codigo
- -e email do desenvolvedor de codigo

No caso de existir o ficheiro ```.METADATA.json``` na root do computador que contenha as keys ```Username``` e ```Email``` as flags e e u serão ignoradas. Caso uma flag não seja adicionada o valor será pedido posteriormente no input.

O programa ira mover todos os documentos da pasta atual para uma nova pasta com o <nome do programa> / <nome do programa>. 
Na base da primeira pasta será criado um ```pyproject.toml``` só faltando as dependencias por preencher, assim como um ```README.md``` vazio.
Dentro da pasta <nome do programa> o ficheiro que continha a função main passa a ser chamado ```__init__.py```, e passa a ter no seu inicio os headers nesserarios para ser instalado pelo ```PIP```, entre os quais sinopse,versão e executavel de python.
