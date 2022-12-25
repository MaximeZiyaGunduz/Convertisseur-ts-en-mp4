# Convertisseur-ts-en-mp4

# Convertisseur de fichiers vidéo
Ce script Python permet de convertir des fichiers vidéo d'un format à un autre en utilisant FFmpeg.

# Prérequis
Avant de pouvoir exécuter ce script, assurez-vous d'avoir installé les éléments suivants sur votre ordinateur:
## Roadmap

- Python
- FFmpeg
- subprocess (fait partie de la bibliothèque standard de Python)
- os (fait partie de la bibliothèque standard de Python)
- ffmpeg (installation requise: pip install ffmpeg)
- time (fait partie de la bibliothèque standard de Python)

# Utilisation
Pour utiliser ce script, vous devrez modifier la valeur de la variable dirPath afin qu'elle pointe vers le répertoire contenant les fichiers vidéo à convertir. Vous devrez également modifier la valeur de la variable sorti afin qu'elle pointe vers l'emplacement où vous souhaitez enregistrer les fichiers vidéo convertis.

Une fois ces modifications effectuées, vous pouvez exécuter le script en utilisant la commande python nom_du_script.py.

Le script parcourra tous les fichiers du répertoire spécifié dans dirPath, et convertira chacun d'entre eux au format MP4 en utilisant FFmpeg. Les fichiers originaux seront ensuite supprimés. Le script affichera également le nombre de fichiers convertis et le temps total de conversion.

# En savoir plus sur FFmpeg
Pour en savoir plus sur FFmpeg et ses possibilités, consultez la documentation de FFmpeg.
