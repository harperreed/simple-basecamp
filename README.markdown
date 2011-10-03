#Simple Basecamp API Wrapper

I didn't like the incompleteness of the other python basecamp api wrappers, so I wrote my own incomplete python api wrapper for basecamp. 

It works decently well. 

A little known secret about the basecamp API. On some interfaces, if you replace .xml with .json it will return json. This isn't supported on all interfaces though. 

###Todo
There is a lot of stuff to fix

* Convert the xml responses to python objects
* add support for adding, updating and deleting objects
* finish the api coverage
* add tests
* make money

###Use

    from simple_basecamp import simple_basecamp
	api_token = ""
    domain = ""
    api = simple_basecamp(domain=domain, api_token=api_token)
    print api.account()['name']
    projects = api.get_projects()
	for p in projects:
        print p['name']

This will print out your account name and then all your projects.