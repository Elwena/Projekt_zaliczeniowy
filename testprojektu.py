
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


### DANE TESTOWE
valid_firstname = "Marcin"
valid_lastname = "Nowak"
valid_gender = "female"
valid_country_code = "+48"
valid_phone = "123123234"
valid_password = 'Qwerty1232@'
valid_country = "Polska"

invalid_email = "kashkfhash.pl"

# Scenariusz testowy:
# Rejestracja na stronie wizzair.com
class WizzairRegistration(unittest.TestCase):
    # Warunki wstępne:
    def setUp(self):
        # 1. Uruchomiona przeglądarka
        self.driver = webdriver.Chrome()
        # Maksymalizacja okna
        self.driver.maximize_window()
        # 2. Na stronie https://wizzair.com/pl-pl#/
        self.driver.get("https://wizzair.com/pl-pl#/")

        # Włączenie implicitly wait - mechanizmu czekania na elementy max. 60 sekund
        self.driver.implicitly_wait(60)

    # Przypadek testowy 001:
    # Rejestracja przy użyciu błędnego adresu e-mail
    def testInvalidEmail(self):
        driver = self.driver
        # KROKI:
        # 1. Kliknij przycisk ZALOGUJ SIĘ
        # Metoda odszuka element i zwraca WebElement
        zaloguj_btn = driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        zaloguj_btn.click()
        # 2. Kliknij REJESTRACJA
        driver.find_element_by_css_selector('button[data-test="registration"]').click()
        # 3. Wpisz imię
        imie_input = driver.find_element_by_name('firstName')
        imie_input.send_keys(valid_firstname)
        # 4. Wpisz nazwisko
        nazwisko_input = driver.find_element_by_name('lastName')
        nazwisko_input.send_keys(valid_lastname)
        # 5. Wybierz płeć
        if valid_gender == "male":
            # wybierz faceta
            imie_input.click()
            driver.find_element_by_xpath('//label[@data-test="register-gendermale"]').click()
        else:
            # Wybierz kobietę
            nazwisko_input.click()
            driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]').click()
        # 6. Wpisz kod kraju
        driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]').click()
        cc_input = driver.find_element_by_name('phone-number-country-code')
        cc_input.send_keys(valid_country_code, Keys.RETURN)
        # 7. Wpisz nr telefonu
        phone_input = driver.find_element_by_name('phoneNumberValidDigits')
        phone_input.send_keys(valid_phone)
        # 8. Wpisz nieprawidłowy adres e-mail (brak znaku '@')
        email_input = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        email_input.click()
        email_input.send_keys(invalid_email)
        # 9. Wpisz hasło
        psswd_input = driver.find_element_by_name('password')
        psswd_input.send_keys(valid_password)
        # 10. Wybierz narodowość
        country_input = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        country_input.click()
        # Lista WebElementów
        countries = driver.find_elements_by_xpath('//div[@class="register-form__country-container__locations"]/label')
        # Iterujemy po liście WebElementów
        for label in countries:
            # Szukamy wewnątrz WebElementu [label]
            option = label.find_element_by_tag_name('strong')

            # Debugowy print - pobranie atrybutu innerText
            # print(option.get_attribute('innerText'))

            # Jeśli tekst elementu to kraj, który chcemy wybrać
            if option.get_attribute('innerText') == valid_country:
                # Przewiń do tego kraju
                option.location_once_scrolled_into_view
                # Kliknij w niego
                option.click()
                # Przerwij pętle
                break
        # UWAGA! TUTAJ BĘDZIE PRAWDZIWY TEST !!!!
        # Wyszukuję wszystkie błędy
        error_messages = driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        # Tworzę listę WIDOCZNYCH komunikatów
        visible_error_notices = list() # Pusta lista
        for error in error_messages:
            # Jeśli komunikat jest widoczny
            if error.is_displayed():
                # Dodajemy ten komunikat do listy WIDOCZNYCH
                visible_error_notices.append(error)

        # Sprawdzam, czy ta lista WIDOCNYCH komunikatów zawiera tylko jeden błąd
        # "czysty" Python
        assert len(visible_error_notices) == 1, "Liczba widocznych komunikatów nie zgadza się!"
        # Z wykorzystaniem unittesta
        self.assertEqual(len(visible_error_notices), 1, msg="Liczba widocznych komunikatów nie zgadza się!")
        # Sprawdzam treść błędu
        self.assertEqual(visible_error_notices[0].text, "Nieprawidłowy adres e-mail")


        # Poczekaj 3 sekudny
        sleep(3)

    def tearDown(self):
        # Zakończenie testu
        self.driver.quit()

# Jeśli uruchamiamy z tego pliku
if __name__ == "__main__":
    # Użyjmy metody main(), która zajmie się resztą
    unittest.main(verbosity=2)

    # Użyjmy metody main(), która zajmie się resztą
    unittest.main(verbosity=2)
