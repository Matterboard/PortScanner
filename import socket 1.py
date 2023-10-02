import socket

def scan_port(ip_address, port):
  """
  Scan un port pour voir s'il est ouvert.

  Args:
    ip_address: L'adresse IP de la cible.
    port: Le numéro de port à scanner.

  Returns:
    True si le port est ouvert, False sinon.
  """

  try:
    # Créer une socket TCP.
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Essayer de se connecter au port.
    socket_client.connect((ip_address, port))

    # Si la connexion est établie, le port est ouvert.
    return True

  finally:
    # Fermer la socket.
    socket_client.close()


def main():
  # Demander à l'utilisateur l'adresse IP et le numéro de port à scanner.
  ip_address = input("Adresse IP : ")
  port = int(input("Numéro de port : "))

  # Scanner le port.
  is_open = scan_port(ip_address, port)

  # Afficher le résultat.
  if is_open:
    print("Le port {} est ouvert.".format(port))
  else:
    print("Le port {} est fermé.".format(port))


if __name__ == "__main__":
  main()
