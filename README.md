# Aapplication de test de l'api Azure Content Moderator sur un contenu textuel

## Contexte

L'application permet de tester l'implémentation de l'api Azure Content Moderator en utilisant des requêtes HTTP.
Elle est basée sur une autre [application préexistante de publication de contenus en base de données développée par les équipe de la société Sahar](https://github.com/sahar-team/MSP-2-APP)

## Lancement de l'application 

### directement en local 
Après réalisation d'un clone du repository, lancez la commande depuis le dossier cloné 

```
pip install -r requirements.txt
```

Pour installer la package python nécessaires.

Ensuite lancer la commande pour démarrer l'applicaton
```
flask run 
```

### Via la création, le lancement d'un conteneur dockeur 

Après réalisation d'un clone du repository, lancez la commande depuis le dossier cloné
pour construire l'image de conteneur
 
```
docker build -t <nom-de-l-image> .

```

Puis lancez la commande suivante pour démarer le conteneur de l'application

```
docker run -it -v “$(pwd):/app” --name <nom-de-l-imgae> -p 5000:5000 <nom-du-conteneur>
```
## Point de vigilance :

Les identifiants de l'api sont à intégrer dans un fichier .env. Celui-ci sera appelé via le package python-dotenv