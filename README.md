# Serveur de reconnaissance facial

Ce travail est une application de la reconnaissance facial.
- Dans main.py on trouve un program qui fait la comparaison de quelque photo de test contre une photo de referance
- Dans server.py on trouve un rest api qui prend comme requet une image de referance est des image de test; il les compare et envoie une reponse selon le resultat de la comparaison

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

    pip install cv2
    pip install face_recognition
    pip install flask

## Usage

    python main.py (pour les images locaux)
    python server.py (pour le serveur des images)