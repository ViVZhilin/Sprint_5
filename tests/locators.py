from selenium.webdriver.common.by import By

class Locators:

    PERSONAL_PAGE = (By.LINK_TEXT, "Личный Кабинет") #Кнопка "Личный кабинет"
    CONSTRUCTOR_PAGE = (By.LINK_TEXT, "Конструктор") #Кнопка "Конструктор"
    REGISTRATION_BUTTON = (By.LINK_TEXT, "Зарегистрироваться") #Кнопка "Зарегистрироваться"
    PASSWORD_RECOVER_BUTTON = (By.LINK_TEXT, "Восстановить пароль") #Кнопка "Восстановить пароль"
    EMAIL_INPUT_ACTIVE = (By.XPATH, ".//label[contains(text(), 'Email')]") #Блок отображения Email
    EMAIL_INPUT = (By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default input_status_active']/input") #Поле ввода Email
    NAME_INPUT = (By.XPATH, ".//input[@name = 'name']") #Поле ввода имени
    PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']") #Поле ввода пароля
    LOGIN_BUTTON = (By.LINK_TEXT, "Войти") #Кнопка "Войти"
    LOGIN_BUTTON_ON_LOGIN_PAGE = (By.XPATH, ".//form[@class = 'Auth_form__3qKeq mb-20']/button") #Кнопка "Войти" на странице логина
    PERSONAL_EMAIL_DATA = (By.XPATH, ".//ul[@class = 'Profile_profileList__3vTor']/li[2]/div/div/input") #Поле отображения Email пользователя в личном кабинете
    PERSONAL_EMAIL_FIELD = (By.XPATH, ".//div[@class = 'input pr-6 pl-6 input_type_text input_size_default input_status_disabled']") #Поле с данными Email
    EMAIL_FIELD = (By.XPATH, ".//label[contains(text(), 'Email')]") #Значение поля Email пользователя в личном кабинете
    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//form/fieldset[3]/div/p[@class = 'input__error text_type_main-default']") #Сообщение об ошибке при неверном пароле
    EMAIL_ERROR_MESSAGE = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']/p[@class = 'input__error text_type_main-default']") #Сообщение об ошибке при неверном Email
    LOGO = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']") #Логотип
    SOUS_TITLE_BLOCK = (By.XPATH, "//h2[text()='Соусы']") #Заголовок блока соусов в конструкторе
    FILLINGS_TITLE_BLOCK = (By.XPATH, "//h2[text()='Начинки']")#Заголовок блока начинок в конструкторе
    BUNS_TITLE_BLOCK = (By.XPATH, "//h2[text()='Булки']") #Заголовок блока булок в конструкторе
    SOUS_TITLE = (By.XPATH, "//div/span[text()='Соусы']/parent::div") #Заголовок раздела соусов
    FILLINGS_TITLE = (By.XPATH, "//div/span[text()='Начинки']/parent::div") #Заголовок раздела начинок в конструкторе
    BUNS_TITLE = (By.XPATH, "//div/span[text()='Булки']/parent::div") #Заголовок раздела булок в конструкторе
    LOGIN_BUTTON_ON_MAIN_PAGE = (By.XPATH, ".//div[@class = 'BurgerConstructor_basket__container__2fUl3 mt-10']/button") #Кнопка "Войти" на главной странице
    LOGIN_BUTTON_ON_REGISTRATION_PAGE = (By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") #Кнопка "Войти" на странице регистрации
