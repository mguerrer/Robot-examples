# BIQ Test Automation
This project run Python/Robot test suites for regression. The way to use is the following:

## Installation
1- Install Python https://www.python.org/downloads/release/python-3918/
2- Install pip: <code>python.exe -m pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org pip</code>
3- Install libraries: <code>python3.9 -m pip install --user -r requirements.txt</code>

## Running tests
Tests will be executed on git root folder in any case.
### 1. Run sequential with robot framework executor
   In this execution method you will get a single sequential process (safest but slower).
   <pre><code>robot businessiq/TestSuite/027-AccountDetailsV2.robot</code></pre>

### 2. Run suite parallel using pabot
   This method is useful when you want to run many suites, e.g. in Jenkins pipeline or a local round.   In this execution method you will get --processes threads runing in each thread one suite and tests in sequential.
   <pre><code>pabot --processes 4 --verbose -d results businessiq/TestSuite/001-Login.robot</code></pre>
   Notes:

   * You can run test cases in parallel by adding --testlevelsplit option.  However, this method is reccomended only when you are sure that all tests are designed to support parallel execution.
   * Reccomended threads on local execution is 4 for safe execution.
   * You will need to add -d results when execute with pabot to get reports correctly in "results" folder.

## Developing tests
### Branch and merge strategy
Use the following branches to support new developments and run:
   * **UAT**: Tied to UAT pipeline on Jenkins that will run on every pushed change, only for run on Jenkins.
   * **DEV**: For dev updates integration.   
   * **master**: Synchronized with production code.

### Code structure
Readability is a very important attribute of any software code, specially if it needs long term maintenance and minimal documentation.   
The rules followed to write the code are:
   * Test suites and cases are written in robot files.
   * Test cases uses python keywords.
   * Python keywords are grouped in files according to major functionalities ("modules").

     - Uses keywords of **FrameworkKeywords.py** to handle web browser, provide test data in Excel and generate custom reports.

         - Uses locators that are independent of Selenium library to select web elements. Locators has the form <code>"method=value"</code>
         - Web interactions are written as <code>command( locator, value )</code>
     
     
### Naming locators 
This small guideline is just to suggest style ideas collected during BIQ Automation to make code readable when we replace hardcoded/repeated web elements locators by variables making web elements uniquely defined in code.

   *  ***Group and document:*** Every functionality will contain all the locators used by workflows.  This will include their own windows/forms, and probably locators of elements in other modules.   Make it clear for reader, by grouping (e.g. by page) and comment.
   *  ***Format***: Use lowercase words separated by _.  E.g.:

         <code> manage_portfolios_title = "xpath=//h2[text()='Manage Portfolios']"</code> 
   *  ***Inherit:*** As much as possible, do not create locators of other dependant modules, but include and use.
   *  ***Not too long***: When a module/functionality uses more than one page/form, you may want to try to add the breathcrumb to element to imply the page it belongs to.   This can finally attempt against readability.   Instead use no more than 20 characters, combined with rule ***Group and document***.
   *  ***Suggested***: Use 2 or 3 initial words to describe the functional meaning, and a last one that relates the type (tag or visual) of the element.  E.g. <code>yes_on_confirmation_panel_button</code>