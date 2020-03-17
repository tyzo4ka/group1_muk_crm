Feature: Дисциплина

  Scenario: Вход на страницу просмотра Дисциплины
    Given Я открыл страницу "Дисциплина"
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    Then Я должен быть на странице "Дисциплина"

  Scenario: Создание
    Given Я перехожу на страницу создания Дисциплины
    When Я ввожу текст "NewCreate" в поле "name"
    And Я ввожу текст "Айдай Исаева" в поле "teacher"
    And Я отправляю форму
    Then Я должен быть на странице "Дисциплина"

  Scenario: Обновление
    Given Я открыл страницу "Дисциплина"
    Then Я нажимаю на кнопку "Обновить"
    When Я очищаю поле "name"
    And Я ввожу текст "NewUpdate" в поле "name"
    And Я очищаю поле "teacher"
    And Я ввожу текст "Айдай Исаева" в поле "teacher"
    And Я отправляю форму
    Then Я должен быть на странице "Дисциплина"

    Scenario: Удаление
    Given Я открыл страницу "Дисциплина"
    Then Я нажимаю на кнопку "Удалить"
    When Я нажимаю на кнопку "Да"
    Then Я должен быть на странице "Дисциплина"