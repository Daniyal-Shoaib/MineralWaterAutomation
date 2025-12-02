class LoginPage:

    def __init__(self, page):
        self.page = page
        self.url = "https://mineral.hassancontractingco.com/login"

        self.email_input = "#email"
        self.password_input = "#password"
        self.login_button = "button.btn-water"
        self.error_message = ".invalid-feedback"  # Adjust if needed

    def open(self):
        self.page.goto(self.url)

    def enter_email(self, email):
        self.page.fill(self.email_input, email)

    def enter_password(self, password):
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.click(self.login_button)

    def get_error_text(self):
        return self.page.text_content(self.error_message)
