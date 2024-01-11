from businnes.peliculas import lista_peliculas

def listar_peliculas_por_genero():
    tipo_genero = input("Ingrese el tipo de género a buscar: ")

    peliculas_encontradas = [pelicula for pelicula in lista_peliculas.values() if tipo_genero in pelicula.get("Generos", {}).values()]

    if peliculas_encontradas:
        print(f"Películas encontradas para el género '{tipo_genero}':")
        for pelicula in peliculas_encontradas:
            print(f"ID: {pelicula['Id']}, Nombre: {pelicula['Nombre pelicula']}")
    else:
        print(f"No se encontraron películas para el género '{tipo_genero}'.")


def listar_peliculas_por_actor():
    nombre_actor = input("Ingrese el nombre del actor a buscar: ")

    peliculas_encontradas = []

    for pelicula in lista_peliculas.values():
        actores_en_pelicula = pelicula.get("Actores", {}).values()

        for actor in actores_en_pelicula:
            if actor.get("Nombre Actor") == nombre_actor:
                peliculas_encontradas.append(pelicula)

    if peliculas_encontradas:
        print(f"Películas encontradas para el actor '{nombre_actor}':")
        for pelicula in peliculas_encontradas:
            print(f"ID: {pelicula['Id']}, Nombre: {pelicula['Nombre pelicula']}")
    else:
        print(f"No se encontraron películas para el actor '{nombre_actor}'.")
        
        
def buscar_pelicula_mostrar_info():

    id_pelicula = input("Ingrese el ID de la película a buscar: ")

    pelicula = lista_peliculas.get(id_pelicula)

    if pelicula:
        print(f"Información de la película '{pelicula['Nombre pelicula']}':")
        print(f"Sinopsis: {pelicula.get('Sinopsis', 'No disponible')}")
        
        actores = pelicula.get("Actores", {})
        if actores:
            print("Actores:")
            for actor_id, actor_info in actores.items():
                print(f"  - {actor_info.get('Nombre Actor', 'Sin nombre')}, Rol: {actor_info.get('Rol', 'Sin rol')}")
        else:
            print("No hay información de actores para esta película.")
    else:
        print(f"No se encontró una película con el ID '{id_pelicula}'.")

