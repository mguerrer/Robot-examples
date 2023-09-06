*** Settings ***
Library  SeleniumLibrary
Documentation  Home web application page object.

*** Variables ***
# ${home.account_list_name_1}                                                                                                                                                               id=saveEditAccountListName
# ${home.account_list_name_2}                                                                                                                                                               id=account_list_description
# ${home.account_list_name_3}                                                                                                                                                               name=sharing
# ${home.account_list_name_4}                                                                                                                                                               name=sharing
# ${home.account_list_name_5}                                                                                                                                                               name=sharing
# ${home.account_list_name_value}                                                                                                                                                           P
# ${home.account_list_name_value}                                                                                                                                                           PV
# ${home.account_list_name_value}                                                                                                                                                           PE
# ${home.add_a_note_1}                                                                                                                                                                      id=addFilterNoteLink
# ${home.add_a_note_2}                                                                                                                                                                      id=addAccountListNoteLink
# ${home.add_note}                                                                                                                                                                          id=manage_notes_panel_add
# ${home.add_owner_1}                                                                                                                                                                       css=a.add_owner
# ${home.add_owner_2}                                                                                                                                                                       css=a.add_bci_owner
# ${home.address_1}                                                                                                                                                                         id=address_0
# ${home.address_2}                                                                                                                                                                         id=address_1
# ${home.address_3}                                                                                                                                                                         id=contact_address
# ${home.address_4}                                                                                                                                                                         name=address
# ${home.address_5}                                                                                                                                                                         name=address
# ${home.age_1}                                                                                                                                                                             id=age_0
# ${home.age_2}                                                                                                                                                                             id=age_1
# ${home.alerts}                                                                                                                                                                            css=a[href='/App/secure/menuAction?level1Key=Alerts']
# ${home.apply_all_filters_to_the_list_1}                                                                                                                                                   name=applyFilterOption
# ${home.apply_all_filters_to_the_list_2}                                                                                                                                                   name=applyFilterOption
# ${home.apply_all_filters_to_the_list_3}                                                                                                                                                   name=refreshOption
# ${home.apply_all_filters_to_the_list_4}                                                                                                                                                   name=refreshOption
# ${home.apply_all_filters_to_the_list_value}                                                                                                                                               and
# ${home.apply_all_filters_to_the_list_value}                                                                                                                                               or
# ${home.apply_all_filters_to_the_list_value}                                                                                                                                               manual
# ${home.apply_all_filters_to_the_list_value}                                                                                                                                               automatic
# ${home.assigned_to_1}                                                                                                                                                                     id=taskAssignedBy
# ${home.assigned_to_2}                                                                                                                                                                     id=taskAssignedByName
# ${home.bin}                                                                                                                                                                               id=bin
# ${home.birth_date_1}                                                                                                                                                                      name=year_of_birth
# ${home.birth_date_2}                                                                                                                                                                      name=year_of_birth
# ${home.business_name}                                                                                                                                                                     id=business_name
# ${home.businessiq_v2}                                                                                                                                                                     css=a.biqv2
# ${home.cancel_1}                                                                                                                                                                          css=#task_panel div:nth-of-type(3) div.button_group button:nth-of-type(3)
# ${home.cancel_10}                                                                                                                                                                         css=#deleteScorecard div:nth-of-type(2) div:nth-of-type(2) span:nth-of-type(2) button.standard_button.close
# ${home.cancel_11}                                                                                                                                                                         id=cancel_contact_us
# ${home.cancel_12}                                                                                                                                                                         css=button.standard_button.close_bci
# ${home.cancel_2}                                                                                                                                                                          id=tasklist_panel_cancel
# ${home.cancel_3}                                                                                                                                                                          css=#broadcast_panel div:nth-of-type(3) div.button_group button:nth-of-type(2)
# ${home.cancel_4}                                                                                                                                                                          css=#business_owner_panel div:nth-of-type(2) table:nth-of-type(2) tbody tr td:nth-of-type(2) div.button_group button:nth-of-type(2)
# ${home.cancel_5}                                                                                                                                                                          css=#formFooter table.stretch tbody tr td:nth-of-type(2) div.button_group button:nth-of-type(2)
# ${home.cancel_6}                                                                                                                                                                          css=#formFooter table.stretch tbody tr td:nth-of-type(2) div.button_group button:nth-of-type(2)
# ${home.cancel_7}                                                                                                                                                                          id=noteCancelBtn
# ${home.cancel_8}                                                                                                                                                                          id=manage_notes_panel_cancel
# ${home.cancel_9}                                                                                                                                                                          css=#editScorecard div:nth-of-type(2) div:nth-of-type(4) button:nth-of-type(2)
# ${home.cant_make_the_changes_you_want_1}                                                                                                                                                  id=scorecardName
# ${home.cant_make_the_changes_you_want_2}                                                                                                                                                  id=scorecardDescription
# ${home.category}                                                                                                                                                                          id=taskCategory
# ${home.change_owner_1}                                                                                                                                                                    css=#sharing-box-div table.sharing-box tbody tr td:nth-of-type(10) a.change_owner.change_owner_related
# ${home.change_owner_2}                                                                                                                                                                    css=#sharing-box-div table.sharing-box tbody tr td:nth-of-type(10) a.change_owner.change_owner_related
# ${home.change_subscriber}                                                                                                                                                                 id=change_subscriber
# ${home.check_box_to_acknowledge_you_have}                                                                                                                                                 id=isBlended_0
# ${home.check_to_signify_agreement_to_these}                                                                                                                                               id=insurance_underwriter
# ${home.city_1}                                                                                                                                                                            id=city_0
# ${home.city_2}                                                                                                                                                                            id=city_1
# ${home.city_3}                                                                                                                                                                            id=contact_city
# ${home.city_4}                                                                                                                                                                            name=city
# ${home.city_5}                                                                                                                                                                            name=city
# ${home.city_6}                                                                                                                                                                            id=city
# ${home.clear_fields}                                                                                                                                                                      id=clear_quicksearch
# ${home.click_here_for_expanded_search}                                                                                                                                                    id=expandedSearchLinkDynamic
# ${home.close}                                                                                                                                                                             css=a.container-close
# ${home.combusinessiqdashboard_}                                                                                                                                                           css=#promo_box a
# ${home.comments}                                                                                                                                                                          id=broadcastComments
# ${home.company}                                                                                                                                                                           id=companyName
# ${home.company_name}                                                                                                                                                                      id=contact_company_name
# ${home.contact_us_1}                                                                                                                                                                      id=contact
# ${home.contact_us_2}                                                                                                                                                                      id=contact
# ${home.contact_us_3}                                                                                                                                                                      id=contact_us
# ${home.create_a_task_1}                                                                                                                                                                   id=create_a_task2
# ${home.create_a_task_2}                                                                                                                                                                   id=create_a_task
# ${home.create_filter}                                                                                                                                                                     css=button.standard_button.create
# ${home.create_new_account_list}                                                                                                                                                           id=createNewButton
# ${home.credit_application}                                                                                                                                                                css=a[href='/App/secure/secondLevelMenuAction?level2Key=creditApplication']
# ${home.credit_application_status_last_90_days}                                                                                                                                            id=yui-pg0-0-rpp
# ${home.datebusinesstrigger_typeprioritydatebusinesstrigger_typepriorityno_alerts_found_1}                                                                                                 id=yui-pg1-0-rpp
# ${home.datebusinesstrigger_typeprioritydatebusinesstrigger_typepriorityno_alerts_found_2}                                                                                                 id=yui-pg3-0-rpp
# ${home.decisioning}                                                                                                                                                                       css=#top_tab_Decisioning a.centered
# ${home.decisioniq}                                                                                                                                                                        css=a[href='/App/secure/secondLevelMenuAction?level2Key=decisionIQ']
# ${home.delete_1}                                                                                                                                                                          id=delete_task_button
# ${home.delete_2}                                                                                                                                                                          id=delete_tasks_button
# ${home.delete_3}                                                                                                                                                                          css=button.standard_button.delete
# ${home.delete_4}                                                                                                                                                                          id=delScardCnfrm
# ${home.delete_note}                                                                                                                                                                       id=noteDeleteBtn
# ${home.delete_owner_1}                                                                                                                                                                    css=a.delete_owner.disabled
# ${home.delete_owner_2}                                                                                                                                                                    css=a.delete_bci_owner.disabled
# ${home.delete_selected_account_lists}                                                                                                                                                     id=deleteSelectedButton
# ${home.delete_selected_note}                                                                                                                                                              id=manage_notes_panel_delete
# ${home.description}                                                                                                                                                                       id=filter_description
# ${home.details}                                                                                                                                                                           id=taskDescription
# ${home.do_not_show_this_message_again}                                                                                                                                                    id=chkBoxDoNotShowMultiAcctsMessageAgain
# ${home.drivers_license_1}                                                                                                                                                                 id=drivers_license_0
# ${home.drivers_license_2}                                                                                                                                                                 id=drivers_license_1
# ${home.drivers_license_3}                                                                                                                                                                 name=drivers_license
# ${home.drivers_license_4}                                                                                                                                                                 name=drivers_license
# ${home.due_date}                                                                                                                                                                          id=taskDueDate
# ${home.due_date}                                                                                                                                                                          css=a[title='Click to sort descending']
# ${home.email_1}                                                                                                                                                                           id=broadcastEmail
# ${home.email_2}                                                                                                                                                                           id=userEmail
# ${home.email_3}                                                                                                                                                                           id=contact_email
# ${home.expanded_search_1}                                                                                                                                                                 css=a[href='/App/secure/menuAction?level1Key=ExpandedSearch']
# ${home.expanded_search_2}                                                                                                                                                                 id=expandedSearchLink
# ${home.experian}                                                                                                                                                                          css=#branding div:nth-of-type(1) a
# ${home.export_1}                                                                                                                                                                          id=export_tasks_button
# ${home.export_2}                                                                                                                                                                          id=notesview_exportNotesLink
# ${home.first_name_1}                                                                                                                                                                      id=firstName
# ${home.first_name_2}                                                                                                                                                                      id=first_name_0
# ${home.first_name_3}                                                                                                                                                                      id=first_name_1
# ${home.first_name_4}                                                                                                                                                                      id=contact_first_name
# ${home.first_name_5}                                                                                                                                                                      name=first_name
# ${home.first_name_6}                                                                                                                                                                      name=first_name
# ${home.fraud}                                                                                                                                                                             css=#top_tab_Fraud a.centered
# ${home.generation_code_1}                                                                                                                                                                 id=generation_code_0
# ${home.generation_code_1}                                                                                                                                                                 id=generation_code
# ${home.generation_code_2}                                                                                                                                                                 id=generation_code_1
# ${home.generation_code_2}                                                                                                                                                                 id=generation_code
# ${home.home}                                                                                                                                                                              css=a[href='/App/secure/menuAction?level1Key=Home']
# ${home.last_name_1}                                                                                                                                                                       id=broadcastLName
# ${home.last_name_1}                                                                                                                                                                       id=last_name_0
# ${home.last_name_2}                                                                                                                                                                       id=lastName
# ${home.last_name_2}                                                                                                                                                                       id=last_name_1
# ${home.last_name_3}                                                                                                                                                                       id=contact_last_name
# ${home.last_name_3}                                                                                                                                                                       name=last_name
# ${home.last_name_4}                                                                                                                                                                       name=last_name
# ${home.learn_more_about_alerts}                                                                                                                                                           css=a[href='http://www.experian.com/enterprise-services/video/BusinessIQ-Alerts-Demo/player.html']
# ${home.learn_more_about_collections}                                                                                                                                                      css=a[href='http://www.experian.com/enterprise-services/video/business-collections-demo/player.html']
# ${home.legal_terms_conditions}                                                                                                                                                            id=legal
# ${home.link_to_account_1}                                                                                                                                                                 id=find_in_task_pfm_input
# ${home.link_to_account_2}                                                                                                                                                                 id=find_in_note_pfm_input
# ${home.manage_notes_1}                                                                                                                                                                    id=viewFilterNotesLink
# ${home.manage_notes_2}                                                                                                                                                                    id=viewAccountListNotesLink
# ${home.manage_tasks}                                                                                                                                                                      id=open_tasklist2
# ${home.message}                                                                                                                                                                           id=contact_message
# ${home.middle_initial_1}                                                                                                                                                                  id=middle_initial_0
# ${home.middle_initial_2}                                                                                                                                                                  id=middle_initial_1
# ${home.middle_initial_3}                                                                                                                                                                  name=middle_initial
# ${home.middle_initial_4}                                                                                                                                                                  name=middle_initial
# ${home.my_settings}                                                                                                                                                                       css=a[href='/App/secure/getInitialSettingData']
# ${home.no_1}                                                                                                                                                                              id=note_delete_cancel_btn
# ${home.no_2}                                                                                                                                                                              id=close_panel
# ${home.note}                                                                                                                                                                              id=noteContent
# ${home.ok_1}                                                                                                                                                                              css=button.action_button.ok
# ${home.ok_2}                                                                                                                                                                              css=button.action_button.ok_bci
# ${home.page_loaded_text}                                                                                                                                                                  Experian and the Experian marks used herein are trademarks or registered trademarks of Experian Information Solutions, Inc
# ${home.page_url}                                                                                                                                                                          /App/dashboard/home.action
# ${home.percent_complete}                                                                                                                                                                  id=taskPercentComplete
# ${home.phone_area_code}                                                                                                                                                                   id=contact_phone_area
# ${home.phone_number_1}                                                                                                                                                                    id=broadcastPhone
# ${home.phone_number_2}                                                                                                                                                                    id=userPhone
# ${home.phone_number_3}                                                                                                                                                                    name=zip_bci
# ${home.phone_number_4}                                                                                                                                                                    name=phone
# ${home.phone_number_5}                                                                                                                                                                    name=zip_bci
# ${home.phone_number_6}                                                                                                                                                                    name=phone
# ${home.phone_prefix}                                                                                                                                                                      id=contact_phone_prefix
# ${home.phone_suffix}                                                                                                                                                                      id=contact_phone_suffix
# ${home.portfolio}                                                                                                                                                                         css=a[href='/App/secure/menuAction?level1Key=Portfolio']
# ${home.print_1}                                                                                                                                                                           id=print_tasks_button
# ${home.print_2}                                                                                                                                                                           id=print_snapshot_btn
# ${home.print_3}                                                                                                                                                                           id=print_snapshot_btn
# ${home.print_4}                                                                                                                                                                           id=notesview_printNotesLink
# ${home.print_5}                                                                                                                                                                           id=printPRGraph
# ${home.print_6}                                                                                                                                                                           id=printFSRGraph
# ${home.print_7}                                                                                                                                                                           id=printSOTGraph
# ${home.print_fcra_agreement}                                                                                                                                                              css=a[href='/App/search/printFCRA']
# ${home.print_insurance_certificate}                                                                                                                                                       css=a[href='/App/pages/search/common/PrintInsuranceUnderwrite.jsp']
# ${home.priority}                                                                                                                                                                          id=taskPriority
# ${home.privacy_policy}                                                                                                                                                                    id=privacy
# ${home.private_1}                                                                                                                                                                         name=taskSharing
# ${home.private_2}                                                                                                                                                                         name=sharing
# ${home.private_value}                                                                                                                                                                     P
# ${home.private_value}                                                                                                                                                                     P
# ${home.public_view_edit}                                                                                                                                                                  name=sharing
# ${home.public_view_edit_value}                                                                                                                                                            PE
# ${home.public_view_only}                                                                                                                                                                  name=sharing
# ${home.public_view_only_value}                                                                                                                                                            PV
# ${home.pull_credit_reports}                                                                                                                                                               css=a[href='http://www.experian.com/enterprise-services/video/BusinessIQ-Demo/player.html']
# ${home.report_manager}                                                                                                                                                                    css=a[href='/App/secure/menuAction?level1Key=ReportManager']
# ${home.request_a_customized_scorecard}                                                                                                                                                    css=a[href='mailto:bizappsinquiries@experian.com']
# ${home.reset}                                                                                                                                                                             id=ResetScorecard
# ${home.resources}                                                                                                                                                                         css=a[href='/App/secure/menuAction?level1Key=Resources']
# ${home.save_1}                                                                                                                                                                            css=#formFooter table.stretch tbody tr td:nth-of-type(2) div.button_group button:nth-of-type(1)
# ${home.save_2}                                                                                                                                                                            css=#formFooter table.stretch tbody tr td:nth-of-type(2) div.button_group button:nth-of-type(1)
# ${home.save_3}                                                                                                                                                                            id=noteSaveBtn
# ${home.save_4}                                                                                                                                                                            id=saveScorecard
# ${home.save_close}                                                                                                                                                                        id=save_task_button
# ${home.search_1}                                                                                                                                                                          id=notesSearchBtn
# ${home.search_2}                                                                                                                                                                          id=searchAcctInPortfolio
# ${home.search_3}                                                                                                                                                                          id=expanded_search_button
# ${home.sharing}                                                                                                                                                                           name=taskSharing
# ${home.sharing_value}                                                                                                                                                                     W
# ${home.sign_off}                                                                                                                                                                          id=logout
# ${home.social_security_no__1}                                                                                                                                                             id=social_security_number_0
# ${home.social_security_no__2}                                                                                                                                                             id=social_security_number_1
# ${home.social_security_no__3}                                                                                                                                                             name=social_security_number
# ${home.social_security_no__4}                                                                                                                                                             name=social_security_number
# ${home.start_date}                                                                                                                                                                        id=taskStartDate
# ${home.state_1}                                                                                                                                                                           id=state_0
# ${home.state_2}                                                                                                                                                                           id=state_1
# ${home.state_3}                                                                                                                                                                           id=contact_state
# ${home.state_4}                                                                                                                                                                           id=state_1
# ${home.state_5}                                                                                                                                                                           id=state_1
# ${home.state_6}                                                                                                                                                                           id=state_1
# ${home.state_7}                                                                                                                                                                           id=state_1
# ${home.state_8}                                                                                                                                                                           id=state
# ${home.status}                                                                                                                                                                            id=taskStatus
# ${home.submit_1}                                                                                                                                                                          id=submit_broadcast_button
# ${home.submit_2}                                                                                                                                                                          id=submit_contact_us
# ${home.system_administration}                                                                                                                                                             css=a[href='/App/secure/menuAction?level1Key=SysAdmin']
# ${home.systembroadcast2}                                                                                                                                                                  css=a[href='https://biq-jboss-eap-uat.internal.uat.ascendbis.us.coaas.net/App/resources/v2/dashboard']
# ${home.task}                                                                                                                                                                              css=a[title='Click to sort ascending']
# ${home.task_name_1}                                                                                                                                                                       id=taskID
# ${home.task_name_2}                                                                                                                                                                       id=taskName
# ${home.telephone_1}                                                                                                                                                                       id=qs_phone_1
# ${home.telephone_2}                                                                                                                                                                       id=qs_phone_2
# ${home.test_awstest_aws_again}                                                                                                                                                            css=a.promoLink
# ${home.test_filter_set}                                                                                                                                                                   css=button.test.standard_button
# ${home.to_1}                                                                                                                                                                              name=accountDataType
# ${home.to_2}                                                                                                                                                                              name=accountVariable
# ${home.to_3}                                                                                                                                                                              name=accountOperator
# ${home.to_4}                                                                                                                                                                              name=filterDropDownValue
# ${home.to_5}                                                                                                                                                                              name=filterValue
# ${home.to_6}                                                                                                                                                                              name=filterValueFrom
# ${home.to_7}                                                                                                                                                                              name=filterValueTo
# ${home.view_a_user_guide}                                                                                                                                                                 css=a[href='/App/rsrc/userguide']
# ${home.view_all_1}                                                                                                                                                                        css=a[href='/App/ams/AlertHome?']
# ${home.view_all_2}                                                                                                                                                                        css=a[href='/App/ams/showIntlAlerts?']
# ${home.view_all_3}                                                                                                                                                                        css=a[href='/App/credec/caps/inProgress/inProgressTab?']
# ${home.year_of_birth_1}                                                                                                                                                                   id=year_of_birth_0
# ${home.year_of_birth_2}                                                                                                                                                                   id=year_of_birth_1
# ${home.yes_1}                                                                                                                                                                             id=note_delete_cfm_btn
# ${home.yes_2}                                                                                                                                                                             id=proceed_view_report
# ${home.zip_4_1}                                                                                                                                                                           id=zip_0
# ${home.zip_4_2}                                                                                                                                                                           id=zip_1
# ${home.zip_4_3}                                                                                                                                                                           id=zip
# ${home.zip_code}                                                                                                                                                                          id=contact_zip

