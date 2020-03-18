Feature: Социальные Статусы

  Scenario: Вход на страницу просмотра Социальные Статусы
    Given Я открыл страницу "Социальный Статус"
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    Then Я должен быть на странице "Социальный Статус"

  Scenario: Создание
    Given Я перехожу на страницу создания Социального Статуса
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    When Я ввожу текст "NewCreate" в поле "name"
    Then Я нажимаю на кнопку "Создать"
    Then Я должен быть на странице "Социальный Статус"

  Scenario: Обновление
    Given Я открыл страницу "Социальный Статус"
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    Then Я нажимаю на кнопку "Обновить-2"
    When Я очищаю поле "name"
    And Я ввожу текст "NewUpdate" в поле "name"
    And Я отправляю форму
    Then Я должен быть на странице "Социальный Статус"

  Scenario: Удаление
    Given Я открыл страницу "Социальный Статус"
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    Then Я нажимаю на кнопку "Удалить-2"
    When Я нажимаю на кнопку "Да"
    Then Я должен быть на странице "Социальный Статус"