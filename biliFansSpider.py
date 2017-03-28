from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,re,json

driver = webdriver.Chrome()
driver.get("https://passport.bilibili.com/login")
username = input('plz enter username:  ')
password = input('plz enter pwd:  ')

driver.find_element_by_id('userIdTxt').send_keys(username)
driver.find_element_by_id('passwdTxt').send_keys(password)
driver.find_element_by_id('vdCodeTxt').click()
# 等待输入验证码
wait = WebDriverWait(driver, 20)
element = driver.find_element_by_id('passwdTxt')
wait.until(EC.staleness_of(element))
time.sleep(0.5)
driver.get('http://space.bilibili.com/#!/fans/fans')
wait = WebDriverWait(driver, 5)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'fans-name')))
jsCode = '''
if(!window.jQuery){
	document.write('<script src="//cdn.bootcss.com/jquery/2.1.4/jquery.js"></script>');
}
$(function(){
	$.ajax({
		url: 'http://space.bilibili.com/ajax/member/GetInfo',
		type: 'POST',
		data: {mid: '13363787'}
	}).done(function(info){
		console.log(info);
	})
});
'''
driver.execute_script(jsCode)
# wait = WebDriverWait(driver, 5)
# element = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'fanInfoNode')))
# pattern = re.compile(r'<p class="fanInfoNode">(.*?)</p>')
# fanInfo = re.findall(pattern,driver.page_source)
# print(fanInfo)