*** Keywords ***
# Click .Combusinessiqdashboard Link
#     [Documentation]  Click on .Combusinessiqdashboard Link.
#     Click Link  ${home.combusinessiqdashboard_}

# Click Add A Note 1 Link
#     [Documentation]  Click on Add A Note Link.
#     Click Link  ${home.add_a_note_1}

# Click Add A Note 2 Link
#     [Documentation]  Click on Add A Note Link.
#     Click Link  ${home.add_a_note_2}

# Click Add Note Button
#     [Documentation]  Click on Add Note Button.
#     Click Button  ${home.add_note}

# Click Add Owner 1 Link
#     [Documentation]  Click on Add Owner Link.
#     Click Link  ${home.add_owner_1}

# Click Add Owner 2 Link
#     [Documentation]  Click on Add Owner Link.
#     Click Link  ${home.add_owner_2}

# Click Alerts Link
#     [Documentation]  Click on Alerts Link.
#     Click Link  ${home.alerts}

# Click Businessiq V2 Link
#     [Documentation]  Click on Businessiq V2 Link.
#     Click Link  ${home.businessiq_v2}

# Click Cancel 1 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_1}

# Click Cancel 10 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_10}

# Click Cancel 11 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_11}

# Click Cancel 12 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_12}

# Click Cancel 2 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_2}

