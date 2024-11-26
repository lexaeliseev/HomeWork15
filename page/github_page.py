from selene import browser, be


class GitHubPage:
    def __init__(self):
        pass

    @staticmethod
    def desktop_window():
        browser.element('.HeaderMenu-link--sign-up').should(be.visible).click()
        browser.element('[name="user[email]"]').should(be.visible)

    def mobile_window(self):
        browser.element('.Button-label').should(be.visible).click()
        self.desktop_window()
