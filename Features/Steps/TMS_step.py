# import argparse
import time

from behave import *

from Pages.TMSPage import LoginPage
from Utilities.GenericMethod import genericmethod
from Utilities.customLogger import LogGen

# baseURL = ReadConfig.getURL()
myLogger = LogGen.loggeen()


# *********************Login*********************************************#


@given(u'launch the "{TMS_Url}"')
def LandingPage(context, TMS_Url):
    global lPage
    lPage = LoginPage(context.driver)
    context.gMethod = genericmethod(context.driver)
    myLogger.info("****** Url Launched ******")
    time.sleep(2)
    lPage.LaunchBrowser(TMS_Url)


@then(u'Provide the username "{user}" in the username field')
def step_impl(context, user):
    myLogger.info('******Entering Username **********')
    lPage.enterUserName(user)


@then(U'Click on Proceed')
def Proceed(context):
    lPage.ClickProceed()
    time.sleep(3)


@then(u'Provide the Password "{pwd}" in the Password field')
def step_impl(context, pwd):
    lPage.enterPassword(pwd)


@then(u'Click on the LoginIn button')
def step_impl(context):
    lPage.clickOnLogin()


@then(U'Mouse Hover and Click on Dashboard Menu')
def hover_dashboards(context):
    lPage.hover_dashboards()


@then(U'Mouse Hover and Click on Delivery Timeliness')
def hover_deliverytimeliness(context):
    lPage.hover_deliverytimeliness()


@then(U'Mouse Hover and Click on Dashboard')
def MovetoFilter(context):
    lPage.MovetoFilter()


@then(U'Uncheck the ETD field in filter')
def CheckETD(context):
    lPage.CheckETD()


@then(U'Uncheck the ETA field in filter')
def CheckETA(context):
    lPage.CheckETA()


@then(U'Click on Apply button')
def apply_delivery_filter(context):
    lPage.apply_delivery_filter()


@then(U'Click on Close button')
def close_delivery_filter(context):
    lPage.close_delivery_filter()


@then(U'Mouse Hover and Click on At Risk In-transit Shipments')
def hover_AtRiskIntransitShipments(context):
    lPage.hover_AtRiskIntransitShipments()


@then(U'Uncheck the At Risk In-transit Shipments ETD field in filter')
def IntransitCheckETD(context):
    lPage.IntransitCheckETD()


@then(U'Uncheck the At Risk In-transit Shipments ETA field in filter')
def IntransitCheckETA(context):
    lPage.IntransitCheckETA()


@then(U'Click on At Risk In-transit Shipments Apply button')
def apply_transitShipments_filter(context):
    lPage.apply_transitShipments_filter()


@then(U'Click on At Risk In-transit Shipments Close button')
def close_transitShipments_filter(context):
    lPage.close_transitShipments_filter()


@then(U'Click on the dropdown1 in the dashboard')
def dropdown1_dashboard(context):
    lPage.dropdown1_dashboard()


@then(U'Click on Carrier Bookings Pending Confirmation filter')
def pending_filter(context):
    lPage.pending_filter()


@then(U'Uncheck booking Dt in Bookings Pending Confirmation filter')
def Uncheck_BookingDt_filter(context):
    lPage.Uncheck_BookingDt_filter()


# @then(U'Click on apply in Carrier Bookings Pending Confirmation filter')
# def Apply_carrierbooking_filter(context):
#     lPage.Apply_carrierbooking_filter()

@then(U'Close the Carrier Bookings Pending Confirmation')
def Close_CarrierBookingsPending(context):
    lPage.Close_CarrierBookingsPending()


@then(U'Click on the dropdown2 in the dashboard')
def dropdown2_dashboard(context):
    lPage.dropdown2_dashboard()


#

# **************  Rule_Set_Creation  ********************#

@then(u"Click on Planning Button")
def Planning(context):
    lPage.clickPlanning()


@then(u"Click on Rule")
def Rule(context):
    lPage.clickRule()


@then(u'Click on create ruleset')
def ruleset(context):
    lPage.clickRuleset()


@then(u'Enter the Ruleset "{Name}" Rule Set Name textbox')
def Name(context, Name):
    lPage.clickName(Name)


@then(u'Enter the "{Description}" for the ruleset')
def Description(context, Description):
    lPage.clickDescription(Description)


@then(u'Select the "{Policy_type}" from the dropdown')
def Policy_type(context, Policy_type):
    lPage.clickPolicyType(Policy_type)


@then(u'Click on the Active toggle button to activate the column')
def Active(context):
    lPage.clickActive()


@then(u'Check on Add to an Open Order')
def Open_Order(context):
    lPage.clickOrder()


@then(u'Click on Next Button')
def Next(context):
    lPage.clickNext()


@then(u'Drag and drop the "{rule}" consolidation field')
def consolidation(context, rule):
    lPage.clickconsolidation(rule)


