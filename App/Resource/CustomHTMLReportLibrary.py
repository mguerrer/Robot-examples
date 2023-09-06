import os
import datetime
from robot.libraries.BuiltIn import BuiltIn

def create_report_directory(reportDirectory, suiteName):
    # This keyword creates the necessary folder structure for reporting

    dt_tme = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    SuiteReportFolderName = suiteName + "_" + dt_tme
    # dirPath = reportDirectory + "\\" + SuiteReportFolderName
    dirPath = os.path.join(reportDirectory, SuiteReportFolderName)

    # suiteResult = dirPath + "\\" + suiteName + ".html"
    suiteResult = os.path.join(dirPath, suiteName + ".html")

    directory = os.path.dirname(suiteResult)
    if not os.path.exists(directory):
        os.makedirs(directory)

    os.chdir(dirPath)
    os.mkdir("Details")
    os.mkdir("Screenshots")
    # DetailFolderPath = dirPath + "\\" + "Details"
    # DetailFolderPath = os.path.join(dirPath, "Details")
    # ScreenshotPath = dirPath + "\\" + "Screenshots"
    # ScreenshotPath = os.path.join(dirPath, "Screenshots")

    return SuiteReportFolderName, suiteResult


def generate_test_report_header(testReportpath, testName):
    # This keyword generates the report header in the test report html and returns the test report html path
    # testReportpath = testReportpath + "\\" + testName + ".html"
    # os.path.normpath()
    print( testReportpath )
    testReportpath = os.path.join(testReportpath, testName + ".html")
    print("--------------" + testReportpath)

    # Generate Header Content with heading columns
    header_content = """<html>
	<head>
	<title>""" + "BIQ Automation Result" + """</title>
	<style>
	table {
	color: #333;
	font-family: Helvetica, Arial, sans-serif;
	font-size: 14;
	width: 640px;
	border-collapse:
	collapse; border-spacing: 0;
	}

	td, th { border: 2px solid #CCC; height: 30px; }

	th {
	font-weight: bold;
	}

	td {
	background: #FFF8DC;
	text-align: center;
	}
	</style>

	</head>
	<body>
	<table style="width:100%" border="1px">
		<tr>
		<th bgcolor="#cacdd1"><font size="5">""" + "BIQ Automation Result" + """</font></th>
		</tr>
	</table>
	<table style="width:100%" border="1px">
		<tr>
		<th bgcolor="#e0e2e1">Test Name: """ + testName + """</th>
		<th bgcolor="#e0e2e1">Execution Start Time: """ + datetime.datetime.now().strftime('%d-%b-%y %I:%M %p') + """</th>
		<th bgcolor="#e0e2e1">Execution End Time:</th>
		</tr></table>
		<table style="width:100%" border="1px"><tr><th bgcolor="#e0e2e1">Step</th><th bgcolor="#e0e2e1">Expected Result</th><th bgcolor="#e0e2e1">Actual Result</th><th bgcolor="#e0e2e1">Status</th><th bgcolor="#e0e2e1">Screenshot</th></tr>"""

    report_file = open(testReportpath, "w")
    report_file.write(header_content)
    report_file.close()
    print( testReportpath )
    return testReportpath


def generate_suite_report_header(suiteResultPath, suiteName):
    # This keyword generates suite report header to the suite report

    header_content = """<html>
		<head>
		<title>""" + "BIQ Automation Result" + """</title>
		<style>
		table {
		color: #333;
		font-family: Helvetica, Arial, sans-serif;
		font-size: 14;
		width: 640px;
		border-collapse:
		collapse; border-spacing: 0;
		}

		td, th { border: 2px solid #CCC; height: 30px; }

		th {
		font-weight: bold;
		}

		td {
		background: #FFF8DC;
		text-align: center;
		}
		</style>

		</head>
		<body>
		<table style="width:100%" border="1px">
			<tr>
			<th bgcolor="#cacdd1"><font size="5">""" + "BIQ Automation Result" + """</font></th>
			</tr>
		</table>
		<table style="width:100%" border="1px">
			<tr>
			<th bgcolor="#e0e2e1">Test Suite: """ + suiteName + """</th>
			</tr>
		</table>

		<table style="width:100%" border="1px"><tr><th bgcolor="#e0e2e1">TestCaseID</th><th bgcolor="#e0e2e1">Test Description</th><th bgcolor="#e0e2e1">Status</th></tr>"""

    report_file = open(suiteResultPath, "w")
    report_file.write(header_content)
    report_file.close()

