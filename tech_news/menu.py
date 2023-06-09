import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)

menu = {
    0: "Popular o banco com notícias",
    1: "Buscar notícias por título",
    2: "Buscar notícias por data",
    3: "Buscar notícias por categoria",
    4: "Listar top 5 categorias",
    5: "Sair.",
}

mensagens = {
    0: "Digite quantas notícias serão buscadas:\n",
    1: "Digite o título:\n",
    2: "Digite a data no formato aaaa-mm-dd:\n",
    3: "Digite a categoria:\n",
}


def handle_special_options(option: int) -> list[str] | None:
    if option == 4:
        return top_5_categories()

    else:
        print("Encerrando script\n")
        SystemExit()


def analyzer_menu():
    functionalities = [
        get_tech_news,
        search_by_title,
        search_by_date,
        search_by_category,
        top_5_categories,
    ]

    try:
        option = int(
            input("Selecione uma das opções a seguir:\n" + "".join(
                    [(f" {key} - {menu[key]};\n") for key in menu]
                )
            )
        )

        if option in menu and option > 3:
            return handle_special_options(option)

        parameter = input(f"{mensagens[option]}")
        return functionalities[option](parameter)
    except (KeyError, ValueError):
        sys.stderr.write("Opção inválida\n")
