Feature: Оценка

  Scenario: Вход на страницу просмотра Оценки
    Given Я открыл страницу "Оценка"
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    Then Я должен быть на странице "Оценка"

  Scenario: Создание
    Given Я перехожу на страницу создания Оценки
    When Я ввожу текст "2" в поле "value"
    And Я ввожу текст "NewCreate" в поле "description"
    Then Я нажимаю на кнопку "Создать"
    Then Я должен быть на странице "Оценка"

  Scenario: Обновление
    Given Я открыл страницу "Оценка"
    Then Я нажимаю на кнопку "Обновить-2"
    When Я очищаю поле "value"
    And Я ввожу текст "3" в поле "value"
    And Я очищаю поле "description"
    And Я ввожу текст "NewUpdate" в поле "description"
    And Я отправляю форму
    Then Я должен быть на странице "Оценка"

    Scenario: Удаление
    Given Я открыл страницу "Оценка"
    Then Я нажимаю на кнопку "Удалить-2"
    When Я нажимаю на кнопку "Да"
    Then Я должен быть на странице "Оценка"