@then(u'Click on Rule_Next Button')
def Rule_Next(context):
    lPage.Rule_Next()


@then(u'Drag and drop the "{criteria}" field')
def criteria(context, criteria):
    lPage.DragDropCriteria(criteria)


@then(u'Enter Values in selected field')
def CODE(context):
    lPage.CODEINPUT()


@then(u'Click on Finish')
def Finishbutton(context):
    lPage.Finishbutton()


@then(u'Click on Confirm')
def Confirm(context):
    lPage.Confirmbutton()

    # ************************************** Ruleset_sequence *************************************************#


#
# @then(u'Filter the "{policytype}"')
# def policytype(context, policytype):
#     lPage.Filterpolicytype(policytype)
#
#
# @then(u'Sequence the rule set present')
# def step_impl(context):
#     lpage.u'STEP: Then Sequence the rule set present')
#
#
# @then(u'Click on save sequence')
# def save_sequence(context):
#     lPage.Click_Savesequence()
#
#
# @then(u'ruleset "{sequence}" successfully changed')
# def sequence_Message(context, sequence):
#     lPage.sequence_Message(sequence)
#
#
# @then(u'Click to sequence the default ruleset')
# def Sequence(context):
#     lPage.Click_DefaultSequence()

# *********************************** Edit Ruleset *****************************************************#


@then(u'Click on ruleset and edit')
def view_of_any_ruleset(context):
    lPage.click_Ruleset_Edit()


@then(u'Modify the "{rulesetname}" and save')
def Custom(context, rulesetname):
    lPage.Modify_Ruleset(rulesetname)

    # *********************************** View Ruleset *****************************************************#


@then(u'Click on view of any ruleset')
def view_of_any_ruleset(context):
    lPage.Click_viewRuleSet()


#
# *********************************** Delete Ruleset *****************************************************#
# @then(u'Click on view of any ruleset')
# def view_of_any_ruleset(context):
#     lPage.Click_viewRuleSet()
#
# @then(u'Click on delete')
# def delete(context):
#     lPage.Click_delete()

# ************************************** Orders *****************************************#


@then(u'Scroll through menu to view orders menu')
def Sequence(context):
    lPage.MouseHover_Order()


@then(u'Click on orders button')
def Orders(context):
    lPage.clickOrders()


# ***************************** autogenrate_FO_with_the_available_rulesets ***************************#


@then(u'Scroll through menu to view planning option')
def planning(context):
    lPage.ScrollOnPlanning()


@then(u'Sequence the rule set')
def rule_set(context):
    lPage.Sequence_rule_set()


@then(u'Goto order menu and click on filter')
def filter(context):
    lPage.ClickFilter()


@then(u'Choose "{unconsolidate}" from consolidation status')
def consolidation(context, unconsolidate):
    lPage.ClickconsolidationStatus(unconsolidate)


@then(u'select "{DateType}" From date')
def Custom(context, DateType):
    lPage.ChooseDateTyper(DateType)


@then(u'click on calender')
def Calender(context):
    lPage.clickcalender()


@then(u'select the "{month}" from calender')
def Month(context, month):
    lPage.slectMonth(month)


@then(u'select "{from_date}" and "{to_date}" from the calender')
def DateSelection(context, from_date, to_date):
    lPage.slectDate(from_date, to_date)


@then(u'choose "{from_date1}" and "{to_date1}" from the calender')
def DateSelection(context, from_date1, to_date1):
    lPage.ChooseDate(from_date1, to_date1)


@then(u'Click on search')
def search(context):
    lPage.searchButton()


@then(u'Then select order/orderline from the list')
def orderOrderline(context):
    lPage.order_orderline()


@then(u'save the Order Reference Number')
def OrderReferenceNumber(context):
    lPage.Order_Reference_Number()


@then(u'Click on consolidation order')
def consolidation(context):
    lPage.consolidationButton()


@then(u'Save the TR no')
def consolidation(context):
    lPage.Tr_No()


@then(u'Click on that notification')
def notification(context):
    lPage.notificationButton()


@then(u'Click on notification')
def notification(context):
    lPage.NotificationClick()


@then(u'Click on the notification')
def notification(context):
    lPage.Notification_Click()

    # *****************************      create_FO_from_orders          ****************************#


