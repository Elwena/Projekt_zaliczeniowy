# Automatyzacja przypadku testowego przy pomocy Selenium Webdriver

# Tworzymy Przypadek testowy
# Scenariusz testowy: Rejestracja na stronie wizzair.com


# Tytuł: Rejestracja nowego użytkownika używając niepoprawnego adresu e-mail
# Środowisko: Chrome wersja 90.0.4430.212,  Ubuntu 20.04.2 LTS
# Warunki wstępne:
# Uruchomiona przeglądarka na stronie https://wizzair.com/pl-pl#/
# Użytkownik nie jest zalogowany.
# Kroki:
# 1.Kliknij przycisk "ZALOGUJ SIĘ"

# 2. Kliknij "REJESTRACJA"
# 3. Wpisz imię
# 4. Wpisz nazwisko
# 5. Wybierz płeć
# 6. Wpisz kod kraju
# 7. Wpisz nr telefonu
# 8. Wprowadź niepoprawny e-mail (brak znaku'@')
# 9. Wpisz hasło
# 10. Wybierz narodowość


#  Oczekiwany rezultat:
# Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny

#  II. Automatyzacja przypadku testowego przy pomocy Selenium Webdriver

#  import unittest
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys


### DANE TESTOWE
#  valid_firstname
#  valid_lastname
#  valid_gender
#  valid_country_code
#  valid_phone
#  valid_password
#  valid_country

#  invalid_email =

# Scenariusz testowy:
# Rejestracja na stronie wizzair.com class WizzairRegistration(unittest.TestCase):

# Warunki wstępne:
# def setUp(self):
# 1. Uruchomiona przeglądarka self.driver = webdriver.Chrome()
# Maksymalizacja okna self.driver.maximize_window()
# 2. Na stronie https://wizzair.com/pl-pl#/ self.driver.get("https://wizzair.com/pl-pl#/")
