Feature: Verify the TMS functionality

  @LoginPage
  Scenario Outline: The user should be able to login to the application successfully
    Given launch the "<TMS_Url>"
    Then Provide the username "<UserID>" in the username field
    Then Click on Proceed
    And Provide the Password "<Password>" in the Password field
    And Click on the LoginIn button
    And Mouse Hover and Click on Dashboard Menu
    And Mouse Hover and Click on Delivery Timeliness
    And Mouse Hover and Click on Dashboard
    And Uncheck the ETD field in filter
    And Uncheck the ETA field in filter
    And Click on Apply button
    And Click on Close button
#    And Mouse Hover and Click on At Risk In-transit Shipments
#    And Uncheck the At Risk In-transit Shipments ETD field in filter
#    And Uncheck the At Risk In-transit Shipments ETA field in filter
#    And Click on At Risk In-transit Shipments Apply button
#    And Click on At Risk In-transit Shipments Close button
#    And Click on the dropdown1 in the dashboard
#    And Click on Carrier Bookings Pending Confirmation filter
#    And Uncheck booking Dt in Bookings Pending Confirmation filter
#    And Click on apply in Carrier Bookings Pending Confirmation filter
#    And Close the Carrier Bookings Pending Confirmation
#    And Click on the dropdown2 in the dashboard
#    And Click on Carrier Bookings Pending Confirmation
#    And Uncheck the carrierbookingdate
#    And Click on apply
#    And close the filter



    Examples:
      | TMS_Url              | UserID | Password |
      | https://192.168.0.84 | jenny1 | 12345    |


 # @Dashboard
#  Scenario Outline: The user should be able to view the dashboard
#  #  Given The user should be able to Mouse Hover on Dashboard Menu
#  #  And Mouse hover on delivery quality tab
#    And Mouse hover on delivery Timeliness
#    And click on advance filter
#    And click on Checkbox and uncheck for ETD
#    And click on Checkbox and uncheck for ETA
#    And click on apply button

  @Rule_Set_Creation
  Scenario Outline: The user should be able to create a ruleset successfully.
    And Click on Planning Button
    And Click on Rule
    And Click on create ruleset
    Then Enter the Ruleset "<Name>" Rule Set Name textbox
    And Enter the "<Description>" for the ruleset
    And Select the "<Policy_type>" from the dropdown
    And Click on the Active toggle button to activate the column
    And Check on Add to an Open Order
    And Click on Next Button
    And Drag and drop the "<rule>" consolidation field
    And Click on Rule_Next Button
    And Drag and drop the "<criteria>" field
    And Enter Values in selected field
    And Click on Finish
    And Click on Confirm


    Examples:
      | Name    | Description | Policy_type | rule         | month | from_date | to_date | criteria      | Values |
      | Ruleset | Nothing     | SO          | Order Status | Dec   | 1         | 28      | Customer Code | TEY    |

###  @Ruleset_sequence
###  Scenario Outline: The user should be able to sequence the already created Ruleset
###    And Click on Planning Button
###    And Click on rule
###    And Filter the "<policytype>"
###    And Click on any ruleset for sequencing
###    And Sequence the rule set present
###    And Click on save sequence
###    And ruleset "<sequence>" successfully changed
###    And Click to sequence the default ruleset
###
###
###    Examples:
###      | Policytype | sequence                            | DEB                                    |
###      | SO         | Ruleset sequence have been updated. | Ruleset sequence changed successfully. |
##
####
###  @Edit_ruleset
###  Scenario Outline: The user should be able to edit ruleset successfully.
###    And Click on ruleset and edit
###    And Modify the "<rulesetname>" and save
###    And Click on Next Button
###    And Click on Rule_Next Button
###    And Click on Finish
###    And Click on Confirm
###
###    Examples:
###      | rulesetname                  |
###      | consolidation ruleset check1 |
##
##    ##  @View_ruleset
####  Scenario: The user should be able to view ruleset successfully.
####    And Click on view of any ruleset
####
####  @delete_ruleset
####  Scenario: The user should be able to delete ruleset successfully.
####    And Click on delete
##
####
  @Orders
  Scenario: The user should be able to view orders repository
    And Scroll through menu to view planning option
    And Scroll through menu to view orders menu
    And Click on orders button

  @autogenrate_FO_with_the_available_rulesets
  Scenario Outline: The user should be able to select orders and autogenrate FO with the available rulesets
    And Goto order menu and click on filter