# Click Cancel 3 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_3}

# Click Cancel 4 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_4}

# Click Cancel 5 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_5}

# Click Cancel 6 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_6}

# Click Cancel 7 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_7}

# Click Cancel 8 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_8}

# Click Cancel 9 Button
#     [Documentation]  Click on Cancel Button.
#     Click Button  ${home.cancel_9}

# Click Change Owner 1 Link
#     [Documentation]  Click on Change Owner Link.
#     Click Link  ${home.change_owner_1}

# Click Change Owner 2 Link
#     [Documentation]  Click on Change Owner Link.
#     Click Link  ${home.change_owner_2}

# Click Change Subscriber Link
#     [Documentation]  Click on Change Subscriber Link.
#     Click Link  ${home.change_subscriber}

# Click Clear Fields Button
#     [Documentation]  Click on Clear Fields Button.
#     Click Button  ${home.clear_fields}

# Click Click Here For Expanded Search Link
#     [Documentation]  Click on Click Here For Expanded Search There Were No Quicksearch Suggestions Link.
#     Click Link  ${home.click_here_for_expanded_search}

# Click Close Link
#     [Documentation]  Click on Close Link.
#     Click Link    ${home.close}

# Click Contact Us 1 Link
#     [Documentation]  Click on Contact Us Link.
#     Click Link  ${home.contact_us_1}

