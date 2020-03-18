from behave import given, then


@given('Я открыл страницу "Дисциплина"')
def open_login_page(context):
    context.browser.get('http://134.122.82.126/disciplines/')


@then('Я должен быть на странице "Дисциплина"')
def should_be_at_list_page(context):
    assert context.browser.current_url == "http://134.122.82.126/disciplines/"


@given('Я перехожу на страницу создания Дисциплины')
def should_be_at_main(context):
    context.browser.get('http://134.122.82.126/disciplines/add/')
