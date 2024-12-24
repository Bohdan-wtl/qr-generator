from pytest import fixture

from pages.admin_page import AdminPage
from pages.login_page import LogInPage
from pages.main_page import MainPage
from pages.menu_page import MenuPage
from pages.my_account_page import AccountPage
from pages.my_qr_codes_page import MyQrCodesPage
from pages.payment_page import PaymentPage
from pages.plans_and_prices_page import PlanAndPricesPage
from pages.qr_creation_flow_page import QrCreationPage
from pages.register_page import RegisterPage


class BaseTest:
    _main_page = None
    _admin_page = None
    _login_page = None
    _menu_page = None
    _account_page = None
    _my_qr_codes_page = None
    _payment_page = None
    _plan_and_prices_page = None
    _qr_creation_page = None
    _register_page = None

    @fixture(autouse=True)
    def setup(self, request, page):
        request.cls.page = page

    @property
    def main_page(self):
        if self._main_page is None:
            self._main_page = MainPage(self.page)
        return self._main_page

    @property
    def admin_page(self):
        if self._admin_page is None:
            self._admin_page = AdminPage(self.page)
        return self._admin_page

    @property
    def login_page(self):
        if self._login_page is None:
            self._login_page = LogInPage(self.page)
        return self._login_page

    @property
    def menu_page(self):
        if self._menu_page is None:
            self._menu_page = MenuPage(self.page)
        return self._menu_page

    @property
    def my_account_page(self):
        if self._account_page is None:
            self._account_page = AccountPage(self.page)
        return self._account_page

    @property
    def my_qr_codes_page(self):
        if self._my_qr_codes_page is None:
            self._my_qr_codes_page = MyQrCodesPage(self.page)
        return self._my_qr_codes_page

    @property
    def payment_page(self):
        if self._payment_page is None:
            self._payment_page = PaymentPage(self.page)
        return self._payment_page

    @property
    def plan_and_prices_page(self):
        if self._plan_and_prices_page is None:
            self._plan_and_prices_page = PlanAndPricesPage(self.page)
        return self._plan_and_prices_page

    @property
    def qr_creation_page(self):
        if self._qr_creation_page is None:
            self._qr_creation_page = QrCreationPage(self.page)
        return self._qr_creation_page

    @property
    def register_page(self):
        if self._register_page is None:
            self._register_page = RegisterPage(self.page)
        return self._register_page
