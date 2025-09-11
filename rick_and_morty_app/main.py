import requests

def get_character(character_id):
  url = f"https://rickandmortyapi.com/api/character/{character_id}"
  res = requests.get(url)
  if res.status_code == 200:
    data = res.json()
    print(f"Name: {data['name']}")
    print(f"Status: {data['status']}")
    print(f"Species: {data['species']}")
    print(f"Origin: {data['origin']['name']}")
  else:
    print("Character not found.")

if __name__ == "__main__":
  char_id = input("Enter a Rick and Morty character ID: ")
  get_character(char_id)