from bs4 import BeautifulSoup
import requests
import url_shortener

'''
with open ("home.html","r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    course_cards = soup.find_all('div', class_ = 'card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')

def get_details():
    position = str(input('Enter the position you would like to search for: '))
    location = str(input('Enter the location you would like to search for: '))

    unfam_skills = []
    n = int(input("Enter number of unfamiliar skills which you would like to input: "))
    for i in range(0,n):
        s = str(input("Enter skill: "))
        unfam_skills.append(s)
    print('Filtering our these skills ->',unfam_skills)

    tjobs(position,location,unfam_skills)

def tjobs(position,location,unfam_skills):
    
    def get_url(position,location):
        template = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={}&txtLocation={}'
        url = template.format(position,location)
        return url

    web_url = get_url(position,location)
    html_text = requests.get(web_url).text

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")
    print('Extracting jobs from TIMESJOBS -> \n')
    for job in jobs:
        date_posted = job.find('span', class_ = 'sim-posted').span.text
        if 'few' or '1' or '2' in date_posted:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(" ",'')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            job_link = job.header.a['href']
            short_job_link = url_shortener.shortener(job_link)

            skill_list = skills.split(',')
            if all(x not in unfam_skills for x in skill_list):
                print('----------------------')
                print(f"company name: {company_name.strip()}")
                print(f"skills required: {skills.strip()}")
                print(f"date posted: {date_posted.strip()}")
                print(f"job info: {short_job_link}")
    print('------END OF TIMESJOBS ---- \n')
'''
def get_details():
    position = str(input('Enter the position you would like to search for: '))
    location = str(input('Enter the location you would like to search for: '))

    unfam_skills = []
    n = int(input("Enter number of unfamiliar skills which you would like to input: "))
    for i in range(0,n):
        s = str(input("Enter skill: "))
        unfam_skills.append(s)
    print('Filtering our these skills ->',unfam_skills)

    tjobs(position,location,unfam_skills)

def tjobs(position,location,unfam_skills):

    def get_url(position,location):
        template = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={}&txtLocation={}'
        url = template.format(position,location)
        return url

    web_url = get_url(position,location)
    html_text = requests.get(web_url).text

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")

    master_list = []
    temp_list = []    

    for job in jobs:
        date_posted = job.find('span', class_ = 'sim-posted').span.text
        if 'few' or '1' or '2' in date_posted:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip(" ").strip('\r\n')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','').strip('\n\r\n')
            job_link = job.header.a['href']
            short_job_link = url_shortener.shortener(job_link)
            skill_list = skills.split(',')
            if all(x not in unfam_skills for x in skill_list):
                temp_list.append(company_name.strip())
                temp_list.append(date_posted.strip())
                temp_list.append(skill_list)
                temp_list.append(short_job_link)
                '''
                print('----------------------')
                print(f"company name: {company_name.strip()}")
                print(f"skills required: {skills.strip()}")
                print(f"date posted: {date_posted.strip()}")
                print(f"job info: {short_job_link}")
                '''
                master_list.append(temp_list)
        temp_list = []

    #print('\n NUMBER OF OBJECTS IN MASTER LIST -> \n',len(master_list),'\n')
    #for x in range(len(master_list)):
        #print (master_list[x],'\n')
    return master_list
