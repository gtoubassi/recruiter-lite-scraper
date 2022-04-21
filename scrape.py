import argparse
import json
import csv
import re
import sys
from types import SimpleNamespace
import jsonpickle

parser = argparse.ArgumentParser()
parser.add_argument("har", nargs=1)

args = parser.parse_args()

#print('Arguments: %s' % (args))

def processResult(result):

  # Uncomment to explore results
  #print(jsonpickle.encode(result, unpicklable=False, indent=4))

  publicUrl = result.memberProfileResolutionResult.publicProfileUrl
  name = result.memberProfileResolutionResult.firstName + ' ' + result.memberProfileResolutionResult.lastName

  memberProfile = result.memberProfile
  #memberProfile: urn:li:ts_profile:AEMHI8B2nvGLnJyJrX_SiyXj83D50-hasd4

  reresult = re.search(r'urn:li:ts_profile:(.*)', memberProfile)
  if reresult:
    liteProfileId = reresult.group(1)
    projectUrn = result.hiringProjectRecruitingProfileResolutionResult.currentHiringProjectCandidate.hiringProjectResolutionResult.entityUrn
    # projectUrn: urn:li:ts_hiring_project:(urn:li:ts_contract:311211611,11321234020)
    reresult = re.search(r'urn:li:ts_hiring_project:\(urn:li:ts_contract:\d+,(\d+)\)', projectUrn)
    if reresult:
      projectId = reresult.group(1)
      #url format: https://www.linkedin.com/talent/profile/AEMHI8B2nvGLnJyJrX_SiyXj83D50-hasd4-hrw4?project=11321234020
      recruiterLiteProfileUrl = 'https://www.linkedin.com/talent/profile/' + liteProfileId + '?project=' + projectId

  return [name, publicUrl, recruiterLiteProfileUrl]

def processEntries(entries, csvwriter):
  entries = filter(lambda e: e.request.url.endswith('search/api/talentRecruiterSearchHits'), entries)
  responseText = map(lambda e: e.response.content.text, entries)
  metadata = map(lambda r: json.loads(r, object_hook=lambda d: SimpleNamespace(**d)), responseText)
  elements = map(lambda m : m.elements, metadata)
  for e in elements:
    for result in e:
      csvwriter.writerow(processResult(result))

csvwriter = csv.writer(sys.stdout)
for filename in args.har:
  with open(filename) as jsonfile:
    data = json.load(jsonfile, object_hook=lambda d: SimpleNamespace(**d))
    processEntries(data.log.entries, csvwriter)


