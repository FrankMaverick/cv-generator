import json
from bs4 import BeautifulSoup

def populate_html_template(template_path, data_path):
    # Load the HTML template
    with open(template_path, 'r') as file:
        html_content = file.read()

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Load data from JSON
    with open(data_path, 'r') as file:
        data = json.load(file)

    # Populate sections of the HTML template with JSON data
    soup.find(id='name').string = data['name']
    soup.find(id='position').string = data['position']
    soup.find(id='phone').string = data['contact']['phone']
    soup.find(id='mail').string = data['contact']['email']
    soup.find(id='address').string = data['contact']['address']
    soup.find(id='linkedin').string = data['contact']['linkedin']

    # Populate the "Hard Skill" section
    if 'hard_skills' in data:
        populate_hard_skill_section(soup, data['hard_skills'])

    # Populate the "Soft Skill" section
    if 'hard_skills' in data:
        populate_soft_skill_section(soup, data['soft_skills'])

    # Populate the "Education" section
    if 'education' in data:
        populate_education_section(soup, data['education'])

    # Populate the "Languages" section
    populate_language_section(soup, data['languages'])

    # Populate the "About Me" section
    about_me_div = soup.find(id='aboutMe')
    about_me_div.clear()
    for paragraph in data['about_me']:
        about_me_div.append(BeautifulSoup(f'<p>{paragraph}</p>', 'html.parser'))

    # Populate the "Work Experience" section
    if 'work_experience' in data:
        populate_experience_section(soup, data['work_experience'])

    with open(template_path, 'w') as file:
        file.write(str(soup))

def populate_education_section(soup, education_data):
    # Find the div with id "educationSection"
    education_section = soup.find('div', id='educationSection')
    if education_section:
        # Remove all existing elements in the education section
        education_section.clear()

        # For each education entry in the education_data list
        for i, education_entry in enumerate(education_data, start=1):
            # Create a new div element for the education entry
            new_education = soup.new_tag('div', **{'class': 'smallText', 'id': f'education-{i}'})

            # Create and populate HTML tags with education details
            p_title = soup.new_tag('p', **{'class': 'bolded white', 'id': 'eduTitle'})
            p_title.string = education_entry.get('title', '')
            new_education.append(p_title)

            p_institute = soup.new_tag('p', id='eduInstitute')
            p_institute.string = education_entry.get('institute', '')
            new_education.append(p_institute)

            p_dates = soup.new_tag('p', id='eduYears')
            p_dates.string = education_entry.get('dates', '')
            new_education.append(p_dates)

            # Add the new education element to the "educationSection" in the HTML template
            education_section.append(new_education)

def populate_experience_section(soup, experience_data):
    experience_section = soup.find('ul', id='workExperiences')
    if experience_section:
        # Remove all existing elements in the work experience section
        experience_section.clear()

        for i, job in enumerate(experience_data, start=1):
            # Create a new li element for each job experience
            new_job = soup.new_tag('li', id=f'job-{i}')

            # Create the internal structure of the new li element
            div_job_position = soup.new_tag('div', **{'class': 'jobPosition'})
            span_job_position = soup.new_tag('span', **{'class': 'bolded', 'id': f'jobPosition-{i}'})
            span_job_position.string = job.get('position', '')
            div_job_position.append(span_job_position)
            span_job_dates = soup.new_tag('span', id=f'jobDates-{i}')
            span_job_dates.string = job.get('dates', '')
            div_job_position.append(span_job_dates)
            new_job.append(div_job_position)

            div_project_name = soup.new_tag('div', **{'class': 'projectName bolded'})
            span_project_name = soup.new_tag('span', id=f'jobProjectCompany-{i}')
            span_project_name.string = job.get('project_company', '')
            div_project_name.append(span_project_name)
            new_job.append(div_project_name)

            div_small_text = soup.new_tag('div', **{'class': 'smallText'})
            p_job_description = soup.new_tag('p', id=f'jobDescription-{i}')
            p_job_description.string = job.get('description', '')
            div_small_text.append(p_job_description)

            ul_description_list = soup.new_tag('ul')
            description_list = job.get('description_list', [])
            for j, description in enumerate(description_list, start=1):
                li_description = soup.new_tag('li', id=f'jobDescription-{i}-list{j}')
                li_description.string = description
                ul_description_list.append(li_description)
            div_small_text.append(ul_description_list)

            p_skills = soup.new_tag('p')
            span_bolded_skills = soup.new_tag('span', **{'class': 'bolded'})
            span_bolded_skills.string = 'Skills: '
            p_skills.append(span_bolded_skills)
            span_job_skills = soup.new_tag('span', id=f'jobSkills-{i}')
            skills = ', '.join(job.get('skills', []))
            span_job_skills.string = skills
            p_skills.append(span_job_skills)
            div_small_text.append(p_skills)

            new_job.append(div_small_text)

            # Add the populated new element to the work experience section
            experience_section.append(new_job)

def populate_language_section(soup, language_data):
    # Find the language section in the HTML template
    language_section = soup.find(id='languagesList')
    
    # Clear the current content of the language section
    language_section.clear()
    
    # Populate the language section with the provided data
    for i, language in enumerate(language_data, start=1):
        # Create a new div for each language
        language_div = soup.new_tag('div', attrs={'class': 'skill', 'id': f'language-{i}'})
        
        # Create the div for the language name
        name_div = soup.new_tag('div')
        name_span = soup.new_tag('span', id=f'lang-{i}')
        name_span.string = language['name']
        name_div.append(name_span)
        language_div.append(name_div)
        
        # Create the div for the language level
        level_div = soup.new_tag('div', attrs={'class': 'yearsOfExperience'})
        level_span = soup.new_tag('span', id=f'langLevel-{i}', attrs={'class': 'alignright'})
        level_span.string = language['level']
        level_div.append(level_span)
        language_div.append(level_div)
        
        # Add the populated language div to the language section
        language_section.append(language_div)

def populate_hard_skill_section(soup, hard_skill_data):
    # Find the skills section in the HTML template
    hard_skill_section = soup.find(id='hardSkill')
    
    # Clear the current content of the skills section
    hard_skill_section.clear()
    
    # Populate the skills section with the provided data
    for i, skill in enumerate(hard_skill_data, start=1):
        # Create a new div for each skill
        hard_skill_div = soup.new_tag('div', attrs={'class': 'skill', 'id': f'hardSkill-{i}'})
        
        # Create the span for the skill
        hard_skill_span = soup.new_tag('span')
        hard_skill_span.string = skill
        hard_skill_div.append(hard_skill_span)
        
        # Add the populated skill div to the skills section
        hard_skill_section.append(hard_skill_div)

def populate_soft_skill_section(soup, soft_skill_data):
    # Find the skills section in the HTML template
    soft_skill_section = soup.find(id='softSkill')
    
    # Clear the current content of the skills section
    soft_skill_section.clear()
    
    # Populate the skills section with the provided data
    for i, skill in enumerate(soft_skill_data, start=1):
        # Create a new div for each skill
        soft_skill_div = soup.new_tag('div', attrs={'class': 'skill', 'id': f'softSkill-{i}'})
        
        # Create the span for the skill
        soft_skill_span = soup.new_tag('span')
        soft_skill_span.string = skill
        soft_skill_div.append(soft_skill_span)
        
        # Add the populated skill div to the skills section
        soft_skill_section.append(soft_skill_div)