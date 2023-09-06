*** Settings ***
Library      ListenerLibrary
Test Teardown    Teardown Keyword


*** Test Cases ***
Moshes Example Passing Test
	Register End Test Listener    Allways
	Log  This is an example of a test that passed

Moshes Example Failing Test
	Register End Test Listener    Allways
	Fail  This is an example of a test that failed


*** Keywords ***
Allways
	Log  This line is always executed, ${TEST NAME}: ${TEST STATUS}
	# https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#automatic-variables
	IF  "${TEST STATUS}" == "FAIL"
		Another Keyword
	END

Another Keyword
	Log  This keyword only gets called by the listener when the test failed.

Teardown Keyword
	Log  The teardown is called after the Listener Keyword, ${TEST NAME}: ${TEST STATUS}
	IF  "${TEST STATUS}" == "FAIL"
		Yet Another Keyword
	END

Yet Another Keyword
	Log  This keyword only gets called by the teardown when the test failed.