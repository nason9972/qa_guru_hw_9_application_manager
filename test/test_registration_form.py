from model.application_manager import ApplicationManagerPage


def test_simple_registration_form(config_browser):
    app = ApplicationManagerPage()
    app.open()

    #WHEN
    app.simple_registration_form()
    #THEN
    app.should_registration_user()