@then(u'Click on the create freight order')
def freightorder(context):
    lPage.CreateFreightOrder()

    @then(u'click on create from order')
    def CreateOrder(context):
        lPage.Create_Order()

    @then(u'Click on notification button')
    def CreateOrder(context):
        lPage.notification_button()

    @then(u'goto the load icon in the notificaion and click on view details')
    def View_Details(context):
        lPage.ViewDetails()

    @then(u'save the equipment number')
    def equipmentnumber(context):
        lPage.equipmentnumber()

    @then(u'Click on view Load in notification')
    def viewLoad(context):
        lPage.viewLoad()

    @then(u'choose the equipment type')
    def equipmenttype(context):
        lPage.equipmenttype()

    @then(u'enter the equipment number in equipment field')
    def equipmentfield(context):
        lPage.equipmentfield()

    @then(u'Click on Equipment search button')
    def equipmentsearch(context):
        lPage.equipmentsearch()

    @then(u'Click on procced')
    def proceed(context):
        lPage.proceed()

    @then(u'mouse hover all the field present in the FO header page')
    def Foheader(context):
        lPage.Mousehoverfoheader()

    @then(
        u'Fill all the details in party details page "{ShipperAttention}","{ShipperBECode}","{ShipperName}","{ShipperPhone}","{ShipperMobile}","{ShipperEmail}","{ShipperFax}","{ConsigneeAttention}","{ConsigneeBECode}","{ConsigneeName}","{ConsigneePhone}","{ConsigneeMobile}","{ConsigneeEmail}","{ConsigneeFax}"')
    def partydetailspage(context, ShipperAttention, ShipperBECode, ShipperName, ShipperPhone, ShipperMobile,
                         ShipperEmail,
                         ShipperFax, ConsigneeAttention, ConsigneeBECode, ConsigneeName, ConsigneePhone,
                         ConsigneeMobile,
                         ConsigneeEmail,
                         ConsigneeFax):
        lPage.clickPartyDetailsPage(ShipperAttention, ShipperBECode, ShipperName, ShipperPhone, ShipperMobile,
                                    ShipperEmail,
                                    ShipperFax, ConsigneeAttention, ConsigneeBECode, ConsigneeName, ConsigneePhone,
                                    ConsigneeMobile,
                                    ConsigneeEmail, ConsigneeFax)

    @then(u'Click on save and procced')
    def saveandprocced(context):
        lPage.saveandprocced()

    @then(u'click on any item')
    def item(context):
        lPage.item()

    @then(u'Mouse over all the details present in the booking details')
    def bookingdetails(context):
        lPage.bookingdetails()

    @then(u'Mouse over all the details present in the item details')
    def itemdetails(context):
        lPage.itemdetails()

    @then(u'Mouse over all the details present in the handling details')
    def handlingdetails(context):
        lPage.handlingdetails()

    @then(u'Mouse over all the details present in the origin and destination')
    def originanddestination(context):
        lPage.originanddestination()

    @then(u'Mouse over all the details present in the party details')
    def partydetails(context):
        lPage.Party_detailscheck()

    @then(u'Mouse over all the details present in the load and discharge')
    def loadanddischarge(context):
        lPage.loadanddischarge()

    @then(u'click on save')
    def save(context):
        lPage.saveButton()

    @then(u'click on save botton present in the FO line list page')
    def savedetails_Orderline(context):
        lPage.saveDetails()

    @then(u'Verify the toast "{message}"')
    def ToastMessage(context, message):
        lPage.ToastMessage(message)

    @then(u'save the fo')
    def ManuallFOSave(context):
        lPage.ManuallFOSave()

    # ***************************** Edit_FO ***************************#


@then(u'Click on edit')
def EditFO(context):
    lPage.EditFO()


@then(u'Click on any item FO Line List')
def FOItemClick(context):
    lPage.FOItemClick()


@then(u'Click on the party details')
def party_details(context):
    lPage.party_details()


@then(u'Enter the "{shipper_name1}" in shipper_name field')
def shipper_name(context, shipper_name1):
    lPage.shippername(shipper_name)


@then(u'Enter the "{consignee_name1}" in consignee_name field')
def consignee_name(context, consignee_name1):
    lPage.consigneename(consignee_name)

    # ***************************** Delete_FO ***************************#
    # @then(u'Scroll through menu to view planning option click on shipment and then click on freight orders')
    # def freightorders(context):
    #     lPage.freightButon()
    #

    # @then(u'Enter the FO in Freight Order field and search')
    # def FOEnter(context):
    #     lPage.FOEnter()
    #
    #
    # @then(u'Delete the FO')
    # def FOEnter(context):
    #     lPage.DeleteFO()
    #
    #
    # @then(u'Mousehover on FO save the order number')
    # def MousehoverFO(context):
    #     lPage.SaveOrderNumber()
    #
    #
    # @then(u'Click on single FO for delete')
    # def singleFO(context):
    #     lPage.singleFO()
    #
    #
    # @then(u'Click on single FO for delete')
    # def singleFO(context):
    #     lPage.DeletesingleFO()

    # @then(u'Select multiple FO')
    # def multipleFO(context):
    #     lPage.SelectmultipleFO()

    #
    # @then(u'Move to order repository')
    # def orderrepository(context):
    #     lPage.orderrepository()
    #
    #
    # @then(u'Enter Order "{refnumber}" in order Ref num field')
    # def ORDERREFNUM(context, refnumber):
    #     lPage.ORDERREFNUM(refnumber)
    #
    #
    # @then(u'click on check box')
    # def RefCheckBoxM(context):
    #     lPage.RefCheckBoxM()
    #
    #
    # @then(u'Search that deleted order using order number')
    # def OrderReFNumberSearch(context):
    #     lPage.OrderReFNumberSearch()
    #
    #
    # @then(u'check the "{status}" will be Unconsolidated')
    # def OrderReFNumberSearch(context, status):
    #     lPage.OrderReFNumberstatus(status)
    #
    #
    # ********************************************* LOAD (Build Load) *************************************************


