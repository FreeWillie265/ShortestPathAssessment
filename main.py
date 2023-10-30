from graph import Graph


def add_vertices(graph: Graph):
    graph.add_vertex("Mchinji")     # 0
    graph.add_vertex("Kasungu")     # 1
    graph.add_vertex("Ntchisi")     # 2
    graph.add_vertex("Nkhotakota")  # 3
    graph.add_vertex("Dowa")        # 4
    graph.add_vertex("Salima")      # 5
    graph.add_vertex("Lilongwe")    # 6
    graph.add_vertex("Dedza")       # 7
    graph.add_vertex("Ntcheu")      # 8


def add_edges(graph: Graph):
    # Mchinji
    graph.add_edge(0, 1, 141)
    graph.add_edge(0, 6, 109)

    # Kasungu
    graph.add_edge(1, 2, 66)
    graph.add_edge(1, 4, 117)

    # Ntchisi
    graph.add_edge(2, 4, 38)
    graph.add_edge(2, 3, 66)

    # Nkhotakota
    graph.add_edge(3, 5, 112)

    # Dowa
    graph.add_edge(4, 5, 67)
    graph.add_edge(4, 6, 55)

    # Salima
    graph.add_edge(5, 7, 96)

    # Lilongwe
    graph.add_edge(6, 7, 92)

    # Dedza
    graph.add_edge(7, 8, 74)

    # Ntcheu's edge has already been defined at Dedza




if __name__ == '__main__':
    exit_program = '1'

    graph = Graph()
    add_vertices(graph)
    add_edges(graph)

    while exit_program == '1':
        print("Choose a district from the following: \n"
              "Mchinji, Lilongwe, Kasungu, Dowa, Ntchisi \n"
              "Dedza, Ntcheu, Nkhotakota, Salima")
        source = input("Enter the source district: ")
        destination = input("Enter the destination district: ")

        graph.execute(source, destination)

        exit_program = input("\n"
                             "Re-Try? \n "
                             "1 for yes, any other character to exit: ")
