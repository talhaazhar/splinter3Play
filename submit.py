from splinter import Browser
import credentials
import time
import utils



home_url = "https://account.3playmedia.com/"
search_url = "https://account.3playmedia.com/video_platform_integrations/3673"
user = credentials.Creds()




def run_casper(faculty_username, video_list):
    browser = Browser('chrome')

    # with Browser('chrome') as browser:
    # Visit URL
    browser.visit(home_url)

    username = browser.find_by_css('.input-block-level')[0]
    username.type(user.username)
    password = browser.find_by_css('.input-block-level')[1]
    password.type(user.password)


    browser.find_by_xpath('//*[@id="main_content"]/div[2]/form/div[3]/button').click()
    browser.visit(search_url)

    utils.username_searcher(browser, faculty_username)

    # for video_name in video_list:
    for video_name in video_list:
        utils.video_selector(browser, video_name)


    # call the Process
    browser.find_by_xpath('//*[@id="process"]').click()



    # go through query in Process:

    ############ 1. Service ############
    time.sleep(1)
    browser.find_by_xpath('//*[@id="media_files_upload_form"]/div[2]/div[1]/div[2]/div[1]').click()



    ############ 2. Option ############
    time.sleep(1)
    browser.find_by_xpath('//*[@id="turnaround"]/div[2]/div[1]').click()



    ############ 3. Location ############
    # into Existing Folder
    time.sleep(1)
    browser.find_by_xpath('//*[@id="media_files_upload_form"]/div[2]/div[4]/div[1]/label[2]/input').click()

    ## Select 'My Latest Upload' Folder
    time.sleep(1)
    browser.find_by_xpath('//*[@id="existing_folder_content"]/div/div[2]/table/tbody/tr[12]/td[1]/label/input').click()

    # Press Continue button
    time.sleep(1)
    browser.find_by_xpath('//*[@id="media_files_upload_form"]/div[2]/div[4]/div[2]/div[1]').click()


    #
    # ############ 3. Summary ############
    # # check 'I Agree'
    # time.sleep(2)
    # browser.is_element_present_by_xpath('//*[@id="confirm_order"]',
    #                                     wait_time=None)
    # browser.find_by_xpath('//*[@id="confirm_order"]').click()
    # browser.find_by_xpath('//*[@id="place_order"]').click()



faculty_username, video_list = utils.read_videos()
browser = run_casper(faculty_username, video_list)
while 1:
    browser = browser