# Click Contact Us 2 Link
#     [Documentation]  Click on Contact Us Link.
#     Click Link  ${home.contact_us_2}

# Click Contact Us 3 Link
#     [Documentation]  Click on Contact Us Link.
#     Click Link  ${home.contact_us_3}

# Click Create A Task 1 Link
#     [Documentation]  Click on Create A Task Link.
#     Click Button  ${home.create_a_task_1}

# Click Create A Task 2 Link
#     [Documentation]  Click on Create A Task Link.
#     Click Link  ${home.create_a_task_2}

# Click Create Filter Button
#     [Documentation]  Click on Create Filter Button.
#     Click Button  ${home.create_filter}

# Click Create New Account List Button
#     [Documentation]  Click on Create New Account List Button.
#     Click Button  ${home.create_new_account_list}

# Click Credit Application Link
#     [Documentation]  Click on Credit Application Link.
#     Click Link  ${home.credit_application}

# Click Decisioning Link
#     [Documentation]  Click on Decisioning Link.
#     Click Link  ${home.decisioning}

# Click Decisioniq Link
#     [Documentation]  Click on Decisioniq Link.
#     Click Link  ${home.decisioniq}

# Click Delete 1 Button
#     [Documentation]  Click on Delete Button.
#     Click Button  ${home.delete_1}