@then(u'Click on loads')
def LoadsButton(context):
    lPage.LoadsButton()


@then(u'Click on Plan loads')
def PlanloadsButton(context):
    lPage.PlanloadsButton()


@then(u'Click on show active only')
def showactiveonly(context):
    lPage.showactiveonlyButton()

    # **************************************************************************************************#


@then(u'Click on create new workbench')
def workbench(context):
    lPage.workbench()


@then(u'Enter a value in workbench title "{title}"')
def workbenchTitel(context, title):
    lPage.workbench_Titel(title)


@then(u'Enter a value in workbench descprition "{descprition}"')
def workbenchDescprition(context, descprition):
    lPage.workbench_descprition(descprition)


@then(u'Select customer name from the workbench "{Customer}" dropdown')
def workbenchcustomer(context, Customer):
    lPage.workbenchcustomer(Customer)


@then(u'select "{DateTypeETA}" From Requested ETA')
def RequestedETA(context, DateTypeETA):
    lPage.RequestedETA(DateTypeETA)


@then(u'click on Requested ETA calender')
def ETAcalender(context):
    lPage.ETA_calender()


@then(u'select the "{month2}" from calender in Requested ETA')
def RequestedETAMonth(context, month2):
    lPage.RequestedETA_Month(month2)


@then(u'choose Depature "{from_date2}" and "{to_date2}" from the calender')
def DepatureDate(context, from_date2, to_date2):
    lPage.Depature_Date(from_date2, to_date2)


@then(u'choose Arrival "{from_date3}" and "{to_date3}" from the calender')
def ArrivalDate(context, from_date3, to_date3):
    lPage.Arrival_Date(from_date3, to_date3)


@then(u'Click on add mannualy')
def AddMannualy(context):
    lPage.Add_Mannualy()


@then(u'choose origin country and city from the drop down list')
def OriginCountry(context):
    lPage.Origin_Country()


@then(u'select Load')
def SelectLoad(context):
    lPage.SelectLoad()


@then(u'choose destination country and city from the drop down list')
def DestinationCountry(context):
    lPage.DestCountry()


@then(u'select unload')
def SelectUNLoad(context):
    lPage.SelectUNLoad()


@then(u'Click on search button')
def search(context):
    lPage.searchBTN()


@then(u'Select FO/FO from the list and click add fo line to workbench')
def ListFO(context):
    lPage.ListFO()


@then(u'Select x/y axis')
def xy_Axis_click(context):
    lPage.xy_Axis_click()


@then(u'Click on save and proceed')
def save_proceed(context):
    lPage.save_proceed()


@then(u'Select site in the route leg tab')
def RouteLeg(context):
    lPage.Route_Leg()


@then(u'click on save route as')
def RouteSaveAS(context):
    lPage.RouteSaveAS()


@then(u'Enter the "{routeName}" in route name field and save the route')
def RouteNameEnter(context, routeName):
    lPage.RouteNameEnter(routeName)


@then(u'Click on save and procced route leg')
def RL_save_proceed(context):
    lPage.RL_save_proceed()


@then(u'Select equipment type from the list')
def equipmentType(context):
    lPage.equipmentType()


@then(u'click on generate load plan')
def LoadPlan(context):
    lPage.Genearte_LoadPlan()


@then(u'click on 3d plan')
def threeDPlan(context):
    lPage.Three_D_Plan()


@then(u'check the Animated mode of load & unload')
def GraphicalMode(context):
    lPage.GraphicalMode()


@then(u'click on load Result1')
def loadResult1(context):
    lPage.loadResult1()


@then(u'click the check box of EquipmentID')
def Test_Size(context):
    lPage.ChooseEquipment()


@then(u'click on Generate Load')
def Generate_Load(context):
    lPage.Generate_Load()


@then(u'verify the Generate Load "{meassage}"')
def GenerateLoad_meassage(context, meassage):
    lPage.GenerateLoad_meassage(meassage)


@then(u'click on Save Result')
def SaveResult(context):
    lPage.Save_Result()


@then(u'verify the Save Result "{meassage1}"')
def GenerateLoad_meassage(context, meassage1):
    lPage.SaveResult_meassage(meassage1)


@then(u'Click on view details')
def SaveResult(context):
    lPage.Save_Result()


@then(u'Scroll the notificaion and copy the equipment number')
def SaveResult(context):
    lPage.Save_Result()


@then(u'Click on view load')
def SaveResult(context):
    lPage.Save_Result()


