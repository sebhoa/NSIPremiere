# Scripts d'administration

## Gestion des qcm

* [Ajouter une question](http://localhost/Commun/ajout_qcm.html)

* Partie barre de navigation du fichier mkdocs.yml :
 
{{ genere_nav() }}

## Ubuntu Lycée

```bash
sudo apt-get update
sudo apt-get install openssh-server
sudo ufw allow ssh
sudo systemctl enable ssh
sudo systemctl start ssh
```