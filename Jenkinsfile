pipeline {
    agent { label 'Linux' }

    stages {
        stage('Install') {
            steps {
                sh 'python3.9 -m pip install --user virtualenv'
                sh 'virtualenv uat'
                sh 'source uat/bin/activate'
                sh 'python3.9 -m pip install --user -r requirements.txt'
                sh 'python3.9 --version'
            }
        }
        stage('UAT group 1') { 
            steps {
                sh 'rm -rf UAT1'
                catchError {     // https://github.com/mkorpela/pabot           
                    //sh "pabot --processes 4 --verbose -d UAT1 --SuiteStatLevel 2 --pythonpath businessiq/Resource --nostatusrc   businessiq/TestFramework/LT-Suite1.robot businessiq/TestFramework/LT-Suite2.robot"
                    //sh "pabot --processes 4 --verbose -d UAT1 --pythonpath businessiq/Resource --nostatusrc  businessiq/TestSuite/001-Login.robot businessiq/TestSuite/002-SystemAdministrationPortfolio.robot businessiq/TestSuite/003-SystemAdministrationPolicy.robot businessiq/TestSuite/004-SystemAdministrationCreditApplication.robot businessiq/TestSuite/005-SystemAdministrationUserManagement.robot businessiq/TestSuite/009-ExpandedSearch.robot"
                    sh "pabot --processes 4 --verbose -d UAT1 --pythonpath businessiq/Resource --nostatusrc businessiq/TestSuite/001-Login.robot businessiq/TestSuite/014-DomesticReports.robot"
                }
            }
        }
        stage('UAT group 2') { 
            steps {
                sh 'rm -rf UAT2'
                catchError {
                    //sh "pabot --processes 4 --verbose -d UAT2 --SuiteStatLevel 2 --pythonpath businessiq/Resource --nostatusrc   businessiq/TestFramework/LT-Suite3.robot"
                    //sh "pabot --processes 4 --verbose -d UAT2 --pythonpath businessiq/Resource --nostatusrc   businessiq/TestSuite/01*.robot"
                    sh "pabot --processes 4 --verbose -d UAT2 --pythonpath businessiq/Resource --nostatusrc businessiq/TestSuite/002-SystemAdministrationPortfolio.robot businessiq/TestSuite/015-InternationalSearchAndPullReports.robot"
                }
            }
        }
        stage('Publish') { 
            steps {
                catchError {
                    sh 'rebot --output output.xml UAT1/output.xml UAT2/output.xml'
                }                     
                robot otherFiles: 'UAT1/*/Screenshots/*.*,UAT1/**/*.html,UAT2/*/Screenshots/*.*,UAT2/**/*.html', outputPath: '.', logFileName: 'log.html', outputFileName: 'output.xml', reportFileName: 'report.html', passThreshold: 100, unstableThreshold: 75.0
                archiveArtifacts artifacts: 'UAT1/**/*.*,UAT1/*/Screenshots/*.*,UAT2/**/*.*,UAT2/*/Screenshots/*.*', allowEmptyArchive: true, onlyIfSuccessful: false 
                sh 'echo "BUILD="$BUILD_NUMBER;echo "DIR="$PWD;ls -laR'
            }
        }
    }
}