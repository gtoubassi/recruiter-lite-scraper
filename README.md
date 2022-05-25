### Scrape LinkedIn Recruiter Lite Candidates into a CSV

In using LinkedIn Recruiter Lite I was frustrated that I couldn’t export or download my candidate list into a csv and process it with my own tools/spreadsheet (e.g. Excel or Google Sheets).  This repo lets you record a browsing session in Google Chrome, save that browsing session, and then extract the relevant candidate details into a CSV.  All you have to do is manually page through each result to capture it in the browsing session.  The idea of scraping small bits of data for websites that require you to login simply by manually viewing the pages and then post processing the browsing session archive is a powerful one I will use in the future.

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

### Caveat Emptor

This script is offered as is and is far from "high art".  YMMV