#    And Enter "<Orderref number>" in Orderref field
    And Choose "<unconsolidate>" from consolidation status
    Then select "<DateType>" From date
    And click on calender
    And choose "<from_date1>" and "<to_date1>" from the calender
    And Click on search
    And Then select order/orderline from the list
    And save the Order Reference Number
    And Click on consolidation order
    And Save the TR no
    And Click on that notification

    Examples:
      | unconsolidate  | DateType | month | from_date1 | to_date1 |
      | Unconsolidated | Custom   | Aug   | 1          | 28       |

#  @workbench_autogenerate_FO
#  Scenario Outline: The user should be able to filter the workbench using different parameters for autogenrateFO
#    And Scroll through menu to view planning option click on shipment and then click on freight orders
#    And Click on Planning Button
#    And Scroll through menu to view Load option
#    And Click on build loads
#    And Click on show active only
#
#    Examples:
#      | status         |
#      | Unconsolidated |
#
#  @Create_workbench_autogenerate_FO
#  Scenario Outline: The user should be able to create the workbench for autogenrateFO
#    And Click on create new workbench
#    And Enter a value in workbench title "<title>"
#    And Enter a value in workbench descprition "<descprition>"
#    And Select customer name from the workbench Customer dropdown
#    Then select "<DateType>" From date
#    And click on calender
#    And choose Depature "<from_date2>" and "<to_date2>" from the calender
#    Then select "<DateTypeETA>" From Requested ETA
#    And Select "<ServiceType>" from the Service dropdown
#    And Click on add mannualy
#    And choose origin country and city from the drop down list
#    Then select Load
#    And choose destination country and city from the drop down list
#    Then select unload
#    And Click on search button
#    And Select FO/FO from the list and click add fo line to workbench
#    And Click on save and proceed
#    And Select site in the route leg tab
#    And click on save route as
#    And Enter the "<routeName>" in route name field and save the route
#    And Click on save and procced route leg
#    And Select equipment type from the list
#    And click on generate load plan
#    And click on load Result1
#    And click the check box of EquipmentID
#    And click on Generate Load
#    And verify the Generate Load "<meassage>"
#    And click on Save Result
#    And verify the Save Result "<meassage1>"
#    And click on 3d plan
#    And check the Animated mode of load & unload
#
#    Examples:
#      | title | description | customer name | ServiceType | DateType | month | from_date2 | to_date2 | month2 | DateTypeETA | from_date3 | to_date3 | routeName | meassage                    | meassage1                             | Changed                                  |
#      | WB    | description | Boat          | FCL         | Custom   | Dec   | 1          | 28       | Dec    | None        | 1          | 28       | Route     | Load(s) saved successfully. | Work bench result(s) have been saved. | Work bench result(s) saved successfully. |
#
##  @LOAD_autogenerate_FO
##  Scenario Outline: The user should be able to create the Built Load for autogenerateFO
##    And Click on notification button
##    And goto the load icon in the notification and click on view details
##    And save the equipment number
##    And Click on view Load in notification
##    And choose the equipment type
##    And enter the equipment number in equipment field
##    And Click on Equipment search button
##
##    Examples:
##      | title |
##      | bb    |
##  @create_FO_from_orders_Manually
##  Scenario Outline: The user should be be able to create FO from orders.
##    And Scroll through menu to view planning option click on shipment and then click on freight orders
##    And Click on the create freight order
##    Then click on create from order
##    And Move to order repository
##    And Choose "<unconsolidate>" from consolidation status
##    Then select "<DateType>" From date
##    And click on calender
##    And select the "<month>" from calender
##    And choose "<from_date1>" and "<to_date1>" from the calender
##    And Click on search
##    And Then select order/orderline from the list
##    And Click on procced
##    Then mouse hover all the field present in the FO header page
##    And Fill all the details in party details page "<ShipperAttention>","<ShipperBECode>","<ShipperName>","<ShipperPhone>","<ShipperMobile>","<ShipperEmail>","<ShipperFax>","<ConsigneeAttention>","<ConsigneeBECode>","<ConsigneeName>","<ConsigneePhone>","<ConsigneeMobile>","<ConsigneeEmail>","<ConsigneeFax>"
##    And Click on save and procced
##    And Click on any item
##    And Mouse over all the details present in the booking details
##    And Mouse over all the details present in the item details
##    And Mouse over all the details present in the handling details
##    And Mouse over all the details present in the origin and destination
##    And Mouse over all the details present in the party details
##    And Mouse over all the details present in the load and discharge
##    Then click on save
##    Then click on save botton present in the FO line list page
##    Then Verify the toast "<message>"
##    And Click on notification
##    Then save the fo
##
##    Examples:
##      | unconsolidate  | DateType | month | from_date1 | to_date1 | ShipperAttention | ShipperBECode | ShipperName | ShipperPhone | ShipperMobile         | ShipperEmail | ShipperFax | ConsigneeAttention | ConsigneeBECode | ConsigneeName | ConsigneePhone | ConsigneeMobile       | ConsigneeEmail | ConsigneeFax | message                            | chn                                   |
##      | Unconsolidated | Custom   | Dec   | 1          | 28       | a                | a             | a           | 986546976    | zainabsalma@gmail.com | a            | a          | Sultan Ahmed       | 74864748939     | a             | 1234567890     | zainabsalma@gmail.com | a              | a            | FreightOrder(s) have been created. | FreightOrder(s) created successfully. |
###
###
###  @manually/autogenrated_FO_EDIT
###  Scenario Outline: The user should be able to Edit an FO that is created manually/autogenrated
###    And Scroll through menu to view planning option click on shipment and then click on freight orders
###    And Select freight order from the list.
###    And Click on edit
###    And Click  to edit ETA.
###    And Click  to edit ETD.
###    And mouse over to the fields presents in FO header
###    And Click on the party details
###    And Enter consignee
###    And Enter consignee_be_code
###    And Enter the "<shipper_name1>" in shipper_name field
###    And Enter the "<consignee_name1>" in consignee_name field
###    And Enter consignee_attention_to
###    And Enter consignee_phone
###    And Enter consignee_mobile
###    And Enter consignee_email
###    And Enter Consignee_fax
###    And Enter shipper
###    And Enter shipper_attention_to
###    And Enter shipper_be_code
###    And Enter shipper_phone
###    And Enter shipper_mobile
###    And Enter shipper_email
###    And Enter shipper_fax
###    And Click on save and procced
###    And Click on any item FO Line List
###    And Mouse over all the details present in the item details
###    And Mouse over all the details present in the handling details
###    And Mouse over all the details present in the origin and destination
###    And Mouse over all the details present in the party details
###    And Mouse over all the details present in the load and discharge
###    Then click on save
###    Then click on save button present in the FO line list page
###    And Click on Save and Proceed
##
##
###    Examples:
###      | consignee_name1 | shipper_name1 |
###      | DH              | CH            |
###
##  @workbench_ManuallyFO
##  Scenario Outline: The user should be able to filter the workbench using different parameters for ManuallyFO
##    And Click on Planning Button
##    And Click on loads
##    And Click on Plan loads
##    And Click on show active only
##
##    Examples:
##      | status         |
##      | Unconsolidated |
##
##  @Create_workbench_ManuallyFO
##  Scenario Outline: The user should be able to create the workbench for ManuallyFO
##    And Click on create new workbench
##    And Enter a value in workbench title "<title>"
##    And Enter a value in workbench descprition "<descprition>"
###    And Select customer name from the workbench Customer dropdown
##    Then select "<DateType>" From date
##    And click on calender
##    And choose Depature "<from_date2>" and "<to_date2>" from the calender
##    Then select "<DateTypeETA>" From Requested ETA
###    And Select "<ServiceType>" from the Service dropdown
##    And Click on add mannualy
##    And choose origin country and city from the drop down list
##    Then select Load
##    And choose destination country and city from the drop down list
##    Then select unload
##    And Click on search button
##    And Select manuall FO/FO from the list and click add fo line to workbench
##    And Click on save and proceed
##    And Select site in the route leg tab
##    And click on save route as
##    And Enter the "<routeName>" in route name field and save the route
##    And Click on save and procced route leg
##    And Select equipment type from the list
##    And click on generate load plan
##    And click on load Result1
##    And click the check box of EquipmentID
##    And click on Generate Load
##    And verify the Generate Load "<meassage>"
##    And click on Save Result
##    And verify the Save Result "<meassage1>"
##    And click on 3d plan
##
##
##    Examples:
##      | title | description | DateType | ServiceType | month | from_date2 | to_date2 | month2 | DateTypeETA | from_date3 | to_date3 | routeName | meassage                    | meassage1                             | Changed                                  |
##      | WB    | description | Custom   | FCL         | Dec   | 1          | 28       | Dec    | None        | 1          | 28       | RouteName | Load(s) saved successfully. | Work bench result(s) have been saved. | Work bench result(s) saved successfully. |
##
##
##    Examples:
##      | licescne | Fname | Lname  | email       | phonenumber | mobilenumber | currency | message                   | Changed                      |
##      | V6       | Rahul | Sharma | b@gmail.com | 442288993   | 8477755596   | USD      | Carrier has been updated. | Carrier Updated Successfully |
##
##  @Contracts
##  Scenario Outline: The user should be able to create contract successfully
##    And click on rate & contracts
##    Then Click on contract
##    And choose carrier from the drop down
##    Then click on create contract
##    And Enter "<contract name>" in the contract name field
##    And Enter "<contract>" in the contract field
##    And Select "<customer name>" from the dropdown
##    Then select contr#  @LOAD_ManuallyFO
##
##  Scenario Outline: The user should be able to create the Built Load for ManuallyFO
##    And Click on notification button
##    And goto the load icon in the notification and click on view details
##    And save the equipment number
##    And Click on view Load in notification
##    And choose the equipment type
##    And enter the equipment number in equipment field
##    And Click on Equipment search button
##
##    Examples:
##      | title |
##      | bb    |
##
##  @Delete_Workbench
##  Scenario Outline: The user should be able to delete WorkBench sucessfully
##    And Click on Planning Button
##    And Scroll through menu to view Load option
##    And Click on build loads
##    And Click on show active only
##    And Enter workbench title in Search field
##    Then delete the workbench
##
##    Examples:
##      | status         |
##      | Unconsolidated |
##
##
##  @Delete_FO
##  Scenario Outline: The user should be able to delete a FO sucessfully
##    And Scroll through menu to view planning option click on shipment and then click on freight orders
##    And Enter the FO in Freight Order field and search
##    And Delete the FO
##    And Search that deleted order using order number
##    And check the "<status>" will be Unconsolidated
##    Examples:
##      | status         |
##      | Unconsolidated |
##
###  @Same_COuntry_Diffrent_CITY_FO_Manually
##  Scenario Outline: Manual Fo should not be created Origin same country&city and destination same country & different city.
##    And Scroll through menu to view planning option click on shipment and then click on freight orders
##    And Click on the create freight order
##    Then click on create from order
##    And Move to order repository
##    Then Enter Order "<ref number>" in order Ref num field
##    Then Enter Order "<ref number1>" in order Ref num field
##    And Click on search
##    And click on check box
##    And Click on proceed
##    And verify the "<message>"
##
##    Examples:
##      | message           | ref number | ref number1 | status |
##      | Validation Error. | 2294243    | 1981010     | 501865 |
##
##  @Different_Country_Different_CITY_FO_Manually
##  Scenario Outline: Manual Fo should not be created both origin & destination different country & different city.
##    And Scroll through menu to view planning option click on shipment and then click on freight orders
##    And Click on the create freight order
##    Then click on create from order
##    And Move to order repository
##    Then Enter Order "<ref number>" in order Ref num field
##    Then Enter Order "<ref number1>" in order Ref num field
##    And Click on search
##    And click on check box
##    And Click on procced
##    And verify the "<message>"
##
##    Examples:
##      | message           | ref number | ref number1 | status |
##      | Validation Error. | 3353639    | 9637108     | 501865 |
##
##  @Origin_Same_Country/Diffrent_City_Destination_Same_Country&CITY_FO_Manually
##  Scenario Outline: Manuall Fo should not be created origin same country and diffrent city and destination same country&city.
##    And Scroll through menu to view planning option click on shipment and then click on freight orders
##    And Click on the create freight order
##    Then click on create from order
##    And Move to order repository
##    Then Enter Order "<ref number>" in order Ref num field
##    Then Enter Order "<ref number1>" in order Ref num field
##    And Click on search
##    And click on check box
##    And Click on procced
##    And verify the "<message>"
##    Examples:
##      | message           | ref number | ref number1 | status |
##      | Validation Error. | 8282929    | 1981010     | 501865 |
##
#  @Carriers
#  Scenario Outline: The user should be able to create carrier sucessfully
#    And click on rate & contracts
#    Then click on carriers
#    And click on create carrier
#    And Enter "<carriercode>" in carrier code field
##    And Choose "<parrent>" from parrent carrier dropdown box
#    And Enter "<carriername>" in carrier name field
#    And Enter "<licescne>" on hazardous licescne
#    And Choose operating "<region>" from dropdown
#    And Enter "<currency>" in billing currency field
#    And Enter "<Fname>" in first name field
#    And Enter "<Lname>" in last name field
#    And Enter the "<email>" in email id field
#    And Enter the "<phonenumber>" in Phone number field
#    And Enter the "<mobilenumber>" in mobile number
#    And click on carrier dangerous goods check box
#    And click on registration details
#    And choose "<Registration code>" from Registration dropdown box
#    And Enter "<Registration Number>" in Registration Number field
#    And Enter "<country Name>" in issuing country field
#    And Enter the "<agency code>" in issuing agency field
#    And Enter date in effective date filed
#    And Enter date in expired date field
#    And Click on save Button
#    And verify the "<message>"
#
#    Examples:
#      | carriercode | parrent     | carriername  | licescne | region | currency | Fname | Lname | email       | phonenumber | mobilenumber | Registration code | Registration Number | country Name | agency code | expireddate | message                 | chnaged                     |
#      | C777        | Morrexcargo | Rati_carrier | D1234    | MUM    | INR      | Pat   | Lat   | d@gmail.com | 067489562   | 9853634323   | TRN               | A0009               | IND          | I1234       | 2024-02-15  | Carrier has been saved. | Carrier saved successfully. |
#
##  @EDIT_Carriers
##  Scenario Outline: The user should be able to Edit carrier sucessfully
##    And click on rate & contracts
##    Then click on carriers
##    And Enter carrier Code in carrier code field
##    And click on carrier dangerous goods check box
##    Then click on carrier search button
##    And Click on carrier Code
##    And Click on edit carrier
##    And Enter "<licescne>" on hazardous licescne
##    And Edit "<licescne>" on hazardous licescne
##    And Enter "<currency>" in billing currency field
##    And Enter "<Fname>" in first name field
##    And Enter "<Lname>" in last name field
##    And Enter the "<email>" in email id field
##    And Enter the "<phonenumber>" in Phone number field
##    And Enter the "<mobilenumber>" in mobile number
##    And click on registration details
##    And Enter date in expired date field
##    And Click on save Button
##    And verify the "<message>"act start date from the calender
##    Then select contract end date from the calender
##    And If is it expired then click on has expired toggle
##    Then click on the create contract
##    And verify the "<message>"
##
##    Examples:
##      | contract name | contract | customer name       | message                     | changed                        |
##      | C777          | c777co   | Innovative Apparels | Contract(s) has been saved. | contract created successfully. |
##
#  @Rate_Cards
#  Scenario Outline: The user should be able to create Rate card sucessfully
#    And click on rate & contracts
#    And click on Rates
#    And click on Rate Cards
#    And click on create Rate Card
#    And Enter "<Name>" in Rate Card name field
#    And Select Rate "<type>" in Rate type field
##    And Enter carrrier name in rate_card carrier field
##    And Select "<customer name>" from the Customer dropdown
#    And Select "<ServiceType>" from the Service dropdown
#    And Select "<IncoTerms>" from the Inco dropdown
#    And Select "<PaymentTerms>" from the Payment dropdown
##    And select date for rate validity
#    And Enter "<account>" in Named Account field
#    And click on save button for rates
#    And verify the rate save "<message>"
#    And import the rate card file
#    And verify the rate card "<Uploadmessage>"
#
#    Examples:
#      | Name       | type | customer name       | ServiceType | IncoTerms    | PaymentTerms | account | message                          | Uploadmessage                            |
#      | RATE_CHECK | Spot | Innovative Apparels | FCL         | Free Carrier | Collect      | 123456  | Rate card  created successfully. | Rate card upload is in processing state. |