# Click Delete 2 Button
#     [Documentation]  Click on Delete Button.
#     Click Button  ${home.delete_2}

# Click Delete 3 Button
#     [Documentation]  Click on Delete Button.
#     Click Button  ${home.delete_3}

# Click Delete 4 Button
#     [Documentation]  Click on Delete Button.
#     Click Button  ${home.delete_4}

# Click Delete Note Button
#     [Documentation]  Click on Delete Note Button.
#     Click Button  ${home.delete_note}

# Click Delete Owner 1 Link
#     [Documentation]  Click on Delete Owner Link.
#     Click Link  ${home.delete_owner_1}

# Click Delete Owner 2 Link
#     [Documentation]  Click on Delete Owner Link.
#     Click Link  ${home.delete_owner_2}

# Click Delete Selected Account Lists Button
#     [Documentation]  Click on Delete Selected Account Lists Button.
#     Click Button  ${home.delete_selected_account_lists}

# Click Delete Selected Note Button
#     [Documentation]  Click on Delete Selected Note Button.
#     Click Button  ${home.delete_selected_note}

# Click Due Date Link
#     [Documentation]  Click on Due Date Link.
#     Click Link  ${home.due_date}

# Click Expanded Search 1 Link
#     [Documentation]  Click on Expanded Search Link.
#     Click Link  ${home.expanded_search_1}

