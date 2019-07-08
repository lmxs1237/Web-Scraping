# Web-Scraping  
This project scrape data from two different New York City house rental websites, analyse the house rental price distribution and affecting factors.  
### Prerequisites  
Install homebrew: http://brew.sh/
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap caskroom/cask
brew cask install chromedriver
```
Install selenium
```
pip install -r requirements.txt
```
### Files
* web_scraping:  
-- leasebreak_scrape.py: Using Selenium scrape data from [leasebreak](https://www.leasebreak.com/advanced-search)  
-- renthop_scrape.ipynb: Using Beautiful Soup scrape data from [renthop](https://www.renthop.com/?gclid=EAIaIQobChMIpby8q8Gl4wIVmP_jBx0KlAelEAAYASAAEgLhd_D_BwE)  
-- test file
