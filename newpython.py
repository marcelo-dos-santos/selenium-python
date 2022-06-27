# newpython.py - 09/06/2022
# print ("Hello World, this is my first python-selenium line")

from nturl2path import url2pathname
from tkinter import BROWSE
from selenium.webdriver import Firefox
from selenium.webdriver import Chrome


from time import sleep


url2pathname = 'https://www.oracle.com/br/index.html'
browser = Firefox()
browser.get(url2pathname)
sleep(3)

oracle_logo = browser.find_element_by_css_selector('#u30logo')

productstag = browser.find_element_by_css_selector('.u30navul > li:nth-child(1) > button:nth-child(1)')
DevOps = browser.find_element_by_css_selector('#cloud-infrastructure > li:nth-child(12) > a:nth-child(1)')

print(f'return text from oracle_logo class{oracle_logo.text}')
print(f'return text from products-buttom tag: {productstag.text}')
productstag.click()
sleep(3)
DevOps.click()

for click in range (1,5):
    productstag.click
    print(f'4 clicks sent')
    
    
OCI_logo = browser.find_element_by_css_selector('#u30brandtxt')
print(f'return text from OCI_logo class{OCI_logo.text}')
print(f'click on products-buttom tag: {productstag.click}')
services = browser.find_element_by_xpath('/html/body/div[2]/section[1]/div[1]/div[2]/nav/ul/li[1]/button')
sleep(4)
services.click()

bi_analises = browser.find_element_by_css_selector('#analytics-tab')
sleep(2)
bi_analises.click()
print(f'return text from bi_analises {bi_analises.text}')

cloud_regions = browser.find_element_by_css_selector('#cloud-regions-tab')
cloud_regions.click()
print(f'return text from cloud_regions: {cloud_regions}')
#Assert
confirmidade = browser.find_element_by_css_selector('#compliance-tab')
confirmidade.click()
print(f'return text from CONFIRMIDADE - {confirmidade.text}')

computing = browser.find_element_by_css_selector('#compute-tab')
computing.click()
print(f'return text from COMPUTING - {computing.text}')
containers_and_functions = browser.find_element_by_css_selector('#containers-tab')
containers_and_functions.click()
print(f'return text from CONTAINERS AND FUNCTIONS - {containers_and_functions.text}')

data_lakehouse = browser.find_element_by_css_selector('#lakehouse-tab')
data_lakehouse.click()
print(f'return text from DATA LAKEHOUSE - {data_lakehouse.text}')
services_and_datebase = browser.find_element_by_css_selector('#database-services-tab')
services_and_datebase.click()
print(f'return text from SERVICES AND DATEBASE - {services_and_datebase.text}')

database_tools = browser.find_element_by_css_selector('#database-tools-tab')
database_tools.click()
print(f'return text from DATABASE TOOLS - {database_tools.text}')

developer_services_tab = browser.find_element_by_css_selector('#developer-services-tab')
developer_services_tab.click()
print(f'return text from DEVELOPER SERVICES TAB - {developer_services_tab.text}')

hybrid_cloud_tab = browser.find_element_by_css_selector('#hybrid-cloud-tab')
hybrid_cloud_tab.click()
print(f'return text from HYBRID CLOUD TAB - {hybrid_cloud_tab.text}')

integration_tab = browser.find_element_by_css_selector('#integration-tab')
integration_tab.click()
print(f'return text from INTEGRATION TAB - {integration_tab.text}')

ml_and_ai_tab = browser.find_element_by_css_selector('#ml-and-ai-tab')
ml_and_ai_tab.click()
print(f'return text from ML AND AI TAB - {ml_and_ai_tab.text}')

networking_tab = browser.find_element_by_css_selector('#networking-tab')
networking_tab.click()
print(f'return text from NETWORKING TAB - {networking_tab.text}')

observability_tab = browser.find_element_by_css_selector('#observability-tab')
observability_tab.click()
print(f'return text from OBSERVABILITY TAB - {observability_tab.text}')

saas_apps_tab = browser.find_element_by_css_selector('#saas-apps-tab')
saas_apps_tab.click()
print(f'return text from SAAS APPS TAB - {saas_apps_tab.text}')

security_tab = browser.find_element_by_css_selector('#security-tab')
security_tab.click()
print(f'return text from SECURITY TAB - {security_tab.text}')

storage_tab = browser.find_element_by_css_selector('#storage-tab')
storage_tab.click()
print(f'return text from STORAGE TAB - {storage_tab.text}')

vmware_tab = browser.find_element_by_css_selector('#vmware-tab')
vmware_tab.click()
print(f'return text from VMWARE TAB - {vmware_tab.text}')








#browser.quit()

 