# Click Expanded Search 2 Link
#     [Documentation]  Click on Expanded Search Link.
#     Click Link  ${home.expanded_search_2}

# Click Experian Link
#     [Documentation]  Click on Experian Link.
#     Click Link  ${home.experian}

# Click Export 1 Button
#     [Documentation]  Click on Export Button.
#     Click Link  ${home.export_1}

# Click Export 2 Button
#     [Documentation]  Click on Export Button.
#     Click Button  ${home.export_2}

# Click Fraud Link
#     [Documentation]  Click on Fraud Link.
#     Click Link  ${home.fraud}

# Click Home Link
#     [Documentation]  Click on Home Link.
#     Click Link  ${home.home}

# Click Learn More About Alerts Link
#     [Documentation]  Click on Learn More About Alerts Link.
#     Click Link  ${home.learn_more_about_alerts}

# Click Learn More About Collections Link
#     [Documentation]  Click on Learn More About Collections Link.
#     Click Link  ${home.learn_more_about_collections}

# Click Legal Terms Conditions Link
#     [Documentation]  Click on Legal Terms Conditions Link.
#     Click Link  ${home.legal_terms_conditions}

# Click Manage Notes 1 Link
#     [Documentation]  Click on Manage Notes Link.
#     Click Link  ${home.manage_notes_1}

