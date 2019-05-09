import time

def video_selector(browser, videoname):

    # type in the video name
    time.sleep(1)
    search_bar = browser.find_by_xpath('//*[@id="ensemble_search_form"]/form/input[2]')
    search_bar.clear()
    search_bar.type(videoname)

    # search for the video
    time.sleep(1)
    search_button = browser.find_by_xpath('//*[@id="ensemble_search_form"]/form/button')
    search_button[0].click()


    # Press Select All since video name search (in the best case)
    # will leave behind a single video
    time.sleep(1)
    browser.find_by_xpath('//*[@id="select_all"]').click()



def username_searcher(browser, username):
    # This function looks up a username.
    # NOTE: Will pick the first one if multiple of the same name!

    time.sleep(1)
    dropdown = browser.find_by_xpath('//*[@id="search_library_id"]')

    for option in dropdown.find_by_tag('option'):
        if option.text == username:
            option.click()
            break



def read_videos():
    file = open('videonames.txt', 'r')
    video_list = file.readlines()
    video_list = [video_name.rstrip() for video_name in video_list]


    return video_list[0], video_list[1:]