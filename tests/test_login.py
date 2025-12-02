def test_valid_login(login_page):
    login_page.open()
    login_page.enter_email("admin@mineral.com")
    login_page.enter_password("123456")
    login_page.click_login()

    assert "dashboard" in login_page.page.url.lower()


def test_invalid_login(login_page):
    login_page.open()
    login_page.enter_email("admin@mineral.com")
    login_page.enter_password("wrong123")
    login_page.click_login()

    # Wait for the error message containing specific text
    selector = "li:has-text('These credentials do not match')"
    login_page.page.wait_for_selector(selector)
    
    # Get the error text
    error_text = login_page.page.inner_text(selector)

    # Assert the expected message is in the error text
    assert "these credentials do not match" in error_text.lower()



def test_empty_fields(login_page):
    login_page.open()
    login_page.enter_email("")     # empty
    login_page.enter_password("")  # empty
    login_page.click_login()

    login_page.page.wait_for_selector(".invalid-feedback")
    error_text = login_page.get_error_text()

    assert "email" in error_text.lower() or "required" in error_text.lower()
