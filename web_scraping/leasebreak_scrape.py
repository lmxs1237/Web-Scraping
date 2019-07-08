from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
# options = webdriver.ChromeOptions()
# options.add_experimental_option('w3c', False)

# Go to the page that we want to scrape
driver = webdriver.Chrome()
web ='https://www.leasebreak.com/advanced-search?AdvancedSearchModel%5BearliestDateIn%5D=07%2F01%2F2019&AdvancedSearchModel%5BflexibleDateIn%5D=1&AdvancedSearchModel%5BlatestDateInPeriod%5D=38&AdvancedSearchModel%5BearliestDateOut%5D=&AdvancedSearchModel%5BflexibleDateOut%5D=0&AdvancedSearchModel%5BlatestDateOutPeriod%5D=&AdvancedSearchModel%5BboroughIds%5D%5B1%5D=0&AdvancedSearchModel%5BboroughIds%5D%5B2%5D=0&AdvancedSearchModel%5BboroughIds%5D%5B3%5D=0&AdvancedSearchModel%5BboroughIds%5D%5B4%5D=4&AdvancedSearchModel%5BboroughIds%5D%5B5%5D=0&AdvancedSearchModel%5BboroughIds%5D%5B6%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B5%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B6%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B7%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B8%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B88%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B10%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B11%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B13%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B14%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B12%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B104%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B15%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B16%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B17%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B71%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B87%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B18%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B29%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B31%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B21%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B1%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B3%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B30%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B24%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B2%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B4%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B100%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B72%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B33%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B84%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B34%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B73%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B35%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B85%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B86%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B36%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B37%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B70%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B39%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B40%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B41%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B89%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B42%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B69%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B43%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B44%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B91%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B92%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B93%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B45%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B95%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B46%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B96%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B83%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B74%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B47%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B67%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B98%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B101%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B102%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B103%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B55%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B48%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B49%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B99%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B105%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B50%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B109%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B51%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B52%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B53%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B54%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B56%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B63%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B90%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B64%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B58%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B68%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B59%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B97%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B62%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B57%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B134%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B26%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B60%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B107%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B106%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B94%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B108%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B61%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B110%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B111%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B112%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B123%5D=123&AdvancedSearchModel%5BneighborhoodIds%5D%5B128%5D=128&AdvancedSearchModel%5BneighborhoodIds%5D%5B131%5D=131&AdvancedSearchModel%5BneighborhoodIds%5D%5B135%5D=135&AdvancedSearchModel%5BneighborhoodIds%5D%5B120%5D=120&AdvancedSearchModel%5BneighborhoodIds%5D%5B129%5D=129&AdvancedSearchModel%5BneighborhoodIds%5D%5B122%5D=122&AdvancedSearchModel%5BneighborhoodIds%5D%5B127%5D=127&AdvancedSearchModel%5BneighborhoodIds%5D%5B117%5D=117&AdvancedSearchModel%5BneighborhoodIds%5D%5B116%5D=116&AdvancedSearchModel%5BneighborhoodIds%5D%5B125%5D=125&AdvancedSearchModel%5BneighborhoodIds%5D%5B130%5D=130&AdvancedSearchModel%5BneighborhoodIds%5D%5B132%5D=132&AdvancedSearchModel%5BneighborhoodIds%5D%5B115%5D=115&AdvancedSearchModel%5BneighborhoodIds%5D%5B66%5D=66&AdvancedSearchModel%5BneighborhoodIds%5D%5B114%5D=114&AdvancedSearchModel%5BneighborhoodIds%5D%5B126%5D=126&AdvancedSearchModel%5BneighborhoodIds%5D%5B65%5D=65&AdvancedSearchModel%5BneighborhoodIds%5D%5B119%5D=119&AdvancedSearchModel%5BneighborhoodIds%5D%5B121%5D=121&AdvancedSearchModel%5BneighborhoodIds%5D%5B118%5D=118&AdvancedSearchModel%5BneighborhoodIds%5D%5B133%5D=133&AdvancedSearchModel%5BneighborhoodIds%5D%5B124%5D=124&AdvancedSearchModel%5BneighborhoodIds%5D%5B28%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B82%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B81%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B75%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B76%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B79%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B80%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B77%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B113%5D=0&AdvancedSearchModel%5BneighborhoodIds%5D%5B78%5D=0&AdvancedSearchModel%5BprivateRoom%5D=&AdvancedSearchModel%5BapartmentSizeId%5D=&AdvancedSearchModel%5BbathroomsId%5D=&AdvancedSearchModel%5Bfurnished%5D=&AdvancedSearchModel%5Bprice%5D=0%3B1000000&AdvancedSearchModel%5BamenitiesIds%5D=&AdvancedSearchModel%5BfeaturesIds%5D=&AdvancedSearchModel%5BrequiredToPay%5D=Yes&AdvancedSearchModel%5BpreApprovedStatus%5D=&AdvancedSearchModel%5BrenewalOption%5D=&AdvancedSearchModel%5BshowAllTypes%5D=Yes&AdvancedSearchModel%5Bshow12mo%5D=Yes&AdvancedSearchModel%5Blocation%5D=&page=1'
driver.get(web)

