def me():  
    firstname = input('What is your first name?\n')
    lastname = input('What is your last name?\n')
    daily_job = input('What do you do for work?\n')
    sector = input('What sector do you work?\n')
    industry = input('Which industry do you work?\n')
    passion = input('What are passionate about?\n')
    studying = input('What are your studying?\n')
    school = input('Where do you school?\n')

    #fact about ME!
    # OLayinka dictionary
    fname = firstname + " " + lastname

    fname = {
        'Name' : firstname + " " + lastname,
        'Job' : daily_job,
        'Sector': sector,
        'Industry': industry,
        'Passion' : passion,
        'Studies' : studying,
        'School' : school
    }
    print(f"This is {firstname} {lastname}, He currently works as a {daily_job} in the {sector} sector. {firstname}'s passion spans from {passion}. He is a current student at {school} studying {studying}. He intends to acquired this knowledge to improve bigdata frameworks in {industry} industry.")


if __name__ == '__main__':
    me()