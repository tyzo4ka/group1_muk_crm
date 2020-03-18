Feature: Аудитория

  Scenario: Вход на страницу просмотра Аудитории
    Given Я открыл страницу "Аудитория"
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    Then Я должен быть на странице "Аудитория"

  Scenario: Создание
    Given Я перехожу на страницу создания Аудитории
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    When Я ввожу текст "NewCreate" в поле "name"
    And Я ввожу текст "35" в поле "places"
    And Я ввожу текст "CreateTest" в поле "description"
    Then Я нажимаю на кнопку "Создать"
    Then Я должен быть на странице "Аудитория"

  Scenario: Обновление
    Given Я открыл страницу "Аудитория"
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    Then Я нажимаю на кнопку "Обновить-2"
    When Я очищаю поле "name"
    And Я ввожу текст "NewUpdate" в поле "name"
    And Я очищаю поле "places"
    And Я ввожу текст "33" в поле "places"
    And Я очищаю поле "description"
    And Я ввожу текст "NewUpdate" в поле "description"
    And Я отправляю форму
    Then Я должен быть на странице "Аудитория"

  Scenario: Удаление
    Given Я открыл страницу "Аудитория"
    When Я ввожу текст "admin" в поле "username"
    And Я ввожу текст "admin" в поле "password"
    And Я отправляю форму
    Then Я нажимаю на кнопку "Удалить-2"
    When Я нажимаю на кнопку "Да"
    Then Я должен быть на странице "Аудитория"