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

    pindia(position,location,unfam_skills)


def pindia(position,location,unfam_skills):

    def get_url(position,location):
        template = 'https://www.placementindia.com/job-search/search.php?filter=date&id2=refine_search&seeker_search_city={}&seeker_search_keyword={}'
        url = template.format(location,position)
        return url

    web_url = get_url(position,location)
    print('Fetching latest job openings from PLACEMENTINDIA-> \n')
    html_text = requests.get(web_url).text

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('div', class_ = 'sjc-iteam pr_list')
    skill_list = []
    for job in jobs:
        job_name = job.find('h2', class_ = 'sjci-heading').text
        skills = job.find_all('span')
        for span in skills:
            text = span.text  # Using the text attribute
            skill_list.append(text)
        company_name = job.find('p', class_ = 'job-cname').text
        job_link = job.h2.a['href']
        short_job_link = url_shortener.shortener(job_link)
        if all(x not in unfam_skills for x in skill_list):
            print('----------------------')
            print(f"company name: {company_name.strip()}")
            print(f"posy name: {job_name.strip()}")
            print(f"skills required: {skill_list}")
            print(f"learn more: {short_job_link}")
        skill_list = []
    print('------END OF PLACEMENT INDIA ---- \n')
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

    pindia(position,location,unfam_skills)

def pindia(position,location,unfam_skills):

    def get_url(position,location):
        template = 'https://www.placementindia.com/job-search/search.php?filter=date&id2=refine_search&seeker_search_city={}&seeker_search_keyword={}'
        url = template.format(location,position)
        return url

    web_url = get_url(position,location)
    html_text = requests.get(web_url).text

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('div', class_ = 'sjc-iteam pr_list')

    skill_list = []
    master_list = []
    temp_list = []

    for job in jobs:
        job_name = job.find('h2', class_ = 'sjci-heading').text.strip('\n')
        skills = job.find_all('span')
        for span in skills:
            text = span.text  # Using the text attribute
            skill_list.append(text)
        company_name = job.find('p', class_ = 'job-cname').text
        job_link = job.h2.a['href']
        short_job_link = url_shortener.shortener(job_link)
        if all(x not in unfam_skills for x in skill_list):
            temp_list.append(company_name)
            temp_list.append(job_name)
            temp_list.append(skill_list)
            temp_list.append(short_job_link)
            '''
            print('----------------------')
            print(f"company name: {company_name.strip()}")
            print(f"posy name: {job_name.strip()}")
            print(f"skills required: {skill_list}")
            print(f"learn more: {short_job_link}")
            '''
            master_list.append(temp_list)
        skill_list = []
        temp_list = []
    #print('\n NUMBER OF OBJECTS IN MASTER LIST -> \n',len(master_list),'\n')
    #for x in range(len(master_list)):
        #print (master_list[x],'\n')
    
    return master_list


       

