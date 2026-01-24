class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Error fiero!: {err}")


#lanzando la excepcion personalizada de arriba
try:
    raise MiExcepcion("LOLLL")
except:
    print("apa")

