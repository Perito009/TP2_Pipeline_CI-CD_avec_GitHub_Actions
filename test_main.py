import pytest
from main import hello
import time


# Test basique de la fonction hello sans argument
def test_hello():
    assert hello() == "Hello, GitHub Actions!"


# Test avec un nom personnalisé
def test_hello_custom_name():
    assert hello("EPSI") == "Hello, EPSI!"


# Test avec une erreur de type attendue
def test_hello_type_error():
    with pytest.raises(TypeError):
        hello(123)


# Test de performance : s'assurer que l'appel est rapide
def test_hello_performance():
    start = time.time()
    for _ in range(1000):
        hello("EPSI")
    duration = time.time() - start
    assert duration < 1


# Test pour vérifier la gestion du prénom et nom complet
def test_hello_full_name():
    assert hello("Jane", "Smith") == "Hello, Jane Smith!"

# Fin du fichier (bonne pratique : ajouter une ligne vide à la fin)
