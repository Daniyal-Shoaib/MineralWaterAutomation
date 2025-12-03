import time
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



def test_dashboard_elements(login_page):
    # Login
    login_page.open()
    login_page.enter_email("admin@mineral.com")
    login_page.enter_password("123456")
    login_page.click_login()

    # ASSERT login success
    assert "dashboard" in login_page.page.url.lower()
    time.sleep(20)

    # Wait for Dashboard to fully load
    login_page.page.wait_for_selector("text=Total Users")

    # Verify important dashboard boxes exist
    dashboard_items = [
        "Total Users",
        "Customers",
        "Products",
        "Orders",
        "Total Payments",
        "Bottles Issued",
        "Bottles Returned",
        "Bottle Balance",
        "Expenses",
        "Routes",
        "Customer Routes",
    ]

    for item in dashboard_items:
        assert login_page.page.is_visible(f"text={item}")