@then(u'Select manuall FO/FO from the list and click add fo line to workbench')
def ListManuallFO(context):
    lPage.ListManuallFO()
    # ****************************************** Load (Delete WB) ****************************************************#

    # @then(u'Enter workbench title in Search field')
    # def WBTitle(context):
    #     lPage.WBTitle()
    #
    #
    # @then(u'delete the workbench')
    # def DeleteWB(context):
    #     lPage.DeleteWB()
    #

    # ##############################################################################################################
    # # ********************************************** Rates & Contracts *****************************************#
    # # ********************************************** Carriers *****************************************#


@then(u'click on rate & contracts')
def rateContracts(context):
    lPage.rate_Contracts()


@then(u'click on carriers')
def carriers(context):
    lPage.carriers()


@then(u'click on create carrier')
def create_carriers(context):
    lPage.create_carriers()


@then(u'Enter "{carriercode}" in carrier code field')
def carriercode(context, carriercode):
    lPage.carrier_code(carriercode)


@then(u'Choose "{parrent}" from parrent carrier dropdown box')
def parrentcarrier(context, parrent):
    lPage.parrentcarrier(parrent)


@then(u'Enter "{carriername}" in carrier name field')
def carrier_name(context, carriername):
    lPage.carrier_name(carriername)


@then(u'Enter "{licescne}" on hazardous licescne')
def licescne(context, licescne):
    lPage.hazardouslicescne(licescne)


@then(u'Choose operating "{region}" from dropdown')
def region(context, region):
    lPage.operatingregion(region)


@then(u'Enter "{currency}" in billing currency field')
def currency(context, currency):
    lPage.billingcurrency(currency)


@then(u'Enter "{Fame}" in first name field')
def Fname(context, Fname):
    lPage.Firstname(Fname)


@then(u'Enter "{Lname}" in last name field')
def Lname(context, Lname):
    lPage.Lastname(Lname)


@then(u'Enter the "{email}" in email id field')
def email(context, email):
    lPage.Carrieremail(email)


@then(u'Enter the "{phonenumber}" in Phone number field')
def phonenumber(context, phonenumber):
    lPage.Carrierphonenumber(phonenumber)


@then(u'Enter the "{mobilenumber}" in mobile number')
def mobilenumber(context, mobilenumber):
    lPage.Carriermobilenumber(mobilenumber)


@then(u'click on carrier dangerous goods check box')
def checkbox(context):
    lPage.CDGcheckbox()


@then(u'click on registration details')
def registration_Details(context):
    lPage.registration_Details()


@then(u'choose "{Registrationcode}" from Registration dropdown box')
def Registrationcode(context, Registrationcode):
    lPage.Registration_code(Registrationcode)


@then(u'Enter "{RegistrationNumber}" in Registration Number field')
def RegistrationNumber(context, RegistrationNumber):
    lPage.Registration_Number(RegistrationNumber)


@then(u'Enter "{countryName}" in issuing country field')
def countryName(context, countryName):
    lPage.IssuingCountry(countryName)


@then(u'Enter the "{agencycode}" in issuing agency field')
def agencycode(context, agencycode):
    lPage.IssuingAgency(agencycode)


@then(u'Enter date in effective date filed')
def effective_Date(context):
    lPage.effective_Date()


@then(u'Enter date in expired date field')
def expireddate(context, ):
    lPage.Expired_date()


@then(u'Click on save Button')
def CarrierSaveButton(context):
    lPage.CarrierSaveButton()

    # ********************************************** Edit Carrier *****************************************#
    # @then(u'Enter carrrier Code in carrier code field')
    # def EditCarrierCode(context):
    #     lPage.EditCarrierCode()
    #
    #
    # @then(u'click on Carries Dangerous Goods')
    # def CarriesDangerousGoods(context):
    #     lPage.CarriesDangerousGoods()
    #
    #
    # @then(u'click on carrier search button')
    # def carrierSearchButton(context):
    #     lPage.carrierSearchButton()
    #
    #
    # @then(u'Click on carrrier Code')
    # def carrrierCode(context):
    #     lPage.carrrierCode()
    #
    #
    # @then(u'Click on edit carrrier')
    # def EditCarrrier(context):
    #     lPage.EditCarrrier()
    #
    #
    # @then(u'Edit "{licescne}" on hazardous licescne')
    # def EditHL(context, licescne):
    #     lPage.EditHL(licescne)
    #

    # ********************************************** Contract *****************************************#


@then(u'Click on contract')
def contract(context):
    lPage.contractButton()


@then(u'Choose carrier from the drop down')
def CarrierDropDown(context):
    lPage.CarrierDropDownButton()


@then(u'click on create contract')
def createcontract(context):
    lPage.createcontractButton()


@then(u'Enter "{contractname}" in the contrcat name field')
def contractname(context, contractname):
    lPage.contractnametButton(contractname)


@then(u'Enter "{contract}" in the contract field')
def contractNumber(context, contract):
    lPage.contractNumberButton(contract)