def log_execution_endtime_to_report_file(testReportpath):
    # This keyword writes the test execution end time and log file path to the report
    # Read in the file
    with open(testReportpath, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('Execution End Time:',
                                'Execution End Time: ' + datetime.datetime.now().strftime('%d-%b-%y %I:%M %p'))

    # Write the file out again
    with open(testReportpath, 'w') as file:
        file.write(filedata)

    # end html
    with open(testReportpath, 'a') as file:
        logtext = "</table></body></html>"
        file.write(logtext)

def write_result_to_TestReport(testResultPath, ScreenshotName, Step, ExpectedResult, ActualResult, Status):
    # This keyword appends the result of a step to the test html report
    screenshotPath = "../Screenshots/" + ScreenshotName
    rpt_fl = open(testResultPath, "a")
    if Status == "PASS" or Status == "PASS" or Status == "PASS" or Status == "pass":
        rpt_data = "<tr><td>" + Step + "</td><td>" + ExpectedResult + "</td><td>" + ActualResult + """</td><td><font color="#2eb82e"><b>PASSED</b></font></td>""" + """<td><a href=" """ + screenshotPath + """ ">Screenshot</a></td>"""
    elif Status == "FAIL" or Status == "FAIL" or Status == "FAIL" or Status == "fail":
        rpt_data = "<tr><td>" + Step + "</td><td>" + ExpectedResult + "</td><td>" + ActualResult + """</td><td><font color="#ff3300"><b>FAILED</b></font></td>""" + """<td><a href=" """ + screenshotPath + """ ">Screenshot</a></td>"""
    else:
        rpt_data = "<tr><td>" + Step + "</td><td>" + ExpectedResult + "</td><td>" + ActualResult + "</td><td><b>INFO</b></td>" + """<td><a href=" """ + screenshotPath + """ ">Screenshot</a></td>"""

    rpt_data += "</tr>"

    rpt_fl.write(rpt_data)
    rpt_fl.close()

def write_result_to_TestReport_Without_Screenshot(testResultPath, Step, ExpectedResult, ActualResult, Status):
    # This keyword appends the result of a step to the test html report
    # screenshotPath = "../Screenshots/" + ScreenshotName
    rpt_fl = open(testResultPath, "a")
    if Status == "PASS" or Status == "PASS" or Status == "PASS" or Status == "pass":
        rpt_data = "<tr><td>" + Step + "</td><td>" + ExpectedResult + "</td><td>" + ActualResult + """</td><td><font color="#2eb82e"><b>PASSED</b></font></td>""" + """<td></td>"""
    elif Status == "FAIL" or Status == "FAIL" or Status == "FAIL" or Status == "fail":
        rpt_data = "<tr><td>" + Step + "</td><td>" + ExpectedResult + "</td><td>" + ActualResult + """</td><td><font color="#ff3300"><b>FAILED</b></font></td>""" + """<td></td>"""
    else:
        rpt_data = "<tr><td>" + Step + "</td><td>" + ExpectedResult + "</td><td>" + ActualResult + "</td><td><b>INFO</b></td>" + """<td></td>"""

    rpt_data += "</tr>"

    rpt_fl.write(rpt_data)
    rpt_fl.close()

def write_result_to_SuiteReport(suiteReportPath, testReportPath, testcaseID, testcaseDescription, testStatus):
    # This keyword appends a test result to the test suite report
    suiteReportfile = open(suiteReportPath, "a")
    suite_folder = BuiltIn().get_variable_value("${suite_result_folder}")
    # Adds relative images for robot 
    testReportPath = suite_folder + "/Details/" + testcaseID + ".html"
    testReportPath = os.path.relpath( testReportPath, suite_folder)
    dquote = '"'
    testReportPath = dquote + testReportPath + dquote
   
    if testStatus == "PASS" or testStatus == "pass":
        reportData = "<tr><td><a href=" + testReportPath + ">" + testcaseID + "</a></td><td>" + testcaseDescription + """</td><td><font color="#2eb82e"><b>PASSED</b></font></td>"""
    elif testStatus == "FAIL" or testStatus == "fail":
        reportData = "<tr><td><a href=" + testReportPath + ">" + testcaseID + "</a></td><td>" + testcaseDescription + """</td><td><font color="#ff3300"><b>FAILED</b></font></td>"""
    else:
        reportData = "<tr><td><a href=" + testReportPath + ">" + testcaseID + "</a></td><td>" + testcaseDescription + """</td><td><b>PASSED</b></td>"""

    reportData += "</tr>"
    suiteReportfile.write(reportData)
    suiteReportfile.close()