##  @Rate_Cards_RateRevision
##  Scenario Outline: The user should be able to check rate revision sucessfully
##    And click on Rate Revision status
##    And change the "<status>"
##    And click on save for update
##    And click on Rate Revision status
##    And change the "<status1>"
##    And click on save for update
##    And verify the approval history "<message>"
##
##    Examples:
##      | status            | message           | status1            |
##      | Approved Revision | Approved Revision | Candidate Revision |
##
##  @Rate_Cards_Delete
##  Scenario Outline: The user should be able to delete rate card sucessfully
##    And Enter new "<Name>" in Rate Card name field
##    And click on save button for rates
##    And verify the "<message>"
##    And import the rate card file
##    And delete the rate card
##    And verify the "<message1>"
##
##    Examples:
##      | Name  | message                         | message1                              |
##      | Rate4 | Rate card updated successfully. | Rate version(s) deleted successfully. |
##
##  @Rate_Cards_RateRevision
##  Scenario Outline: The user should be able to change the rate revision sucessfully
##    And click on Rate Revision status
##    And change the "<status>"
##    And click on save for update
##    And verify the approval history "<message>"
##
##    Examples:
##      | status            | message           |
##      | Approved Revision | Approved Revision |
##
##  @Carrier_AssignTO_Ratecard
##  Scenario Outline: The user should be able to assign rate to the carrier sucessfully
##    And click on rate & contracts
##    Then Click on contract
##    And choose carrier from the drop down
##    Then Click on contract filter button
##    And enter contract number in contract number field
##    And Uncheck the approved only Checkbox
##    Then search the unapproved contract
##    And click on assign rates
##    And click on rate Card from dropdown list
##    And click on Assign
##
##    And verify the approval history "<message>"
##
##    Examples:
##      | status            | message           |
##      | Approved Revision | Approved Revision |
##
#  @Create_Rate_marigin
#  Scenario Outline: The user should be able to create margin sucessfully
#    And click on rate & contracts
#    And click on Rates
#    Then click on rate margin
#    And Click on create margin
##    And Select MOT(Road/Sea/Air)
#    And select "<Service type>" from service type dropdown
#    And select "<rate unit>" from rate unit dropdown
#    And select "<equipment type>" from dropdown
#    And select customer "<customer Code>" from lookup dropdown
#    And select hs "<HS code>" from lookup dropdown
#    And select on "<hazardous code>" from lookup dropdown
#    And Click on checkbox of is dangerous cargo
##    And Click on "<load country>" and select from lookup dropdown
##    And select "<load city>" code
##    And Enter valid "<Pin>" in load postcode
##    And select and click "<discharge country>" from lookup dropdown
##    And select the discharge "<discharge city>" from lookup dropdown
###    And Enter valid "<Pin1>" in discharge postcode
#    And Enter valid "<data2>" in margin
#    And select the "<currency>" from lookup dropdown
#    And click on is percentage checkbox
#    And choose valid date From
#    And choose valid date To
#    Then click on save button of margin
#    And verify the "<message>"
#
#
#    Examples:
#      | Service type | rate unit | equipment type | customer Code   | HS code | hazardous code | load country | load city | Pin        | discharge country    | discharge city | Pin1       | data2 | currency | message                       |
#      | FCL          | All       | 10FT/DRY       | Sneaker Company | 1       | Flammable gas  | Oman         | Ibri      | 2890096335 | United Arab Emirates | Dubai          | 2890096667 | 10    | USD      | Rate margin has been created. |
#
#  @Delete_RateMargin
#  Scenario Outline: The user should be able to delete the rate margin successfully
#    And click on rate & contracts
#    And click on Rates
#    Then click on rate margin
#    And click on filter button
#    And Select "<ServiceType>" from the Service dropdown
#    Then Click on checkbox of is dangerous cargo
##    Then click on search button for rate margin
#    And delete the rate margin
#    And verify the "<message>"
#
#    Examples:
#      | ServiceType | message                          |
#      | FCL         | Delete rate margin successfully. |
#
#  @Autogenerate_Generate_CompareRate
#  Scenario Outline: The user should be able to create the autogenrate generate compareRate
#    And Click on Planning Button
#    And Scroll through menu to view Load option
#    And Click on manage load
#    And choose the equipment type
#    And enter the equipment number in equipment field
#    And Click on Equipment search button
#    And Click on equipment number for checking details
#    Then Click on the check box of assign carrier
#    And click on the assign carrier
#    And click on auto generate compare rates
#    Then click on compare button
#    And save the booking number
#    And verify the "<message>"
#
#    Examples:
#      | message |
#      |         |
#
#  @Manuall_Compare_Rate
#  Scenario Outline: The user should be successfully campare rate manually
#    And click on rate & contracts
#    And click on Rates
#    Then click on Compare Rates
#    And Select "<ServiceType>" from the Service dropdown
#    And Select "<customer>" from the compare rate Customer dropdown
#    And select the "<currency>" from lookup dropdown
#    And select hs "<HS code>" from lookup dropdown
#    And select on "<HazCode>" from HazCode dropdown
#    Then Click on checkbox of is dangerous goods
#    Then click on Add route leg
#    Then enter org-country name in counrty field
#    Then enter org-city name in city field
#    Then enter des-country name in counrty field
#    Then enter des-city name in city field
#    And choose equipment number from the dropdown box
#    And Enter equipment quantity in the text field
#    And choose weight type in the dropdown box
#    And Enter weight in the text field
#    And choose Volume type in the dropdown box
#    And Enter Volume in the text field
#    And choose MOT type in the dropdown box
#    Then click on the Add Route Leg
#    Then click on check box of route leg
#    And Apply the route leg
#    Then click on compare button
#    And choose weight type in the dropdown box
#    Then click on compare button
#
#    Examples:
#      | ServiceType | message                          | ServiceType | customer            | currency | HS code | HazCode |
#      | FTL         | Delete rate margin successfully. | FTL         | Innovative Apparels | USD      | 1       | H201    |
#
##  @Carrier_Booking
##  Scenario Outline: The user should be able to booked carrier successfully.
##    And Click on Planning Button
##    And Scroll through menu to view Load option
##    And Click on manage load
##    And choose the equipment type
##    And enter the equipment number in equipment field
##    And Click on Equipment search button
##    And Click on equipment number for checking details
##    Then Click on the check box of assign carrier
##    And click on the assign carrier
##    And click on assign direct
##    Then choose carrier from choose carrier
##    Then click on assign carrier
##    And save the booking number
##    Then Click on Execution Menu
##    And Click on Bookings Button
##    And Click on Carrier Bookings Button
##    And check the carrier booking
##    Then Click on Execution Menu
##
##    And verify the "<message>"
##
##    Examples:
##      | message |
##      |         |
##
##  @Dispatch
##  Scenario Outline: The user should be able to click on filter and view the all details
##    Then Click on Execution Menu
##    Then click on dispatch
##    Then click on dispatch planning
##    Then enter the load country for dispatch
##    Then enter the load city for dispatch
##    Then enter the load site for dispatch
##    Then click on proceed button
##    Then click on filter
##    Then Mouse hover on Load site
##    Then Mousehover on all fields and click on carrier code and Mousehover on carrier
##    Then click on MOT and search by Mot
##    Then click on service type and then search with service type
##    Then click on booking confirmation number and give the booking confirmation number
##    Then click and mousehover transport status
##    Then click on shipment date dispatch
##    And Click on check box and then give latest ETD ,ETA ,ATD ,ATA
##
##
##    Examples:
##      | status            | message           |
##      | Approved Revision | Approved Revision |
##
##  @Intake
##  Scenario Outline: The user should be able to create Intake
##    Then Click on Execution Menu
##    Then click on dispatch
##    Then click on intake planning
##    And enter the load country for intake
##    And enter the load city for intake
##    And enter the load site for intake
##    Then click on proceed button
##    And click on filter
##
##    Examples:
##      | status            | message           |
##      | Approved Revision | Approved Revision |
##
##
##  @trips
##  Scenario Outline:The user should be able to view the trip details successfully
##    Then Click on Execution Menu
##    Then click on dispatch
##    Then click on trips
##    Then click on carrier and select carrier from the drop down
##    Then click on search
##
##    Examples:
##      | status            | message           |
##      | Approved Revision | Approved Revision |


#  @Carrierbookingstatus
#  Scenario Outline: The user should be able to change the trip status.
#    Then Click on Execution Menu
#    Then Click on Bookings Button
#    Then Click on Transportorders
##    Then click on filter
##    Then select Booking request from Transport Status
#    Then Click on expand page
##    Then Scroll the page
#    Then Expand the carrier booking dropdown
#    Then Click on the load hyperlink
#    Then Click on Transport status
#    Then Click on Trip Status
#    Then Then click on save button
#    Then Close trip status menu
#    Then Click on trip details edit
#    Then Enter Booking confirmation number
#
#    Examples:
#      | Booking confirmation number | message           |
#      | Bh9989                      | Approved Revision |

##
##  @Freightaudit
##  Scenario Outline:The user should be able to view the freight audit search and list successfully
##    Then click on Settlement menu
##    Then Click on freightaudit
##    Then click on importinvoice
##    And And import the auditfile
##
##    Examples:
##      | status            | message           |
##      | Approved Revision | Approved Revision |
##
#
  @Logout
  Scenario Outline: The user should be able to logout to the application successfully
    Then Click on Esspl logo
    And Click on logout

    Examples:
      | status            | message           |
      | Approved Revision | Approved Revision |
