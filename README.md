Port Scanner Cyber - Projet 2e année

Scanner de ports simple en Python** réalisé dans le cadre de mes études en cybersécurité.

   Objectif
Détecter les ports ouverts sur une machine cible (utilisé en reconnaissance / pentest).

   Fonctionnalités
- Scan d’une plage de ports configurable
- Interface en ligne de commande (CLI)
- Gestion des timeouts
- Code propre et commenté

   Comment l'utiliser

```bash
# Installer les dépendances (aucune ici !)
python port_scanner.py 127.0.0.1 -p 1-500
# Ou pour des ports spécifiques
python port_scanner.py [scanme.nmap.org](http://scanme.nmap.org) -p 80,443,8080
