require 'selenium-webdriver'

    Selenium::WebDriver::Chrome.driver_path = `which chromedriver-helper`.chomp 
    options = Selenium::WebDriver::Chrome::Options.new 
    options.add_argument('--disable-gpu') 
    options.add_argument('--headless') 
    @browser = Selenium::WebDriver.for :chrome, options: options 
    
    # 리디북스 주소 
    ridi_url = 'https://ridibooks.com' 
    @browser.get ridi_url
    
    # 입력창 주소
    input = "//*[@id=\"book_search_input\"]"
    search = @browser.find_element(xpath: input)
    # 검색어 입력, 엔터 
    search.send_keys("김영하", :return)

    # 책 제목들
    lists_xpath = "/html/body/div[2]/div/div/section/div[1]/article[2]/div[3]/div" 
    lists = @browser.find_elements(xpath: lists_xpath)


    lists.each_with_index do |book,rank|
        rank = rank+ 1
        title = book.find_element(class: "title_text").text
        link = book.find_element(class: "trackable").attribute("href")
        
        puts "[책제목#{rank}] #{title}"
        puts "주소: #{link}"
    end

@browser.quit
