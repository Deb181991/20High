import time

import allure
import select
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.Assertion import assertion
from Utilities.GenericMethod import genericmethod
from Utilities.customLogger import LogGen
from Utilities.readproperty import ReadConfig

# from selenium.webdriver.support.select import Select

# from webdriver_manager import driver
# from webdriver_manager.chrome import ChromeDriverManager

myLogger = LogGen.loggeen()
DateTime = time.ctime()

# SrnRd = ScreenRecord()


baseURL = ReadConfig.getURL()


# myScreenshot = pyautogui.screenshot()
# keyboard = pynput.keyboard.Controller()
# Driver.get(baseURL)

class LoginPage:

    def __init__(self, driver: object) -> object:
        """

        :rtype: object
        """
        self.driver = driver
        self.genericMethod = genericmethod(driver)
        self.assertion = assertion(driver)
        self.act = ActionChains(driver)
        # self.SrnRd = ScreenRecord()
        # self.Api_helper = Api_helper()

    ##*************************************************************************##
    #############################"""""""""XPATH""""""""##########################
    #############################"""""""""Login Page""""""""##########################

    def Username(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='username']")

    def Proceed(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")

    def getPassword(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='password']")

    def LoginBtn(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(),'Login')]")

    def hover_dashboards(self):
        self.genericMethod.MouseHoverAndClick(LoginPage.DashboardMenubtn(self))

    def hover_deliverytimeliness(self):
        self.genericMethod.MouseHoverAndClick(LoginPage.delivery_timeliness(self))

    def MovetoFilter(self):
        self.genericMethod.MouseHoverAndClick(LoginPage.DashboardFilter(self))

    def CheckETD(self):
        self.genericMethod.click(LoginPage.delivery_etd_click(self))

    def CheckETA(self):
        self.genericMethod.click(LoginPage.delivery_eta_click(self))

    def apply_delivery_filter(self):
        self.genericMethod.click(LoginPage.ApplyDeliveryFilter(self))

    def close_delivery_filter(self):
        self.genericMethod.click(LoginPage.CloseDeliveryFilter(self))

    def CloseDeliveryFilter(self):
        return self.driver.find_element(By.XPATH, "(//button[@aria-label='Close']//em)[2]")

    def ApplyDeliveryFilter(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Apply ']")

    def DashboardFilter(self):
        return self.driver.find_element(By.XPATH, "// *[@id = 'dashboardFilter']")

    def delivery_etd_click(self):
        return self.driver.find_element(By.XPATH, "//input[@formcontrolname='isETDChecked']")

    def delivery_eta_click(self):
        return self.driver.find_element(By.XPATH, "//input[@formcontrolname='isETAChecked']")

    def DashboardMenubtn(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'Dashboard')]")

    def delivery_timeliness(self):
        return self.driver.find_element(By.XPATH, "(//button[@data-bs-target='#dashboardFilter'])[1]")

    def hover_AtRiskIntransitShipments(self):
        self.genericMethod.MouseHoverAndClick(LoginPage.AtRiskIntransitShipments(self))

    def IntransitCheckETD(self):
        self.genericMethod.click(LoginPage.Intransit_ETD_click(self))

    def IntransitCheckETA(self):
        self.genericMethod.click(LoginPage.intransit_ETA_click(self))

    def apply_transitShipments_filter(self):
        self.genericMethod.click(LoginPage.ApplyAtRiskIn_transitShipmentsFilter(self))

    def close_transitShipments_filter(self):
        self.genericMethod.click(LoginPage.clickclose_transitShipments_filter(self))

    def AtRiskIntransitShipments(self):
        return self.driver.find_element(By.XPATH, "(//phoenix-icons[@name='filter'])[2]")

    def Intransit_ETD_click(self):
        return self.driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")

    def intransit_ETA_click(self):
        return self.driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")

    def ApplyAtRiskIn_transitShipmentsFilter(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Apply ']")

    def clickclose_transitShipments_filter(self):
        return self.driver.find_element(By.XPATH, "(//button[@aria-label='Close'])[2]")

    def dropdown1_dashboard(self):
        self.genericMethod.click(LoginPage.click_dropdown1_dashboard(self))

    # def dropdown_Carrier_Management_Efficiency(self):
    #     self.genericMethod.click(LoginPage.click_dropdown_Carrier_Management_Efficiency(self))
    #
    def pending_filter(self):
        self.genericMethod.click(LoginPage.click_pending_filter(self))

    def Uncheck_BookingDt_filter(self):
        self.genericMethod.click(LoginPage.BookingDt_fiter_Uncheck(self))

    # def Apply_carrierbooking_filter(self):
    #     self.genericMethod.click(LoginPage.apply_carrierbooking_filter(self))
    #
    # def Close_CarrierBookingsPending(self):
    #     self.genericMethod.click(LoginPage.clickClose_CarrierBookingsPending(self))

    def click_dropdown1_dashboard(self):
        return self.driver.find_element(By.XPATH, "(//button[contains(@class,'btn-function-light shadow')])[3]")

    def click_pending_filter(self):
        return self.driver.find_element(By.XPATH, "(//button[@placement='top']/following-sibling::button)[3]")

    def BookingDt_fiter_Uncheck(self):
        return self.driver.find_element(By.XPATH, "(//input[@formcontrolname='isImportantChecked']")

    # def Uncheck_carrierbookingDt_filter(self):
    #     return self.driver.find_element(By.XPATH, "(//div[contains(@class,'btn btn-outline-secondary')]//input)[3]")
    #
    def clickClose_CarrierBookingsPending(self):
        return self.driver.find_element(By.XPATH, "(//em[contains(@class,'bi bi-x-lg')])[2]")

    # def dropdown2_dashboard(self):
    #     self.genericMethod.click(LoginPage.click_dropdown2_dashboard(self))

    # def
    #
    # (self):
    #     return self.driver.find_element(By.XPATH,
    #                                     "((//button[contains(@class,'btn-function-light shadow')]//phoenix-icons)[3]")

    # *************************************************************************************#
    def Orders(self):
        return self.driver.find_element(By.XPATH, "// span[contains(text(), 'Orders')]")

    def OrderType(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='estimatedDateTypeETD']")

    def calendar(self):
        return self.driver.find_element(By.XPATH, "// *[contains( @name, 'calendar')]")

    def Left_Arrow(self):
        return self.driver.find_element(By.XPATH, "(//*[@class='ngb-dp-navigation-chevron'])[1]")

    def Month_Select(self):
        return self.driver.find_element(By.XPATH, "// *[contains( @ title, 'Select month')]")

    def Advanced(self):
        return self.driver.find_element(By.XPATH, "//*[@id='details-button']")

    def Url_link(self):
        return self.driver.find_element(By.XPATH, "//*[@class='small-link']")

    ##################################################################################################
    # ************************************** LOGIN **************************************************#
    def LaunchBrowser(self, TMS_Url):
        self.genericMethod.navigateTo(TMS_Url)
        time.sleep(6)
        self.genericMethod.click(LoginPage.Advanced(self))
        time.sleep(4)
        self.genericMethod.click(LoginPage.Url_link(self))

    def LaunchBrowser2(self):
        BU = baseURL
        self.genericMethod.navigateTo(BU)
        time.sleep(2)

    def enterUserName(self, text):
        self.genericMethod.type(LoginPage.Username(self), text)

    def ClickProceed(self):
        self.genericMethod.click(LoginPage.Proceed(self))

    def enterPassword(self, text):
        self.genericMethod.waitForElementToBeVisible(LoginPage.getPassword(self), 'password')
        self.genericMethod.type(LoginPage.getPassword(self), text)
        allure.attach(self.driver.get_screenshot_as_png(), name="LoginPage", attachment_type=AttachmentType.PNG)

    def clickOnLogin(self):
        self.genericMethod.clickUsingJS(LoginPage.LoginBtn(self))
        time.sleep(3)

        # Cell = 'B5'
        # d = self.genericMethod.READEXCELDATA(Cell)
        # myLogger.info(d)
        # cl = 'D6'
        # V = "RiTiDEBA"
        # self.genericMethod.WRITEEXCELDATA(cl, V)
        # myLogger.info(p)
        # self.genericMethod.CurrentDay()
        # self.genericMethod.duplicate_Tab(1)
        # self.genericMethod.Tab()
        # self.genericMethod.Tab()
        # self.genericMethod.Tab()
        # url3 = "https://couponswala.com/blog/yulu-bike-price-and-rental/"
        # self.genericMethod.switchToTab(1)
        # self.genericMethod.navigateTo(url3)
        # self.genericMethod.switchToTab(0)
        # myLogger.info(a)
        # self.driver.get_screenshot_as_file(".\Fail-ScreenShots\screenshot" + ".png")
        def Dashboard(self):
            self.genericMethod.clickUsingJS(LoginPage.Dashboard(self))
            time.sleep(2)

    # ******************* Rule Set ********************************************************#
    def Planning(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'Planning')]")

    def Rule(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Rule']")

    def CreateRule(self):
        return self.driver.find_element(By.XPATH, "//*[contains(text(),'Create Ruleset')]")

    def RuleSetName(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='ruleSetName']")

    def description(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='description']")

    def PolicyType(self):
        return self.driver.find_element(By.XPATH, "//*[text()= '" + PolicyName + "']")

    def Active_toggle(self):
        return self.driver.find_element(By.XPATH, "//*[contains(@class,'slider round')]")

    def Add(self):
        return self.driver.find_element(By.XPATH, "// *[contains( @class ,'form-check-label')]")

    def descNext(self):
        return self.driver.find_element(By.XPATH, "(//button[text()=' Next '])[1]")

    def consolidation(self):
        # return self.driver.find_element(By.XPATH, "(//span[text()= '" + Srcrule + "'])[1]")
        return self.driver.find_element(By.XPATH, "(//*[text()='Order Status'])[1]")

    def consolidation2(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Mode of Transportation']")

    def Next(self):
        return self.driver.find_element(By.XPATH, "(// *[contains(text(), ' Next ')])[2]")

    def SearchRuleSet(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Search...'])[1]")

    def SearchRuleSet2(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Search...'])[3]")

    def af(self):
        return self.driver.find_element(By.XPATH, "(//*[text()='Customer Code'])[2]")

    def C(self):
        return self.driver.find_element(By.XPATH, "//form[@class='ng-untouched ng-pristine ng-valid']")
        return self.driver.find_element(By.XPATH, "(//input[@placeholder='Search...'])[2]")

    def StatusCheck(self):
        return self.driver.find_element(By.XPATH, "//*[@role='combobox']")

    def CustomerCODE(self):
        return self.driver.find_element(By.XPATH, "//*[@name='Customer Code0value1']")

    def ETD_from_date(self):
        return self.driver.find_element(By.XPATH,
                                        "(// div[contains( @class ,'ngb-dp-month')][1] // span[contains(text(), '" + date + "')])[1]")

    def ETD_tO_date(self):
        return self.driver.find_element(By.XPATH,
                                        "(// div[contains( @class ,'ngb-dp-month')][1] // span[contains(text(), '" + date1 + "')])[1]")

    def ETD_tO_date(self):
        return self.driver.find_element(By.XPATH,
                                        "(// div[contains( @class ,'ngb-dp-month')][1] // span[contains(text(), '" + date1 + "')])[2]")

    def Criteria_Field(self):
        return self.driver.find_element(By.XPATH, "//*[text()= 'Criteria Field']")

    def Finish(self):
        return self.driver.find_element(By.XPATH, "// *[contains(text(), 'Finish')]")

    def Confirm(self):
        return self.driver.find_element(By.XPATH, "//*[text()= 'Confirm ']")

    #
    #############################################################################################
    def clickPlanning(self):
        self.genericMethod.click(LoginPage.Planning(self))
        time.sleep(2)
        # time.sleep(2)

    def clickRule(self):
        self.genericMethod.click(LoginPage.Rule(self))
        time.sleep(4)

    def clickRuleset(self):
        self.genericMethod.click(LoginPage.CreateRule(self))
        time.sleep(2)

    def clickName(self, Name):
        a = Name
        myLogger.info(a)
        c = self.genericMethod.NumIncrement()
        myLogger.info(c)
        global d
        d = a + str(c)
        myLogger.info(d)
        self.genericMethod.type(LoginPage.RuleSetName(self), d)
        # time.sleep(2)

    def clickDescription(self, Description):
        self.genericMethod.type(LoginPage.description(self), Description)
        # time.sleep(2)

    def clickPolicyType(self, Policy_type):
        global PolicyName
        PolicyName = Policy_type
        self.genericMethod.click(LoginPage.PolicyType(self))
        # time.sleep(2)

    def clickActive(self):
        self.genericMethod.click(LoginPage.Active_toggle(self))
        # time.sleep(2)

    def clickOrder(self):
        self.genericMethod.click(LoginPage.Add(self))
        # time.sleep(2)

    def clickNext(self):
        self.genericMethod.click(LoginPage.descNext(self))
        time.sleep(1)

    def clickconsolidation(self, rule):
        self.genericMethod.click(LoginPage.SearchRuleSet(self))
        self.genericMethod.Clear(LoginPage.SearchRuleSet(self))
        self.genericMethod.type(LoginPage.SearchRuleSet(self), rule)
        global Srcrule
        Srcrule = rule
        self.act.click_and_hold(on_element=LoginPage.consolidation(self)).move_to_element(
            LoginPage.consolidation2(self)).pause(2).release(on_element=LoginPage.consolidation2(self)).perform()
        time.sleep(3)

    def Rule_Next(self):
        self.genericMethod.click(LoginPage.Next(self))
        time.sleep(1)

    def DragDropCriteria(self, criteria):
        global Srcrule1
        Srcrule1 = criteria
        self.genericMethod.type(LoginPage.SearchRuleSet2(self), criteria)
        self.act.click_and_hold(on_element=LoginPage.af(self)).move_to_element(
            LoginPage.C(self)).release(on_element=LoginPage.C(self)).perform()
        time.sleep(2)

    def clickcalender(self):
        self.genericMethod.click(LoginPage.calendar(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Left_Arrow(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Left_Arrow(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Left_Arrow(self))
        time.sleep(1)

    def CODEINPUT(self):
        # value = self.genericMethod.NumIncrement()
        # self.genericMethod.type(LoginPage.CustomerCODE(self), value)
        customer = "INV"
        self.genericMethod.type(LoginPage.CustomerCODE(self), customer)
        time.sleep(2)
        # time.sleep(1)

    def slectMonth(self, month):
        drp = Select(LoginPage.Month_Select(self))
        drp.select_by_visible_text(month)
        time.sleep(2)

    def slectDate(self, from_date, to_date):
        global date
        global date1
        date = from_date
        date1 = to_date
        self.genericMethod.click(LoginPage.ETD_from_date(self))
        self.genericMethod.click(LoginPage.ETD_tO_date(self))
        self.genericMethod.click(LoginPage.Criteria_Field(self))

    def Finishbutton(self):
        self.genericMethod.click(LoginPage.Finish(self))
        time.sleep(1)

    def Confirmbutton(self):
        self.genericMethod.click(LoginPage.Confirm(self))
        time.sleep(1)

    # ************************************* Tag2 ********************************************#
    def policy_type(self):
        return self.driver.find_element(By.XPATH, "//*[text()= '" + Policy + "']")

    def Sequence(self):
        return self.driver.find_element(By.XPATH, "//*[text()= '" + d + "']")

    def SequencePos2(self):
        return self.driver.find_element(By.XPATH, "//*[@value='2']")

    def Default_Sequence(self):
        return self.driver.find_element(By.XPATH, "//*[text()= 'Default Ruleset for Sales Orders']")

    def Save_Sequence(self):
        return self.driver.find_element(By.XPATH, "//*[text()= ' Save Sequence ']")

    def SequenceMessage(self):
        return self.driver.find_element(By.XPATH, "//*[@class='toast-body']")

    def Close_Button(self):
        return self.driver.find_element(By.XPATH, "//*[text()= 'Close']")

    def Rule_Set_Name(self):
        return self.driver.find_element(By.XPATH, "// *[text() = ' Rule Set Name ']")

    ##########################################################################################
    def Filterpolicytype(self, policytype):
        global Policy
        Policy = policytype
        myLogger.info(Policy)
        self.genericMethod.click(LoginPage.policy_type(self))
        time.sleep(1)

    def ClickSequence(self):
        self.act.click_and_hold(on_element=LoginPage.Sequence(self)).move_to_element(
            LoginPage.Default_Sequence(self)).release(on_element=LoginPage.SequencePos2(self)).perform()
        time.sleep(1)

    def Click_Savesequence(self):
        self.genericMethod.click(LoginPage.Save_Sequence(self))
        time.sleep(1)

    def sequence_Message(self, sequence):
        expected_status = sequence
        myLogger.info(expected_status)
        actual_status = self.genericMethod.getText(LoginPage.SequenceMessage(self))
        myLogger.info(actual_status)
        if actual_status == expected_status:
            assert True
        else:
            time.sleep(2)
            # allure.attach(self.driver.get_screenshot_as_png(), name="Tr_Status",
            #               attachment_type=AttachmentType.PNG)
            message = "The actual and expected are not matched", "actual->  " + actual_status, 'expected-> ' + expected_status
            assert actual_status == expected_status, message
            time.sleep(2)
            assert False

    def Click_DefaultSequence(self):
        self.act.click_and_hold(on_element=LoginPage.Default_Sequence(self)).move_to_element(
            LoginPage.Sequence(self)).release(on_element=LoginPage.Sequence(self)).perform()
        time.sleep(2)
        self.genericMethod.click(LoginPage.Rule_Set_Name(self))
        time.sleep(2)

    # ************************************* Edit RuleSet ********************************************#

    def Edit_ruleset(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + d + "']/../..//*[@id='edit']")

        # ************************************* Tag3 ********************************************#

    def DeleteButton(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()= '" + Edit_Ruleset + "']/parent::*/following-sibling::td[6]//*[@id='delete']")

    def DeleteIcon(self):
        return self.driver.find_element(By.XPATH, "//button[text()= 'Delete ']")

    def ViewRuleset(self):
        return self.driver.find_element(By.XPATH, "//*[text()= '" + Edit_Ruleset + "']")

        ##########################################################################################

    def Click_viewRuleSet(self):
        self.genericMethod.click(LoginPage.ViewRuleset(self))
        time.sleep(2)
        self.genericMethod.click(LoginPage.Close_Button(self))
        # self.genericMethod.click(LoginPage.Sequence(self))
        time.sleep(1)

    def Click_delete(self):
        self.genericMethod.click(LoginPage.DeleteButton(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.DeleteIcon(self))
        time.sleep(2)
        self.genericMethod.Refresh()

    # ***************************************** Orderrs *******************************************#
    #################################################################################################
    def MouseHover_Order(self):
        self.genericMethod.MouseHover(LoginPage.Orders(self))

    def clickOrders(self):
        self.genericMethod.click(LoginPage.Orders(self))
        time.sleep(2)

        # self.genericMethod.Refresh()

        # ********************** autogenrate_FO_with_the_available_rulesets ****************************#

        # def Filter(self):
        #     return self.driver.find_element(By.XPATH, "//*[@class='bi bi-funnel']")

        def Filter(self):
            return self.driver.find_element(By.XPATH, "//*[@name='filter']")

        # def Filter(self):
        #     return self.driver.find_element(By.XPATH, "//*[@role='submit']")

        def Consolidation_Status(self):
            return self.driver.find_element(By.XPATH, "// *[ @ id = 'consStatus']")

        def from_date1(self):
            return self.driver.find_element(By.XPATH,
                                            "//div[contains(@class,'ngb-dp-month ng-star-inserted')][1]//span[contains(text(),'" + date2 + "')]")

        def to_date1(self):
            return self.driver.find_element(By.XPATH,
                                            "//div[contains(@class,'ngb-dp-month ng-star-inserted')][2]//span[contains(text(),'" + date3 + "')]")

        def FT_date(self):
            return self.driver.find_element(By.XPATH, "// *[contains(text(), 'From / To Date')]")

        def search(self):
            return self.driver.find_element(By.XPATH, "// *[contains( @ type, 'submit')]")

        def Unconsolidated(self):
            return self.driver.find_element(By.XPATH,
                                            "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td//*[contains(@type,'checkbox')]")

        def SaveFORefNo(self):
            return self.driver.find_element(By.XPATH,
                                            "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td//*[contains(@class,'cursor-pointer')]")

        def Unconsolidated2(self):
            return self.driver.find_element(By.XPATH,
                                            "(//ngb-highlight[contains(text(),'Unconsolidated')])[2]/parent::*/preceding-sibling::td//*[contains(@type,'checkbox')]")

        def OrderRefNo(self):
            return self.driver.find_element(By.XPATH,
                                            "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td//*[@class='cursor-pointer']")

        def Origin_Country_City(self):
            return self.driver.find_element(By.XPATH,
                                            "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td/../*[5]")

        def Destination_Country_City(self):
            return self.driver.find_element(By.XPATH,
                                            "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td/../*[6]")

        def CustCodeR(self):
            return self.driver.find_element(By.XPATH,
                                            "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td[6]/*")

        def Consolidate(self):
            return self.driver.find_element(By.XPATH, "// *[contains(text(), 'Consolidate Order')]")

        def Tracking_No(self):
            return self.driver.find_element(By.XPATH, "//*[@class='toast-body']")

        def Fo_Status(self):
            return self.driver.find_element(By.XPATH, "//*[text()='fo created successfully']")

        def notification(self):
            return self.driver.find_element(By.XPATH, "// *[contains( @ alt, 'notification')]")

        def TrSearch(self):
            return self.driver.find_element(By.XPATH, "//*[@id='Capa_1']")

        def SearchBTN_TR(self):
            return self.driver.find_element(By.XPATH,
                                            "//input[@placeholder='Search...']/..//*[@class='form-control form-control-sm ng-untouched ng-pristine ng-valid ng-star-inserted']")

        def notificationCheck(self):
            return self.driver.find_element(By.XPATH, "(// *[contains(text(), 'Request is complete')])[1]")

        def View_Fos(self):
            return self.driver.find_element(By.XPATH, " (//*[contains(text(),'View Fos')])[1]")

        def FO_Number_save(self):
            return self.driver.find_element(By.XPATH, "//*[@class='cursor-pointer']")

        def togglemenu(self):
            return self.driver.find_element(By.XPATH, "//*[@id='togglemenu']")

        def Shipment(self):
            return self.driver.find_element(By.XPATH, "// span[text() = 'Shipment']")

        def FreightOrders(self):
            return self.driver.find_element(By.XPATH, "// a[text() = 'Freight Orders']")

        def RightArrow(self):
            return self.driver.find_element(By.XPATH, "//*[@title='Next month']")

        #################################################################################################
        def ScrollOnPlanning(self):
            self.genericMethod.Refresh()
            time.sleep(1)
            self.genericMethod.click(LoginPage.Planning(self))

        def Sequence_rule_set(self):
            # self.genericMethod.click(LoginPage.PolicyType(self))
            self.genericMethod.click(LoginPage.Default_Sequence(self))
            time.sleep(1)
            self.genericMethod.click(LoginPage.Close_Button(self))
            time.sleep(1)

        def ClickFilter(self):
            self.genericMethod.click(LoginPage.Orders(self))
            time.sleep(1)
            self.genericMethod.click(LoginPage.Filter(self))
            time.sleep(1)

        def ClickconsolidationStatus(self, unconsolidate):
            Con = Select(LoginPage.Consolidation_Status(self))
            Con.select_by_visible_text(unconsolidate)
            # time.sleep(2)

        def ChooseDateTyper(self, DateType):
            # self.genericMethod.click(LoginPage.OrderType(self))
            drp = Select(LoginPage.OrderType(self))
            drp.select_by_visible_text(DateType)
            time.sleep(2)

        # def clickcalender(self):
        #     self.genericMethod.click(LoginPage.calendar(self))
        #     time.sleep(2)

        # def slectMonth(self, month):
        #     drp = Select(LoginPage.Month_Select(self))
        #     drp.select_by_visible_text(month)
        #     time.sleep(2)
        #
        def ChooseDate(self, from_date1, to_date1):
            global date2
            global date3
            date2 = from_date1
            date3 = to_date1
            self.genericMethod.click(LoginPage.from_date1(self))
            self.genericMethod.click(LoginPage.RightArrow(self))
            time.sleep(1)
            # self.genericMethod.click(LoginPage.RightArrow(self))
            # time.sleep(1)
            # self.genericMethod.click(LoginPage.RightArrow(self))
            # time.sleep(1)
            # self.genericMethod.click(LoginPage.RightArrow(self))
            self.genericMethod.click(LoginPage.to_date1(self))
            self.genericMethod.click(LoginPage.FT_date(self))

        def searchButton(self):
            self.genericMethod.click(LoginPage.search(self))
            time.sleep(1)

        def order_orderline(self) -> object:
            global country
            global city
            global Dest_country
            global Dest_city
            self.genericMethod.click(LoginPage.Unconsolidated(self))
            v = self.genericMethod.getText(LoginPage.SaveFORefNo(self))
            myLogger.info(v)
            self.genericMethod.WriteData(".//TestData//FORefNumber.json", "OrderRefNumber", v)
            Country_City = self.genericMethod.getText(LoginPage.Origin_Country_City(self))
            dest_Con_City = self.genericMethod.getText(LoginPage.Destination_Country_City(self))
            v = Country_City.split("|")
            country = v[0].strip(" ") + "-"
            self.genericMethod.WriteData(".//TestData//OriginCountry.json", "OriginCountry", country)
            city = v[1].strip(" ") + "-"
            self.genericMethod.WriteData(".//TestData//OriginCity.json", "OriginCity", city)
            a = dest_Con_City.split("|")
            Dest_country = a[0].strip(" ") + "-"
            self.genericMethod.WriteData(".//TestData//DestinationCountry.json", "Dest_country", Dest_country)
            Dest_city = a[1].strip(" ") + "-"
            self.genericMethod.WriteData(".//TestData//DestinationCity.json", "Dest_city", Dest_city)
            custCode = self.genericMethod.getText(LoginPage.CustCodeR(self))
            self.genericMethod.WriteData(".//TestData//Customer.json", "Customer", custCode)

        def Order_Reference_Number(self):
            global OrdRefNo
            OrdRefNo = self.genericMethod.getText(LoginPage.OrderRefNo(self))
            myLogger.info(OrdRefNo)
            self.genericMethod.WriteData(".//TestData//OrderRefNumber.json", "OrderRefNumber", OrdRefNo)

        def consolidationButton(self):
            self.genericMethod.click(LoginPage.Consolidate(self))
            time.sleep(2)

        def Tr_No(self):
            global c1
            v1 = self.genericMethod.getText(LoginPage.Tracking_No(self))
            myLogger.info(v1)
            c1 = v1.split("-")
            expected_status = "Order Consolidation Initiated"
            actual_status = c1[0]
            myLogger.info(actual_status)
            myLogger.info(c1[1])
            if actual_status == expected_status:
                assert True
            else:
                time.sleep(2)
                allure.attach(self.driver.get_screenshot_as_png(), name="Tr_Status",
                              attachment_type=AttachmentType.PNG)
                message = "The actual and expected are not matched", "actual->  " + actual_status, 'expected-> ' + expected_status
                assert actual_status == expected_status, message
                time.sleep(2)
                assert False

        def notificationButton(self):
            self.genericMethod.click(LoginPage.notification(self))
            time.sleep(4)
            self.genericMethod.click(LoginPage.TrSearch(self))
            time.sleep(1)
            self.genericMethod.type(LoginPage.SearchBTN_TR(self), c1[1])
            # time.sleep(1)
            # self.genericMethod.click(LoginPage.notificationCheck(self))
            time.sleep(1)
            self.genericMethod.click(LoginPage.View_Fos(self))
            time.sleep(2)
            global fo
            fo = self.genericMethod.getText(LoginPage.FO_Number_save(self))
            myLogger.info(fo)
            self.genericMethod.click(LoginPage.togglemenu(self))
            time.sleep(1)

        def NotificationClick(self):
            self.genericMethod.click(LoginPage.notification(self))
            time.sleep(4)
            self.genericMethod.click(LoginPage.View_Fos(self))
            time.sleep(2)
            self.genericMethod.click(LoginPage.togglemenu(self))
            time.sleep(1)

        def Notification_Click(self):
            self.genericMethod.click(LoginPage.notification(self))
            time.sleep(2)

        # ***********************************     Manually create_FO_from_orders     **************************************#
        def FrieghtOrder(self):
            return self.driver.find_element(By.XPATH, "//*[text()='Create Freight Order']")

        def OrderCreate(self):
            return self.driver.find_element(By.XPATH, "//*[text()=' Create From Orders ']")

        def proceedButton(self):
            return self.driver.find_element(By.XPATH, "//*[text()=' Proceed '] ")

        def FoHeader(self):
            return self.driver.find_element(By.XPATH, "//*[text()='FO Header']")

        def PartyDetails(self):
            return self.driver.find_element(By.XPATH, "//*[text()='Party Details']")

        def ShipperAttentionTo(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperAttentionTo']")

        def ShipperBECode(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperBeCode']")

        def shipperName(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperName']")

        def shipperPhone(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperPhone']")

        def shipperMobile(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperMobile']")

        def shipperEmail(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperEmail']")

        def shipperFax(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperFax']")

        def consigneeAttentionTo(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeAttentionTo']")

        def consigneeBECode(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeBeCode']")

        def consigneeName(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeName']")

        def consigneePhone(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneePhone']")

        def consigneeMobile(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeMobile']")

        def consigneeEmail(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeEmail']")

        def consigneeFax(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeFax']")

        def Save_Proceed(self):
            return self.driver.find_element(By.XPATH, "//*[text()=' Save & Proceed ']")

        def Itemselect(self):
            return self.driver.find_element(By.XPATH, "//*[@class='c-p ng-star-inserted'][1]/./td[3]")

        def ItemDetails(self):
            return self.driver.find_element(By.XPATH, "//*[text()='Item Details']")

        def HandlingDetails(self):
            return self.driver.find_element(By.XPATH, "//*[text()='Handling Details']")

        def O_D_Details(self):
            return self.driver.find_element(By.XPATH, "//*[text()='Origin & Destination']")

        def checkPartyDetails(self):
            return self.driver.find_element(By.XPATH, "(//*[text()='Party Details'])[2]")

        def LoadDetails(self):
            return self.driver.find_element(By.XPATH, "//*[text()='Load & Discharge (AIR/SEA)']")

        def SaveAllDetails(self):
            return self.driver.find_element(By.XPATH, "//*[@id='save']")

        def DetailsSaveOrderline(self):
            return self.driver.find_element(By.XPATH, "//*[text()=' Save ']")

        def Toast_Message(self):
            return self.driver.find_element(By.XPATH, "//*[@class='toast-body']")

        ###########################################################################################################
        def CreateFreightOrder(self):
            self.genericMethod.click(LoginPage.FrieghtOrder(self))
            time.sleep(1)

        def Create_Order(self):
            self.genericMethod.click(LoginPage.OrderCreate(self))
            time.sleep(2)
            self.genericMethod.click(LoginPage.Filter(self))
            time.sleep(1)

        def proceed(self):
            self.genericMethod.click(LoginPage.proceedButton(self))
            time.sleep(1)

        def Mousehoverfoheader(self):
            self.genericMethod.click(LoginPage.FoHeader(self))
            time.sleep(1)

        def clickPartyDetailsPage(self, ShipperAttention, ShipperBECode, ShipperName, ShipperPhone, ShipperMobile,
                                  ShipperEmail, ShipperFax, ConsigneeAttention, ConsigneeBECode, ConsigneeName,
                                  ConsigneePhone, ConsigneeMobile, ConsigneeEmail, ConsigneeFax):
            self.genericMethod.click(LoginPage.PartyDetails(self))
            time.sleep(1)
            self.genericMethod.type(LoginPage.ShipperAttentionTo(self), ShipperAttention)

            self.genericMethod.type(LoginPage.ShipperBECode(self), ShipperBECode)

            self.genericMethod.type(LoginPage.shipperName(self), ShipperName)

            self.genericMethod.type(LoginPage.shipperPhone(self), ShipperPhone)

            self.genericMethod.type(LoginPage.shipperMobile(self), ShipperMobile)

            self.genericMethod.type(LoginPage.shipperEmail(self), ShipperEmail)

            self.genericMethod.type(LoginPage.shipperFax(self), ShipperFax)

            self.genericMethod.type(LoginPage.consigneeAttentionTo(self), ConsigneeAttention)

            self.genericMethod.type(LoginPage.consigneeBECode(self), ConsigneeBECode)

            self.genericMethod.type(LoginPage.consigneeName(self), ConsigneeName)

            self.genericMethod.type(LoginPage.consigneePhone(self), ConsigneePhone)

            self.genericMethod.type(LoginPage.consigneeMobile(self), ConsigneeMobile)

            self.genericMethod.type(LoginPage.consigneeEmail(self), ConsigneeEmail)

            self.genericMethod.type(LoginPage.consigneeFax(self), ConsigneeFax)

        def saveandprocced(self):
            self.genericMethod.click(LoginPage.Save_Proceed(self))
            time.sleep(1)

        def item(self):
            self.genericMethod.click(LoginPage.Itemselect(self))
            time.sleep(1)

        def bookingdetails(self):
            self.genericMethod.click(LoginPage.Itemselect(self))
            time.sleep(2)

        def itemdetails(self):
            self.genericMethod.click(LoginPage.ItemDetails(self))
            time.sleep(2)

        def handlingdetails(self):
            self.genericMethod.click(LoginPage.HandlingDetails(self))
            time.sleep(2)

        def originanddestination(self):
            self.genericMethod.click(LoginPage.O_D_Details(self))
            time.sleep(2)

        def Party_detailscheck(self):
            self.genericMethod.click(LoginPage.checkPartyDetails(self))
            time.sleep(2)

        def loadanddischarge(self):
            self.genericMethod.click(LoginPage.LoadDetails(self))
            time.sleep(2)

        def saveButton(self):
            self.genericMethod.click(LoginPage.SaveAllDetails(self))
            time.sleep(1)

        def saveDetails(self):
            self.genericMethod.click(LoginPage.DetailsSaveOrderline(self))
            time.sleep(1)

        def ToastMessage(self, message):
            Expected = message
            Actual = self.genericMethod.getText(LoginPage.Toast_Message(self))
            if Actual == Expected:
                assert True
            else:
                # time.sleep(2)
                message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
                assert Actual == Expected, message
                time.sleep(2)
                assert False

        def ManuallFOSave(self):
            global ManuallFO
            ManuallFO = self.genericMethod.getText(LoginPage.FO_Number_save(self))
            myLogger.info(ManuallFO)
            # self.genericMethod.WriteData(".//TestData//EquipmentID.json", "EquipmentID", d)
            time.sleep(1)

        # ********************************* Edit_FO  ************************************************
        def FO_EDIT(self):
            return self.driver.find_element(By.XPATH, "//*[@id='edit']")

        def REF_FOLINE(self):
            return self.driver.find_element(By.XPATH, "(//td[text()=' SO '])[1]")

        ###########################################################################################################
        def EditFO(self):
            self.genericMethod.click(LoginPage.FO_EDIT(self))
            time.sleep(1)

        def FOItemClick(self):
            # global FO
            # FO = self.genericMethod.ReadData(".//TestData//FORefNumber.json", "OrderRefNumber")
            # myLogger.info("****************" + s)
            self.genericMethod.click(LoginPage.REF_FOLINE(self))
            time.sleep(1)

        def party_details(self):
            self.genericMethod.click(LoginPage.PartyDetails(self))
            time.sleep(1)

        def shippername(self, shipper_name):
            self.genericMethod.click(LoginPage.shipperName(self))
            # self.genericMethod.Clear()
            self.genericMethod.type(LoginPage.shipperName(self), shipper_name)
            time.sleep(1)

        def consigneename(self, consignee_name):
            self.genericMethod.click(LoginPage.consigneeName(self))
            self.genericMethod.type(LoginPage.consigneeName(self), consignee_name)
            time.sleep(1)

        # ********************************* Delete_FO  ************************************************

        def FoField(self):
            return self.driver.find_element(By.XPATH, "//th[text()=' FO #']")

        def close(self):
            return self.driver.find_element(By.XPATH, "(//*[@id='close'])[1]")

        def SinglecheckBox(self):
            return self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[2]")

        def SingleDelete(self):
            return self.driver.find_element(By.XPATH,
                                            "(//*[@ type='checkbox'])[2]//parent::*/following-sibling::td[12]//*[@id='delete']")

        def viewFo(self):
            return self.driver.find_element(By.XPATH,
                                            "(//*[@ type='checkbox'])[2]//parent::*/following-sibling::td[13]//*[@type]")

        def UOM(self):
            return self.driver.find_element(By.XPATH, "//th[text()='UOM'][1]")

        def RefOrder(self):
            return self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[4]//parent::*/following-sibling::td[2]")

        def OrderRefference(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='item']")

        def Status_OrderRefference(self):
            return self.driver.find_element(By.XPATH,
                                            "//*[text()='" + b + "']/.././/parent::*/following-sibling::td[7]")

        def DeleteFO_Button(self):
            return self.driver.find_element(By.XPATH, "//*[@id='delete']")

        # NEWLY ADDED
        def Ref_Check_Box(self):
            return self.driver.find_element(By.XPATH,
                                            "(//*[@type='checkbox'])[1]")

        #################################################################################################
        def freightButon(self):
            self.genericMethod.Refresh()
            time.sleep(3)
            self.genericMethod.click(LoginPage.Planning(self))
            time.sleep(1)
            self.genericMethod.click(LoginPage.Shipment(self))
            time.sleep(1)
            self.genericMethod.click(LoginPage.FreightOrders(self))
            time.sleep(1)

        def FOEnter(self):
            self.genericMethod.type(LoginPage.OrderRefference(self), ManuallFO)
            self.act.send_keys(Keys.ENTER).perform()
            time.sleep(2)
            self.genericMethod.click(LoginPage.search(self))
            time.sleep(2)

        def DeleteFO(self):
            self.genericMethod.click(LoginPage.DeleteFO_Button(self))
            time.sleep(1)
            self.genericMethod.click(LoginPage.DeleteIcon(self))
            time.sleep(1)

        def SaveOrderNumber(self):
            self.genericMethod.click(LoginPage.FoField(self))
            self.genericMethod.click(LoginPage.close(self))
            self.genericMethod.click(LoginPage.SinglecheckBox(self))
            self.genericMethod.click(LoginPage.viewFo(self))
            time.sleep(2)
            self.genericMethod.click(LoginPage.RefOrder(self))
            global b
            b = self.genericMethod.getText(LoginPage.RefOrder(self))
            myLogger.info(b)
            time.sleep(2)

        def singleFO(self):
            self.genericMethod.click(LoginPage.SinglecheckBox(self))
            self.genericMethod.click(LoginPage.SingleDelete(self))
            time.sleep(1)
            self.genericMethod.click(LoginPage.DeleteIcon(self))

        def SelectmultipleFO(self):
            self.genericMethod.click(LoginPage.FoField(self))

        def orderrepository(self):
            # self.genericMethod.click(LoginPage.Planning(self))
            # self.genericMethod.click(LoginPage.Orders(self))
            # time.sleep(2)
            self.genericMethod.click(LoginPage.OrderRefference(self))
            # self.act.send_keys(Keys.ENTER).perform()

        def ORDERREFNUM(self, refnumber):
            # Ref1 = "501865"
            # Ref2 = "501805"
            self.genericMethod.type(LoginPage.OrderRefference(self), refnumber)
            self.act.send_keys(Keys.ENTER).perform()
            time.sleep(3)
            # self.genericMethod.type(LoginPage.OrderRefference(self), refnumber)
            # self.act.send_keys(Keys.ENTER).perform()
            # time.sleep(1)

        def OrderReFNumberSearch(self):
            self.genericMethod.click(LoginPage.search(self))
            time.sleep(2)
            # self.genericMethod.click(LoginPage.Ref_Check_Box(self))
            # time.sleep(1)

        def RefCheckBoxM(self):
            self.genericMethod.click(LoginPage.Ref_Check_Box(self))
            time.sleep(2)

        def OrderReFNumberstatus(self, status):
            expected = status
            actual = self.genericMethod.getText(LoginPage.Status_OrderRefference(self))
            myLogger.info(actual)
            if actual == expected:
                assert True
            else:
                time.sleep(1)
                allure.attach(self.driver.get_screenshot_as_png(), name="Status",
                              attachment_type=AttachmentType.PNG)
                message = "The actual and expected are not matched", "actual->  " + actual, 'expected-> ' + expected
                assert actual == expected, message
                assert False
                time.sleep(1)

            # self.genericMethod.click(LoginPage.search(self))
            # time.sleep(1)

        # ******************************************* Load ********************************************#
        def Loads(self):
            return self.driver.find_element(By.XPATH, "//span[text()='Loads']")

        def Planloads(self):
            return self.driver.find_element(By.XPATH, "//*[text()='Plan Load']")

        def ActiveOnly(self):
            return self.driver.find_element(By.XPATH, "//*[text()=' Show Active Only ']/parent::*//*[@type='checkbox']")

        ################################################################################################
        def LoadsButton(self):
            self.genericMethod.click(LoginPage.Loads(self))
            time.sleep(8)

        def PlanloadsButton(self):
            self.genericMethod.click(LoginPage.Planloads(self))
            time.sleep(1)

        def showactiveonlyButton(self):
            self.genericMethod.click(LoginPage.ActiveOnly(self))
            time.sleep(1)

        # ******************************************* Load ********************************************#
        def New_Workbench(self):
            return self.driver.find_element(By.XPATH, "//*[text()=' Create New Workbench']")

        def workbenchTitle(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='workbenchTitle']")

        def workbenchDesc(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='workbenchDesc']")

        def Requested_ETA(self):
            return self.driver.find_element(By.XPATH, "//*[@formcontrolname='estimatedDateTypeETA']")

        # def Requested_ETA_Month(self):
        #     return self.driver.find_element(By.XPATH, "(// *[contains( @name, 'calendar')])[2]")

        def Requested_ETA_Calender(self):
            return self.driver.find_element(By.XPATH, "(// *[contains( @name, 'calendar')])[2]")

        def fromdate2(self):
            return self.driver.find_element(By.XPATH, "//span[normalize-space(text())='" + date4 + "']")

        def todate2(self):
            return self.driver.find_element(By.XPATH, "//span[normalize-space(text())='" + date5 + "']")

        def Arrfromdate2(self):
            return self.driver.find_element(By.XPATH,
                                            "//div[contains(@class,'ngb-dp-month ng-star-inserted')][1]//span[contains(text(),'" + date6 + "')]")

        def Arrtodate2(self):
            return self.driver.find_element(By.XPATH,
                                            "//div[contains(@class,'ngb-dp-month ng-star-inserted')][1]//span[contains(text(),'" + date7 + "')]")

        def AddManually(self):
            return self.driver.find_element(By.XPATH, "//*[text()='Add Manually']")

        def OriginCountry(self):
            return self.driver.find_element(By.XPATH, "//*[@placeholder='Enter the Country Name']")

        def Origincountrycode(self):
            return self.driver.find_element(By.XPATH, "//*[text()='" + originCtr_Code + "']")

        def Fetch_Country(self):
            return self.driver.find_element(By.XPATH, "//a[@class='ng-star-inserted']")

        def OriginCity(self):
            return self.driver.find_element(By.XPATH, "//*[@placeholder='Enter the City Name']")

        def OCity(self):
            return self.driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']")

        def OriginCityCode(self):
            return self.driver.find_element(By.XPATH, "//*[text()='" + Oricitycode + "']")

        def PlusButton(self):
            return self.driver.find_element(By.XPATH, "//*[@class='bi bi-plus-lg']")

        def LoadTrack(self):
            return self.driver.find_element(By.XPATH, "//*[text()='Load']")

        def UnLoadTrack(self):
            return self.driver.find_element(By.XPATH, "(//*[text()='Unload'])[1]")

        def Dest_Country(self):
            return self.driver.find_element(By.XPATH, "(//*[@placeholder='Enter the Country Name'])[1]")

        def Destcountrycode(self):
            return self.driver.find_element(By.XPATH, "//*[text()='" + DestCtr_Code + "']")

        def DestCity(self):
            return self.driver.find_element(By.XPATH, "(//*[@placeholder='Enter the City Name'])[1]")

        def DestCityCode(self):
            return self.driver.find_element(By.XPATH, "//*[text()='" + Destcitycode + "']")

        def DC(self):
            return self.driver.find_element(By.XPATH, "//a[@class='ng-star-inserted']")

        def SearchUNL_L(self):
            return self.driver.find_element(By.XPATH, "//*[text()=' Search ']")

        def FO_Choose(self):
            return self.driver.find_element(By.XPATH, "//*[text()= '" + fo + "']/..//*[@type='checkbox']")

        def ManuallFO_Choose(self):
            return self.driver.find_element(By.XPATH, "//*[text()= '" + ManuallFO + "']/..//*[@type='checkbox']")

        def Fo_lineClick(self):
            return self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[2]")

        def Add_Foline(self):
            return self.driver.find_element(By.XPATH, "//*[text()=' Add FO Lines to Workbench ']")

        def XYAxis(self):
            return self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[6]")

        def Save_Proceed1(self):
            return self.driver.find_element(By.XPATH, "(//*[text()=' Save & Proceed '])[1]")

        def Rout_Site1(self):
            return self.driver.find_element(By.XPATH, "(//*[@name='site'])[1]")

        def Value1(self):
            return self.driver.find_element(By.XPATH, "(//*[@name='site'])[1]/.//option[@value='1']")

        def Rout_Site2(self):
            return self.driver.find_element(By.XPATH, "(//*[@name='site'])[2]")

        def Value2(self):
            return self.driver.find_element(By.XPATH, "(//*[@name='site'])[1]/.//option[@value='0']")

        def SaveRouteAs(self):
            return self.driver.find_element(By.XPATH, "//*[text()=' Save Route As ']")

        def RouteName(self):
            return self.driver.find_element(By.XPATH, "//*[@placeholder='Route Name']")

        def RouteSave(self):
            return self.driver.find_element(By.XPATH, "//*[text()=' Save ']")

        def RLSave_Proceed(self):
            return self.driver.find_element(By.XPATH, "(//*[text()=' Save & Proceed '])[2]")

        # def Equipment_CheckBox(self):
        #     return self.driver.find_element(By.XPATH, "//*[text()='Equipment']/..//*[@id='inlineCheckbox1']")
        def Equipment_CheckBox(self):
            return self.driver.find_element(By.XPATH, "(//*[@class='first-col']//*[@type='checkbox'])[2]")

        def Equipment_ID(self):
            return self.driver.find_element(By.XPATH,
                                            "(//*[@class='first-col']//*[@type='checkbox'])[2]/../..//parent::*/following-sibling::td[2]")

        def Equipment_AVL(self):
            z

        return self.driver.find_element(By.XPATH,
                                        "(//*[@class='first-col']//*[@type='checkbox'])[2]/parent::*/../..//*[@type='number']")

    def Save_WB(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save Equipment ']")

    def GenerateLoadPaln(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Generate Load Plan ']")

    def MaxTime(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Max. Evalution Time (In Sec):']/..//*[@type='number']")

    def ExpandLoadResult(self):
        return self.driver.find_element(By.XPATH, "//*[@class='d-flex justify-content-start']")

    def ThreeDloadplan(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' View 3D Load Plan ']")

    def Animated(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='animate']")

    def ItemSizeCheckBox(self):
        # return self.driver.find_element(By.XPATH, "//*[@value='" + equipment + "']")
        return self.driver.find_element(By.XPATH, "//*[text()='Equipment Type']/..//*[@type='checkbox']")

    def SaveResult(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save Result ']")

    def GenerateLoad(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Generate Load']")

    def GENERATELoadMessage(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Load(s) saved successfully.']")

    def SAVEresult(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save Result ']")

    def TRNO_CLEAR(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Search...']")

    #########################################################################################################
    def workbench(self):
        self.genericMethod.click(LoginPage.New_Workbench(self))
        time.sleep(2)

    def workbench_Titel(self, title):
        a = title
        c = self.genericMethod.NumIncrement()
        global WBtitle
        WBtitle = a + str(c)
        self.genericMethod.WriteData(".//TestData//WBTitle.json", "WorkBenchTitle", WBtitle)
        self.genericMethod.type(LoginPage.workbenchTitle(self), WBtitle)
        time.sleep(1)

    def workbench_descprition(self, descprition):
        a = descprition
        c = self.genericMethod.NumIncrement()
        global WBdesc
        WBdesc = a + str(c)
        self.genericMethod.type(LoginPage.workbenchDesc(self), WBdesc)
        time.sleep(1)

    def workbenchcustomer(self, customer):
        customerName = self.genericMethod.ReadData(".//TestData//Customer.json", "Customer")
        self.genericMethod.type(LoginPage.CustomerBox(self), customer)
        # self.act.send_keys(Keys.BACKSPACE).perform()
        # time.sleep(2)
        # self.genericMethod.click(LoginPage.Customer_option(self))

    def Depature_Date(self, from_date2, to_date2):
        global date4
        global date5
        date4 = from_date2
        date5 = to_date2
        self.genericMethod.click(LoginPage.fromdate2(self))
        self.genericMethod.click(LoginPage.RightArrow(self))
        self.genericMethod.click(LoginPage.RightArrow(self))
        self.genericMethod.click(LoginPage.todate2(self))
        self.genericMethod.click(LoginPage.workbenchTitle(self))
        time.sleep(2)

    def RequestedETA(self, DateTypeETA):
        self.genericMethod.click(LoginPage.workbenchTitle(self))
        drp = Select(LoginPage.Requested_ETA(self))
        drp.select_by_visible_text(DateTypeETA)
        time.sleep(2)

    def ETA_calender(self):
        self.genericMethod.click(LoginPage.Requested_ETA_Calender(self))

    def RequestedETA_Month(self, month2):
        drp3 = Select(LoginPage.Month_Select(self))
        drp3.select_by_visible_text(month2)
        time.sleep(2)

    def Arrival_Date(self, from_date3, to_date3):
        global date6
        global date7
        date6 = from_date3
        date7 = to_date3
        self.genericMethod.click(LoginPage.Arrfromdate2(self))
        self.genericMethod.click(LoginPage.Arrtodate2(self))
        self.genericMethod.click(LoginPage.workbenchTitle(self))
        time.sleep(2)

    def Add_Mannualy(self):
        self.genericMethod.click(LoginPage.AddManually(self))
        time.sleep(1)

    def Origin_Country(self):
        self.genericMethod.click(LoginPage.OriginCountry(self))
        global originCtr_Code
        global Oricitycode
        global r2
        originCtr_Code = self.genericMethod.ReadData(".//TestData//OriginCountry.json", "OriginCountry")
        self.genericMethod.type(LoginPage.OriginCountry(self), originCtr_Code)
        v = self.genericMethod.getText(LoginPage.Fetch_Country(self))
        Cell = 'B4'
        self.genericMethod.WRITEEXCELDATA_XLSM(Cell, v)
        self.genericMethod.click(LoginPage.Origincountrycode(self))

        time.sleep(2)
        Oricitycode = self.genericMethod.ReadData(".//TestData//OriginCity.json", "OriginCity")
        self.genericMethod.type(LoginPage.OriginCity(self), Oricitycode)
        self.genericMethod.click(LoginPage.OriginCityCode(self))
        self.genericMethod.click(LoginPage.OriginCity(self))
        c = self.genericMethod.getText(LoginPage.OCity(self))
        Cell = 'C4'
        self.genericMethod.WRITEEXCELDATA_XLSM(Cell, c)
        r = c.split("-")
        r2 = r[1]
        myLogger.info(r2)
        time.sleep(3)
        self.genericMethod.click(LoginPage.OCity(self))
        time.sleep(1)

    def SelectLoad(self):
        self.genericMethod.click(LoginPage.LoadTrack(self))
        self.genericMethod.click(LoginPage.PlusButton(self))
        time.sleep(1)

    def DestCountry(self):
        self.genericMethod.click(LoginPage.Dest_Country(self))
        global DestCtr_Code
        global Destcitycode
        global r3
        DestCtr_Code = self.genericMethod.ReadData(".//TestData//DestinationCountry.json", "Dest_country")
        self.genericMethod.type(LoginPage.Dest_Country(self), DestCtr_Code)
        v = self.genericMethod.getText(LoginPage.Fetch_Country(self))
        Cell = 'E4'
        self.genericMethod.WRITEEXCELDATA_XLSM(Cell, v)
        self.genericMethod.click(LoginPage.Destcountrycode(self))
        # c = self.genericMethod.getText(LoginPage.DCountry(self))
        # r = c.split("-")
        # r2 = r[1]
        # myLogger.info(r2)
        # self.genericMethod.click(LoginPage.DCountry(self))
        time.sleep(1)
        Destcitycode = self.genericMethod.ReadData(".//TestData//DestinationCity.json", "Dest_city")
        self.genericMethod.type(LoginPage.DestCity(self), Destcitycode)
        self.genericMethod.click(LoginPage.DestCityCode(self))
        self.genericMethod.click(LoginPage.DestCity(self))
        d = self.genericMethod.getText(LoginPage.DC(self))
        Cell = 'F4'
        self.genericMethod.WRITEEXCELDATA_XLSM(Cell, d)
        r1 = d.split("-")
        r3 = r1[1]
        myLogger.info(r3)
        self.genericMethod.click(LoginPage.DC(self))

    def SelectUNLoad(self):
        self.genericMethod.click(LoginPage.UnLoadTrack(self))
        self.genericMethod.click(LoginPage.PlusButton(self))
        time.sleep(1)

    def searchBTN(self):
        self.genericMethod.click(LoginPage.SearchUNL_L(self))
        time.sleep(1)

    def ListFO(self):
        self.genericMethod.click(LoginPage.FO_Choose(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Add_Foline(self))
        time.sleep(1)

    def ListManuallFO(self):
        self.genericMethod.click(LoginPage.ManuallFO_Choose(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Add_Foline(self))
        time.sleep(1)

    def xy_Axis_click(self):
        self.genericMethod.click(LoginPage.XYAxis(self))
        time.sleep(1)

    def save_proceed(self):
        self.genericMethod.click(LoginPage.Save_Proceed1(self))
        time.sleep(1)

    def Route_Leg(self):
        RL = Select(LoginPage.Rout_Site1(self))
        RL.select_by_index(0)
        self.act.send_keys(Keys.ARROW_DOWN).perform()
        self.act.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        RL1 = Select(LoginPage.Rout_Site2(self))
        RL1.select_by_index(1)
        self.act.send_keys(Keys.ARROW_UP).perform()
        self.act.send_keys(Keys.ENTER).perform()
        time.sleep(1)

    def RouteSaveAS(self):
        self.genericMethod.click(LoginPage.SaveRouteAs(self))
        time.sleep(1)

    def RouteNameEnter(self, routeName):
        a = routeName
        c = self.genericMethod.NumIncrement()
        global routeName1
        routeName1 = a + str(c)
        myLogger.info(routeName1)
        self.genericMethod.type(LoginPage.RouteName(self), routeName1)
        time.sleep(1)
        self.genericMethod.click(LoginPage.RouteSave(self))

    def RL_save_proceed(self):
        self.genericMethod.click(LoginPage.RLSave_Proceed(self))
        time.sleep(1)

    def equipmentType(self):
        self.genericMethod.click(LoginPage.Equipment_CheckBox(self))
        d = self.genericMethod.getText(LoginPage.Equipment_ID(self))
        self.genericMethod.WriteData(".//TestData//EquipmentID.json", "EquipmentID", d)
        time.sleep(1)
        v = "8"
        self.genericMethod.type(LoginPage.Equipment_AVL(self), v)
        self.genericMethod.Clear(LoginPage.MaxTime(self))
        time.sleep(2)
        MaxSec = "5"
        self.genericMethod.type(LoginPage.MaxTime(self), MaxSec)
        self.genericMethod.click(LoginPage.Save_WB(self))
        time.sleep(2)

    def Genearte_LoadPlan(self):
        self.genericMethod.click(LoginPage.GenerateLoadPaln(self))
        time.sleep(10)
        # self.genericMethod.defaultTime()
        # self.genericMethod.click(LoginPage.ExpandLoadResult(self))
        # time.sleep(1)

    def loadResult1(self):
        self.genericMethod.click(LoginPage.ExpandLoadResult(self))
        # self.genericMethod.defaultTime()
        time.sleep(1)

    def ChooseEquipment(self):
        global equipment
        equipment = self.genericMethod.ReadData(".//TestData//EquipmentID.json", "EquipmentID")
        self.genericMethod.click(LoginPage.ItemSizeCheckBox(self))
        time.sleep(1)

    def Generate_Load(self):
        self.genericMethod.click(LoginPage.GenerateLoad(self))
        time.sleep(6)

    def GenerateLoad_meassage(self, meassage):
        Expected = meassage
        Actual = self.genericMethod.getText(LoginPage.Toast_Message(self))
        myLogger.info(Actual)
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    def Save_Result(self):
        time.sleep(3)
        self.genericMethod.click(LoginPage.SAVEresult(self))
        time.sleep(4)

    def SaveResult_meassage(self, meassage1):
        Expected = meassage1
        myLogger.info(Expected)
        Actual = self.genericMethod.getText(LoginPage.Toast_Message(self))
        myLogger.info(Actual)
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    def Three_D_Plan(self):
        self.genericMethod.click(LoginPage.ThreeDloadplan(self))
        time.sleep(1)
        self.genericMethod.Refresh()
        time.sleep(2)

    def GraphicalMode(self):
        RL1 = Select(LoginPage.Animated(self))
        RL1.select_by_index(2)
        time.sleep(60)
        RL1 = Select(LoginPage.Animated(self))
        RL1.select_by_index(1)
        time.sleep(2)

    # WBtitle ******************************************* Delete wb *******************************************#
    def WORKbenchtitle(self):
        return self.driver.find_element(By.XPATH, "//*[@placeholder='Search...']")

    def WorkbenchNumber(self):
        return self.driver.find_element(By.XPATH, "//*[@id='delete']")

    ###########################################################################################################
    def WBTitle(self):
        global WBT
        WBT = self.genericMethod.ReadData(".//TestData//WBTitle.json", "WorkBenchTitle")
        self.genericMethod.type(LoginPage.WORKbenchtitle(self), WBT)
        time.sleep(4)

    def DeleteWB(self):
        self.genericMethod.click(LoginPage.WorkbenchNumber(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.DeleteIcon(self))
        time.sleep(1)

    # **************************************** Build Load & Manage Load ******************************************#
    def View_Details(self):
        return self.driver.find_element(By.XPATH, "(//*[text()=' View Details '])[1]")

    def EquipmentNumberSave(self):
        return self.driver.find_element(By.XPATH, "(//*[@class='badge bg-secondary'])[1]")

    def View_Load(self):
        return self.driver.find_element(By.XPATH, "(//*[text()='View Loads'])[1]")

    def Equipment_Type(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='equipmentType']")

    def Equipment_Number(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='equipmentNumber']")

    def Equipment_Search(self):
        return self.driver.find_element(By.XPATH, "//*[@type='submit']")

    def Up_Arrow(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Consolidation']/parent::*/following-sibling::div/*/*")

    ###############################################################################################################
    def notification_button(self):
        self.genericMethod.Refresh()
        self.genericMethod.click(LoginPage.notification(self))
        time.sleep(2)
        # time.sleep(6)
        # self.genericMethod.click(LoginPage.TRNO_CLEAR(self))
        # time.sleep(2)
        # self.genericMethod.Clear(LoginPage.TRNO_CLEAR(self))
        # self.genericMethod.type(LoginPage.TRNO_CLEAR(self), "b")
        # self.act.send_keys(Keys.BACKSPACE).perform()

        self.genericMethod.click(LoginPage.Up_Arrow(self))
        time.sleep(1)

    def ViewDetails(self):
        self.genericMethod.click(LoginPage.View_Details(self))
        time.sleep(1)

    def equipmentnumber(self):
        self.genericMethod.click(LoginPage.EquipmentNumberSave(self))
        global equipmentNO
        cl = 'A2'
        equipmentNO = self.genericMethod.getText(LoginPage.EquipmentNumberSave(self))
        self.genericMethod.WRITEEXCELDATA(cl, equipmentNO)
        myLogger.info(equipmentNO)

    def viewLoad(self):
        self.genericMethod.click(LoginPage.View_Load(self))
        time.sleep(2)
        self.genericMethod.Refresh()

    def equipmenttype(self):
        time.sleep(2)
        Type = "Virtual"
        drp = Select(LoginPage.Equipment_Type(self))
        drp.select_by_visible_text(Type)
        time.sleep(1)

    def equipmentfield(self):
        Cell = 'A2'
        equipmentNO = self.genericMethod.READEXCELDATA(Cell)
        self.genericMethod.type(LoginPage.Equipment_Number(self), equipmentNO)
        time.sleep(1)

    def equipmentsearch(self):
        self.genericMethod.click(LoginPage.Equipment_Search(self))
        # self.genericMethod.click(LoginPage.notification(self))
        time.sleep(2)
        # self.genericMethod.click(LoginPage.togglemenu(self))
        # time.sleep(1)

    # ******************************************* Rates & Contracts ********************************************#
    def rateContracts(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Rates & Contracts']")

    def CarriersButton(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Carriers']")

    def CreateCarrier(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Create Carrier']")

    def carrieCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='carrieCode']")

    def ParentCarrier(self):
        return self.driver.find_element(By.XPATH, "//*[@role='combobox']")

    def ParentCarrier_Suggestion(self):
        return self.driver.find_element(By.XPATH, "//*[@id='suggestions']")

    def carriername(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='carrierName']")

    def hazLicenseNumber(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='hazLicenseNumber']")

    def operatingRegionCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='operatingRegionCode']")

    def billingCurrencyCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='billingCurrencyCode']")

    def primaryContactFirstName(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='primaryContactFirstName']")

    def primaryContactLastName(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='primaryContactLastName']")

    def primaryContactEmailId(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='primaryContactEmailId']")

    def primaryContactPhone(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='primaryContactPhone']")

    def primaryContactMobile(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='primaryContactMobile']")

    def CDG_Checkbox(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()=' Carries Dangerous Goods ']/..//*[@formcontrolname='canCarryDangerousGoods']")

    def RegistrationDetails(self):
        # return self.driver.find_element(By.XPATH, "//*[text()='Registration Details']/..//*[@name='downangle']")
        return self.driver.find_element(By.XPATH, "//*[text()='Registration Details']/..//*[@type='button']")

    def RegistrationTypCode(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='carrierRegistrationTypCode']")

    def RegistrationNumber(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='carrierRegistrationNumber']")

    def issuingCountryCode(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='issuingCountryCode']")

    def issuingAgencyName(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='issuingAgencyName']")

    def Effctive_Date(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()='Effective Date']/parent::*/*/*//*[@placeholder='yyyy-mm-dd']")

    def ExpireDAte(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='expiryDate']")

    def YearSelect(self):
        return self.driver.find_element(By.XPATH, "//*[@title='Select year']")

    def DateSelect(self):
        return self.driver.find_element(By.XPATH, "//*[contains(@class, 'btn-light' ) and text() = '" + day4 + "']")

    def SaveCarrier(self):
        return self.driver.find_element(By.XPATH, "//*[text() =' Save ']")

    ##################################################### Carrier #######################################################
    def rate_Contracts(self):
        self.genericMethod.Refresh()
        time.sleep(4)
        self.genericMethod.click(LoginPage.rateContracts(self))
        time.sleep(1)

    def carriers(self):
        self.genericMethod.click(LoginPage.CarriersButton(self))
        time.sleep(1)

    def create_carriers(self):
        self.genericMethod.click(LoginPage.CreateCarrier(self))
        time.sleep(1)

    def carrier_code(self, carriercode):
        a = carriercode
        c = self.genericMethod.NumIncrement()
        global carriercode2
        carriercode2 = a + str(c)
        self.genericMethod.WriteData(".//TestData//CarrierCode.json", "CarrierCode", carriercode2)
        self.genericMethod.type(LoginPage.carrieCode(self), carriercode2)
        time.sleep(1)

    def parrentcarrier(self, parrent):
        self.genericMethod.type(LoginPage.ParentCarrier(self), parrent)
        time.sleep(1)
        self.genericMethod.click(LoginPage.ParentCarrier_Suggestion(self))
        time.sleep(1)

    def carrier_name(self, carriername):
        c = self.genericMethod.NumIncrement()
        global carriername2
        carriername2 = carriername + str(c)
        self.genericMethod.WriteData(".//TestData//Carrier.json", "CarrierName", carriername2)
        self.genericMethod.type(LoginPage.carrierName(self), carriername2)
        # time.sleep(8)

    def hazardouslicescne(self, licescne):
        self.genericMethod.Clear(LoginPage.hazLicenseNumber(self))
        self.genericMethod.type(LoginPage.hazLicenseNumber(self), licescne)
        # time.sleep(1)

    def operatingregion(self, region):
        self.genericMethod.type(LoginPage.operatingRegionCode(self), region)
        # time.sleep(1)

    def billingcurrency(self, currency):
        self.genericMethod.Clear(LoginPage.billingCurrencyCode(self))
        self.genericMethod.type(LoginPage.billingCurrencyCode(self), currency)
        # time.sleep(1)

    def Firstname(self, Fname):
        self.genericMethod.Clear(LoginPage.primaryContactFirstName(self))
        self.genericMethod.type(LoginPage.primaryContactFirstName(self), Fname)
        # time.sleep(1)

    def Lastname(self, Lname):
        self.genericMethod.Clear(LoginPage.primaryContactLastName(self))
        self.genericMethod.type(LoginPage.primaryContactLastName(self), Lname)
        # time.sleep(1)

    def Carrieremail(self, email):
        self.genericMethod.Clear(LoginPage.primaryContactEmailId(self))
        self.genericMethod.type(LoginPage.primaryContactEmailId(self), email)
        # time.sleep(1)

    def Carrierphonenumber(self, phonenumber):
        self.genericMethod.Clear(LoginPage.primaryContactPhone(self))
        self.genericMethod.type(LoginPage.primaryContactPhone(self), phonenumber)
        # time.sleep(1)

    def Carriermobilenumber(self, mobilenumber):
        self.genericMethod.Clear(LoginPage.primaryContactMobile(self))
        self.genericMethod.type(LoginPage.primaryContactMobile(self), mobilenumber)
        # time.sleep(1)

    def CDGcheckbox(self):
        self.genericMethod.click(LoginPage.CDG_Checkbox(self))
        # time.sleep(1)

    def registration_Details(self):
        self.genericMethod.click(LoginPage.RegistrationDetails(self))
        time.sleep(1)

    def Registration_code(self, Registrationcode):
        # self.genericMethod.type(LoginPage.RegistrationDetails(self), Registrationcode)
        drp = Select(LoginPage.RegistrationTypCode(self))
        drp.select_by_visible_text(Registrationcode)
        time.sleep(1)

    def Registration_Number(self, RegistrationNumber):
        self.genericMethod.type(LoginPage.RegistrationNumber(self), RegistrationNumber)
        # time.sleep(1)

    def IssuingCountry(self, countryName):
        self.genericMethod.type(LoginPage.issuingCountryCode(self), countryName)
        # time.sleep(1)

    def IssuingAgency(self, agencycode):
        self.genericMethod.type(LoginPage.issuingAgencyName(self), agencycode)
        # time.sleep(1)

    def effective_Date(self):
        self.genericMethod.click(LoginPage.Effctive_Date(self))
        time.sleep(1)
        global day4
        current_time1 = datetime.datetime.now().day
        day4 = str(current_time1)
        myLogger.info(day4)
        self.genericMethod.click(LoginPage.DateSelect(self))

    def Expired_date(self):
        self.genericMethod.click(LoginPage.ExpireDAte(self))
        time.sleep(1)
        # self.genericMethod.getText(LoginPage.YearSelect(self))
        current_time = datetime.datetime.now().year
        day1 = current_time + 1
        myLogger.info(day1)
        day2 = str(day1)
        myLogger.info(day2)
        drp = Select(LoginPage.YearSelect(self))
        drp.select_by_visible_text(day2)
        time.sleep(1)
        global day4
        current_time1 = datetime.datetime.now().day
        day4 = str(current_time1)
        myLogger.info(day4)
        self.genericMethod.click(LoginPage.DateSelect(self))

    def CarrierSaveButton(self):
        self.genericMethod.click(LoginPage.SaveCarrier(self))
        time.sleep(1)

    # ********************************************** Edit Carrier ********************************************#
    def CarrierSearch(self):
        return self.driver.find_element(By.XPATH, "//*[@type='submit']")

    def Edit_Carrier(self):
        return self.driver.find_element(By.XPATH, "//*[@id='edit']")

    def Edit_CarrierCODE(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='carrierCode']")

    def ClickCarrierCode(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + CarrireCode + "']")

    def EditHZLN(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='hazLicenseNumber']")

    ###########################################################################################################
    def EditCarrierCode(self):
        global CarrireCode
        CarrireCode = self.genericMethod.ReadData(".//TestData//CarrierCode.json", "CarrierCode")
        self.genericMethod.type(LoginPage.Edit_CarrierCODE(self), CarrireCode)
        time.sleep(1)

    def CarriesDangerousGoods(self):
        self.genericMethod.click(LoginPage.CDG_Checkbox(self))
        time.sleep(1)

    def carrierSearchButton(self):
        self.genericMethod.click(LoginPage.CarrierSearch(self))
        time.sleep(1)

    def carrrierCode(self):
        self.genericMethod.click(LoginPage.ClickCarrierCode(self))
        time.sleep(1)

    def EditCarrrier(self):
        self.genericMethod.click(LoginPage.Edit_Carrier(self))
        time.sleep(3)

    def EditHL(self, licescne):
        # self.genericMethod.click(LoginPage.EditHZLN(self))
        self.genericMethod.Clear(LoginPage.hazLicenseNumber(self))
        self.genericMethod.type(LoginPage.hazLicenseNumber(self), licescne)
        time.sleep(1)

    # ********************************************** Contract *************************************************#
    def Contracts(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Contracts']")

    def ChooseCarrier(self):
        return self.driver.find_element(By.XPATH, "//*[@id='status']")

    def CreateContractSymbol(self):
        return self.driver.find_element(By.XPATH, "//*[@ngbtooltip='Create Contract']")

    def ContractNAme(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='contractName']")

    def ContractNum(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='contractName']/../../..//*[@formcontrolname='contractNumber']")

    def CustomerBox(self):
        return self.driver.find_element(By.XPATH, "//*[@role='combobox']")

    def SelectCustomerBox(self):
        return self.driver.find_element(By.XPATH, "//*[@id='suggestions']")

    def StartDate(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='validFromDateUtc']")

    # def startDatechoose(self):
    #     return self.driver.find_element(By.XPATH, "//div[contains(@class,'btn-light') and text()='" + stardate1 + "']")

    def startDatechoose(self):
        return self.driver.find_element(By.XPATH, "//*[@class='ngb-dp-day ngb-dp-today']")

    def EndDate(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='validTillDateUtc']")

    def EndtDatechoose(self):
        return self.driver.find_element(By.XPATH, "//*[@class='btn-light' and text()='" + stardate2 + "']")

    def CreateContract1(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Create Contract ']")

    def SelectMonth(self):
        return self.driver.find_element(By.XPATH, "//*[@title='Select month']")

    ############################################################################################################
    def contractButton(self):
        self.genericMethod.click(LoginPage.Contracts(self))
        time.sleep(2)

    def CarrierDropDownButton(self):
        self.genericMethod.click(LoginPage.Contracts(self))
        time.sleep(2)
        CarrierName3 = self.genericMethod.ReadData(".//TestData//Carrier.json", "CarrierName")
        # month = 'bv'
        drp = Select(LoginPage.ChooseCarrier(self))
        drp.select_by_visible_text(CarrierName3)
        time.sleep(1)

    def createcontractButton(self):
        self.genericMethod.click(LoginPage.CreateContractSymbol(self))
        time.sleep(1)

    def contractnametButton(self, contractname):
        self.genericMethod.type(LoginPage.ContractNAme(self), contractname)
        time.sleep(1)

    def contractNumberButton(self, contract):
        self.genericMethod.type(LoginPage.ContractNum(self), contract)
        time.sleep(1)

    def customernameButton(self, customername):
        # global custname
        # custname = customername
        self.genericMethod.type(LoginPage.CustomerBox(self), customername)
        time.sleep(2)
        self.genericMethod.click(LoginPage.SelectCustomerBox(self))
        time.sleep(1)

    def contractstartdateButton(self):
        self.genericMethod.click(LoginPage.StartDate(self))
        # today_month = datetime.datetime.today().month
        # datetime_object = datetime.datetime.strptime(str(today_month), "%m")
        # month_name = datetime_object.strftime("%b")
        # NextDay_Date = datetime.datetime.today().date() + datetime.timedelta(days=1)
        # NextMonth = NextDay_Date.month
        # global Nextdate1
        # NextMonth1 = NextDay_Date.day
        # Nextdate1 = str(NextMonth1)
        # datetime_object1 = datetime.datetime.strptime(str(NextMonth), "%m")
        # month_name1 = datetime_object1.strftime("%b")
        # if today_month == NextMonth:
        #     drp = Select(LoginPage.SelectMonth(self))
        #     drp.select_by_visible_text(month_name)
        #     self.genericMethod.click(LoginPage.startDatechoose(self))
        # elif today_month < NextMonth:
        #     drp = Select(LoginPage.SelectMonth(self))
        #     drp.select_by_visible_text(month_name1)
        #     self.genericMethod.click(LoginPage.startDatechoose(self))
        #     print(month_name1)
        time.sleep(1)
        global stardate1
        current_time1 = datetime.datetime.now().day
        stardate1 = str(current_time1)
        myLogger.info(stardate1)
        self.genericMethod.click(LoginPage.startDatechoose(self))
        time.sleep(1)

    def contractenddateButton(self):
        self.genericMethod.click(LoginPage.EndDate(self))
        time.sleep(1)
        current_time = datetime.datetime.now().year
        day1 = current_time + 1
        myLogger.info(day1)
        day2 = str(day1)
        myLogger.info(day2)
        drp = Select(LoginPage.YearSelect(self))
        drp.select_by_visible_text(day2)
        time.sleep(1)
        global stardate2
        current_time1 = datetime.datetime.now().day
        stardate2 = str(current_time1)
        myLogger.info(stardate2)
        self.genericMethod.click(LoginPage.EndtDatechoose(self))

    def expiredtoggleButton(self):
        self.genericMethod.click(LoginPage.CreateContractSymbol(self))
        time.sleep(1)

    def createcontractButton1(self):
        self.genericMethod.click(LoginPage.CreateContract1(self))
        time.sleep(1)

    def VeryMessage(self, message):
        Expected = message
        myLogger.info(Expected)
        Actual = self.genericMethod.getText(LoginPage.Toast_Message(self))
        myLogger.info(Actual)
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    # **********************************************  RATES  ***************************************************#
    def Rates(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Rates']")

    def RateCard(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Rate Cards']")

    def CreateRateCard(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Create Rate Card ']")

    def RateCard_Name(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='rateCardName']")

    def RateCard_type(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='rateCardTypeCode']")

    def Rate_Carrier(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='carrier']")

    def Rate_customerCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='customerCode']")

    def Customer_option(self):
        return self.driver.find_element(By.XPATH, "//*[@role='option']")

    def Rate_serviceTypeCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='serviceTypeCode']")

    def Rate_incoTermCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='incoTermCode']")

    def Rate_paymentTermCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='paymentTermCode']")

    def Rate_Validity(self):
        return self.driver.find_element(By.XPATH, "//*[@name='calendar']")

    def Rate_namedAccount(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='namedAccount']")

    def Rate_Save(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save ']")

    def Rate_FileImport(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Import ']")

    def Rate_FileInsert(self):
        return self.driver.find_element(By.XPATH, "//input[@type='file']")

    def Rate_FileUpload(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Upload ']")

    def RateValidityStartDate(self):
        return self.driver.find_element(By.XPATH,
                                        "(// div[contains( @class ,'ngb-dp-month')][1] // span[contains(text(), '" + Nextdate1 + "')])[1]")

    ###############################################################################################################
    def RateCLICK(self):
        self.genericMethod.click(LoginPage.Rates(self))
        time.sleep(1)

    def RateCards(self):
        self.genericMethod.click(LoginPage.RateCard(self))
        time.sleep(1)

    def create_RateCard(self):
        self.genericMethod.click(LoginPage.CreateRateCard(self))
        time.sleep(1)

    def RateCardName(self, Name):
        value = self.genericMethod.READEXCELDATA('B2')
        myLogger.info(value)
        v = value + 1
        self.genericMethod.WRITEEXCELDATA('B2', v)
        myLogger.info(v)
        data = Name + str(v)
        myLogger.info(data)
        self.genericMethod.Clear(LoginPage.RateCard_Name(self))
        time.sleep(1)
        self.genericMethod.type(LoginPage.RateCard_Name(self), data)
        cl = 'C2'
        self.genericMethod.WRITEEXCELDATA(cl, data)
        time.sleep(1)

    def RateCardType(self, type):
        self.genericMethod.type(LoginPage.RateCard_type(self), type)
        time.sleep(1)

    def RateCardcarrrier(self):
        CarrierName = self.genericMethod.ReadData(".//TestData//Carrier.json", "CarrierName")
        self.genericMethod.type(LoginPage.Rate_Carrier(self), CarrierName)
        time.sleep(1)
        self.genericMethod.click(LoginPage.Customer_option(self))
        time.sleep(1)

    def Ratecustomername(self, customername):
        self.genericMethod.type(LoginPage.Rate_customerCode(self), customername)
        time.sleep(1)
        self.genericMethod.click(LoginPage.Customer_option(self))
        time.sleep(1)

    def RateServiceType(self, ServiceType):
        self.genericMethod.type(LoginPage.Rate_serviceTypeCode(self), ServiceType)
        time.sleep(1)

    def RateCardIncoTerms(self, IncoTerms):
        self.genericMethod.type(LoginPage.Rate_incoTermCode(self), IncoTerms)
        time.sleep(1)

    def RateCardPaymentTerms(self, PaymentTerms):
        self.genericMethod.type(LoginPage.Rate_paymentTermCode(self), PaymentTerms)
        time.sleep(1)

    def Ratevalidity(self):
        self.genericMethod.click(LoginPage.Rate_Validity(self))
        time.sleep(1)
        today_month = datetime.datetime.today().month
        datetime_object = datetime.datetime.strptime(str(today_month), "%m")
        Year = datetime.datetime.today().year
        Year1 = Year + 1
        NextYear = str(Year1)
        month_name = datetime_object.strftime("%b")
        NextDay_Date = datetime.datetime.today().date() + datetime.timedelta(days=1)
        NextMonth = NextDay_Date.month
        global Nextdate1
        NextMonth1 = NextDay_Date.day
        Nextdate1 = str(NextMonth1)
        datetime_object1 = datetime.datetime.strptime(str(NextMonth), "%m")
        month_name1 = datetime_object1.strftime("%b")
        if today_month == NextMonth:
            drp = Select(LoginPage.SelectMonth(self))
            drp.select_by_visible_text(month_name)
            self.genericMethod.click(LoginPage.RateValidityStartDate(self))
            drp = Select(LoginPage.YearSelect(self))
            drp.select_by_visible_text(NextYear)
            self.genericMethod.click(LoginPage.RateValidityStartDate(self))
        elif today_month < NextMonth:
            drp = Select(LoginPage.SelectMonth(self))
            drp.select_by_visible_text(month_name1)
            self.genericMethod.click(LoginPage.RateValidityStartDate(self))
            drp = Select(LoginPage.YearSelect(self))
            drp.select_by_visible_text(NextYear)
            self.genericMethod.click(LoginPage.RateValidityStartDate(self))

    def RateAccount(self, account):
        self.genericMethod.type(LoginPage.Rate_namedAccount(self), account)
        time.sleep(1)

    def RateSAve(self):
        self.genericMethod.click(LoginPage.Rate_Save(self))
        time.sleep(3)

    def VeryRateSaveToast(self, message):
        f = message
        d = self.genericMethod.READEXCELDATA('C2')
        Expected = f[:10] + d + f[10:]
        myLogger.info(Expected)
        Actual = self.genericMethod.getText(LoginPage.Toast_Message(self))
        myLogger.info(Actual)
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    def RateFileImport(self):
        self.genericMethod.click(LoginPage.Rate_FileImport(self))
        time.sleep(1)
        # Path = "E://Phoenix_20High//Upload//RateCard_Function.xlsm"
        Path = "E://Phoenix_20High//Upload//XBEES.xlsm"
        self.genericMethod.Upload(LoginPage.Rate_FileInsert(self), Path)
        self.genericMethod.click(LoginPage.Rate_FileUpload(self))
        time.sleep(8)

    def RateUploadmessage(self, Uploadmessage):
        Msg = self.genericMethod.click(LoginPage.Toast_Message(self))
        Msg.is_displayed()
        time.sleep(1)
        myLogger.info(Msg)
        Msg1 = Msg.split("-")
        Expected = Uploadmessage
        Actual = Msg1[0]
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    # ******************************************      Rate REvision      ******************************************#
    def RatecardStatus(self):
        # return self.driver.find_element(By.XPATH, "//*[text()='Candidate Revision']")
        return self.driver.find_element(By.XPATH, "//button[@aria-controls='offcanvasRight']")

    def UpdaterateCard_status(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='revisionStatusCode']")

    def Status_Save(self):
        return self.driver.find_element(By.XPATH, "(//*[@name='save'])[2]")

    def Approval_Status(self):
        # return self.driver.find_element(By.XPATH, "//*[text()='Approval History']/../div[3]/*/*/*")
        return self.driver.find_element(By.XPATH,
                                        "//*[text()='Approval History']/../div[3]/*//*[text()='" + Status + "']")

    ###############################################################################################################
    def RateRevisionstatus(self):
        self.genericMethod.click(LoginPage.RatecardStatus(self))
        time.sleep(1)

    def Revisionstatus(self, status):
        self.genericMethod.type(LoginPage.UpdaterateCard_status(self), status)
        time.sleep(1)
        self.genericMethod.WriteData(".//TestData//Status.json", "Status", status)

    def RevisionSave(self):
        self.genericMethod.click(LoginPage.Status_Save(self))
        time.sleep(5)

    def ApprovalHistory(self, message):
        self.genericMethod.click(LoginPage.RatecardStatus(self))
        time.sleep(1)
        global Status
        Status = self.genericMethod.ReadData(".//TestData//Status.json", "Status")

        Expected = message
        Actual = self.genericMethod.getText(LoginPage.Approval_Status(self))
        myLogger.info(Actual)
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    # ***************************************************** Delete Rate Card *********************************************#

    def RateCard_Delete(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Delete Rate Revision ']")

    # def ButtonLogOUT(self):
    #     return self.driver.find_element(By.XPATH, "//*[text()='Logout ']")

    ############################################################################################################
    def New_RateCard_Name(self, Name):
        value = self.genericMethod.READEXCELDATA('B2')
        myLogger.info(value)
        v = value + 1
        self.genericMethod.WRITEEXCELDATA('B2', v)
        myLogger.info(v)
        data = Name + str(v)
        myLogger.info(data)
        self.genericMethod.Clear(LoginPage.RateCard_Name(self))
        time.sleep(1)
        self.genericMethod.type(LoginPage.RateCard_Name(self), data)
        cl = 'E2'
        self.genericMethod.WRITEEXCELDATA(cl, data)
        time.sleep(1)

    def DeleteRateCard(self):
        self.genericMethod.click(LoginPage.RateCard_Delete(self))
        time.sleep(3)

    # *************************************** Carrier_AssignTO_Ratecard ***********************************#

    def Filter_Button(self):
        return self.driver.find_element(By.XPATH, "//*[@aria-controls='collapseFilterOpen']")

    def ApprovedOnly(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Approved Only']")

    def Search_Button(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()='Approved Only']/../parent::*/*/following-sibling::*//*[@type='submit']")

    def assignRates(self):
        return self.driver.find_element(By.XPATH, "//*[@name='arrowleft']")

    def RateCard_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@name='marginCurrencyCode']")

    def Assign_Button(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Assign ']")

    def RateCard_click(self):
        return self.driver.find_element(By.XPATH, "//[text()=' ESSPL_KART137 ']")

    def CloseButton_Click(self):
        return self.driver.find_element(By.XPATH, "//*[@class='btn-close']")

    ############################################################################################################
    def Contract_Filter_Button(self):
        self.genericMethod.click(LoginPage.Filter_Button(self))
        time.sleep(1)

    def Approved_Only(self):
        self.genericMethod.click(LoginPage.ApprovedOnly(self))
        time.sleep(1)

    def unapproved_contract(self):
        self.genericMethod.click(LoginPage.Search_Button(self))
        time.sleep(1)

    def assign_rates(self):
        self.genericMethod.click(LoginPage.assignRates(self))
        time.sleep(1)

    def RateCoardChoose(self):
        # self.genericMethod.click(LoginPage.RateCard_Choose(self))
        # time.sleep(1)
        value = self.genericMethod.READEXCELDATA('C2')
        myLogger.info(value)
        drp = Select(LoginPage.RateCard_Choose(self))
        drp.select_by_visible_text(value)
        time.sleep(1)

    def Assign(self):
        self.genericMethod.click(LoginPage.Assign_Button(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.CloseButton_Click(self))
        time.sleep(1)

    # ***************************************************** Rate Margin *********************************************#

    def RateMargin_Button(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Rate Margin']")

    def Create_Margin(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Create Margin ']")

    def Drp_ServiceType(self):
        return self.driver.find_element(By.XPATH, "//*[@name='serviceType']")

    def Drp_RateUnit(self):
        return self.driver.find_element(By.XPATH, "//*[@name='rateUomCode']")

    def Drp_equipmentSize(self):
        return self.driver.find_element(By.XPATH, "//*[@name='equipmentSizetypes']")

    def Drp_Customer(self):
        return self.driver.find_element(By.XPATH, "//*[@placeholder='Select Customer']")

    def Click_Customer(self):
        return self.driver.find_element(By.XPATH, "//*[@class='dropdown-item active']")

    def Drp_hsCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='hsCode']")

    def Drp_DangerousCargo(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='isDangerousCargo']")

    def Drp_hazardousCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='hazardousCode']")

    def Drp_LoadCountry(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Load']/../*/*/*/*/*//*[@placeholder='Select Country']")

    def Drp_LC(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + LC + "']")

    def loadCityCode(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='loadCityCode']/./*/*/*[@placeholder='Select City']")

    def lC_Code(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + LCity + "']")

    def loadSitePostalCode(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='loadSitePostalCode']/./*/*/*[@placeholder='Select Post Code']")

    def lC_PinCode(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + LoadPinCode + "']")

    def dischargeCountryCode(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='dischargeCountryCode']/./*/*/*[@placeholder='Select Country']")

    def DC_Code(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + DCCode + "']")

    def dischargeCityCode(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='dischargeCityCode']/./*/*/*[@placeholder='Select City']")

    def DCity_Code(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + DCity + "']")

    def dischargeSitePostalCode(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='dischargeSitePostalCode']/./*/*/*[@placeholder='Select Site']")

    def Discharge_PinCode(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + DischargePinCode + "']")

    def marginValue(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='marginValue']")

    def marginCurrencyCode(self):
        return self.driver.find_element(By.XPATH, "//*[@name='marginCurrencyCode']")

    def isPercentage(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='isPercentage']")

    def validFromDateUtc(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='validFromDateUtc']")

    def validNextDate(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + NextDate + "']")

    def validTillDateUtc(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='validTillDateUtc']")

    def SaveMargin(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save ']")

    ############################################################################################################
    def RateMargin(self):
        self.genericMethod.click(LoginPage.RateMargin_Button(self))
        time.sleep(2)

    def CreateMargin(self):
        self.genericMethod.click(LoginPage.Create_Margin(self))
        time.sleep(2)

    def MarginServiceType(self, Servicetype):
        self.genericMethod.type(LoginPage.Drp_ServiceType(self), Servicetype)
        time.sleep(1)

    def RateUnit(self, rateunit):
        self.genericMethod.type(LoginPage.Drp_RateUnit(self), rateunit)
        time.sleep(1)

    def Margin_equipmenttype(self, equipmenttype):
        self.genericMethod.type(LoginPage.Drp_equipmentSize(self), equipmenttype)
        time.sleep(1)

    def Margin_customer(self, customerCode):
        self.genericMethod.type(LoginPage.Drp_Customer(self), customerCode)
        time.sleep(1)
        self.genericMethod.click(LoginPage.Click_Customer(self))
        time.sleep(1)

    def Margin_HSCode(self, HScode):
        self.genericMethod.type(LoginPage.Drp_hsCode(self), HScode)
        time.sleep(1)

    def Margin_hazardouscode(self, hazardouscode):
        self.genericMethod.type(LoginPage.Drp_hazardousCode(self), hazardouscode)
        time.sleep(1)

    def Margin_dangerouscargo(self):
        self.genericMethod.click(LoginPage.Drp_DangerousCargo(self))
        time.sleep(1)

    def Load_country(self, loadcountry):
        self.genericMethod.type(LoginPage.Drp_LoadCountry(self), loadcountry)
        time.sleep(1)
        global LC
        LC = loadcountry
        self.genericMethod.click(LoginPage.Drp_LC(self))
        time.sleep(1)

    def Load_city(self, loadcity):
        self.genericMethod.type(LoginPage.loadCityCode(self), loadcity)
        time.sleep(1)
        global LCity
        LCity = loadcity
        self.genericMethod.click(LoginPage.lC_Code(self))
        time.sleep(1)

    def Load_postcode(self, Pin):
        self.genericMethod.type(LoginPage.loadSitePostalCode(self), Pin)
        time.sleep(1)
        global LoadPinCode
        LoadPinCode = Pin
        self.genericMethod.click(LoginPage.lC_PinCode(self))
        time.sleep(1)

    def Discharge_country(self, dischargecountry):
        self.genericMethod.type(LoginPage.dischargeCountryCode(self), dischargecountry)
        time.sleep(1)
        global DCCode
        DCCode = dischargecountry
        self.genericMethod.click(LoginPage.DC_Code(self))
        time.sleep(1)

    def Discharge_city(self, dischargecity):
        self.genericMethod.click(LoginPage.dischargeCityCode(self))
        time.sleep(1)
        self.genericMethod.type(LoginPage.dischargeCityCode(self), dischargecity)
        time.sleep(1)
        global DCity
        DCity = dischargecity
        self.genericMethod.click(LoginPage.DCity_Code(self))
        time.sleep(1)

    def Discharge_postcode(self, Pin1):
        self.genericMethod.type(LoginPage.dischargeSitePostalCode(self), Pin1)
        time.sleep(1)
        global DischargePinCode
        DischargePinCode = Pin1
        self.genericMethod.click(LoginPage.Discharge_PinCode(self))
        time.sleep(1)

    def MarginNumber(self, validdata):
        self.genericMethod.type(LoginPage.marginValue(self), validdata)
        time.sleep(1)

    def Margin_currency(self, currency):
        self.genericMethod.type(LoginPage.marginCurrencyCode(self), currency)
        time.sleep(2)

    def Margin_isPercentage(self):
        self.genericMethod.click(LoginPage.isPercentage(self))
        time.sleep(1)

    def validdate_From(self):
        self.genericMethod.click(LoginPage.validFromDateUtc(self))
        time.sleep(1)
        Date = datetime.datetime.today().date() + datetime.timedelta(days=1)
        NextDay = Date.day
        global NextDate
        NextDate = str(NextDay)
        self.genericMethod.click(LoginPage.validNextDate(self))
        time.sleep(1)

    def validdate_To(self):
        self.genericMethod.click(LoginPage.validTillDateUtc(self))
        time.sleep(1)
        Date = datetime.datetime.today().date() + datetime.timedelta(days=1)
        NextDay = Date.day
        global NextDate
        NextDate = str(NextDay)
        self.genericMethod.click(LoginPage.validNextDate(self))
        time.sleep(1)

    def Margin_Save(self):
        self.genericMethod.click(LoginPage.SaveMargin(self))
        time.sleep(2)
        # self.genericMethod.click(LoginPage.SaveMargin(self))
        # time.sleep(1)

    # ******************************************** Rate Margin **********************************************#

    def FilterButton(self):
        self.genericMethod.click(LoginPage.Filter(self))
        time.sleep(1)

    # ***************************************************** Compare Rate *********************************************#
    def Auto_CompareRates(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Compare Rates']")

    def CompareRates(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Compare Rates']")

    def CompareRateCustomer(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='customer']/*/*//input")

    def CLickSugesstion(self):
        return self.driver.find_element(By.XPATH, "//*[@id='suggestions']//a")

    def HAZCode(self):
        return self.driver.find_element(By.XPATH, "//*[@aria-label='Select HAZ. Code']")

    def RouteLeg(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Route Leg']")

    def ORG_LoadCountry(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Select Country'])[3]")

    def ORG_LoadCity(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Select City'])[3]")

    def Des_dischargeCountry(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Select Country'])[4]")

    def Des_dischargeCity(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Select City'])[4]")

    def Option_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@class='item']")

    def Equipment_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='equipmentName']")

    def EquipmentNumber_Select(self):
        return self.driver.find_element(By.XPATH, "//*[@value='20FTDRY']")

    def EquipmentNumber_Enter(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='equipmentNumber']")

    def Weight_Enter(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='weightUOM']/parent::*//*[@formcontrolname='weight']")

    def Weight_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='weightUOM']")

    def Weight_Select(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Kilogram (Kg) ']")

    def Volume_Enter(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='volume']")

    def Volume_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='volumeUOM']")

    def Volume_Select(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' cubic centimetre ']")

    def MOT_Choose(self):
        return self.driver.find_element(By.XPATH, "// *[ @ formcontrolname = 'MOT']")

    def MOT_Select(self):
        return self.driver.find_element(By.XPATH, "// *[text() = ' Air ']")

    def AddLEG(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Add Route Leg ']")

    def CheckBox_LEG(self):
        return self.driver.find_element(By.XPATH, "// *[ @ id = 'checkboxNoLabel']")

    def ApplyLeg(self):
        return self.driver.find_element(By.XPATH, "// *[text() = 'Apply']")

    def CloseLeg(self):
        return self.driver.find_element(By.XPATH, "(//*[@data-bs-dismiss='offcanvas'])[2]")

    def CompareButton(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Compare ']")

    ############################################################################################################

    def auto_generate_Compare_Rates(self):
        self.genericMethod.click(LoginPage.Auto_CompareRates(self))
        time.sleep(1)

    def Compare_Rates(self):
        self.genericMethod.click(LoginPage.CompareRates(self))
        time.sleep(1)

    def compareRate_Customer(self, customer):
        global Cust
        Cust = customer
        self.genericMethod.type(LoginPage.CompareRateCustomer(self), customer)
        time.sleep(1)
        self.genericMethod.click(LoginPage.CLickSugesstion(self))
        time.sleep(1)

    def compareRate_HazCode(self, HazCode):
        self.genericMethod.type(LoginPage.HAZCode(self), HazCode)
        time.sleep(1)
        self.genericMethod.click(LoginPage.CLickSugesstion(self))
        time.sleep(1)

    def Add_route_leg(self):
        self.genericMethod.click(LoginPage.RouteLeg(self))
        time.sleep(1)

    def org_country(self):
        value = self.genericMethod.READEXCELDATA_XLSM('B4')
        myLogger.info(value)
        time.sleep(1)
        # self.genericMethod.click(LoginPage.ORG_LoadCountry(self))
        self.genericMethod.type(LoginPage.ORG_LoadCountry(self), value)
        self.genericMethod.click(LoginPage.Option_Choose(self))

    def org_city(self):
        value = self.genericMethod.READEXCELDATA_XLSM('C4')
        myLogger.info(value)
        time.sleep(1)
        # self.genericMethod.click(LoginPage.ORG_LoadCountry(self))
        self.genericMethod.type(LoginPage.ORG_LoadCity(self), value)
        self.genericMethod.click(LoginPage.Option_Choose(self))

    def des_country(self):
        value = self.genericMethod.READEXCELDATA_XLSM('E4')
        myLogger.info(value)
        time.sleep(1)
        self.genericMethod.type(LoginPage.Des_dischargeCountry(self), value)
        self.genericMethod.click(LoginPage.Option_Choose(self))

    def des_city(self):
        value = self.genericMethod.READEXCELDATA_XLSM('F4')
        myLogger.info(value)
        time.sleep(1)
        self.genericMethod.type(LoginPage.Des_dischargeCity(self), value)
        self.genericMethod.click(LoginPage.Option_Choose(self))
        time.sleep(1)

    def equipment_numberSelect(self):
        v = self.genericMethod.getText(LoginPage.EquipmentNumber_Select(self))
        myLogger.info(v)
        drp = Select(LoginPage.Equipment_Choose(self))
        drp.select_by_visible_text(v)
        time.sleep(2)

    def equipment_quantity(self):
        v = '2'
        self.genericMethod.type(LoginPage.EquipmentNumber_Enter(self), v)
        time.sleep(1)

    def Enter_Weight(self):
        v = '2'
        self.genericMethod.type(LoginPage.Weight_Enter(self), v)
        time.sleep(1)

    def choose_weight(self):
        v = self.genericMethod.getText(LoginPage.Weight_Select(self))
        myLogger.info(v)
        drp = Select(LoginPage.Weight_Choose(self))
        drp.select_by_visible_text(v)
        time.sleep(2)

    def Enter_Volume(self):
        v = '2'
        self.genericMethod.type(LoginPage.Volume_Enter(self), v)
        time.sleep(1)

    def choose_Volume(self):
        v = self.genericMethod.getText(LoginPage.Volume_Select(self))
        myLogger.info(v)
        drp = Select(LoginPage.Volume_Choose(self))
        drp.select_by_visible_text(v)
        time.sleep(2)

    def MOT_type(self):
        v = self.genericMethod.getText(LoginPage.MOT_Select(self))
        myLogger.info(v)
        drp = Select(LoginPage.MOT_Choose(self))
        drp.select_by_visible_text(v)
        time.sleep(2)

    def Add_RouteLeg(self):
        self.genericMethod.click(LoginPage.AddLEG(self))
        time.sleep(1)

    def RouteLeg_CheckBox(self):
        self.genericMethod.click(LoginPage.CheckBox_LEG(self))
        time.sleep(1)

    def RouteLeg_Apply(self):
        self.genericMethod.click(LoginPage.ApplyLeg(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.CloseLeg(self))
        time.sleep(1)

    def compare_button(self):
        self.genericMethod.click(LoginPage.CompareButton(self))
        time.sleep(1)

    # ********************************************* Compare Rate Auto ****************************************#
    def manageload(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Manage Loads']")

    def EnterEquipment(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Manage Loads']")

    def EquipmentDetails(self):
        return self.driver.find_element(By.XPATH, "//*[@class='virtual-equip']")

    def AssignCarrier_CheckBox(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Assign Carrier ']/../*[@type='checkbox']")

    def AssignCarrierClick(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Assign Carrier']")

    def AssignDirect(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Assign Direct']")

    def Carrier_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='carriers']")

    # def Carrier_Choose1(self):
    #     return self.driver.find_element(By.XPATH, "//*[text()=' Everglory Carrier ']")
    def Carrier_Choose1(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Everglory Carrier ']")

    def CarrierSave(self):
        return self.driver.find_element(By.XPATH, "//*[@id='save']")

    def CloseAssignWindow(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[text()='Assign Carrier']/../*/*[@class='bi bi-x-lg text-white']")

    def AssignCompareRates(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Compare Rates']")

    def Compare(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Compare ']")

    ############################################################################################################
    def manage_load(self):
        self.genericMethod.click(LoginPage.manageload(self))
        time.sleep(2)

    def Enter_Equipment(self):
        self.genericMethod.click(LoginPage.manageload(self))
        time.sleep(1)

    def equipment_details(self):
        self.genericMethod.click(LoginPage.EquipmentDetails(self))
        time.sleep(1)

    def Assign_carrier(self):
        self.genericMethod.click(LoginPage.AssignCarrier_CheckBox(self))
        time.sleep(1)

    def Click_AssignCarrier(self):
        self.genericMethod.click(LoginPage.AssignCarrierClick(self))
        time.sleep(1)

    def Assign_Direct(self):
        self.genericMethod.click(LoginPage.AssignDirect(self))
        time.sleep(3)

    def CarrierChoose(self):
        self.genericMethod.click(LoginPage.Carrier_Choose(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Carrier_Choose1(self))
        time.sleep(1)

    def Assigned_Carrier(self):
        self.genericMethod.click(LoginPage.CarrierSave(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.CloseAssignWindow(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.AssignCarrierClick(self))
        time.sleep(1)
        # self.genericMethod.click(LoginPage.AssignCompareRates(self))
        # time.sleep(1)
        # self.genericMethod.click(LoginPage.Compare(self))
        # time.sleep(8)

    def Save_BookingNumber(self):
        BookingId = self.genericMethod.getText(LoginPage.Toast_Message(self))
        myLogger.info(BookingId)
        cl = "D2"
        self.genericMethod.WRITEEXCELDATA(cl, BookingId)
        time.sleep(1)

    # ******************************************* Carrier Bookings*******************************************#
    def Execution(self):
        return self.driver.find_element(By.XPATH, "// *[text() = 'Execution']")

    def Bookings(self):
        return self.driver.find_element(By.XPATH, "// *[text() = 'Bookings']")

    def Transportorders(self):
        return self.driver.find_element(By.XPATH, "//a[contains(text(),'Transport Orders')]")

    def Clickfilter(self):
        return self.driver.find_element(By.XPATH, "//a[contains(@class,'btn-float py-2')]//phoenix-icons[1]")

    def TransportStatus_select(self):
        return self.driver.find_element(By.XPATH, "//select[@formcontrolname='transportStatus']")
        time.sleep(3)

    def page_expand(self):
        return self.driver.find_element(By.XPATH,
                                        "(//button[contains(@class,'btn-function-light shadow')]//phoenix-icons)[1]")
        time.sleep(3)

    def CarrierBookings_Expand(self):
        return self.driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-icon')]//phoenix-icons)[1]")

    def hyperlink_Click(self):
        return self.driver.find_element(By.XPATH, "//lib-booking-carriers//tr[2]//td[2]")

    def status_Transport(self):
        return self.driver.find_element(By.XPATH, "(//button[contains(@class,'teritory-button py-1')])[1]")

    def click_Trip_status(self):
        return self.driver.find_element(By.XPATH, "//span[contains(@class,'position-relative d-block')]//select[1]")

    def save_Click(self):
        return self.driver.find_element(By.XPATH, "(//button[@type='submit'])[2]")

    def Trip_status_menu_close(self):
        return self.driver.find_element(By.XPATH, "(//em[contains(@class,'bi bi-x-lg')])[3]")

    def Trip_edit_click(self):
        return self.driver.find_element(By.XPATH, "(//button[contains(@class,'btn-float py-2')]//phoenix-icons)[2]")

    def Booking_confirmation_number_Enter(self):
        return self.driver.find_element(By.XPATH, "(//input[@formcontrolname='bookingConfirmationNumber']")

    ##########################################################################################################
    def Execution_Menu(self):
        self.genericMethod.click(LoginPage.Execution(self))
        time.sleep(1)

    def Bookings_Button(self):
        self.genericMethod.click(LoginPage.Bookings(self))
        time.sleep(1)

    def Transport_orders(self):
        self.genericMethod.click(LoginPage.Transportorders(self))
        time.sleep(1)

    def Click_filter(self):
        self.genericMethod.click(LoginPage.Clickfilter(self))
        time.sleep(2)

    def Select_TransportStatus(self):
        self.genericMethod.click(LoginPage.TransportStatus_select(self))
        select.select_by_visible_text("Booking Requested")
        time.sleep(5)

    def expand_page(self):
        self.genericMethod.click(LoginPage.page_expand(self))

    def Expand_Carrier_Bookings(self):
        self.genericMethod.click(LoginPage.CarrierBookings_Expand(self))
        time.sleep(1)

    def Click_hyperlink(self):
        self.genericMethod.click(LoginPage.hyperlink_Click(self))
        time.sleep(1)

        # Cell = 'D2'
        # d = self.genericMethod.READEXCELDATA(Cell)
        # v = d.split(" ")
        # c = v[5]
        # myLogger.info(c)
        # self.genericMethod.type(LoginPage.CarrierBookings_Search(self), c)
        # cl = "D5"
        # self.genericMethod.WRITEEXCELDATA(cl, c)
        # time.sleep(1)

    def Transport_status(self):
        self.genericMethod.click(LoginPage.status_Transport(self))
        time.sleep(1)

    def Tripstatus_click(self):
        # self.genericMethod.click(LoginPage.click_Trip_status(self))
        Trip = Select(LoginPage.click_Trip_status(self))
        Trip.select_by_visible_text("Booking Confirmed")
        time.sleep(2)

    def Click_save(self):
        self.genericMethod.click(LoginPage.save_Click(self))
        time.sleep(1)

    def Close_trip_status_menu(self):
        self.genericMethod.click(LoginPage.Trip_status_menu_close(self))
        time.sleep(1)

    def Click_trip_edit(self):
        self.genericMethod.click(LoginPage.Trip_edit_click(self))
        time.sleep(1)

    def Enter_Booking_confirmation_number(self):
        self.genericMethod.click(LoginPage.Booking_confirmation_number_Enter(self))
        time.sleep(1)

    # ***************************************************** LogOut *********************************************#

    def DipatchIcon(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Dispatch']")

    def DipatchPlanning(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Dispatch Planning']")

    def DispatchCountry(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()=' Select Load (Dispatch) Sites ']/..//parent::*//*[@placeholder='Select Country']")

    def DispatchCity(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()=' Select Load (Dispatch) Sites ']/..//parent::*//*[@placeholder='Select City']")

    def DispatchSite(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()=' Select Load (Dispatch) Sites ']/..//parent::*//*[@placeholder='Select Site']")

    def DispatchProceed(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Proceed ']")

    ############################################################################################################
    def Dispatch(self):
        self.genericMethod.click(LoginPage.DipatchIcon(self))
        time.sleep(1)

    def Dispatch_Planning(self):
        self.genericMethod.click(LoginPage.DipatchPlanning(self))
        time.sleep(1)

    def Dispatch_Country(self):
        self.genericMethod.click(LoginPage.DispatchCountry(self))
        time.sleep(1)

    def Dispatch_City(self):
        self.genericMethod.click(LoginPage.DispatchCity(self))
        time.sleep(1)

    def Dispatch_Site(self):
        self.genericMethod.click(LoginPage.DispatchSite(self))
        time.sleep(1)

    def Dispatch_proceed(self):
        self.genericMethod.click(LoginPage.DispatchProceed(self))
        time.sleep(1)

    # **************************************************** Trips ********************************************#

    def Tripsclick(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Trips']")

    def trips(self):
        self.genericMethod.click(LoginPage.Tripsclick(self))

    # **************************************************Freight audit*********************************************#

    def Settlement(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Settlement']")

    def freightaudit(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Freight Audit']")

    def importinvoice(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Import Invoice ']")

    # def importinvoice(self):
    #     return self.driver.find_element(By.XPATH, "//button[text()=' Import Invoice ']")

    ############################################################################################
    def clickSettlement(self):
        self.genericMethod.click(LoginPage.Settlement(self))

    def Clickfreightaudit(self):
        self.genericMethod.click(LoginPage.freightaudit(self))
        time.sleep(2)

    def clickimportinvoice(self):
        self.genericmethod.click(LoginPage.importinvoice(self))

    def importauditfile(self):
        self.genericMethod.click(LoginPage.freightaudit_fileimport(self))
        time.sleep(1)
        # Path = "E://Phoenix_20High//Upload//RateCard_Function.xlsm"
        Path = "E://Phoenix_20High//Upload//Invoice_Upload_Template.xlsx"
        self.genericMethod.Upload(LoginPage.freightaudit_fileinsert(self), Path)
        self.genericMethod.click(LoginPage.freightaudit_fileimportUpload(self))
        time.sleep(8)

        # ***********************Dashboard****************************#

        def navigatedashboard1(self):
            return self.driver.find_element(By.XPATH, "(//span[text()='Dashboard')]")

        def mouse_hover_on_delivery_quality_tab(self):
            return self.driver.find_element(By.XPATH,
                                            "//*[@id='right-main-panel']/div/lib-dashboard/div/div[2]/div/div/div/div[1]/lib-delivery-timelines/div/div[1]/div[1]/div")

        def mouse_hover_on_delivery_timeliness(self):
            return self.driver.find_element(By.XPATH, "(//div[text()='Delivery Timeliness'])")

        def click_on_advance_filter(self):
            return self.driver.find_element(By.XPATH, "(//phoenix-icons[contains(@name,'filter')])")

        def click_on_checkbox_and_uncheck_for_etd(self):
            return self.driver.find_element(By.XPATH, "(//input[@type='checkbox'])")

        def click_on_checkbox_and_uncheck_for_eta(self):
            return self.driver.find_element(By.XPATH, "(//input[@type='checkbox'])")

        def click_on_apply_button(self):
            return self.driver.find_element(By.XPATH, "(//button[@type='submit']//em)")

        #################################Dashboard############################################

    def mouse_hover_on_delivery_quality_tab(self):
        self.genericMethod.MouseHover(LoginPage.mouse_hover_on_delivery_quality_tab(self))

    # ***************************************************** LogOut *********************************************#

    def EssplLOGO(self):
        return self.driver.find_element(By.XPATH, "//*[@id='dropdownMenuAvatar']")

    def ButtonLogOUT(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Logout ']")

    ############################################################################################################
    def ClikEssplLogo(self):
        self.genericMethod.click(LoginPage.EssplLOGO(self))
        time.sleep(1)

    def LogOutBTN(self):
        self.genericMethod.click(LoginPage.ButtonLogOUT(self))
        time.sleep(1)

    # ********************** autogenrate_FO_with_the_available_rulesets ****************************#

    # def Filter(self):
    #     return self.driver.find_element(By.XPATH, "//*[@class='bi bi-funnel']")

    def Filter(self):
        return self.driver.find_element(By.XPATH, "//*[@name='filter']")

    # def Filter(self):
    #     return self.driver.find_element(By.XPATH, "//*[@role='submit']")

    def Consolidation_Status(self):
        return self.driver.find_element(By.XPATH, "// *[ @ id = 'consStatus']")

    def from_date1(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(@class,'ngb-dp-month ng-star-inserted')][1]//span[contains(text(),'" + date2 + "')]")

    def to_date1(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(@class,'ngb-dp-month ng-star-inserted')][2]//span[contains(text(),'" + date3 + "')]")

    def FT_date(self):
        return self.driver.find_element(By.XPATH, "// *[contains(text(), 'From / To Date')]")

    def search(self):
        return self.driver.find_element(By.XPATH, "// *[contains( @ type, 'submit')]")

    def Unconsolidated(self):
        return self.driver.find_element(By.XPATH,
                                        "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td//*[contains(@type,'checkbox')]")

    def SaveFORefNo(self):
        return self.driver.find_element(By.XPATH,
                                        "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td//*[contains(@class,'cursor-pointer')]")

    def Unconsolidated2(self):
        return self.driver.find_element(By.XPATH,
                                        "(//ngb-highlight[contains(text(),'Unconsolidated')])[2]/parent::*/preceding-sibling::td//*[contains(@type,'checkbox')]")

    def OrderRefNo(self):
        return self.driver.find_element(By.XPATH,
                                        "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td//*[@class='cursor-pointer']")

    def Origin_Country_City(self):
        return self.driver.find_element(By.XPATH,
                                        "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td/../*[5]")

    def Destination_Country_City(self):
        return self.driver.find_element(By.XPATH,
                                        "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td/../*[6]")

    def CustCodeR(self):
        return self.driver.find_element(By.XPATH,
                                        "(//ngb-highlight[contains(text(),'Unconsolidated')])[1]/parent::*/preceding-sibling::td[6]/*")

    def Consolidate(self):
        return self.driver.find_element(By.XPATH, "// *[contains(text(), 'Consolidate Order')]")

    def Tracking_No(self):
        return self.driver.find_element(By.XPATH, "//*[@class='toast-body']")

    def Fo_Status(self):
        return self.driver.find_element(By.XPATH, "//*[text()='fo created successfully']")

    def notification(self):
        return self.driver.find_element(By.XPATH, "// *[contains( @ alt, 'notification')]")

    def TrSearch(self):
        return self.driver.find_element(By.XPATH, "//*[@id='Capa_1']")

    def SearchBTN_TR(self):
        return self.driver.find_element(By.XPATH,
                                        "//input[@placeholder='Search...']/..//*[@class='form-control form-control-sm ng-untouched ng-pristine ng-valid ng-star-inserted']")

    def notificationCheck(self):
        return self.driver.find_element(By.XPATH, "(// *[contains(text(), 'Request is complete')])[1]")

    def View_Fos(self):
        return self.driver.find_element(By.XPATH, " (//*[contains(text(),'View Fos')])[1]")

    def FO_Number_save(self):
        return self.driver.find_element(By.XPATH, "//*[@class='cursor-pointer']")

    def togglemenu(self):
        return self.driver.find_element(By.XPATH, "//*[@id='togglemenu']")

    def Shipment(self):
        return self.driver.find_element(By.XPATH, "// span[text() = 'Shipment']")

    def FreightOrders(self):
        return self.driver.find_element(By.XPATH, "// a[text() = 'Freight Orders']")

    def RightArrow(self):
        return self.driver.find_element(By.XPATH, "//*[@title='Next month']")

    #################################################################################################
    def ScrollOnPlanning(self):
        self.genericMethod.Refresh()
        time.sleep(1)
        self.genericMethod.click(LoginPage.Planning(self))

    def Sequence_rule_set(self):
        # self.genericMethod.click(LoginPage.PolicyType(self))
        self.genericMethod.click(LoginPage.Default_Sequence(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Close_Button(self))
        time.sleep(1)

    def ClickFilter(self):
        self.genericMethod.click(LoginPage.Orders(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Filter(self))
        time.sleep(1)

    def ClickconsolidationStatus(self, unconsolidate):
        Con = Select(LoginPage.Consolidation_Status(self))
        Con.select_by_visible_text(unconsolidate)
        # time.sleep(2)

    def ChooseDateTyper(self, DateType):
        # self.genericMethod.click(LoginPage.OrderType(self))
        drp = Select(LoginPage.OrderType(self))
        drp.select_by_visible_text(DateType)
        time.sleep(2)

    # def clickcalender(self):
    #     self.genericMethod.click(LoginPage.calendar(self))
    #     time.sleep(2)

    # def slectMonth(self, month):
    #     drp = Select(LoginPage.Month_Select(self))
    #     drp.select_by_visible_text(month)
    #     time.sleep(2)
    #
    def ChooseDate(self, from_date1, to_date1):
        global date2
        global date3
        date2 = from_date1
        date3 = to_date1
        self.genericMethod.click(LoginPage.from_date1(self))
        self.genericMethod.click(LoginPage.RightArrow(self))
        time.sleep(1)
        # self.genericMethod.click(LoginPage.RightArrow(self))
        # time.sleep(1)
        # self.genericMethod.click(LoginPage.RightArrow(self))
        # time.sleep(1)
        # self.genericMethod.click(LoginPage.RightArrow(self))
        self.genericMethod.click(LoginPage.to_date1(self))
        self.genericMethod.click(LoginPage.FT_date(self))

    def searchButton(self):
        self.genericMethod.click(LoginPage.search(self))
        time.sleep(1)

    def order_orderline(self) -> object:
        global country
        global city
        global Dest_country
        global Dest_city
        self.genericMethod.click(LoginPage.Unconsolidated(self))
        v = self.genericMethod.getText(LoginPage.SaveFORefNo(self))
        myLogger.info(v)
        self.genericMethod.WriteData(".//TestData//FORefNumber.json", "OrderRefNumber", v)
        Country_City = self.genericMethod.getText(LoginPage.Origin_Country_City(self))
        dest_Con_City = self.genericMethod.getText(LoginPage.Destination_Country_City(self))
        v = Country_City.split("|")
        country = v[0].strip(" ") + "-"
        self.genericMethod.WriteData(".//TestData//OriginCountry.json", "OriginCountry", country)
        city = v[1].strip(" ") + "-"
        self.genericMethod.WriteData(".//TestData//OriginCity.json", "OriginCity", city)
        a = dest_Con_City.split("|")
        Dest_country = a[0].strip(" ") + "-"
        self.genericMethod.WriteData(".//TestData//DestinationCountry.json", "Dest_country", Dest_country)
        Dest_city = a[1].strip(" ") + "-"
        self.genericMethod.WriteData(".//TestData//DestinationCity.json", "Dest_city", Dest_city)
        custCode = self.genericMethod.getText(LoginPage.CustCodeR(self))
        self.genericMethod.WriteData(".//TestData//Customer.json", "Customer", custCode)

    def Order_Reference_Number(self):
        global OrdRefNo
        OrdRefNo = self.genericMethod.getText(LoginPage.OrderRefNo(self))
        myLogger.info(OrdRefNo)
        self.genericMethod.WriteData(".//TestData//OrderRefNumber.json", "OrderRefNumber", OrdRefNo)

    def consolidationButton(self):
        self.genericMethod.click(LoginPage.Consolidate(self))
        time.sleep(2)

    def Tr_No(self):
        global c1
        v1 = self.genericMethod.getText(LoginPage.Tracking_No(self))
        myLogger.info(v1)
        c1 = v1.split("-")
        expected_status = "Order Consolidation Initiated"
        actual_status = c1[0]
        myLogger.info(actual_status)
        myLogger.info(c1[1])
        if actual_status == expected_status:
            assert True
        else:
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="Tr_Status",
                          attachment_type=AttachmentType.PNG)
            message = "The actual and expected are not matched", "actual->  " + actual_status, 'expected-> ' + expected_status
            assert actual_status == expected_status, message
            time.sleep(2)
            assert False

    def notificationButton(self):
        self.genericMethod.click(LoginPage.notification(self))
        time.sleep(4)
        self.genericMethod.click(LoginPage.TrSearch(self))
        time.sleep(1)
        self.genericMethod.type(LoginPage.SearchBTN_TR(self), c1[1])
        # time.sleep(1)
        # self.genericMethod.click(LoginPage.notificationCheck(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.View_Fos(self))
        time.sleep(2)
        global fo
        fo = self.genericMethod.getText(LoginPage.FO_Number_save(self))
        myLogger.info(fo)
        self.genericMethod.click(LoginPage.togglemenu(self))
        time.sleep(1)

    def NotificationClick(self):
        self.genericMethod.click(LoginPage.notification(self))
        time.sleep(4)
        self.genericMethod.click(LoginPage.View_Fos(self))
        time.sleep(2)
        self.genericMethod.click(LoginPage.togglemenu(self))
        time.sleep(1)

    def Notification_Click(self):
        self.genericMethod.click(LoginPage.notification(self))
        time.sleep(2)

    # ***********************************     Manually create_FO_from_orders     **************************************#
    def FrieghtOrder(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Create Freight Order']")

    def OrderCreate(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Create From Orders ']")

    def proceedButton(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Proceed '] ")

    def FoHeader(self):
        return self.driver.find_element(By.XPATH, "//*[text()='FO Header']")

    def PartyDetails(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Party Details']")

    def ShipperAttentionTo(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperAttentionTo']")

    def ShipperBECode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperBeCode']")

    def shipperName(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperName']")

    def shipperPhone(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperPhone']")

    def shipperMobile(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperMobile']")

    def shipperEmail(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperEmail']")

    def shipperFax(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='shipperFax']")

    def consigneeAttentionTo(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeAttentionTo']")

    def consigneeBECode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeBeCode']")

    def consigneeName(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeName']")

    def consigneePhone(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneePhone']")

    def consigneeMobile(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeMobile']")

    def consigneeEmail(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeEmail']")

    def consigneeFax(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='consigneeFax']")

    def Save_Proceed(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save & Proceed ']")

    def Itemselect(self):
        return self.driver.find_element(By.XPATH, "//*[@class='c-p ng-star-inserted'][1]/./td[3]")

    def ItemDetails(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Item Details']")

    def HandlingDetails(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Handling Details']")

    def O_D_Details(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Origin & Destination']")

    def checkPartyDetails(self):
        return self.driver.find_element(By.XPATH, "(//*[text()='Party Details'])[2]")

    def LoadDetails(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Load & Discharge (AIR/SEA)']")

    def SaveAllDetails(self):
        return self.driver.find_element(By.XPATH, "//*[@id='save']")

    def DetailsSaveOrderline(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save ']")

    def Toast_Message(self):
        return self.driver.find_element(By.XPATH, "//*[@class='toast-body']")

    ###########################################################################################################
    def CreateFreightOrder(self):
        self.genericMethod.click(LoginPage.FrieghtOrder(self))
        time.sleep(1)

    def Create_Order(self):
        self.genericMethod.click(LoginPage.OrderCreate(self))
        time.sleep(2)
        self.genericMethod.click(LoginPage.Filter(self))
        time.sleep(1)

    def proceed(self):
        self.genericMethod.click(LoginPage.proceedButton(self))
        time.sleep(1)

    def Mousehoverfoheader(self):
        self.genericMethod.click(LoginPage.FoHeader(self))
        time.sleep(1)

    def clickPartyDetailsPage(self, ShipperAttention, ShipperBECode, ShipperName, ShipperPhone, ShipperMobile,
                              ShipperEmail, ShipperFax, ConsigneeAttention, ConsigneeBECode, ConsigneeName,
                              ConsigneePhone, ConsigneeMobile, ConsigneeEmail, ConsigneeFax):
        self.genericMethod.click(LoginPage.PartyDetails(self))
        time.sleep(1)
        self.genericMethod.type(LoginPage.ShipperAttentionTo(self), ShipperAttention)

        self.genericMethod.type(LoginPage.ShipperBECode(self), ShipperBECode)

        self.genericMethod.type(LoginPage.shipperName(self), ShipperName)

        self.genericMethod.type(LoginPage.shipperPhone(self), ShipperPhone)

        self.genericMethod.type(LoginPage.shipperMobile(self), ShipperMobile)

        self.genericMethod.type(LoginPage.shipperEmail(self), ShipperEmail)

        self.genericMethod.type(LoginPage.shipperFax(self), ShipperFax)

        self.genericMethod.type(LoginPage.consigneeAttentionTo(self), ConsigneeAttention)

        self.genericMethod.type(LoginPage.consigneeBECode(self), ConsigneeBECode)

        self.genericMethod.type(LoginPage.consigneeName(self), ConsigneeName)

        self.genericMethod.type(LoginPage.consigneePhone(self), ConsigneePhone)

        self.genericMethod.type(LoginPage.consigneeMobile(self), ConsigneeMobile)

        self.genericMethod.type(LoginPage.consigneeEmail(self), ConsigneeEmail)

        self.genericMethod.type(LoginPage.consigneeFax(self), ConsigneeFax)

    def saveandprocced(self):
        self.genericMethod.click(LoginPage.Save_Proceed(self))
        time.sleep(1)

    def item(self):
        self.genericMethod.click(LoginPage.Itemselect(self))
        time.sleep(1)

    def bookingdetails(self):
        self.genericMethod.click(LoginPage.Itemselect(self))
        time.sleep(2)

    def itemdetails(self):
        self.genericMethod.click(LoginPage.ItemDetails(self))
        time.sleep(2)

    def handlingdetails(self):
        self.genericMethod.click(LoginPage.HandlingDetails(self))
        time.sleep(2)

    def originanddestination(self):
        self.genericMethod.click(LoginPage.O_D_Details(self))
        time.sleep(2)

    def Party_detailscheck(self):
        self.genericMethod.click(LoginPage.checkPartyDetails(self))
        time.sleep(2)

    def loadanddischarge(self):
        self.genericMethod.click(LoginPage.LoadDetails(self))
        time.sleep(2)

    def saveButton(self):
        self.genericMethod.click(LoginPage.SaveAllDetails(self))
        time.sleep(1)

    def saveDetails(self):
        self.genericMethod.click(LoginPage.DetailsSaveOrderline(self))
        time.sleep(1)

    def ToastMessage(self, message):
        Expected = message
        Actual = self.genericMethod.getText(LoginPage.Toast_Message(self))
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    def ManuallFOSave(self):
        global ManuallFO
        ManuallFO = self.genericMethod.getText(LoginPage.FO_Number_save(self))
        myLogger.info(ManuallFO)
        # self.genericMethod.WriteData(".//TestData//EquipmentID.json", "EquipmentID", d)
        time.sleep(1)

    # ********************************* Edit_FO  ************************************************
    def FO_EDIT(self):
        return self.driver.find_element(By.XPATH, "//*[@id='edit']")

    def REF_FOLINE(self):
        return self.driver.find_element(By.XPATH, "(//td[text()=' SO '])[1]")

    ###########################################################################################################
    def EditFO(self):
        self.genericMethod.click(LoginPage.FO_EDIT(self))
        time.sleep(1)

    def FOItemClick(self):
        # global FO
        # FO = self.genericMethod.ReadData(".//TestData//FORefNumber.json", "OrderRefNumber")
        # myLogger.info("****************" + s)
        self.genericMethod.click(LoginPage.REF_FOLINE(self))
        time.sleep(1)

    def party_details(self):
        self.genericMethod.click(LoginPage.PartyDetails(self))
        time.sleep(1)

    def shippername(self, shipper_name):
        self.genericMethod.click(LoginPage.shipperName(self))
        # self.genericMethod.Clear()
        self.genericMethod.type(LoginPage.shipperName(self), shipper_name)
        time.sleep(1)

    def consigneename(self, consignee_name):
        self.genericMethod.click(LoginPage.consigneeName(self))
        self.genericMethod.type(LoginPage.consigneeName(self), consignee_name)
        time.sleep(1)

    # ********************************* Delete_FO  ************************************************

    def FoField(self):
        return self.driver.find_element(By.XPATH, "//th[text()=' FO #']")

    def close(self):
        return self.driver.find_element(By.XPATH, "(//*[@id='close'])[1]")

    def SinglecheckBox(self):
        return self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[2]")

    def SingleDelete(self):
        return self.driver.find_element(By.XPATH,
                                        "(//*[@ type='checkbox'])[2]//parent::*/following-sibling::td[12]//*[@id='delete']")

    def viewFo(self):
        return self.driver.find_element(By.XPATH,
                                        "(//*[@ type='checkbox'])[2]//parent::*/following-sibling::td[13]//*[@type]")

    def UOM(self):
        return self.driver.find_element(By.XPATH, "//th[text()='UOM'][1]")

    def RefOrder(self):
        return self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[4]//parent::*/following-sibling::td[2]")

    def OrderRefference(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='item']")

    def Status_OrderRefference(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()='" + b + "']/.././/parent::*/following-sibling::td[7]")

    def DeleteFO_Button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='delete']")

    # NEWLY ADDED
    def Ref_Check_Box(self):
        return self.driver.find_element(By.XPATH,
                                        "(//*[@type='checkbox'])[1]")

    #################################################################################################
    def freightButon(self):
        self.genericMethod.Refresh()
        time.sleep(3)
        self.genericMethod.click(LoginPage.Planning(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Shipment(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.FreightOrders(self))
        time.sleep(1)

    def FOEnter(self):
        self.genericMethod.type(LoginPage.OrderRefference(self), ManuallFO)
        self.act.send_keys(Keys.ENTER).perform()
        time.sleep(2)
        self.genericMethod.click(LoginPage.search(self))
        time.sleep(2)

    def DeleteFO(self):
        self.genericMethod.click(LoginPage.DeleteFO_Button(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.DeleteIcon(self))
        time.sleep(1)

    def SaveOrderNumber(self):
        self.genericMethod.click(LoginPage.FoField(self))
        self.genericMethod.click(LoginPage.close(self))
        self.genericMethod.click(LoginPage.SinglecheckBox(self))
        self.genericMethod.click(LoginPage.viewFo(self))
        time.sleep(2)
        self.genericMethod.click(LoginPage.RefOrder(self))
        global b
        b = self.genericMethod.getText(LoginPage.RefOrder(self))
        myLogger.info(b)
        time.sleep(2)

    def singleFO(self):
        self.genericMethod.click(LoginPage.SinglecheckBox(self))
        self.genericMethod.click(LoginPage.SingleDelete(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.DeleteIcon(self))

    def SelectmultipleFO(self):
        self.genericMethod.click(LoginPage.FoField(self))

    def orderrepository(self):
        # self.genericMethod.click(LoginPage.Planning(self))
        # self.genericMethod.click(LoginPage.Orders(self))
        # time.sleep(2)
        self.genericMethod.click(LoginPage.OrderRefference(self))
        # self.act.send_keys(Keys.ENTER).perform()

    def ORDERREFNUM(self, refnumber):
        # Ref1 = "501865"
        # Ref2 = "501805"
        self.genericMethod.type(LoginPage.OrderRefference(self), refnumber)
        self.act.send_keys(Keys.ENTER).perform()
        time.sleep(3)
        # self.genericMethod.type(LoginPage.OrderRefference(self), refnumber)
        # self.act.send_keys(Keys.ENTER).perform()
        # time.sleep(1)

    def OrderReFNumberSearch(self):
        self.genericMethod.click(LoginPage.search(self))
        time.sleep(2)
        # self.genericMethod.click(LoginPage.Ref_Check_Box(self))
        # time.sleep(1)

    def RefCheckBoxM(self):
        self.genericMethod.click(LoginPage.Ref_Check_Box(self))
        time.sleep(2)

    def OrderReFNumberstatus(self, status):
        expected = status
        actual = self.genericMethod.getText(LoginPage.Status_OrderRefference(self))
        myLogger.info(actual)
        if actual == expected:
            assert True
        else:
            time.sleep(1)
            allure.attach(self.driver.get_screenshot_as_png(), name="Status",
                          attachment_type=AttachmentType.PNG)
            message = "The actual and expected are not matched", "actual->  " + actual, 'expected-> ' + expected
            assert actual == expected, message
            assert False
            time.sleep(1)

        # self.genericMethod.click(LoginPage.search(self))
        # time.sleep(1)

    # ******************************************* Load ********************************************#
    def Loads(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Loads']")

    def Planloads(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Plan Load']")

    def ActiveOnly(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Show Active Only ']/parent::*//*[@type='checkbox']")

    ################################################################################################
    def LoadsButton(self):
        self.genericMethod.click(LoginPage.Loads(self))
        time.sleep(8)

    def PlanloadsButton(self):
        self.genericMethod.click(LoginPage.Planloads(self))
        time.sleep(1)

    def showactiveonlyButton(self):
        self.genericMethod.click(LoginPage.ActiveOnly(self))
        time.sleep(1)

    # ******************************************* Load ********************************************#
    def New_Workbench(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Create New Workbench']")

    def workbenchTitle(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='workbenchTitle']")

    def workbenchDesc(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='workbenchDesc']")

    def Requested_ETA(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='estimatedDateTypeETA']")

    # def Requested_ETA_Month(self):
    #     return self.driver.find_element(By.XPATH, "(// *[contains( @name, 'calendar')])[2]")

    def Requested_ETA_Calender(self):
        return self.driver.find_element(By.XPATH, "(// *[contains( @name, 'calendar')])[2]")

    def fromdate2(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space(text())='" + date4 + "']")

    def todate2(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space(text())='" + date5 + "']")

    def Arrfromdate2(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(@class,'ngb-dp-month ng-star-inserted')][1]//span[contains(text(),'" + date6 + "')]")

    def Arrtodate2(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[contains(@class,'ngb-dp-month ng-star-inserted')][1]//span[contains(text(),'" + date7 + "')]")

    def AddManually(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Add Manually']")

    def OriginCountry(self):
        return self.driver.find_element(By.XPATH, "//*[@placeholder='Enter the Country Name']")

    def Origincountrycode(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + originCtr_Code + "']")

    def Fetch_Country(self):
        return self.driver.find_element(By.XPATH, "//a[@class='ng-star-inserted']")

    def OriginCity(self):
        return self.driver.find_element(By.XPATH, "//*[@placeholder='Enter the City Name']")

    def OCity(self):
        return self.driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']")

    def OriginCityCode(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + Oricitycode + "']")

    def PlusButton(self):
        return self.driver.find_element(By.XPATH, "//*[@class='bi bi-plus-lg']")

    def LoadTrack(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Load']")

    def UnLoadTrack(self):
        return self.driver.find_element(By.XPATH, "(//*[text()='Unload'])[1]")

    def Dest_Country(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Enter the Country Name'])[1]")

    def Destcountrycode(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + DestCtr_Code + "']")

    def DestCity(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Enter the City Name'])[1]")

    def DestCityCode(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + Destcitycode + "']")

    def DC(self):
        return self.driver.find_element(By.XPATH, "//a[@class='ng-star-inserted']")

    def SearchUNL_L(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Search ']")

    def FO_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[text()= '" + fo + "']/..//*[@type='checkbox']")

    def ManuallFO_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[text()= '" + ManuallFO + "']/..//*[@type='checkbox']")

    def Fo_lineClick(self):
        return self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[2]")

    def Add_Foline(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Add FO Lines to Workbench ']")

    def XYAxis(self):
        return self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[6]")

    def Save_Proceed1(self):
        return self.driver.find_element(By.XPATH, "(//*[text()=' Save & Proceed '])[1]")

    def Rout_Site1(self):
        return self.driver.find_element(By.XPATH, "(//*[@name='site'])[1]")

    def Value1(self):
        return self.driver.find_element(By.XPATH, "(//*[@name='site'])[1]/.//option[@value='1']")

    def Rout_Site2(self):
        return self.driver.find_element(By.XPATH, "(//*[@name='site'])[2]")

    def Value2(self):
        return self.driver.find_element(By.XPATH, "(//*[@name='site'])[1]/.//option[@value='0']")

    def SaveRouteAs(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save Route As ']")

    def RouteName(self):
        return self.driver.find_element(By.XPATH, "//*[@placeholder='Route Name']")

    def RouteSave(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save ']")

    def RLSave_Proceed(self):
        return self.driver.find_element(By.XPATH, "(//*[text()=' Save & Proceed '])[2]")

    # def Equipment_CheckBox(self):
    #     return self.driver.find_element(By.XPATH, "//*[text()='Equipment']/..//*[@id='inlineCheckbox1']")
    def Equipment_CheckBox(self):
        return self.driver.find_element(By.XPATH, "(//*[@class='first-col']//*[@type='checkbox'])[2]")

    def Equipment_ID(self):
        return self.driver.find_element(By.XPATH,
                                        "(//*[@class='first-col']//*[@type='checkbox'])[2]/../..//parent::*/following-sibling::td[2]")

    def Equipment_AVL(self):
        return self.driver.find_element(By.XPATH,
                                        "(//*[@class='first-col']//*[@type='checkbox'])[2]/parent::*/../..//*[@type='number']")

    def Save_WB(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save Equipment ']")

    def GenerateLoadPaln(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Generate Load Plan ']")

    def MaxTime(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Max. Evalution Time (In Sec):']/..//*[@type='number']")

    def ExpandLoadResult(self):
        return self.driver.find_element(By.XPATH, "//*[@class='d-flex justify-content-start']")

    def ThreeDloadplan(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' View 3D Load Plan ']")

    def Animated(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='animate']")

    def ItemSizeCheckBox(self):
        # return self.driver.find_element(By.XPATH, "//*[@value='" + equipment + "']")
        return self.driver.find_element(By.XPATH, "//*[text()='Equipment Type']/..//*[@type='checkbox']")

    def SaveResult(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save Result ']")

    def GenerateLoad(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Generate Load']")

    def GENERATELoadMessage(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Load(s) saved successfully.']")

    def SAVEresult(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save Result ']")

    def TRNO_CLEAR(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Search...']")

    #########################################################################################################
    def workbench(self):
        self.genericMethod.click(LoginPage.New_Workbench(self))
        time.sleep(2)

    def workbench_Titel(self, title):
        a = title
        c = self.genericMethod.NumIncrement()
        global WBtitle
        WBtitle = a + str(c)
        self.genericMethod.WriteData(".//TestData//WBTitle.json", "WorkBenchTitle", WBtitle)
        self.genericMethod.type(LoginPage.workbenchTitle(self), WBtitle)
        time.sleep(1)

    def workbench_descprition(self, descprition):
        a = descprition
        c = self.genericMethod.NumIncrement()
        global WBdesc
        WBdesc = a + str(c)
        self.genericMethod.type(LoginPage.workbenchDesc(self), WBdesc)
        time.sleep(1)

    def workbenchcustomer(self):
        customerName = self.genericMethod.ReadData(".//TestData//Customer.json", "Customer")
        self.genericMethod.type(LoginPage.CustomerBox(self), customerName)
        self.act.send_keys(Keys.BACKSPACE).perform()
        time.sleep(4)
        self.genericMethod.click(LoginPage.Customer_option(self))

    def Depature_Date(self, from_date2, to_date2):
        global date4
        global date5
        date4 = from_date2
        date5 = to_date2
        self.genericMethod.click(LoginPage.fromdate2(self))
        self.genericMethod.click(LoginPage.RightArrow(self))
        self.genericMethod.click(LoginPage.RightArrow(self))
        self.genericMethod.click(LoginPage.todate2(self))
        self.genericMethod.click(LoginPage.workbenchTitle(self))
        time.sleep(2)

    def RequestedETA(self, DateTypeETA):
        self.genericMethod.click(LoginPage.workbenchTitle(self))
        drp = Select(LoginPage.Requested_ETA(self))
        drp.select_by_visible_text(DateTypeETA)
        time.sleep(2)

    def ETA_calender(self):
        self.genericMethod.click(LoginPage.Requested_ETA_Calender(self))

    def RequestedETA_Month(self, month2):
        drp3 = Select(LoginPage.Month_Select(self))
        drp3.select_by_visible_text(month2)
        time.sleep(2)

    def Arrival_Date(self, from_date3, to_date3):
        global date6
        global date7
        date6 = from_date3
        date7 = to_date3
        self.genericMethod.click(LoginPage.Arrfromdate2(self))
        self.genericMethod.click(LoginPage.Arrtodate2(self))
        self.genericMethod.click(LoginPage.workbenchTitle(self))
        time.sleep(2)

    def Add_Mannualy(self):
        self.genericMethod.click(LoginPage.AddManually(self))
        time.sleep(1)

    def Origin_Country(self):
        self.genericMethod.click(LoginPage.OriginCountry(self))
        global originCtr_Code
        global Oricitycode
        global r2
        originCtr_Code = self.genericMethod.ReadData(".//TestData//OriginCountry.json", "OriginCountry")
        self.genericMethod.type(LoginPage.OriginCountry(self), originCtr_Code)
        v = self.genericMethod.getText(LoginPage.Fetch_Country(self))
        Cell = 'B4'
        self.genericMethod.WRITEEXCELDATA_XLSM(Cell, v)
        self.genericMethod.click(LoginPage.Origincountrycode(self))

        time.sleep(2)
        Oricitycode = self.genericMethod.ReadData(".//TestData//OriginCity.json", "OriginCity")
        self.genericMethod.type(LoginPage.OriginCity(self), Oricitycode)
        self.genericMethod.click(LoginPage.OriginCityCode(self))
        self.genericMethod.click(LoginPage.OriginCity(self))
        c = self.genericMethod.getText(LoginPage.OCity(self))
        Cell = 'C4'
        self.genericMethod.WRITEEXCELDATA_XLSM(Cell, c)
        r = c.split("-")
        r2 = r[1]
        myLogger.info(r2)
        time.sleep(3)
        self.genericMethod.click(LoginPage.OCity(self))
        time.sleep(1)

    def SelectLoad(self):
        self.genericMethod.click(LoginPage.LoadTrack(self))
        self.genericMethod.click(LoginPage.PlusButton(self))
        time.sleep(1)

    def DestCountry(self):
        self.genericMethod.click(LoginPage.Dest_Country(self))
        global DestCtr_Code
        global Destcitycode
        global r3
        DestCtr_Code = self.genericMethod.ReadData(".//TestData//DestinationCountry.json", "Dest_country")
        self.genericMethod.type(LoginPage.Dest_Country(self), DestCtr_Code)
        v = self.genericMethod.getText(LoginPage.Fetch_Country(self))
        Cell = 'E4'
        self.genericMethod.WRITEEXCELDATA_XLSM(Cell, v)
        self.genericMethod.click(LoginPage.Destcountrycode(self))
        # c = self.genericMethod.getText(LoginPage.DCountry(self))
        # r = c.split("-")
        # r2 = r[1]
        # myLogger.info(r2)
        # self.genericMethod.click(LoginPage.DCountry(self))
        time.sleep(1)
        Destcitycode = self.genericMethod.ReadData(".//TestData//DestinationCity.json", "Dest_city")
        self.genericMethod.type(LoginPage.DestCity(self), Destcitycode)
        self.genericMethod.click(LoginPage.DestCityCode(self))
        self.genericMethod.click(LoginPage.DestCity(self))
        d = self.genericMethod.getText(LoginPage.DC(self))
        Cell = 'F4'
        self.genericMethod.WRITEEXCELDATA_XLSM(Cell, d)
        r1 = d.split("-")
        r3 = r1[1]
        myLogger.info(r3)
        self.genericMethod.click(LoginPage.DC(self))

    def SelectUNLoad(self):
        self.genericMethod.click(LoginPage.UnLoadTrack(self))
        self.genericMethod.click(LoginPage.PlusButton(self))
        time.sleep(1)

    def searchBTN(self):
        self.genericMethod.click(LoginPage.SearchUNL_L(self))
        time.sleep(1)

    def ListFO(self):
        self.genericMethod.click(LoginPage.FO_Choose(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Add_Foline(self))
        time.sleep(1)

    def ListManuallFO(self):
        self.genericMethod.click(LoginPage.ManuallFO_Choose(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Add_Foline(self))
        time.sleep(1)

    def xy_Axis_click(self):
        self.genericMethod.click(LoginPage.XYAxis(self))
        time.sleep(1)

    def save_proceed(self):
        self.genericMethod.click(LoginPage.Save_Proceed1(self))
        time.sleep(1)

    def Route_Leg(self):
        RL = Select(LoginPage.Rout_Site1(self))
        RL.select_by_index(0)
        self.act.send_keys(Keys.ARROW_DOWN).perform()
        self.act.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        RL1 = Select(LoginPage.Rout_Site2(self))
        RL1.select_by_index(1)
        self.act.send_keys(Keys.ARROW_UP).perform()
        self.act.send_keys(Keys.ENTER).perform()
        time.sleep(1)

    def RouteSaveAS(self):
        self.genericMethod.click(LoginPage.SaveRouteAs(self))
        time.sleep(1)

    def RouteNameEnter(self, routeName):
        a = routeName
        c = self.genericMethod.NumIncrement()
        global routeName1
        routeName1 = a + str(c)
        myLogger.info(routeName1)
        self.genericMethod.type(LoginPage.RouteName(self), routeName1)
        time.sleep(1)
        self.genericMethod.click(LoginPage.RouteSave(self))

    def RL_save_proceed(self):
        self.genericMethod.click(LoginPage.RLSave_Proceed(self))
        time.sleep(1)

    def equipmentType(self):
        self.genericMethod.click(LoginPage.Equipment_CheckBox(self))
        d = self.genericMethod.getText(LoginPage.Equipment_ID(self))
        self.genericMethod.WriteData(".//TestData//EquipmentID.json", "EquipmentID", d)
        time.sleep(1)
        v = "8"
        self.genericMethod.type(LoginPage.Equipment_AVL(self), v)
        self.genericMethod.Clear(LoginPage.MaxTime(self))
        time.sleep(2)
        MaxSec = "5"
        self.genericMethod.type(LoginPage.MaxTime(self), MaxSec)
        self.genericMethod.click(LoginPage.Save_WB(self))
        time.sleep(2)

    def Genearte_LoadPlan(self):
        self.genericMethod.click(LoginPage.GenerateLoadPaln(self))
        time.sleep(10)
        # self.genericMethod.defaultTime()
        # self.genericMethod.click(LoginPage.ExpandLoadResult(self))
        # time.sleep(1)

    def loadResult1(self):
        self.genericMethod.click(LoginPage.ExpandLoadResult(self))
        # self.genericMethod.defaultTime()
        time.sleep(1)

    def ChooseEquipment(self):
        global equipment
        equipment = self.genericMethod.ReadData(".//TestData//EquipmentID.json", "EquipmentID")
        self.genericMethod.click(LoginPage.ItemSizeCheckBox(self))
        time.sleep(1)

    def Generate_Load(self):
        self.genericMethod.click(LoginPage.GenerateLoad(self))
        time.sleep(6)

    def GenerateLoad_meassage(self, meassage):
        Expected = meassage
        Actual = self.genericMethod.getText(LoginPage.Toast_Message(self))
        myLogger.info(Actual)
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    def Save_Result(self):
        time.sleep(3)
        self.genericMethod.click(LoginPage.SAVEresult(self))
        time.sleep(4)

    def SaveResult_meassage(self, meassage1):
        Expected = meassage1
        myLogger.info(Expected)
        Actual = self.genericMethod.getText(LoginPage.Toast_Message(self))
        myLogger.info(Actual)
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    def Three_D_Plan(self):
        self.genericMethod.click(LoginPage.ThreeDloadplan(self))
        time.sleep(1)
        self.genericMethod.Refresh()
        time.sleep(2)

    def GraphicalMode(self):
        RL1 = Select(LoginPage.Animated(self))
        RL1.select_by_index(2)
        time.sleep(60)
        RL1 = Select(LoginPage.Animated(self))
        RL1.select_by_index(1)
        time.sleep(2)

    # WBtitle ******************************************* Delete wb *******************************************#
    def WORKbenchtitle(self):
        return self.driver.find_element(By.XPATH, "//*[@placeholder='Search...']")

    def WorkbenchNumber(self):
        return self.driver.find_element(By.XPATH, "//*[@id='delete']")

    ###########################################################################################################
    def WBTitle(self):
        global WBT
        WBT = self.genericMethod.ReadData(".//TestData//WBTitle.json", "WorkBenchTitle")
        self.genericMethod.type(LoginPage.WORKbenchtitle(self), WBT)
        time.sleep(4)

    def DeleteWB(self):
        self.genericMethod.click(LoginPage.WorkbenchNumber(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.DeleteIcon(self))
        time.sleep(1)

    # **************************************** Build Load & Manage Load ******************************************#
    def View_Details(self):
        return self.driver.find_element(By.XPATH, "(//*[text()=' View Details '])[1]")

    def EquipmentNumberSave(self):
        return self.driver.find_element(By.XPATH, "(//*[@class='badge bg-secondary'])[1]")

    def View_Load(self):
        return self.driver.find_element(By.XPATH, "(//*[text()='View Loads'])[1]")

    def Equipment_Type(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='equipmentType']")

    def Equipment_Number(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='equipmentNumber']")

    def Equipment_Search(self):
        return self.driver.find_element(By.XPATH, "//*[@type='submit']")

    def Up_Arrow(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Consolidation']/parent::*/following-sibling::div/*/*")

    ###############################################################################################################
    def notification_button(self):
        self.genericMethod.Refresh()
        self.genericMethod.click(LoginPage.notification(self))
        time.sleep(2)
        # time.sleep(6)
        # self.genericMethod.click(LoginPage.TRNO_CLEAR(self))
        # time.sleep(2)
        # self.genericMethod.Clear(LoginPage.TRNO_CLEAR(self))
        # self.genericMethod.type(LoginPage.TRNO_CLEAR(self), "b")
        # self.act.send_keys(Keys.BACKSPACE).perform()

        self.genericMethod.click(LoginPage.Up_Arrow(self))
        time.sleep(1)

    def ViewDetails(self):
        self.genericMethod.click(LoginPage.View_Details(self))
        time.sleep(1)

    def equipmentnumber(self):
        self.genericMethod.click(LoginPage.EquipmentNumberSave(self))
        global equipmentNO
        cl = 'A2'
        equipmentNO = self.genericMethod.getText(LoginPage.EquipmentNumberSave(self))
        self.genericMethod.WRITEEXCELDATA(cl, equipmentNO)
        myLogger.info(equipmentNO)

    def viewLoad(self):
        self.genericMethod.click(LoginPage.View_Load(self))
        time.sleep(2)
        self.genericMethod.Refresh()

    def equipmenttype(self):
        time.sleep(2)
        Type = "Virtual"
        drp = Select(LoginPage.Equipment_Type(self))
        drp.select_by_visible_text(Type)
        time.sleep(1)

    def equipmentfield(self):
        Cell = 'A2'
        equipmentNO = self.genericMethod.READEXCELDATA(Cell)
        self.genericMethod.type(LoginPage.Equipment_Number(self), equipmentNO)
        time.sleep(1)

    def equipmentsearch(self):
        self.genericMethod.click(LoginPage.Equipment_Search(self))
        # self.genericMethod.click(LoginPage.notification(self))
        time.sleep(2)
        # self.genericMethod.click(LoginPage.togglemenu(self))
        # time.sleep(1)

    # ******************************************* Rates & Contracts ********************************************#
    def rateContracts(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Rates & Contracts']")

    def CarriersButton(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Carriers']")

    def CreateCarrier(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Create Carrier']")

    def carrieCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='carrieCode']")

    def ParentCarrier(self):
        return self.driver.find_element(By.XPATH, "//*[@role='combobox']")

    def ParentCarrier_Suggestion(self):
        return self.driver.find_element(By.XPATH, "//*[@id='suggestions']")

    def carriername(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='carrierName']")

    def hazLicenseNumber(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='hazLicenseNumber']")

    def operatingRegionCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='operatingRegionCode']")

    def billingCurrencyCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='billingCurrencyCode']")

    def primaryContactFirstName(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='primaryContactFirstName']")

    def primaryContactLastName(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='primaryContactLastName']")

    def primaryContactEmailId(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='primaryContactEmailId']")

    def primaryContactPhone(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='primaryContactPhone']")

    def primaryContactMobile(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='primaryContactMobile']")

    def CDG_Checkbox(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()=' Carries Dangerous Goods ']/..//*[@formcontrolname='canCarryDangerousGoods']")

    def RegistrationDetails(self):
        # return self.driver.find_element(By.XPATH, "//*[text()='Registration Details']/..//*[@name='downangle']")
        return self.driver.find_element(By.XPATH, "//*[text()='Registration Details']/..//*[@type='button']")

    def RegistrationTypCode(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='carrierRegistrationTypCode']")

    def RegistrationNumber(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='carrierRegistrationNumber']")

    def issuingCountryCode(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='issuingCountryCode']")

    def issuingAgencyName(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='issuingAgencyName']")

    def Effctive_Date(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()='Effective Date']/parent::*/*/*//*[@placeholder='yyyy-mm-dd']")

    def ExpireDAte(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='expiryDate']")

    def YearSelect(self):
        return self.driver.find_element(By.XPATH, "//*[@title='Select year']")

    def DateSelect(self):
        return self.driver.find_element(By.XPATH, "//*[contains(@class, 'btn-light' ) and text() = '" + day4 + "']")

    def SaveCarrier(self):
        return self.driver.find_element(By.XPATH, "//*[text() =' Save ']")

    ##################################################### Carrier #######################################################
    def rate_Contracts(self):
        self.genericMethod.Refresh()
        time.sleep(4)
        self.genericMethod.click(LoginPage.rateContracts(self))
        time.sleep(1)

    def carriers(self):
        self.genericMethod.click(LoginPage.CarriersButton(self))
        time.sleep(1)

    def create_carriers(self):
        self.genericMethod.click(LoginPage.CreateCarrier(self))
        time.sleep(1)

    def carrier_code(self, carriercode):
        a = carriercode
        c = self.genericMethod.NumIncrement()
        global carriercode2
        carriercode2 = a + str(c)
        self.genericMethod.WriteData(".//TestData//CarrierCode.json", "CarrierCode", carriercode2)
        self.genericMethod.type(LoginPage.carrieCode(self), carriercode2)
        time.sleep(1)

    def parrentcarrier(self, parrent):
        self.genericMethod.type(LoginPage.ParentCarrier(self), parrent)
        time.sleep(1)
        self.genericMethod.click(LoginPage.ParentCarrier_Suggestion(self))
        time.sleep(1)

    def carrier_name(self, carriername):
        c = self.genericMethod.NumIncrement()
        global carriername2
        carriername2 = carriername + str(c)
        self.genericMethod.WriteData(".//TestData//Carrier.json", "CarrierName", carriername2)
        self.genericMethod.type(LoginPage.carrierName(self), carriername2)
        # time.sleep(8)

    def hazardouslicescne(self, licescne):
        self.genericMethod.Clear(LoginPage.hazLicenseNumber(self))
        self.genericMethod.type(LoginPage.hazLicenseNumber(self), licescne)
        # time.sleep(1)

    def operatingregion(self, region):
        self.genericMethod.type(LoginPage.operatingRegionCode(self), region)
        # time.sleep(1)

    def billingcurrency(self, currency):
        self.genericMethod.Clear(LoginPage.billingCurrencyCode(self))
        self.genericMethod.type(LoginPage.billingCurrencyCode(self), currency)
        # time.sleep(1)

    def Firstname(self, Fname):
        self.genericMethod.Clear(LoginPage.primaryContactFirstName(self))
        self.genericMethod.type(LoginPage.primaryContactFirstName(self), Fname)
        # time.sleep(1)

    def Lastname(self, Lname):
        self.genericMethod.Clear(LoginPage.primaryContactLastName(self))
        self.genericMethod.type(LoginPage.primaryContactLastName(self), Lname)
        # time.sleep(1)

    def Carrieremail(self, email):
        self.genericMethod.Clear(LoginPage.primaryContactEmailId(self))
        self.genericMethod.type(LoginPage.primaryContactEmailId(self), email)
        # time.sleep(1)

    def Carrierphonenumber(self, phonenumber):
        self.genericMethod.Clear(LoginPage.primaryContactPhone(self))
        self.genericMethod.type(LoginPage.primaryContactPhone(self), phonenumber)
        # time.sleep(1)

    def Carriermobilenumber(self, mobilenumber):
        self.genericMethod.Clear(LoginPage.primaryContactMobile(self))
        self.genericMethod.type(LoginPage.primaryContactMobile(self), mobilenumber)
        # time.sleep(1)

    def CDGcheckbox(self):
        self.genericMethod.click(LoginPage.CDG_Checkbox(self))
        # time.sleep(1)

    def registration_Details(self):
        self.genericMethod.click(LoginPage.RegistrationDetails(self))
        time.sleep(1)

    def Registration_code(self, Registrationcode):
        # self.genericMethod.type(LoginPage.RegistrationDetails(self), Registrationcode)
        drp = Select(LoginPage.RegistrationTypCode(self))
        drp.select_by_visible_text(Registrationcode)
        time.sleep(1)

    def Registration_Number(self, RegistrationNumber):
        self.genericMethod.type(LoginPage.RegistrationNumber(self), RegistrationNumber)
        # time.sleep(1)

    def IssuingCountry(self, countryName):
        self.genericMethod.type(LoginPage.issuingCountryCode(self), countryName)
        # time.sleep(1)

    def IssuingAgency(self, agencycode):
        self.genericMethod.type(LoginPage.issuingAgencyName(self), agencycode)
        # time.sleep(1)

    def effective_Date(self):
        self.genericMethod.click(LoginPage.Effctive_Date(self))
        time.sleep(1)
        global day4
        current_time1 = datetime.datetime.now().day
        day4 = str(current_time1)
        myLogger.info(day4)
        self.genericMethod.click(LoginPage.DateSelect(self))

    def Expired_date(self):
        self.genericMethod.click(LoginPage.ExpireDAte(self))
        time.sleep(1)
        # self.genericMethod.getText(LoginPage.YearSelect(self))
        current_time = datetime.datetime.now().year
        day1 = current_time + 1
        myLogger.info(day1)
        day2 = str(day1)
        myLogger.info(day2)
        drp = Select(LoginPage.YearSelect(self))
        drp.select_by_visible_text(day2)
        time.sleep(1)
        global day4
        current_time1 = datetime.datetime.now().day
        day4 = str(current_time1)
        myLogger.info(day4)
        self.genericMethod.click(LoginPage.DateSelect(self))

    def CarrierSaveButton(self):
        self.genericMethod.click(LoginPage.SaveCarrier(self))
        time.sleep(1)

    # ********************************************** Edit Carrier ********************************************#
    def CarrierSearch(self):
        return self.driver.find_element(By.XPATH, "//*[@type='submit']")

    def Edit_Carrier(self):
        return self.driver.find_element(By.XPATH, "//*[@id='edit']")

    def Edit_CarrierCODE(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='carrierCode']")

    def ClickCarrierCode(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + CarrireCode + "']")

    def EditHZLN(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='hazLicenseNumber']")

    ###########################################################################################################
    def EditCarrierCode(self):
        global CarrireCode
        CarrireCode = self.genericMethod.ReadData(".//TestData//CarrierCode.json", "CarrierCode")
        self.genericMethod.type(LoginPage.Edit_CarrierCODE(self), CarrireCode)
        time.sleep(1)

    def CarriesDangerousGoods(self):
        self.genericMethod.click(LoginPage.CDG_Checkbox(self))
        time.sleep(1)

    def carrierSearchButton(self):
        self.genericMethod.click(LoginPage.CarrierSearch(self))
        time.sleep(1)

    def carrrierCode(self):
        self.genericMethod.click(LoginPage.ClickCarrierCode(self))
        time.sleep(1)

    def EditCarrrier(self):
        self.genericMethod.click(LoginPage.Edit_Carrier(self))
        time.sleep(3)

    def EditHL(self, licescne):
        # self.genericMethod.click(LoginPage.EditHZLN(self))
        self.genericMethod.Clear(LoginPage.hazLicenseNumber(self))
        self.genericMethod.type(LoginPage.hazLicenseNumber(self), licescne)
        time.sleep(1)

    # ********************************************** Contract *************************************************#
    def Contracts(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Contracts']")

    def ChooseCarrier(self):
        return self.driver.find_element(By.XPATH, "//*[@id='status']")

    def CreateContractSymbol(self):
        return self.driver.find_element(By.XPATH, "//*[@ngbtooltip='Create Contract']")

    def ContractNAme(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='contractName']")

    def ContractNum(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='contractName']/../../..//*[@formcontrolname='contractNumber']")

    def CustomerBox(self):
        return self.driver.find_element(By.XPATH, "//*[@role='combobox']")

    def SelectCustomerBox(self):
        return self.driver.find_element(By.XPATH, "//*[@id='suggestions']")

    def StartDate(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='validFromDateUtc']")

    # def startDatechoose(self):
    #     return self.driver.find_element(By.XPATH, "//div[contains(@class,'btn-light') and text()='" + stardate1 + "']")

    def startDatechoose(self):
        return self.driver.find_element(By.XPATH, "//*[@class='ngb-dp-day ngb-dp-today']")

    def EndDate(self):
        return self.driver.find_element(By.XPATH, "//*[@nixerror='validTillDateUtc']")

    def EndtDatechoose(self):
        return self.driver.find_element(By.XPATH, "//*[@class='btn-light' and text()='" + stardate2 + "']")

    def CreateContract1(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Create Contract ']")

    def SelectMonth(self):
        return self.driver.find_element(By.XPATH, "//*[@title='Select month']")

    ############################################################################################################
    def contractButton(self):
        self.genericMethod.click(LoginPage.Contracts(self))
        time.sleep(2)

    def CarrierDropDownButton(self):
        self.genericMethod.click(LoginPage.Contracts(self))
        time.sleep(2)
        CarrierName3 = self.genericMethod.ReadData(".//TestData//Carrier.json", "CarrierName")
        # month = 'bv'
        drp = Select(LoginPage.ChooseCarrier(self))
        drp.select_by_visible_text(CarrierName3)
        time.sleep(1)

    def createcontractButton(self):
        self.genericMethod.click(LoginPage.CreateContractSymbol(self))
        time.sleep(1)

    def contractnametButton(self, contractname):
        self.genericMethod.type(LoginPage.ContractNAme(self), contractname)
        time.sleep(1)

    def contractNumberButton(self, contract):
        self.genericMethod.type(LoginPage.ContractNum(self), contract)
        time.sleep(1)

    def customernameButton(self, customername):
        # global custname
        # custname = customername
        self.genericMethod.type(LoginPage.CustomerBox(self), customername)
        time.sleep(2)
        self.genericMethod.click(LoginPage.SelectCustomerBox(self))
        time.sleep(1)

    def contractstartdateButton(self):
        self.genericMethod.click(LoginPage.StartDate(self))
        # today_month = datetime.datetime.today().month
        # datetime_object = datetime.datetime.strptime(str(today_month), "%m")
        # month_name = datetime_object.strftime("%b")
        # NextDay_Date = datetime.datetime.today().date() + datetime.timedelta(days=1)
        # NextMonth = NextDay_Date.month
        # global Nextdate1
        # NextMonth1 = NextDay_Date.day
        # Nextdate1 = str(NextMonth1)
        # datetime_object1 = datetime.datetime.strptime(str(NextMonth), "%m")
        # month_name1 = datetime_object1.strftime("%b")
        # if today_month == NextMonth:
        #     drp = Select(LoginPage.SelectMonth(self))
        #     drp.select_by_visible_text(month_name)
        #     self.genericMethod.click(LoginPage.startDatechoose(self))
        # elif today_month < NextMonth:
        #     drp = Select(LoginPage.SelectMonth(self))
        #     drp.select_by_visible_text(month_name1)
        #     self.genericMethod.click(LoginPage.startDatechoose(self))
        #     print(month_name1)
        time.sleep(1)
        global stardate1
        current_time1 = datetime.datetime.now().day
        stardate1 = str(current_time1)
        myLogger.info(stardate1)
        self.genericMethod.click(LoginPage.startDatechoose(self))
        time.sleep(1)

    def contractenddateButton(self):
        self.genericMethod.click(LoginPage.EndDate(self))
        time.sleep(1)
        current_time = datetime.datetime.now().year
        day1 = current_time + 1
        myLogger.info(day1)
        day2 = str(day1)
        myLogger.info(day2)
        drp = Select(LoginPage.YearSelect(self))
        drp.select_by_visible_text(day2)
        time.sleep(1)
        global stardate2
        current_time1 = datetime.datetime.now().day
        stardate2 = str(current_time1)
        myLogger.info(stardate2)
        self.genericMethod.click(LoginPage.EndtDatechoose(self))

    def expiredtoggleButton(self):
        self.genericMethod.click(LoginPage.CreateContractSymbol(self))
        time.sleep(1)

    def createcontractButton1(self):
        self.genericMethod.click(LoginPage.CreateContract1(self))
        time.sleep(1)

    def VeryMessage(self, message):
        Expected = message
        myLogger.info(Expected)
        Actual = self.genericMethod.getText(LoginPage.Toast_Message(self))
        myLogger.info(Actual)
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    # **********************************************  RATES  ***************************************************#
    def Rates(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Rates']")

    def RateCard(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Rate Cards']")

    def CreateRateCard(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Create Rate Card ']")

    def RateCard_Name(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='rateCardName']")

    def RateCard_type(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='rateCardTypeCode']")

    def Rate_Carrier(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='carrier']")

    def Rate_customerCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='customerCode']")

    def Customer_option(self):
        return self.driver.find_element(By.XPATH, "//*[@role='option']")

    def Rate_serviceTypeCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='serviceTypeCode']")

    def Rate_incoTermCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='incoTermCode']")

    def Rate_paymentTermCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='paymentTermCode']")

    def Rate_Validity(self):
        return self.driver.find_element(By.XPATH, "//*[@name='calendar']")

    def Rate_namedAccount(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='namedAccount']")

    def Rate_Save(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save ']")

    def Rate_FileImport(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Import ']")

    def Rate_FileInsert(self):
        return self.driver.find_element(By.XPATH, "//input[@type='file']")

    def Rate_FileUpload(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Upload ']")

    def RateValidityStartDate(self):
        return self.driver.find_element(By.XPATH,
                                        "(// div[contains( @class ,'ngb-dp-month')][1] // span[contains(text(), '" + Nextdate1 + "')])[1]")

    ###############################################################################################################
    def RateCLICK(self):
        self.genericMethod.click(LoginPage.Rates(self))
        time.sleep(1)

    def RateCards(self):
        self.genericMethod.click(LoginPage.RateCard(self))
        time.sleep(1)

    def create_RateCard(self):
        self.genericMethod.click(LoginPage.CreateRateCard(self))
        time.sleep(1)

    def RateCardName(self, Name):
        value = self.genericMethod.READEXCELDATA('B2')
        myLogger.info(value)
        v = value + 1
        self.genericMethod.WRITEEXCELDATA('B2', v)
        myLogger.info(v)
        data = Name + str(v)
        myLogger.info(data)
        self.genericMethod.Clear(LoginPage.RateCard_Name(self))
        time.sleep(1)
        self.genericMethod.type(LoginPage.RateCard_Name(self), data)
        cl = 'C2'
        self.genericMethod.WRITEEXCELDATA(cl, data)
        time.sleep(1)

    def RateCardType(self, type):
        self.genericMethod.type(LoginPage.RateCard_type(self), type)
        time.sleep(1)

    def RateCardcarrrier(self):
        CarrierName = self.genericMethod.ReadData(".//TestData//Carrier.json", "CarrierName")
        self.genericMethod.type(LoginPage.Rate_Carrier(self), CarrierName)
        time.sleep(1)
        self.genericMethod.click(LoginPage.Customer_option(self))
        time.sleep(1)

    def Ratecustomername(self, customername):
        self.genericMethod.type(LoginPage.Rate_customerCode(self), customername)
        time.sleep(1)
        self.genericMethod.click(LoginPage.Customer_option(self))
        time.sleep(1)

    def RateServiceType(self, ServiceType):
        self.genericMethod.type(LoginPage.Rate_serviceTypeCode(self), ServiceType)
        time.sleep(1)

    def RateCardIncoTerms(self, IncoTerms):
        self.genericMethod.type(LoginPage.Rate_incoTermCode(self), IncoTerms)
        time.sleep(1)

    def RateCardPaymentTerms(self, PaymentTerms):
        self.genericMethod.type(LoginPage.Rate_paymentTermCode(self), PaymentTerms)
        time.sleep(1)

    def Ratevalidity(self):
        self.genericMethod.click(LoginPage.Rate_Validity(self))
        time.sleep(1)
        today_month = datetime.datetime.today().month
        datetime_object = datetime.datetime.strptime(str(today_month), "%m")
        Year = datetime.datetime.today().year
        Year1 = Year + 1
        NextYear = str(Year1)
        month_name = datetime_object.strftime("%b")
        NextDay_Date = datetime.datetime.today().date() + datetime.timedelta(days=1)
        NextMonth = NextDay_Date.month
        global Nextdate1
        NextMonth1 = NextDay_Date.day
        Nextdate1 = str(NextMonth1)
        datetime_object1 = datetime.datetime.strptime(str(NextMonth), "%m")
        month_name1 = datetime_object1.strftime("%b")
        if today_month == NextMonth:
            drp = Select(LoginPage.SelectMonth(self))
            drp.select_by_visible_text(month_name)
            self.genericMethod.click(LoginPage.RateValidityStartDate(self))
            drp = Select(LoginPage.YearSelect(self))
            drp.select_by_visible_text(NextYear)
            self.genericMethod.click(LoginPage.RateValidityStartDate(self))
        elif today_month < NextMonth:
            drp = Select(LoginPage.SelectMonth(self))
            drp.select_by_visible_text(month_name1)
            self.genericMethod.click(LoginPage.RateValidityStartDate(self))
            drp = Select(LoginPage.YearSelect(self))
            drp.select_by_visible_text(NextYear)
            self.genericMethod.click(LoginPage.RateValidityStartDate(self))

    def RateAccount(self, account):
        self.genericMethod.type(LoginPage.Rate_namedAccount(self), account)
        time.sleep(1)

    def RateSAve(self):
        self.genericMethod.click(LoginPage.Rate_Save(self))
        time.sleep(3)

    def VeryRateSaveToast(self, message):
        f = message
        d = self.genericMethod.READEXCELDATA('C2')
        Expected = f[:10] + d + f[10:]
        myLogger.info(Expected)
        Actual = self.genericMethod.getText(LoginPage.Toast_Message(self))
        myLogger.info(Actual)
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    def RateFileImport(self):
        self.genericMethod.click(LoginPage.Rate_FileImport(self))
        time.sleep(1)
        # Path = "E://Phoenix_20High//Upload//RateCard_Function.xlsm"
        Path = "E://Phoenix_20High//Upload//XBEES.xlsm"
        self.genericMethod.Upload(LoginPage.Rate_FileInsert(self), Path)
        self.genericMethod.click(LoginPage.Rate_FileUpload(self))
        time.sleep(8)

    def RateUploadmessage(self, Uploadmessage):
        Msg = self.genericMethod.click(LoginPage.Toast_Message(self))
        Msg.is_displayed()
        time.sleep(1)
        myLogger.info(Msg)
        Msg1 = Msg.split("-")
        Expected = Uploadmessage
        Actual = Msg1[0]
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    # ******************************************      Rate REvision      ******************************************#
    def RatecardStatus(self):
        # return self.driver.find_element(By.XPATH, "//*[text()='Candidate Revision']")
        return self.driver.find_element(By.XPATH, "//button[@aria-controls='offcanvasRight']")

    def UpdaterateCard_status(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='revisionStatusCode']")

    def Status_Save(self):
        return self.driver.find_element(By.XPATH, "(//*[@name='save'])[2]")

    def Approval_Status(self):
        # return self.driver.find_element(By.XPATH, "//*[text()='Approval History']/../div[3]/*/*/*")
        return self.driver.find_element(By.XPATH,
                                        "//*[text()='Approval History']/../div[3]/*//*[text()='" + Status + "']")

    ###############################################################################################################
    def RateRevisionstatus(self):
        self.genericMethod.click(LoginPage.RatecardStatus(self))
        time.sleep(1)

    def Revisionstatus(self, status):
        self.genericMethod.type(LoginPage.UpdaterateCard_status(self), status)
        time.sleep(1)
        self.genericMethod.WriteData(".//TestData//Status.json", "Status", status)

    def RevisionSave(self):
        self.genericMethod.click(LoginPage.Status_Save(self))
        time.sleep(5)

    def ApprovalHistory(self, message):
        self.genericMethod.click(LoginPage.RatecardStatus(self))
        time.sleep(1)
        global Status
        Status = self.genericMethod.ReadData(".//TestData//Status.json", "Status")

        Expected = message
        Actual = self.genericMethod.getText(LoginPage.Approval_Status(self))
        myLogger.info(Actual)
        if Actual == Expected:
            assert True
        else:
            # time.sleep(2)
            message = "The actual and expected are not matched", "actual->  " + Actual, 'expected-> ' + Expected
            assert Actual == Expected, message
            time.sleep(2)
            assert False

    # ***************************************************** Delete Rate Card *********************************************#

    def RateCard_Delete(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Delete Rate Revision ']")

    # def ButtonLogOUT(self):
    #     return self.driver.find_element(By.XPATH, "//*[text()='Logout ']")

    ############################################################################################################
    def New_RateCard_Name(self, Name):
        value = self.genericMethod.READEXCELDATA('B2')
        myLogger.info(value)
        v = value + 1
        self.genericMethod.WRITEEXCELDATA('B2', v)
        myLogger.info(v)
        data = Name + str(v)
        myLogger.info(data)
        self.genericMethod.Clear(LoginPage.RateCard_Name(self))
        time.sleep(1)
        self.genericMethod.type(LoginPage.RateCard_Name(self), data)
        cl = 'E2'
        self.genericMethod.WRITEEXCELDATA(cl, data)
        time.sleep(1)

    def DeleteRateCard(self):
        self.genericMethod.click(LoginPage.RateCard_Delete(self))
        time.sleep(3)

    # *************************************** Carrier_AssignTO_Ratecard ***********************************#

    def Filter_Button(self):
        return self.driver.find_element(By.XPATH, "//*[@aria-controls='collapseFilterOpen']")

    def ApprovedOnly(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Approved Only']")

    def Search_Button(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()='Approved Only']/../parent::*/*/following-sibling::*//*[@type='submit']")

    def assignRates(self):
        return self.driver.find_element(By.XPATH, "//*[@name='arrowleft']")

    def RateCard_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@name='marginCurrencyCode']")

    def Assign_Button(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Assign ']")

    def RateCard_click(self):
        return self.driver.find_element(By.XPATH, "//[text()=' ESSPL_KART137 ']")

    def CloseButton_Click(self):
        return self.driver.find_element(By.XPATH, "//*[@class='btn-close']")

    ############################################################################################################
    def Contract_Filter_Button(self):
        self.genericMethod.click(LoginPage.Filter_Button(self))
        time.sleep(1)

    def Approved_Only(self):
        self.genericMethod.click(LoginPage.ApprovedOnly(self))
        time.sleep(1)

    def unapproved_contract(self):
        self.genericMethod.click(LoginPage.Search_Button(self))
        time.sleep(1)

    def assign_rates(self):
        self.genericMethod.click(LoginPage.assignRates(self))
        time.sleep(1)

    def RateCoardChoose(self):
        # self.genericMethod.click(LoginPage.RateCard_Choose(self))
        # time.sleep(1)
        value = self.genericMethod.READEXCELDATA('C2')
        myLogger.info(value)
        drp = Select(LoginPage.RateCard_Choose(self))
        drp.select_by_visible_text(value)
        time.sleep(1)

    def Assign(self):
        self.genericMethod.click(LoginPage.Assign_Button(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.CloseButton_Click(self))
        time.sleep(1)

    # ***************************************************** Rate Margin *********************************************#

    def RateMargin_Button(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Rate Margin']")

    def Create_Margin(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Create Margin ']")

    def Drp_ServiceType(self):
        return self.driver.find_element(By.XPATH, "//*[@name='serviceType']")

    def Drp_RateUnit(self):
        return self.driver.find_element(By.XPATH, "//*[@name='rateUomCode']")

    def Drp_equipmentSize(self):
        return self.driver.find_element(By.XPATH, "//*[@name='equipmentSizetypes']")

    def Drp_Customer(self):
        return self.driver.find_element(By.XPATH, "//*[@placeholder='Select Customer']")

    def Click_Customer(self):
        return self.driver.find_element(By.XPATH, "//*[@class='dropdown-item active']")

    def Drp_hsCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='hsCode']")

    def Drp_DangerousCargo(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='isDangerousCargo']")

    def Drp_hazardousCode(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='hazardousCode']")

    def Drp_LoadCountry(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Load']/../*/*/*/*/*//*[@placeholder='Select Country']")

    def Drp_LC(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + LC + "']")

    def loadCityCode(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='loadCityCode']/./*/*/*[@placeholder='Select City']")

    def lC_Code(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + LCity + "']")

    def loadSitePostalCode(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='loadSitePostalCode']/./*/*/*[@placeholder='Select Post Code']")

    def lC_PinCode(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + LoadPinCode + "']")

    def dischargeCountryCode(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='dischargeCountryCode']/./*/*/*[@placeholder='Select Country']")

    def DC_Code(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + DCCode + "']")

    def dischargeCityCode(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='dischargeCityCode']/./*/*/*[@placeholder='Select City']")

    def DCity_Code(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + DCity + "']")

    def dischargeSitePostalCode(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='dischargeSitePostalCode']/./*/*/*[@placeholder='Select Site']")

    def Discharge_PinCode(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + DischargePinCode + "']")

    def marginValue(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='marginValue']")

    def marginCurrencyCode(self):
        return self.driver.find_element(By.XPATH, "//*[@name='marginCurrencyCode']")

    def isPercentage(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='isPercentage']")

    def validFromDateUtc(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='validFromDateUtc']")

    def validNextDate(self):
        return self.driver.find_element(By.XPATH, "//*[text()='" + NextDate + "']")

    def validTillDateUtc(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='validTillDateUtc']")

    def SaveMargin(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Save ']")

    ############################################################################################################
    def RateMargin(self):
        self.genericMethod.click(LoginPage.RateMargin_Button(self))
        time.sleep(2)

    def CreateMargin(self):
        self.genericMethod.click(LoginPage.Create_Margin(self))
        time.sleep(2)

    def MarginServiceType(self, Servicetype):
        self.genericMethod.type(LoginPage.Drp_ServiceType(self), Servicetype)
        time.sleep(1)

    def RateUnit(self, rateunit):
        self.genericMethod.type(LoginPage.Drp_RateUnit(self), rateunit)
        time.sleep(1)

    def Margin_equipmenttype(self, equipmenttype):
        self.genericMethod.type(LoginPage.Drp_equipmentSize(self), equipmenttype)
        time.sleep(1)

    def Margin_customer(self, customerCode):
        self.genericMethod.type(LoginPage.Drp_Customer(self), customerCode)
        time.sleep(1)
        self.genericMethod.click(LoginPage.Click_Customer(self))
        time.sleep(1)

    def Margin_HSCode(self, HScode):
        self.genericMethod.type(LoginPage.Drp_hsCode(self), HScode)
        time.sleep(1)

    def Margin_hazardouscode(self, hazardouscode):
        self.genericMethod.type(LoginPage.Drp_hazardousCode(self), hazardouscode)
        time.sleep(1)

    def Margin_dangerouscargo(self):
        self.genericMethod.click(LoginPage.Drp_DangerousCargo(self))
        time.sleep(1)

    def Load_country(self, loadcountry):
        self.genericMethod.type(LoginPage.Drp_LoadCountry(self), loadcountry)
        time.sleep(1)
        global LC
        LC = loadcountry
        self.genericMethod.click(LoginPage.Drp_LC(self))
        time.sleep(1)

    def Load_city(self, loadcity):
        self.genericMethod.type(LoginPage.loadCityCode(self), loadcity)
        time.sleep(1)
        global LCity
        LCity = loadcity
        self.genericMethod.click(LoginPage.lC_Code(self))
        time.sleep(1)

    def Load_postcode(self, Pin):
        self.genericMethod.type(LoginPage.loadSitePostalCode(self), Pin)
        time.sleep(1)
        global LoadPinCode
        LoadPinCode = Pin
        self.genericMethod.click(LoginPage.lC_PinCode(self))
        time.sleep(1)

    def Discharge_country(self, dischargecountry):
        self.genericMethod.type(LoginPage.dischargeCountryCode(self), dischargecountry)
        time.sleep(1)
        global DCCode
        DCCode = dischargecountry
        self.genericMethod.click(LoginPage.DC_Code(self))
        time.sleep(1)

    def Discharge_city(self, dischargecity):
        self.genericMethod.click(LoginPage.dischargeCityCode(self))
        time.sleep(1)
        self.genericMethod.type(LoginPage.dischargeCityCode(self), dischargecity)
        time.sleep(1)
        global DCity
        DCity = dischargecity
        self.genericMethod.click(LoginPage.DCity_Code(self))
        time.sleep(1)

    def Discharge_postcode(self, Pin1):
        self.genericMethod.type(LoginPage.dischargeSitePostalCode(self), Pin1)
        time.sleep(1)
        global DischargePinCode
        DischargePinCode = Pin1
        self.genericMethod.click(LoginPage.Discharge_PinCode(self))
        time.sleep(1)

    def MarginNumber(self, validdata):
        self.genericMethod.type(LoginPage.marginValue(self), validdata)
        time.sleep(1)

    def Margin_currency(self, currency):
        self.genericMethod.type(LoginPage.marginCurrencyCode(self), currency)
        time.sleep(2)

    def Margin_isPercentage(self):
        self.genericMethod.click(LoginPage.isPercentage(self))
        time.sleep(1)

    def validdate_From(self):
        self.genericMethod.click(LoginPage.validFromDateUtc(self))
        time.sleep(1)
        Date = datetime.datetime.today().date() + datetime.timedelta(days=1)
        NextDay = Date.day
        global NextDate
        NextDate = str(NextDay)
        self.genericMethod.click(LoginPage.validNextDate(self))
        time.sleep(1)

    def validdate_To(self):
        self.genericMethod.click(LoginPage.validTillDateUtc(self))
        time.sleep(1)
        Date = datetime.datetime.today().date() + datetime.timedelta(days=1)
        NextDay = Date.day
        global NextDate
        NextDate = str(NextDay)
        self.genericMethod.click(LoginPage.validNextDate(self))
        time.sleep(1)

    def Margin_Save(self):
        self.genericMethod.click(LoginPage.SaveMargin(self))
        time.sleep(2)
        # self.genericMethod.click(LoginPage.SaveMargin(self))
        # time.sleep(1)

    # ******************************************** Rate Margin **********************************************#

    def FilterButton(self):
        self.genericMethod.click(LoginPage.Filter(self))
        time.sleep(1)

    # ***************************************************** Compare Rate *********************************************#
    def Auto_CompareRates(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Compare Rates']")

    def CompareRates(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Compare Rates']")

    def CompareRateCustomer(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='customer']/*/*//input")

    def CLickSugesstion(self):
        return self.driver.find_element(By.XPATH, "//*[@id='suggestions']//a")

    def HAZCode(self):
        return self.driver.find_element(By.XPATH, "//*[@aria-label='Select HAZ. Code']")

    def RouteLeg(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Route Leg']")

    def ORG_LoadCountry(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Select Country'])[3]")

    def ORG_LoadCity(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Select City'])[3]")

    def Des_dischargeCountry(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Select Country'])[4]")

    def Des_dischargeCity(self):
        return self.driver.find_element(By.XPATH, "(//*[@placeholder='Select City'])[4]")

    def Option_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@class='item']")

    def Equipment_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='equipmentName']")

    def EquipmentNumber_Select(self):
        return self.driver.find_element(By.XPATH, "//*[@value='20FTDRY']")

    def EquipmentNumber_Enter(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='equipmentNumber']")

    def Weight_Enter(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@formcontrolname='weightUOM']/parent::*//*[@formcontrolname='weight']")

    def Weight_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='weightUOM']")

    def Weight_Select(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Kilogram (Kg) ']")

    def Volume_Enter(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='volume']")

    def Volume_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='volumeUOM']")

    def Volume_Select(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' cubic centimetre ']")

    def MOT_Choose(self):
        return self.driver.find_element(By.XPATH, "// *[ @ formcontrolname = 'MOT']")

    def MOT_Select(self):
        return self.driver.find_element(By.XPATH, "// *[text() = ' Air ']")

    def AddLEG(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Add Route Leg ']")

    def CheckBox_LEG(self):
        return self.driver.find_element(By.XPATH, "// *[ @ id = 'checkboxNoLabel']")

    def ApplyLeg(self):
        return self.driver.find_element(By.XPATH, "// *[text() = 'Apply']")

    def CloseLeg(self):
        return self.driver.find_element(By.XPATH, "(//*[@data-bs-dismiss='offcanvas'])[2]")

    def CompareButton(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Compare ']")

    ############################################################################################################

    def auto_generate_Compare_Rates(self):
        self.genericMethod.click(LoginPage.Auto_CompareRates(self))
        time.sleep(1)

    def Compare_Rates(self):
        self.genericMethod.click(LoginPage.CompareRates(self))
        time.sleep(1)

    def compareRate_Customer(self, customer):
        global Cust
        Cust = customer
        self.genericMethod.type(LoginPage.CompareRateCustomer(self), customer)
        time.sleep(1)
        self.genericMethod.click(LoginPage.CLickSugesstion(self))
        time.sleep(1)

    def compareRate_HazCode(self, HazCode):
        self.genericMethod.type(LoginPage.HAZCode(self), HazCode)
        time.sleep(1)
        self.genericMethod.click(LoginPage.CLickSugesstion(self))
        time.sleep(1)

    def Add_route_leg(self):
        self.genericMethod.click(LoginPage.RouteLeg(self))
        time.sleep(1)

    def org_country(self):
        value = self.genericMethod.READEXCELDATA_XLSM('B4')
        myLogger.info(value)
        time.sleep(1)
        # self.genericMethod.click(LoginPage.ORG_LoadCountry(self))
        self.genericMethod.type(LoginPage.ORG_LoadCountry(self), value)
        self.genericMethod.click(LoginPage.Option_Choose(self))

    def org_city(self):
        value = self.genericMethod.READEXCELDATA_XLSM('C4')
        myLogger.info(value)
        time.sleep(1)
        # self.genericMethod.click(LoginPage.ORG_LoadCountry(self))
        self.genericMethod.type(LoginPage.ORG_LoadCity(self), value)
        self.genericMethod.click(LoginPage.Option_Choose(self))

    def des_country(self):
        value = self.genericMethod.READEXCELDATA_XLSM('E4')
        myLogger.info(value)
        time.sleep(1)
        self.genericMethod.type(LoginPage.Des_dischargeCountry(self), value)
        self.genericMethod.click(LoginPage.Option_Choose(self))

    def des_city(self):
        value = self.genericMethod.READEXCELDATA_XLSM('F4')
        myLogger.info(value)
        time.sleep(1)
        self.genericMethod.type(LoginPage.Des_dischargeCity(self), value)
        self.genericMethod.click(LoginPage.Option_Choose(self))
        time.sleep(1)

    def equipment_numberSelect(self):
        v = self.genericMethod.getText(LoginPage.EquipmentNumber_Select(self))
        myLogger.info(v)
        drp = Select(LoginPage.Equipment_Choose(self))
        drp.select_by_visible_text(v)
        time.sleep(2)

    def equipment_quantity(self):
        v = '2'
        self.genericMethod.type(LoginPage.EquipmentNumber_Enter(self), v)
        time.sleep(1)

    def Enter_Weight(self):
        v = '2'
        self.genericMethod.type(LoginPage.Weight_Enter(self), v)
        time.sleep(1)

    def choose_weight(self):
        v = self.genericMethod.getText(LoginPage.Weight_Select(self))
        myLogger.info(v)
        drp = Select(LoginPage.Weight_Choose(self))
        drp.select_by_visible_text(v)
        time.sleep(2)

    def Enter_Volume(self):
        v = '2'
        self.genericMethod.type(LoginPage.Volume_Enter(self), v)
        time.sleep(1)

    def choose_Volume(self):
        v = self.genericMethod.getText(LoginPage.Volume_Select(self))
        myLogger.info(v)
        drp = Select(LoginPage.Volume_Choose(self))
        drp.select_by_visible_text(v)
        time.sleep(2)

    def MOT_type(self):
        v = self.genericMethod.getText(LoginPage.MOT_Select(self))
        myLogger.info(v)
        drp = Select(LoginPage.MOT_Choose(self))
        drp.select_by_visible_text(v)
        time.sleep(2)

    def Add_RouteLeg(self):
        self.genericMethod.click(LoginPage.AddLEG(self))
        time.sleep(1)

    def RouteLeg_CheckBox(self):
        self.genericMethod.click(LoginPage.CheckBox_LEG(self))
        time.sleep(1)

    def RouteLeg_Apply(self):
        self.genericMethod.click(LoginPage.ApplyLeg(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.CloseLeg(self))
        time.sleep(1)

    def compare_button(self):
        self.genericMethod.click(LoginPage.CompareButton(self))
        time.sleep(1)

    # ********************************************* Compare Rate Auto ****************************************#
    def manageload(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Manage Loads']")

    def EnterEquipment(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Manage Loads']")

    def EquipmentDetails(self):
        return self.driver.find_element(By.XPATH, "//*[@class='virtual-equip']")

    def AssignCarrier_CheckBox(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Assign Carrier ']/../*[@type='checkbox']")

    def AssignCarrierClick(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Assign Carrier']")

    def AssignDirect(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Assign Direct']")

    def Carrier_Choose(self):
        return self.driver.find_element(By.XPATH, "//*[@formcontrolname='carriers']")

    # def Carrier_Choose1(self):
    #     return self.driver.find_element(By.XPATH, "//*[text()=' Everglory Carrier ']")
    def Carrier_Choose1(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Everglory Carrier ']")

    def CarrierSave(self):
        return self.driver.find_element(By.XPATH, "//*[@id='save']")

    def CloseAssignWindow(self):
        return self.driver.find_element(By.XPATH,
                                        "//div[text()='Assign Carrier']/../*/*[@class='bi bi-x-lg text-white']")

    def AssignCompareRates(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Compare Rates']")

    def Compare(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Compare ']")

    ############################################################################################################
    def manage_load(self):
        self.genericMethod.click(LoginPage.manageload(self))
        time.sleep(2)

    def Enter_Equipment(self):
        self.genericMethod.click(LoginPage.manageload(self))
        time.sleep(1)

    def equipment_details(self):
        self.genericMethod.click(LoginPage.EquipmentDetails(self))
        time.sleep(1)

    def Assign_carrier(self):
        self.genericMethod.click(LoginPage.AssignCarrier_CheckBox(self))
        time.sleep(1)

    def Click_AssignCarrier(self):
        self.genericMethod.click(LoginPage.AssignCarrierClick(self))
        time.sleep(1)

    def Assign_Direct(self):
        self.genericMethod.click(LoginPage.AssignDirect(self))
        time.sleep(3)

    def CarrierChoose(self):
        self.genericMethod.click(LoginPage.Carrier_Choose(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.Carrier_Choose1(self))
        time.sleep(1)

    def Assigned_Carrier(self):
        self.genericMethod.click(LoginPage.CarrierSave(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.CloseAssignWindow(self))
        time.sleep(1)
        self.genericMethod.click(LoginPage.AssignCarrierClick(self))
        time.sleep(1)
        # self.genericMethod.click(LoginPage.AssignCompareRates(self))
        # time.sleep(1)
        # self.genericMethod.click(LoginPage.Compare(self))
        # time.sleep(8)

    def Save_BookingNumber(self):
        BookingId = self.genericMethod.getText(LoginPage.Toast_Message(self))
        myLogger.info(BookingId)
        cl = "D2"
        self.genericMethod.WRITEEXCELDATA(cl, BookingId)
        time.sleep(1)

    # ******************************************* Carrier Bookings*******************************************#
    def Execution(self):
        return self.driver.find_element(By.XPATH, "// *[text() = 'Execution']")

    def Bookings(self):
        return self.driver.find_element(By.XPATH, "// *[text() = 'Bookings']")

    def CarrierBookings(self):
        return self.driver.find_element(By.XPATH, "// *[text() = 'Carrier Bookings']")

    def CarrierBookings_Search(self):
        return self.driver.find_element(By.XPATH, "//*[@placeholder='Search...']")

    ##########################################################################################################
    def Execution_Menu(self):
        self.genericMethod.click(LoginPage.Execution(self))
        time.sleep(1)

    def Bookings_Button(self):
        self.genericMethod.click(LoginPage.Bookings(self))
        time.sleep(1)

    def Carrier_Bookings(self):
        self.genericMethod.click(LoginPage.CarrierBookings(self))
        time.sleep(1)

    def Check_Carrier_Bookings(self):
        self.genericMethod.click(LoginPage.CarrierBookings_Search(self))
        time.sleep(1)
        Cell = 'D2'
        d = self.genericMethod.READEXCELDATA(Cell)
        v = d.split(" ")
        c = v[5]
        myLogger.info(c)
        self.genericMethod.type(LoginPage.CarrierBookings_Search(self), c)
        cl = "D5"
        self.genericMethod.WRITEEXCELDATA(cl, c)
        time.sleep(1)

    # ***************************************************** LogOut *********************************************#

    def DipatchIcon(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Dispatch']")

    def DipatchPlanning(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Dispatch Planning']")

    def DispatchCountry(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()=' Select Load (Dispatch) Sites ']/..//parent::*//*[@placeholder='Select Country']")

    def DispatchCity(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()=' Select Load (Dispatch) Sites ']/..//parent::*//*[@placeholder='Select City']")

    def DispatchSite(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[text()=' Select Load (Dispatch) Sites ']/..//parent::*//*[@placeholder='Select Site']")

    def DispatchProceed(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Proceed ']")

    ############################################################################################################
    def Dispatch(self):
        self.genericMethod.click(LoginPage.DipatchIcon(self))
        time.sleep(1)

    def Dispatch_Planning(self):
        self.genericMethod.click(LoginPage.DipatchPlanning(self))
        time.sleep(1)

    def Dispatch_Country(self):
        self.genericMethod.click(LoginPage.DispatchCountry(self))
        time.sleep(1)

    def Dispatch_City(self):
        self.genericMethod.click(LoginPage.DispatchCity(self))
        time.sleep(1)

    def Dispatch_Site(self):
        self.genericMethod.click(LoginPage.DispatchSite(self))
        time.sleep(1)

    def Dispatch_proceed(self):
        self.genericMethod.click(LoginPage.DispatchProceed(self))
        time.sleep(1)

    # **************************************************** Trips ********************************************#

    def Tripsclick(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Trips']")

    def trips(self):
        self.genericMethod.click(LoginPage.Tripsclick(self))

    # **************************************************Freight audit*********************************************#

    def Settlement(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Settlement']")

    def freightaudit(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Freight Audit']")

    def importinvoice(self):
        return self.driver.find_element(By.XPATH, "//*[text()=' Import Invoice ']")

    # def importinvoice(self):
    #     return self.driver.find_element(By.XPATH, "//button[text()=' Import Invoice ']")

    ############################################################################################
    def clickSettlement(self):
        self.genericMethod.click(LoginPage.Settlement(self))

    def Clickfreightaudit(self):
        self.genericMethod.click(LoginPage.freightaudit(self))
        time.sleep(2)

    def clickimportinvoice(self):
        self.genericmethod.click(LoginPage.importinvoice(self))

    def importauditfile(self):
        self.genericMethod.click(LoginPage.freightaudit_fileimport(self))
        time.sleep(1)
        # Path = "E://Phoenix_20High//Upload//RateCard_Function.xlsm"
        Path = "E://Phoenix_20High//Upload//Invoice_Upload_Template.xlsx"
        self.genericMethod.Upload(LoginPage.freightaudit_fileinsert(self), Path)
        self.genericMethod.click(LoginPage.freightaudit_fileimportUpload(self))
        time.sleep(8)

        # ***********************Dashboard****************************#

        def navigatedashboard1(self):
            return self.driver.find_element(By.XPATH, "(//span[text()='Dashboard')]")

        def mouse_hover_on_delivery_quality_tab(self):
            return self.driver.find_element(By.XPATH,
                                            "//*[@id='right-main-panel']/div/lib-dashboard/div/div[2]/div/div/div/div[1]/lib-delivery-timelines/div/div[1]/div[1]/div")

        def mouse_hover_on_delivery_timeliness(self):
            return self.driver.find_element(By.XPATH, "(//div[text()='Delivery Timeliness'])")

        def click_on_advance_filter(self):
            return self.driver.find_element(By.XPATH, "(//phoenix-icons[contains(@name,'filter')])")

        def click_on_checkbox_and_uncheck_for_etd(self):
            return self.driver.find_element(By.XPATH, "(//input[@type='checkbox'])")

        def click_on_checkbox_and_uncheck_for_eta(self):
            return self.driver.find_element(By.XPATH, "(//input[@type='checkbox'])")

        def click_on_apply_button(self):
            return self.driver.find_element(By.XPATH, "(//button[@type='submit']//em)")

        #################################Dashboard############################################

    def mouse_hover_on_delivery_quality_tab(self):
        self.genericMethod.MouseHover(LoginPage.mouse_hover_on_delivery_quality_tab(self))

    # ***************************************************** LogOut *********************************************#

    def EssplLOGO(self):
        return self.driver.find_element(By.XPATH, "//*[@id='dropdownMenuAvatar']")

    def ButtonLogOUT(self):
        return self.driver.find_element(By.XPATH, "//*[text()='Logout ']")

    ############################################################################################################
    def ClikEssplLogo(self):
        self.genericMethod.click(LoginPage.EssplLOGO(self))
        time.sleep(1)

    def LogOutBTN(self):
        self.genericMethod.click(LoginPage.ButtonLogOUT(self))
        time.sleep(1)