@then(u'Select "{customername}" from the dropdown')
def customername(context, customername):
    lPage.customernameButton(customername)


@then(u'select contract start date from the calender')
def contractstartdate(context):
    lPage.contractstartdateButton()


@then(u'select contract end date from the calender')
def contractenddate(context):
    lPage.contractenddateButton()


@then(u'If is it expired then click on has expired toggle')
def expiredtoggle(context):
    lPage.expiredtoggleButton()


@then(u'click on the create contract')
def createcontract1(context):
    lPage.createcontractButton1()


@then(u'verify the "{message}"')
def VeryContract(context, message):
    lPage.VeryMessage(message)


# ********************************************** Rates(Rate cards) *****************************************#


@then(u'click on Rates')
def Rates(context):
    lPage.RateCLICK()


@then(u'click on Rate Cards')
def Rates(context):
    lPage.RateCards()
    time.sleep(2)


@then(u'click on create Rate Card')
def create_RateCard(context):
    lPage.create_RateCard()


@then(u'Enter "{Name}" in Rate Card name field')
def RateCardName(context, Name):
    lPage.RateCardName(Name)


@then(u'Select Rate "{type}" in Rate type field')
def RateCardType(context, type):
    lPage.RateCardType(type)


@then(u'Enter carrrier name in rate_card carrier field')
def RateCardcarrrier(context):
    lPage.RateCardcarrrier()


@then(u'Select "{customername}" from the Customer dropdown')
def RateCardCustomername(context, customername):
    lPage.Ratecustomername(customername)


@then(u'Select "{ServiceType}" from the Service dropdown')
def RateCardServiceType(context, ServiceType):
    lPage.RateServiceType(ServiceType)


@then(u'Select "{IncoTerms}" from the Inco dropdown')
def RateCardIncoTerms(context, IncoTerms):
    lPage.RateCardIncoTerms(IncoTerms)


@then(u'Select "{PaymentTerms}" from the Payment dropdown')
def RateCardPaymentTerms(context, PaymentTerms):
    lPage.RateCardPaymentTerms(PaymentTerms)


@then(u'select date for rate validity')
def Ratevalidity(context):
    lPage.Ratevalidity()


@then(u'Enter "{account}" in Named Account field')
def RateAccount(context, account):
    lPage.RateAccount(account)


@then(u'click on save button for rates')
def RateSAve(context):
    lPage.RateSAve()


@then(u'verify the rate save "{message}"')
def VeryToast(context, message):
    lPage.VeryRateSaveToast(message)


@then(u'import the rate card file')
def RateFileImport(context):
    lPage.RateFileImport()


@then(u'verify the rate card "{Uploadmessage}"')
def RateUploadmessage(context, Uploadmessage):
    lPage.RateUploadmessage(Uploadmessage)

    # ***************************Rate_Cards_RateRevision  **********************#


@then(u'click on Rate Revision status')
def RateRevisionstatus(context):
    lPage.RateRevisionstatus()


@then(u'change the "{status}"')
def Revisionstatus(context, status):
    lPage.Revisionstatus(status)


@then(u'click on save for update')
def RevisionSave(context):
    lPage.RevisionSave()


@then(u'verify the approval history "{message}"')
def ApprovalHistory(context, message):
    lPage.ApprovalHistory(message)

    # ******************************************* Rate card Delete *****************************************#


@then(u'Enter new "{Name}" in Rate Card name field')
def New_RateCard_Name(context, Name):
    lPage.New_RateCard_Name(Name)


@then(u'delete the rate card')
def DeleteRateCard(context):
    lPage.DeleteRateCard()

    # ******************************************* Create_Rate_marigin *****************************************#


@then(u'click on rate margin')
def RateMargin(context):
    lPage.RateMargin()


@then(u'Click on create margin')
def CreateMargin(context):
    lPage.CreateMargin()


@then(u'select "{Servicetype}" from service type dropdown')
def ServiceType(context, Servicetype):
    lPage.MarginServiceType(Servicetype)


@then(u'select "{rateunit}" from rate unit dropdown')
def RateUnit(context, rateunit):
    lPage.RateUnit(rateunit)


@then(u'select "{equipmenttype}" from dropdown')
def equipmenttype(context, equipmenttype):
    lPage.Margin_equipmenttype(equipmenttype)


@then(u'select customer "{customerCode}" from lookup dropdown')
def customerName(context, customerCode):
    lPage.Margin_customer(customerCode)


@then(u'select hs "{HScode}" from lookup dropdown')
def HSCode(context, HScode):
    lPage.Margin_HSCode(HScode)


@then(u'Click on checkbox of is dangerous cargo')
def dangerouscargo(context):
    lPage.Margin_dangerouscargo()


@then(u'select on "{hazardouscode}" from lookup dropdown')
def hazardouscode(context, hazardouscode):
    lPage.Margin_hazardouscode(hazardouscode)