# Click Manage Notes 2 Link
#     [Documentation]  Click on Manage Notes Link.
#     Click Link  ${home.manage_notes_2}

# Click Manage Tasks Link
#     [Documentation]  Click on Manage Tasks Link.
#     Click Link  ${home.manage_tasks}

# Click My Settings Link
#     [Documentation]  Click on My Settings Link.
#     Click Link  ${home.my_settings}

# Click No 1 Button
#     [Documentation]  Click on No Button.
#     Click Button  ${home.no_1}

# Click No 2 Button
#     [Documentation]  Click on No Button.
#     Click Button  ${home.no_2}

# Click Ok 1 Button
#     [Documentation]  Click on Ok Button.
#     Click Button  ${home.ok_1}

# Click Ok 2 Button
#     [Documentation]  Click on Ok Button.
#     Click Button  ${home.ok_2}

# Click Portfolio Link
#     [Documentation]  Click on Portfolio Link.
#     Click Link  ${home.portfolio}

# Click Print 1 Button
#     [Documentation]  Click on Print Button.
#     Click Link  ${home.print_1}

# Click Print 2 Button
#     [Documentation]  Click on Print Button.
#     Click Button  ${home.print_2}

# Click Print 3 Button
#     [Documentation]  Click on Print Button.
#     Click Button  ${home.print_3}

# Click Print 4 Button
#     [Documentation]  Click on Print Button.
#     Click Button  ${home.print_4}

# Click Print 5 Button
#     [Documentation]  Click on Print Button.
#     Click Button  ${home.print_5}

# Click Print 6 Button
#     [Documentation]  Click on Print Button.
#     Click Button  ${home.print_6}

# Click Print 7 Button
#     [Documentation]  Click on Print Button.
#     Click Button  ${home.print_7}

# Click Print Fcra Agreement Link
#     [Documentation]  Click on Print Fcra Agreement Link.
#     Click Link  ${home.print_fcra_agreement}

