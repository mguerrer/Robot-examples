# Environment parameters
env_name = "uat"  #  Default.   Can be also be dev or stage.
biq_url = {
    "dev": "https://biq-jboss-eap-dev.internal.dev.ascendbis.us.coaas.net/BusinessIQ/",
    "uat": "https://stg-gateway.secure.experian.com/BusinessIQ/"
}
database = {
    "dev": "pegsdb1",
    "uat": "pegsdb1"
}
hostname = {
    "dev": "localhost",
    "uat": "localhost"
}
port = {
    "dev": "60000",
    "uat": "60000"
}
dbuserid = {
    "dev": "pegetl",
    "uat": "pegetl"    
}
dbuserpwd = {
    "dev": "experian123",
    "uat": "experian123"
}
schema = {
    "dev": "BIZ001",
    "uat": "BIZ001"
}

# Web driver settings
wait_time_subcode_portfolio_v2 = 5
wait_time_my_settings_v2 = 30
wait_time_scoring_model_Report_type = 10
retry_times = 5 # Default retry for framework keywords
V2_portfolio_tab_wait = 15
explicit_timeout_in_seconds:float = 30.0
implicit_timeout_in_seconds:float = 10.0
security_answer = "Bobi"

# Lambdatest settings
project_name = 'BIQ'
runName = 'Auto' # Auto means Suite Setup will be defined as <suite_name>-<date>.
userName = 'marcos.guerrero'
accessKey = 'NSssnHouGPiVWn2yStSN4HqxBTZ3lT7fmvFVLOOlP6s6PUp0FM'
local_browser = True  # This value indicates to use a local browser instead of Lambdatest, only works on Windows

os = 'Windows 10'
resolution = '1366x768'
browserName = 'Chrome'
browserVersion = '96.0'
seleniumVersion = '4.0.0'
idleTimeout = '1200' 