@then(u'Click on "{loadcountry}" and select from lookup dropdown')
def Load_country(context, loadcountry):
    lPage.Load_country(loadcountry)


@then(u'select "{loadcity}" code')
def Load_city(context, loadcity):
    lPage.Load_city(loadcity)


@then(u'Enter valid "{Pin}" in load postcode')
def Load_postcode(context, Pin):
    lPage.Load_postcode(Pin)


@then(u'select and click "{dischargecountry}" from lookup dropdown')
def Discharge_country(context, dischargecountry):
    lPage.Discharge_country(dischargecountry)


@then(u'select the discharge "{dischargecity}" from lookup dropdown')
def Discharge_city(context, dischargecity):
    lPage.Discharge_city(dischargecity)


@then(u'Enter valid "{Pin1}" in discharge postcode')
def Discharge_postcode(context, Pin1):
    lPage.Discharge_postcode(Pin1)


@then(u'Enter valid "{validdata}" in margin')
def marginNumber(context, validdata):
    lPage.MarginNumber(validdata)


@then(u'select the "{currency}" from lookup dropdown')
def Margin_currency(context, currency):
    lPage.Margin_currency(currency)


@then(u'click on is percentage checkbox')
def Margin_isPercentage(context):
    lPage.Margin_isPercentage()


@then(u'choose valid date From')
def validdate_From(context):
    lPage.validdate_From()


@then(u'choose valid date To')
def validdate_To(context):
    lPage.validdate_To()


@then(u'click on save button of margin')
def Margin_Save(context):
    lPage.Margin_Save()


# ********************************************* Delete Margin **********************************************#
@then(u'click on filter button')
def RateMargin_Filter(context):
    lPage.FilterButton()


@then(u'click on search button for rate margin')
def RateMargin_Search(context):
    lPage.RateMargin_Search()
    lPage.carrierSearchButton()


@then(u'delete the rate margin')
def RateMargin_Delete(context):
    lPage.DeleteFO()


# ******************************************* Compare_Rate *****************************************#

@then(u'click on auto generate compare rates')
def auto_generate_Compare_Rates(context):
    lPage.auto_generate_Compare_Rates()


@then(u'click on Compare Rates')
def Compare_Rates(context):
    lPage.Compare_Rates()


@then(u'Select "{customer}" from the compare rate Customer dropdown')
def compareRate_Customer(context, customer):
    lPage.compareRate_Customer(customer)


@then(u'select on "{HazCode}" from HazCode dropdown')
def compareRate_HazCode(context, HazCode):
    lPage.compareRate_HazCode(HazCode)


@then(u'click on Add route leg')
def Add_route_leg(context):
    lPage.Add_route_leg()


@then(u'enter org-country name in counrty field')
def Add_route_leg(context):
    lPage.org_country()


@then(u'enter org-city name in city field')
def org_city(context):
    lPage.org_city()


@then(u'enter des-country name in counrty field')
def des_country(context):
    lPage.des_country()


@then(u'enter des-city name in city field')
def des_city(context):
    lPage.des_city()


@then(u'choose equipment number from the dropdown box')
def equipment_number(context):
    lPage.equipment_numberSelect()


@then(u'Enter equipment quantity in the text field')
def equipment_quantity(context):
    lPage.equipment_quantity()


@then(u'Enter weight in the text field')
def equipment_quantity(context):
    lPage.Enter_Weight()


@then(u'choose weight type in the dropdown box')
def choose_weight(context):
    lPage.choose_weight()


@then(u'choose Volume type in the dropdown box')
def equipment_Volume(context):
    lPage.Enter_Volume()


@then(u'Enter Volume in the text field')
def choose_Volume(context):
    lPage.choose_Volume()


@then(u'choose MOT type in the dropdown box')
def MOT_type(context):
    lPage.MOT_type()


@then(u'click on the Add Route Leg')
def Add_Route_Leg(context):
    lPage.Add_RouteLeg()


@then(u'click on check box of route leg')
def RouteLeg_CheckBox(context):
    lPage.RouteLeg_CheckBox()


@then(u'Apply the route leg')
def RouteLeg_Apply(context):
    lPage.RouteLeg_Apply()


@then(u'click on compare button')
def compare_button(context):
    lPage.compare_button()


# ******************************************* Manage Load *****************************************#
@then(u'Click on manage load')
def manage_load(context):
    lPage.manage_load()


@then(u'Enter equipment number in equipment field')
def Enter_Equipment(context):
    lPage.Enter_Equipment()


@then(u'Click on equipment number for checking details')
def equipment_details(context):
    lPage.equipment_details()


@then(u'Click on the check box of assign carrier')
def Assign_carrier(context):
    lPage.Assign_carrier()


@then(u'click on the assign carrier')
def Click_AssignCarrier(context):
    lPage.Click_AssignCarrier()


@then(u'save the booking number')
def Save_BookingNumber(context):
    lPage.Save_BookingNumber()