# Click Print Insurance Certificate Link
#     [Documentation]  Click on Print Insurance Certificate Link.
#     Click Link  ${home.print_insurance_certificate}

# Click Privacy Policy Link
#     [Documentation]  Click on Privacy Policy Link.
#     Click Link  ${home.privacy_policy}

# Click Pull Credit Reports Link
#     [Documentation]  Click on Pull Credit Reports Link.
#     Click Link  ${home.pull_credit_reports}

# Click Report Manager Link
#     [Documentation]  Click on Report Manager Link.
#     Click Link  ${home.report_manager}

# Click Request A Customized Scorecard Link
#     [Documentation]  Click on Request A Customized Scorecard Link.
#     Click Link  ${home.request_a_customized_scorecard}

# Click Reset Button
#     [Documentation]  Click on Reset Button.
#     Click Button  ${home.reset}

# Click Resources Link
#     [Documentation]  Click on Resources Link.
#     Click Link  ${home.resources}

# Click Save 1 Button
#     [Documentation]  Click on Save Button.
#     Click Button  ${home.save_1}

# Click Save 2 Button
#     [Documentation]  Click on Save Button.
#     Click Button  ${home.save_2}

# Click Save 3 Button
#     [Documentation]  Click on Save Button.
#     Click Button  ${home.save_3}

# Click Save 4 Button
#     [Documentation]  Click on Save Button.
#     Click Button  ${home.save_4}

# Click Save Close Button
#     [Documentation]  Click on Save Close Button.
#     Click Button  ${home.save_close}

# Click Search 1 Button
#     [Documentation]  Click on Search Button.
#     Click Button  ${home.search_1}

# Click Search 2 Button
#     [Documentation]  Click on Search Button.
#     Click Button  ${home.search_2}

# Click Search 3 Button
#     [Documentation]  Click on Search Button.
#     Click Button  ${home.search_3}

# Click Sign Off Link
#     [Documentation]  Click on Sign Off Link.
#     Click Link  ${home.sign_off}

# Click Submit 1 Button
#     [Documentation]  Click on Submit Button.
#     Click Button  ${home.submit_1}

# Click Submit 2 Button
#     [Documentation]  Click on Submit Button.
#     Click Button  ${home.submit_2}

# Click System Administration Link
#     [Documentation]  Click on System Administration Link.
#     Click Link  ${home.system_administration}

# Click Systembroadcast2 Link
#     [Documentation]  Click on Systembroadcast2 Link.
#     Click Link  ${home.systembroadcast2}

# Click Task Link
#     [Documentation]  Click on Task Link.
#     Click Link  ${home.task}

# Click Test Awstest Aws Again Link
#     [Documentation]  Click on Test Awstest Aws Again Link.
#     Click Link  ${home.test_awstest_aws_again}

# Click Test Filter Set Button
#     [Documentation]  Click on Test Filter Set Button.
#     Click Button  ${home.test_filter_set}

# Click View A User Guide Link
#     [Documentation]  Click on View A User Guide Link.
#     Click Link  ${home.view_a_user_guide}

# Click View All 1 Link
#     [Documentation]  Click on View All Link.
#     Click Link  ${home.view_all_1}

# Click View All 2 Link
#     [Documentation]  Click on View All Link.
#     Click Link  ${home.view_all_2}

# Click View All 3 Link
#     [Documentation]  Click on View All Link.
#     Click Link  ${home.view_all_3}

# Click Yes 1 Button
#     [Documentation]  Click on Yes Button.
#     Click Button  ${home.yes_1}

# Click Yes 2 Button
#     [Documentation]  Click on Yes Button.
#     Click Button  ${home.yes_2}

# Set Account List Name 1 Textarea Field
#     [Arguments]  ${account_list_name_1_value}=value
#     [Documentation]  Set value to Account List Name Textarea field.
#     Input Text  ${home.account_list_name_1}  ${account_list_name_1_value}

# Set Account List Name 2 Textarea Field
#     [Arguments]  ${account_list_name_2_value}=value
#     [Documentation]  Set value to Account List Name Textarea field.
#     Input Text  ${home.account_list_name_2}  ${account_list_name_2_value}

Verify Page Loaded
    [Documentation]  Verify that the page loaded completely.
    Wait Until Page Contains  Welcome to BusinessIQ!

