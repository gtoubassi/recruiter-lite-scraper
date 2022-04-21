### Caveat Emptor

This script is offered as is and is far from "high art".

### What? Why?

If you use LinkedIn Recruiter Lite (for which LinkedIn charges a not too shabby 199 per month) you may be frustrated by your ability to collaborate and manage the workflow of sourcing candidates.  So go ahead and upgrade to the full Recruiter product!  Well that apparently is a "whole thing" whereby an enterprise agreement for 12 months is put into place and only suitable for large companies.  I genuinely don't know how anyone can credibly do any real sourcing (even for just a few positions) with Recruiter Lite.

So with this tool you can extract candidate info into a CSV, load it into a spreadsheet and go to town.

### How to use

* Create a LinkedIn Recruiter Lite project and populate it with candidates
* In Chrome go to https://www.linkedin.com/talent/home
* Open up Chrome Developer Tools
* Go to the Network Tab
* Make sure the Record button is on (red/pink).  It should be.  If not make it so.
* Enable "Preserve logs" by clicking the check box
* Now click on the project of interest, which takes you to the first page of results
* Page through the results using the pager control at the top right (e.g. 1-25 >)
* After you have paged through the full results right click on any of the log results down in the inspector and choose "Save all as HAR with Content"
* Clone this repo `https://github.com/gtoubassi/recruiter-lite-scraper.git`
* `cd recruiter-lite-scraper`
* `python3 ./scrape.py path-to-your-har-file`
* The script by default extracts name, public linkedin profile url, and the Recruiter Lite profile url (what you'd get if you clicked on the profile from within LinkedIn Recruiter Lite).

The actual content is fairly well structured JSON coming from `https://www.linkedin.com/talent/search/api/talentRecruiterSearchHits`, so there is a lot more info available that you can extract by poking around.