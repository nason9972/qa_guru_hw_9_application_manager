from selene import browser, have


class ApplicationManagerPage:
    def __init__(self):
        self.user_name = browser.element('#userName')
        self.user_email = browser.element('#userEmail')
        self.user_current_address = browser.element('#currentAddress')
        self.user_permanent_address = browser.element('#permanentAddress')
        self.submit = browser.element('#submit')
        self.table = browser.element('#output')

    def open(self):
        browser.open('/text-box')
        return self

    def simple_registration_form(self):
        self.user_name.type('Ivan')
        self.user_email.type('ivanov@gmail.com')
        self.user_current_address.type('Moscow, st.Lenina, 23')
        self.user_permanent_address.type('Moscow, st.Lenina, 23')
        self.submit.click()
        return self

    def should_registration_user(self):
        self.table.should(have.text('Ivan'))
        self.table.should(have.text('ivanov@gmail.com'))
        self.table.should(have.text('Moscow, st.Lenina, 23'))
        return self