@then(u'click on assign direct')
def Assign_Direct(context):
    lPage.Assign_Direct()


@then(u'choose carrier from choose carrier')
def CarrierChoose(context):
    lPage.CarrierChoose()


@then(u'click on assign carrier')
def Assigned_Carrier(context):
    lPage.Assigned_Carrier()


# ******************************************** Carrier_AssignTO_Ratecard **********************************#
# @then(u'Click on contract filter button')
# def Contract_Filter_Button(context):
#     lPage.Contract_Filter_Button()
#
#
# @then(u'Uncheck the approved only Checkbox')
# def Approved_Only(context):
#     lPage.Approved_Only()
#
#
# @then(u'search the unapproved contract')
# def unapproved_contract(context):
#     lPage.unapproved_contract()
#
#
# @then(u'click on assign rates')
# def assign_rates(context):
#     lPage.assign_rates()
#
#
# @then(u'click on rate Card from dropdown list')
# def RateCoardChoose(context):
#     lPage.RateCoardChoose()
#
#
# @then(u'click on Assign')
# def Assign(context):
#     lPage.Assign()
#
#
# ******************************************* Carrier Bookings *****************************************#

@then(u'Click on Execution Menu')
def Execution_Menu(context):
    lPage.Execution_Menu()


@then(u'Click on Bookings Button')
def Bookings_Button(context):
    lPage.Bookings_Button()


@then(u'Click on Transportorders')
def Transport_orders(context):
    lPage.Transport_orders()


@then(u'click on filter')
def Click_filter(context):
    lPage.Click_filter()


@then(u'select Booking request from Transport Status')
def Select_TransportStatus(context):
    lPage.Select_TransportStatus()


@then(u'Click on expand page')
def expand_page(context):
    lPage.expand_page()


@then(u'Expand the carrier booking dropdown')
def Expand_Carrier_Bookings(context):
    lPage.Expand_Carrier_Bookings()


@then(u'Click on the load hyperlink')
def Click_hyperlink(context):
    lPage.Click_hyperlink()


@then(u'Click on Transport status')
def Transport_status(context):
    lPage.Transport_status()


@then(u'Click on Trip Status')
def Tripstatus_click(context):
    lPage.Tripstatus_click()


@then(u'Then click on save button')
def Click_save(context):
    lPage.Click_save()


@then(u'Close trip status menu')
def Close_trip_status_menu(context):
    lPage.Close_trip_status_menu()


@then(u'Click on trip details edit')
def Click_trip_edit(context):
    lPage.Click_trip_edit()


@then(u'Enter Booking confirmation number')
def Enter_Booking_confirmation_number(context):
    lPage.Enter_Booking_confirmation_number()


# ******************************************* Dispatch *****************************************#
#
# @then(u'click on dispatch')
# def Dispatch(context):
#     lPage.Dispatch()
#
#
# @then(u'click on dispatch planning')
# def Dispatch_Planning(context):
#     lPage.Dispatch_Planning()
#
#
# @then(u'enter the load country for dispatch')
# def Dispatch_Country(context):
#     lPage.Dispatch_Country()
#
#
# @then(u'enter the load city for dispatch')
# def Dispatch_City(context):
#     lPage.Dispatch_City()
#
#
# @then(u'enter the load site for dispatch')
# def Dispatch_Site(context):
#     lPage.Dispatch_Site()
#
#
# @then(u'click on proceed button')
# def Dispatch_proceed(context):
#     lPage.Dispatch_proceed()
#
#
# ******************************************* Intake *****************************************#
# @then(u'click on intake planning')
# def intake_planning(context):
#     lPage.intake_planning()
#
#
# @then(u'enter the load country for intake')
# def intake_Country(context):
#     lPage.intake_planning()
#
#
# @then(u'enter the load city for intake')
# def intake_City(context):
#     lPage.intake_City()
#
#
# @then(u'enter the load site for intake')
# def intake_Site(context):
#     lPage.intake_Site()
#
#
# ******************************************** Trip details *********************************************#
# @then(u'click on trips')
# def trips(context):
#     lPage.trips()
#
#
# @then(u'click on carrier and select carrier from the drop down')
# def selectcarriername(context, lpage=carriername):
#     lpage.selectcarriername()


# @then(u'click on search')
# def search(context, lpage=search):
#     lpage.search()
#
# *******************************************Freight Audit*********************************************
@then(u'click on Settlement menu')
def settlement(context):
    lPage.clickSettlement()


@then(U'Click on freightaudit')
def freightaudit(context):
    lPage.Clickfreightaudit()


@then(U'click on importinvoice')
def importinvoice(context):
    lPage.clickimportinvoice()


# ******************************************* Logout Application *****************************************#
@then(u'Click on Esspl logo')
def EssplLogo(context):
    lPage.ClikEssplLogo()


@then(u'Click on logout')
def LogOut(context):
    lPage.LogOutBTN()
