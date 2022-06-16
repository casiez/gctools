import json

# Sauvegarde fichier JSON
def saveJSON(data: object, file: str) -> None:
  with open(file, 'w') as fp:
      json.dump(data, fp, ensure_ascii=False)

# Chargement de fichiers JSON
def loadJSON(file: str) -> list:
  try:
    with open(file) as json_file:
        data = json.load(json_file)
    return data
  except:
    print("Cound not load %s"%file)
    return []