# ---------------------------------------------------------------------------
# IMPORTS
import os, sys, re, csv, json, math, subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# ---------------------------------------------------------------------------
# Run the tests on the given websites list
# Prints the output  of each test
def RunPageSpeedTests(websites=[]):
	# loop each website
	for site in websites:
		print('----------')
		print('CHECKING: %s\n' % site)
		# run TTFB test
		TestTTFB(site)
		# run selenium test
		SeleniumSpeedTestChrome(site)


# ---------------------------------------------------------------------------
# Tests Server Time To First Byte
def TestTTFB(website=''):
	# ttfb command
	cmd = "ttfb %s" % website
	# run the process
	process = subprocess.run(cmd, shell=True, capture_output=True)
	# get the results
	result = process.stdout.decode("utf-8")[:-3]
	# print output
	print(result)


# ---------------------------------------------------------------------------
# selenium Environment Vars
os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['WDM_PRINT_FIRST_LINE'] = '0'

# Tests page loadtime in Chrome
# Prints back end and front end
# Loosely based on the example code in
# http://www.obeythetestinggoat.com/how-to-get-selenium-to-wait-for-page-load-after-a-click.html
def SeleniumSpeedTestChrome(website=''):
	# Get URL
	hyperlink = 'https://%s' % website
	# Set Chrome Driver Options
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument('window-size=1920x1080')
	options.add_argument("disable-gpu")
	# Start Chrome web driver interface
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
	driver.get(hyperlink)
	# Use Navigation Timing:
	# API to calculate the timings that matter the most
	# Measured in Milliseconds
	navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
	responseStart = driver.execute_script("return window.performance.timing.responseStart")
	domComplete = driver.execute_script("return window.performance.timing.domComplete")
	# calculate the performance
	backendPerformance_calc = float( (responseStart - navigationStart) / 1000 )
	frontendPerformance_calc = float( (domComplete - responseStart) / 1000 )
	overallPerformance_calc = float( backendPerformance_calc + frontendPerformance_calc )
	# print output
	print("Back End: %s" % backendPerformance_calc)
	print("Front End: %s" % frontendPerformance_calc)
	print("Total Time: %s\n" % overallPerformance_calc )
	# close the web driver
	driver.quit()