# Open and write csv file
csv_file = open('leasebreak_bronx.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

# Page index used to keep track of where we are.
index = 1 
while index <= 279:
    try:
        print("Scraping Page number " + str(index))
        # Every page contains 20 house information
        for i in range(20):
            try:
                driver.get(web)
                # Click into every house information page
                manhattans = driver.find_elements_by_xpath('//div[@class="search-item-header-col"]')
                manhattans[i].click()

                info = driver.find_element_by_xpath('//section[@class="main-content"]')
                review_dict = {}

                website = info.find_element_by_xpath(
                    './/div[@class="send-form-wrapper"]//input[@name="SendEmailFormModel[url]"]').get_attribute('value')
                location = info.find_element_by_xpath('.//div[@class="title-detail-apartments-col-55"]/h2').text
                distribution = info.find_element_by_xpath('.//div[@class="title-detail-apartments-col-55"]/span').text
                price = info.find_element_by_xpath('.//span[@class="listing-price"]/span[@class="detail-right-price"]').text
                rentrange = info.find_element_by_xpath('.//div[@class="right-1-price"]/span[@class="min-term"]').text
                movein = info.find_element_by_xpath(
                    './/div[@class="col-50 no-left-padding no-right-padding"]//span[@class="nums-icon"]').text
                moveout = info.find_element_by_xpath('.//div[@class="col-50"]//span[@class="nums-icon"]').text
                bedroom = info.find_elements_by_xpath('.//div[@class="the-basic-about"]//div[@class="col-33"]')[0].text
                bathroom = info.find_elements_by_xpath('.//div[@class="the-basic-about"]//div[@class="col-33"]')[1].text
                furnished = info.find_element_by_xpath(
                    './/div[@class="col-33 hide-on-mobile"]//span[@class="nums-icon"]').text
                feature = info.find_elements_by_xpath('.//div[@class="features-section"]/ul/li')
                features = []
                for item in feature:
                    features.append(item.text)
                listingtype = info.find_elements_by_xpath('.//div[@class="the-basic-table"]//div[@class="col-67 per-100 no-left-padding"]')[0].text
                postedby = info.find_elements_by_xpath('.//div[@class="the-basic-table"]//div[@class="col-67 per-100 no-left-padding"]')[1].text
                kind = info.find_elements_by_xpath('.//div[@class="the-basic-table"]//div[@class="col-67 per-100 no-left-padding"]')[3].text
                renew = info.find_elements_by_xpath('.//div[@class="the-basic-table"]//div[@class="col-67 per-100 no-left-padding"]')[4].text
                broker = info.find_elements_by_xpath('.//div[@class="the-basic-table"]//div[@class="col-67 per-100 no-left-padding"]')[5].text

                review_dict['website'] = website
                review_dict['location'] = location
                review_dict['distribution'] = distribution
                review_dict['price'] = price
                review_dict['rentrange'] = rentrange
                review_dict['movein'] = movein
                review_dict['moveout'] = moveout
                review_dict['bedroom'] = bedroom
                review_dict['bathroom'] = bathroom
                review_dict['furnished'] = furnished
                review_dict['features'] = features
                review_dict['listingtype'] = listingtype
                review_dict['postedby'] = postedby
                review_dict['kind'] = kind
                review_dict['renew'] = renew
                review_dict['broker'] = broker

                writer.writerow(review_dict.values())
                print("Scraping house number " + str(i))

            # Pass the error page
            except Exception as e:
                print(e)
                pass

        index = index + 1
        driver.get(web)
        # Click to next page
        nextpage = driver.find_element_by_xpath('.//ul[@class="pager"]/li[@class="next"]/a')
        nextpage.click()

    except Exception as e:
        print(e)
        pass
