import time
import urllib, urllib2
import base64
import simplejson
from BeautifulSoup import BeautifulStoneSoup

"""

"""

class simple_basecamp:

    api_token = ''
    domain = ''

    def __init__(self,  api_token=None, domain=None):
      self.api_token = api_token
      self.domain = domain

    def make_request(self, request_url, params=None, method='GET', ):



      if params:
        params = urllib.urlencode(params, True).replace('+', '%20')
      if method=='GET':
        if params:
          request_url = request_url + '?'+params
      url = "https://"+ self.domain+ request_url
      print url

      request = urllib2.Request(url)
      base64string = base64.encodestring('%s:%s' % (self.api_token, 'x')).replace('\n', '')
      request.add_header("Authorization", "Basic %s" % base64string)   
      f = urllib2.urlopen(request)
      data = f.read()
      f.close()
      try:
        response = simplejson.loads(data)
      except:
        response = self.parse_xml(data)

      return response

    def parse_xml(self, response):
      soup = BeautifulStoneSoup(response)
      return soup


    def account(self ):
      request_url = '/account.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result

    def get_projects(self ):
      request_url = '/projects.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result['records']

    """
    def get_project_count(self ):
      #fuck XML
      # TODO
      request_url = '/projects/count.json'
      result_xml = self.make_request(request_url=request_url, method='GET')
      print result_xml
      result = {
          'archived':result_xml['count']['archived'],
          'active':result_xml['count']['active'],
            }

      return result
    """

    def get_project(self, project_id):
      request_url = '/projects/'+project_id+'.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result

    def get_current_person(self):
      request_url = '/me.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result

    def get_people(self):
      request_url = '/people.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result['records']

    def get_project_people(self, project_id):
      request_url = '/projects/'+project_id+'/people.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result['records']

    def get_company_people(self, company_id):
      request_url = '/companies/'+company_id+'/people.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result['records']

    def get_person(self, person_id):
      request_url = '/people/'+person_id+'.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result

    def get_companies(self):
      request_url = '/companies.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result['records']

    def get_projects_companies(self, project_id):
      request_url = '/projects/'+project_id+'/companies.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result

    def get_companies(self, company_id):
      request_url = '/companies/'+company_id+'.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result

    def get_project_categories(self, project_id):
      request_url = '/projects/'+project_id+'/categories.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result

    def get_category(self, category_id):
      request_url = '/categories/'+category_id+'.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result

    def get_project_messages(self, project_id, archived=False):
      if archived:
        request_url = '/projects/'+project_id+'/posts/archive.xml'
      else:
        request_url = '/projects/'+project_id+'/posts.json'
      result = self.make_request(request_url=request_url, method='GET')
      try:
        return result['records']
      except:
        return result


    def get_message(self, message_id):
      request_url = '/posts/'+message_id+'.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result

    def get_project_messages_by_category(self, project_id, category_id,archived=False):
      if archived:
        request_url = '/projects/'+project_id+'/cat/'+category_id+'/archive.xml'
      else:
        request_url = '/projects/'+project_id+'/cat/'+category_id+'/posts.json'
      result = self.make_request(request_url=request_url, method='GET')
      return result['records']




    def get_sprojects(self, metro, location_type):
      url = 'http://api.basecamp.com/0.1/locations/'
      params = {
          'metro': metro,
          'location_type':location_type,
          }
      result = self.make_request(url=url, params=params, method='GET')
      locations_xml = result.findAll('location')
      locations = []
      for location_xml in locations_xml:
        location = {
          'id':location_xml['id'],
          'name':location_xml['name'],
          'slug':location_xml['slug'],
          'url':location_xml['url'],
            }
        locations.append(location)
      return locations

if __name__ == "__main__": 
    api_token = ""
    domain = ""
    api = simple_basecamp(domain=domain, api_token=api_token)
    print api.account()['name']
    projects = api.get_projects()
    for p in projects:
        print p['name']
    print api.get_project_count()
    print api.get_project('7240110')
    print api.get_current_person()
    print api.get_people()
    print api.get_project_people('7240110')
    print api.get_company_people('2502788')
    print api.get_person('7883798')
    print api.get_companies()
    print api.get_projects_companies('7240110')
    print api.get_companies('2502788')
    print api.get_project_categories('7240110')
    print api.get_category('73346503')
    print api.get_project_messages('7240110')
    print api.get_message('51194239')
    print api.get_project_messages_by_category('7240110','73346503')
    print api.get_project_messages('7240110',archived=True)
    print api.get_project_messages_by_category('7240110','73346503')

