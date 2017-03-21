""" Test responses for the BCDevExchange API calls """

no_issues = '[]'

one_issue = r'''[
   {
       "__v": 1,
        "_id": "58c9a3c1aa383e001d84d406",
        "assignedTo": null,
        "assignment": "2017-03-28T23:00:00.000Z",
        "code": "first-issue",
        "created": "2017-03-15T20:27:45.304Z",
        "createdBy": {
            "_id": "58c89d9caa383e001d84d3fe",
            "displayName": "Nicole De Greef"
        },
        "criteria": "<ol>\n<li style=\"box-sizing: border-box; margin-left: 0px;\">New KML output must match current, mapserver-based, physical address viewer (<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"http://openmaps.gov.bc.ca/kml/bcgov_physical_address_viewer.kml\" target=\"_blank\" rel=\"noopener noreferrer\">http://openmaps.gov.bc.ca/kml/bcgov_physical_address_viewer.kml</a>).</li>\n<ul style=\"box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; color: #24292e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';\">\n<li style=\"box-sizing: border-box; margin-left: 0px;\">Start up new, geoserver-based, physical address viewer.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Turn on Property Lines.ICF &ndash; Private Ownership Details layer in both viewers.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Turn on Site Addresses layer in both viewers.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Using Find an Address, zoom to 6621 Oldfield Rd, Central Saanich, bc.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Zoom around the associated parcel (e.g., PID 2845857) and confirm that the parcel details placemark is always in view as per the screenshots attached at&nbsp;<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"https://osgeo-org.atlassian.net/browse/GEOS-8033\" target=\"_blank\" rel=\"noopener noreferrer\">https://osgeo-org.atlassian.net/browse/GEOS-8033</a></li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Find other large parcels and confirm that the two versions of the physical address viewer work the same.</li>\n</ul>\n<ol style=\"box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; color: #24292e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';\" start=\"2\">\n<li style=\"box-sizing: border-box; margin-left: 0px;\">\n<p style=\"box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;\">The solution will also avoid duplicate labels where features appear in multiple adjacent tiles when creating tiled maps.</p>\n</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">\n<p style=\"box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;\">The code must be submitted to the&nbsp;<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"https://github.com/geoserver\" target=\"_blank\" rel=\"noopener noreferrer\">GeoServer project on GitHub</a>&nbsp;and accepted into the core GeoServer product.</p>\n</li>\n</ol>\n</ol>",
        "deadline": "2017-03-23T23:00:00.000Z",
        "description": "<p class=\"MsoNormal\">In GeoServer WMS requests for KML output, you can specify that if more than a given number of features are to be returned, render them in a single GroundOverlay plus a point placemark for each feature. In the case of polygonal features, the placemark is located at the centroid of each polygon. These centroids can easily be beyond the BBOX specified in the WMS request in which case the returned placemarks are out of the current map view, leaving Google Earth and Cesium users with no way of seeing the non-spatial attributes of a polygon in the GroundOverlay.</p>\n<p class=\"MsoNormal\">&nbsp;Enhance GeoServer WMS KML output so that Point placemarks associated with a GroundOverlay are positioned within the BBOX of the WMS request. &nbsp;This could be implemented as a new KM option (e.g., kmplacemarkLocation:centroid or kmplacemarkLocation:roving) subject to approval by the GeoServer community.</p>\n<p class=\"MsoNormal\">The solution will also avoid duplicate labels where features appear in multiple adjacent tiles when creating tiled maps.</p>\n<p class=\"MsoNormal\">For more details of the work required, please visit the following GeoServer ticket:</p>\n<p class=\"MsoNormal\"><a href=\"https://osgeo-org.atlassian.net/browse/GEOS-8033\" target=\"_blank\" rel=\"noopener noreferrer\">https://osgeo-org.atlassian.net/browse/GEOS-8033&nbsp;</a></p>",
        "earn": 2500,
        "evaluation": "<p class=\"MsoNormal\">Proposals will be evaluated based on the following:</p>\n<ul style=\"list-style-type: disc;\">\n<li class=\"MsoNormal\">Knowledge and experience with Java (30 points)</li>\n<li class=\"MsoNormal\">Knowledge and experience with GeoServer source code (30 points)</li>\n<li class=\"MsoNormal\">Knowledge and experience with KML output source code within GeoServer (40 points)</li>\n</ul>",
        "github": "https://github.com/bcgov/databc-web-map-services/issues/3",
        "isPublished": true,
        "name": "First Issue",
        "program": {
            "_id": "589101d9677cb9001c6b6d01",
            "code": "pro-databc",
            "isPublished": true,
            "logo": "uploads/logo-1489508615475.png",
            "title": "DataBC"
        },
        "project": {
            "_id": "589104a8677cb9001c6b6d05",
            "code": "prj-data-bc-web-map-services",
            "isPublished": true,
            "name": "DataBC Web Map Services"
        },
        "proposalEmail": "Michelle.Douville@gov.bc.ca",
        "short": "Is Java one of your languages of choice?  Do you value the ability to visualize geographic data on open source software?  If so, check out this GeoServer product enhancement request and opportunity to work with the team @ DataBC.",
        "skills": [
            "GeoServer",
            "Java",
            "KML",
            "GitHub"
        ],
        "start": "2017-04-05T07:00:00.000Z",
        "status": "Pending",
        "tags": [],
        "updated": "2017-03-16T18:54:51.851Z",
        "updatedBy": {
            "_id": "58c89d9caa383e001d84d3fe",
            "displayName": "Nicole De Greef"
        },
        "userIs": {
            "admin": false,
            "gov": false,
            "member": false,
            "request": false
        },
        "wasPublished": true
    }
]'''

two_issues = r'''[
   {
        "__v": 1,
        "_id": "58c9a3c1aa383e001d84d406",
        "assignedTo": null,
        "assignment": "2017-03-28T23:00:00.000Z",
        "code": "first-issue",
        "created": "2017-03-15T20:27:45.304Z",
        "createdBy": {
            "_id": "58c89d9caa383e001d84d3fe",
            "displayName": "Nicole De Greef"
        },
        "criteria": "<ol>\n<li style=\"box-sizing: border-box; margin-left: 0px;\">New KML output must match current, mapserver-based, physical address viewer (<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"http://openmaps.gov.bc.ca/kml/bcgov_physical_address_viewer.kml\" target=\"_blank\" rel=\"noopener noreferrer\">http://openmaps.gov.bc.ca/kml/bcgov_physical_address_viewer.kml</a>).</li>\n<ul style=\"box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; color: #24292e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';\">\n<li style=\"box-sizing: border-box; margin-left: 0px;\">Start up new, geoserver-based, physical address viewer.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Turn on Property Lines.ICF &ndash; Private Ownership Details layer in both viewers.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Turn on Site Addresses layer in both viewers.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Using Find an Address, zoom to 6621 Oldfield Rd, Central Saanich, bc.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Zoom around the associated parcel (e.g., PID 2845857) and confirm that the parcel details placemark is always in view as per the screenshots attached at&nbsp;<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"https://osgeo-org.atlassian.net/browse/GEOS-8033\" target=\"_blank\" rel=\"noopener noreferrer\">https://osgeo-org.atlassian.net/browse/GEOS-8033</a></li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Find other large parcels and confirm that the two versions of the physical address viewer work the same.</li>\n</ul>\n<ol style=\"box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; color: #24292e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';\" start=\"2\">\n<li style=\"box-sizing: border-box; margin-left: 0px;\">\n<p style=\"box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;\">The solution will also avoid duplicate labels where features appear in multiple adjacent tiles when creating tiled maps.</p>\n</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">\n<p style=\"box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;\">The code must be submitted to the&nbsp;<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"https://github.com/geoserver\" target=\"_blank\" rel=\"noopener noreferrer\">GeoServer project on GitHub</a>&nbsp;and accepted into the core GeoServer product.</p>\n</li>\n</ol>\n</ol>",
        "deadline": "2017-03-23T23:00:00.000Z",
        "description": "<p class=\"MsoNormal\">In GeoServer WMS requests for KML output, you can specify that if more than a given number of features are to be returned, render them in a single GroundOverlay plus a point placemark for each feature. In the case of polygonal features, the placemark is located at the centroid of each polygon. These centroids can easily be beyond the BBOX specified in the WMS request in which case the returned placemarks are out of the current map view, leaving Google Earth and Cesium users with no way of seeing the non-spatial attributes of a polygon in the GroundOverlay.</p>\n<p class=\"MsoNormal\">&nbsp;Enhance GeoServer WMS KML output so that Point placemarks associated with a GroundOverlay are positioned within the BBOX of the WMS request. &nbsp;This could be implemented as a new KM option (e.g., kmplacemarkLocation:centroid or kmplacemarkLocation:roving) subject to approval by the GeoServer community.</p>\n<p class=\"MsoNormal\">The solution will also avoid duplicate labels where features appear in multiple adjacent tiles when creating tiled maps.</p>\n<p class=\"MsoNormal\">For more details of the work required, please visit the following GeoServer ticket:</p>\n<p class=\"MsoNormal\"><a href=\"https://osgeo-org.atlassian.net/browse/GEOS-8033\" target=\"_blank\" rel=\"noopener noreferrer\">https://osgeo-org.atlassian.net/browse/GEOS-8033&nbsp;</a></p>",
        "earn": 2500,
        "evaluation": "<p class=\"MsoNormal\">Proposals will be evaluated based on the following:</p>\n<ul style=\"list-style-type: disc;\">\n<li class=\"MsoNormal\">Knowledge and experience with Java (30 points)</li>\n<li class=\"MsoNormal\">Knowledge and experience with GeoServer source code (30 points)</li>\n<li class=\"MsoNormal\">Knowledge and experience with KML output source code within GeoServer (40 points)</li>\n</ul>",
        "github": "https://github.com/bcgov/databc-web-map-services/issues/3",
        "isPublished": true,
        "name": "First Issue",
        "program": {
            "_id": "589101d9677cb9001c6b6d01",
            "code": "pro-databc",
            "isPublished": true,
            "logo": "uploads/logo-1489508615475.png",
            "title": "DataBC"
        },
        "project": {
            "_id": "589104a8677cb9001c6b6d05",
            "code": "prj-data-bc-web-map-services",
            "isPublished": true,
            "name": "DataBC Web Map Services"
        },
        "proposalEmail": "Michelle.Douville@gov.bc.ca",
        "short": "Is Java one of your languages of choice?  Do you value the ability to visualize geographic data on open source software?  If so, check out this GeoServer product enhancement request and opportunity to work with the team @ DataBC.",
        "skills": [
            "GeoServer",
            "Java",
            "KML",
            "GitHub"
        ],
        "start": "2017-04-05T07:00:00.000Z",
        "status": "Pending",
        "tags": [],
        "updated": "2017-03-16T18:54:51.851Z",
        "updatedBy": {
            "_id": "58c89d9caa383e001d84d3fe",
            "displayName": "Nicole De Greef"
        },
        "userIs": {
            "admin": false,
            "gov": false,
            "member": false,
            "request": false
        },
        "wasPublished": true
    },
    {
        "__v": 0,
        "_id": "58c72cf8aa383e001d84d3fb",
        "assignedTo": null,
        "assignment": "2017-03-24T23:00:00.000Z",
        "code": "second-issue",
        "created": "2017-03-13T23:36:24.780Z",
        "createdBy": {
            "_id": "58c0d898f3397f001d1d0a7d",
            "displayName": "Lena Smith"
        },
        "criteria": "<h1><span style=\"color: #003366;\">Definitions</span></h1>\n<p>User = EAO staff member using a browser</p>\n<p>Service = Guidance Microservice&nbsp;</p>\n<h1><span style=\"color: #003366;\">Scope</span></h1>\n<p>This Help Wanted request is for the \"Service\" as defined above and its use described below.</p>\n<p>The outlined service will be hooked into existing code that can be accessed at: &nbsp;https://github.com/bcgov/esm-server. It is advisable that applicants make use of this code when creating their proposal and if selected, in the creation of the service.</p>\n<h2>System Use Case</h2>\n<ol>\n<li>User runs a web browser and points to the microservice URL</li>\n<li>User can add/edit sections in the main page.&nbsp;</li>\n<li>User can add/edit sub-sections for each section in the main page.</li>\n<li>User saves their changes, and the Service persists those changes in a database for all other users to see upon next browser reload.</li>\n<li>User will be able to upload documents that will list on the page</li>\n<li>User will be able to edit text using basic editing functionality including but not limited to &ndash; bold/italic/underline and colour&nbsp;</li>\n<li>User will be able to insert hyperlinks within the text</li>\n<li>All users will be able to search the site or individual pages</li>\n</ol>\n<h2>Service Provider Use Case</h2>\n<ol>\n<li>Install Service, e.g. npm install guidance-service --save-dev</li>\n<li>Fork source and deploy Service in OpenShift</li>\n<li>Configure Service with administrative credentials using OpenShift Deployment Environment Variable, e.g., ADMINPW=</li>\n</ol>\n<h2>Additional Criteria</h2>\n<p><strong>Need to have</strong></p>\n<ol>\n<li>Collaborate with EAO team within 3 business days of award to determine initial design requirements, look and feel, and workflow.</li>\n<li>MongoDB for database storage.</li>\n<li>Content must be password protected and not accessible to public users</li>\n<li>Editing of content must be restricted to authorized users</li>\n<li>Logs to console any errors.</li>\n<li>The service must be re-usable and extendable for future design / development iterations.</li>\n<li>The individual Page URL will be a human readable format based on the name of the page (SEO Friendly)</li>\n<li>The site will use appropriate accessibility standards making use of page readers, tabbing, and keyboard shortcuts&nbsp;</li>\n<li>Must be compatible with Internet Explorer 11, Microsoft Edge, Google Chrome, and Firefox</li>\n<li>The service should be end-user centric with specific attention paid to the user workflow, searchability/discoverability of content on the site, and overall ease of navigation and manipulation of content.&nbsp;</li>\n</ol>\n<p><strong>Nice to Have:</strong></p>\n<ol>\n<li>Solution for making the microservice viewable to only EAO users logged into EPIC</li>\n<li>Ability to integrate for &lsquo;future state&rsquo; with Javascript for NodeJS version 4.x following npm install and npm start conventions, while using Bootstrap 4 for styling the web content is deemed beneficial</li>\n<li>Look-feel will be in line with the BC Government Design Standards</li>\n</ol>\n<p>On <strong>March 17th at 11:00am</strong> we will be available for a virtual meeting to discuss this opportunity. If desired, please contact <strong>rumon.carter@gov.bc.ca</strong>&nbsp;for a meeting invitation.</p>\n<p>&nbsp;</p>",
        "deadline": "2017-03-21T23:00:00.000Z",
        "description": "<h1><span style=\"color: #003366;\"><strong>Background</strong></span></h1>\n<p>The BC Environmental Assessment Office (EAO) has recently launched EPIC (the EAO Project Information &amp; Collaboration system), an online tool for sharing project information with the public and stakeholders, supporting business intelligence, and for managing certain of its business processes (e.g. public comment periods). The launch of this new tool is part of a broader strategy by the EAO to create a digital services team tasked with modernizing and continuously improving its systems, tools and processes.</p>\n<h3><strong>Another of the EAO&rsquo;s aging tools is known as eGuide:&nbsp;</strong></h3>\n<p style=\"padding-left: 30px;\">&ldquo;eGuide is a knowledge base that simplifies the planning and delivery of Environmental Assessments (EAs) by EAO staff, and supports the operational function of the office. It links each step in the environmental assessment process to applicable government policies and procedures, templates and administrative learning resources. This eliminates policy and procedure binders, gives EAO staff quick and reliable access to current and accurate information.&rdquo;</p>\n<p>The problem is that this supposedly e(lectronic) tool, while built in html, is stuck on the EAO&rsquo;s shared drive, rendering it challenging to edit, sub-optimal to use, and ugly. It needs a facelift, and a functionality refresh.&nbsp;</p>\n<p>So the EAO is in the market for a guidance documentation microservice to replace eGuide, enabling members of the Office to better find, share and manage online reference and training materials. Ideally, this microservice will be integrated/integratable into EPIC. &nbsp;&nbsp;</p>\n<h1><span style=\"color: #003366;\"><strong>User Story</strong></span></h1>\n<h2>User Story 1: Content Consumer</h2>\n<p><strong>Need to have</strong></p>\n<p>A new member of the EAO staff needs to know how to draft a Section 10 order. They visit the Guide, navigate to the pertinent section of the EA process to find text describing the process for issuing a s. 10, links to the relevant section of the Environmental Assessment Act, and links to various templates materials (in .doc, .pdf, etc. format). In the alternative, the user enters &ldquo;s.10&rdquo; in a search field to find the same information.&nbsp;</p>\n<p><strong>Future state&nbsp;</strong></p>\n<p>Separate Guidance content is displayed dependent upon the user type / role assigned in the EPIC system, e.g. an EAO staff member will see different Guidance content than a public vs. working group vs. First Nations user.</p>\n<h2>User Story 2: Content Creator</h2>\n<p><strong>Need to have</strong></p>\n<p>A member of the EAO Digital Services team needs to create a new section in the Guide, to describe a new office procedure. They use the microservice to create a new page, entering a description for the page, and start to create sub sections within the page with accompanying hyperlinks and sub section text descriptions. They can create pointers to documents found within the EPIC Documents section, or can load new documents to the file server and point to those documents in that location. To do so they are required to hand code the new materials and solutions described above.</p>\n<p><strong>Nice to have</strong></p>\n<p>All of the above is possible, but enabled through a WYSIWYG interface such that a lay user, with no coding knowledge can create and edit text content as well as related documentation.&nbsp;</p>\n<p><strong>Future state</strong></p>\n<p>Content has enhanced &ldquo;wiki&rdquo; functionality such that all staff users can interact with content, suggest/make changes, etc.&nbsp;</p>\n<p>&nbsp;</p>",
        "earn": 2000,
        "evaluation": "<p>To apply for this work, please email a proposal to <strong>rumon.carter@gov.bc.ca</strong>. Please reference the issue name - \"Guidance Documentation Micro-service&rdquo; in your email subject line.</p>\n<p>With your proposal, you must attach a copy of the <a title=\"Code WIth Us Terms\" href=\"https://github.com/BCDevExchange/code-with-us/raw/master/Code%20With%20Us%20Paid%20Terms_Nov_28.pdf\" target=\"_blank\" rel=\"noopener noreferrer\"><em>Code&nbsp;With Us</em> Terms</a>, with the required information asked for in the &ldquo;Acceptance&rdquo; section of the document&nbsp;(Mandatory).&nbsp;</p>\n<p>We will score your proposal by the following criteria:</p>\n<ol>\n<li>Your confirmation of being able to commit the time to meet all of the Acceptance Criteria by <strong>March 31</strong>, 2017.</li>\n<li>The date you can commit to delivering your first working version for preliminary integration testing (15 points).</li>\n<li>A brief overview of how you will build the microservice.&nbsp;\n<ul>\n<li>Points awarded to the efficient user of Open Source Code</li>\n<li>Points awarded to scope of work within the proposal (i.e. Inclusion of &lsquo;nice to haves')</li>\n</ul>\n</li>\n<li>References to your relevant experience and demonstrated ability to do the work (50 points). For example, a link to your GitHub projects.</li>\n<li>Any added value you can provide within the fixed price (10 points).</li>\n</ol>",
        "github": "",
        "isPublished": true,
        "name": "Second Issue",
        "program": {
            "_id": "589d707509b2ba001d06289b",
            "code": "pro-environmental-assessment-office",
            "isPublished": true,
            "logo": "uploads/logo-1487265841121.jpg",
            "title": "BC Environmental Assessment Office"
        },
        "project": {
            "_id": "589d72e509b2ba001d06289c",
            "code": "prj-esm-server",
            "isPublished": true,
            "name": "EAO Project Information & Collaboration System (EPIC)"
        },
        "proposalEmail": "",
        "short": "EAO is in the market for a guidance documentation micro-service to replace eGuide, enabling members of the Office to better find, share and manage online reference and training materials. Ideally, this micro-service will be integrated/integratable into EPIC.",
        "skills": [],
        "start": "2017-03-24T07:00:00.000Z",
        "status": "Pending",
        "tags": [],
        "updated": "2017-03-14T05:34:57.497Z",
        "updatedBy": {
            "_id": "588b961c739f873d0eb00761",
            "displayName": "Admin Local"
        },
        "userIs": {
            "admin": false,
            "gov": false,
            "member": false,
            "request": false
        },
        "wasPublished": true
    }
]'''


missing_id = r'''[
 {
        "__v": 1,
        "assignedTo": null,
        "assignment": "2017-03-28T23:00:00.000Z",
        "code": "opp-geoserver-enhancement--roving-point",
        "created": "2017-03-15T20:27:45.304Z",
        "createdBy": {
            "_id": "58c89d9caa383e001d84d3fe",
            "displayName": "Nicole De Greef"
        },
        "criteria": "<ol>\n<li style=\"box-sizing: border-box; margin-left: 0px;\">New KML output must match current, mapserver-based, physical address viewer (<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"http://openmaps.gov.bc.ca/kml/bcgov_physical_address_viewer.kml\" target=\"_blank\" rel=\"noopener noreferrer\">http://openmaps.gov.bc.ca/kml/bcgov_physical_address_viewer.kml</a>).</li>\n<ul style=\"box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; color: #24292e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';\">\n<li style=\"box-sizing: border-box; margin-left: 0px;\">Start up new, geoserver-based, physical address viewer.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Turn on Property Lines.ICF &ndash; Private Ownership Details layer in both viewers.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Turn on Site Addresses layer in both viewers.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Using Find an Address, zoom to 6621 Oldfield Rd, Central Saanich, bc.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Zoom around the associated parcel (e.g., PID 2845857) and confirm that the parcel details placemark is always in view as per the screenshots attached at&nbsp;<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"https://osgeo-org.atlassian.net/browse/GEOS-8033\" target=\"_blank\" rel=\"noopener noreferrer\">https://osgeo-org.atlassian.net/browse/GEOS-8033</a></li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Find other large parcels and confirm that the two versions of the physical address viewer work the same.</li>\n</ul>\n<ol style=\"box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; color: #24292e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';\" start=\"2\">\n<li style=\"box-sizing: border-box; margin-left: 0px;\">\n<p style=\"box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;\">The solution will also avoid duplicate labels where features appear in multiple adjacent tiles when creating tiled maps.</p>\n</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">\n<p style=\"box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;\">The code must be submitted to the&nbsp;<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"https://github.com/geoserver\" target=\"_blank\" rel=\"noopener noreferrer\">GeoServer project on GitHub</a>&nbsp;and accepted into the core GeoServer product.</p>\n</li>\n</ol>\n</ol>",
        "deadline": "2017-03-23T23:00:00.000Z",
        "description": "<p class=\"MsoNormal\">In GeoServer WMS requests for KML output, you can specify that if more than a given number of features are to be returned, render them in a single GroundOverlay plus a point placemark for each feature. In the case of polygonal features, the placemark is located at the centroid of each polygon. These centroids can easily be beyond the BBOX specified in the WMS request in which case the returned placemarks are out of the current map view, leaving Google Earth and Cesium users with no way of seeing the non-spatial attributes of a polygon in the GroundOverlay.</p>\n<p class=\"MsoNormal\">&nbsp;Enhance GeoServer WMS KML output so that Point placemarks associated with a GroundOverlay are positioned within the BBOX of the WMS request. &nbsp;This could be implemented as a new KM option (e.g., kmplacemarkLocation:centroid or kmplacemarkLocation:roving) subject to approval by the GeoServer community.</p>\n<p class=\"MsoNormal\">The solution will also avoid duplicate labels where features appear in multiple adjacent tiles when creating tiled maps.</p>\n<p class=\"MsoNormal\">For more details of the work required, please visit the following GeoServer ticket:</p>\n<p class=\"MsoNormal\"><a href=\"https://osgeo-org.atlassian.net/browse/GEOS-8033\" target=\"_blank\" rel=\"noopener noreferrer\">https://osgeo-org.atlassian.net/browse/GEOS-8033&nbsp;</a></p>",
        "earn": 2500,
        "evaluation": "<p class=\"MsoNormal\">Proposals will be evaluated based on the following:</p>\n<ul style=\"list-style-type: disc;\">\n<li class=\"MsoNormal\">Knowledge and experience with Java (30 points)</li>\n<li class=\"MsoNormal\">Knowledge and experience with GeoServer source code (30 points)</li>\n<li class=\"MsoNormal\">Knowledge and experience with KML output source code within GeoServer (40 points)</li>\n</ul>",
        "github": "https://github.com/bcgov/databc-web-map-services/issues/3",
        "isPublished": true,
        "name": "GeoServer Enhancement: Roving Point",
        "program": {
            "_id": "589101d9677cb9001c6b6d01",
            "code": "pro-databc",
            "isPublished": true,
            "logo": "uploads/logo-1489508615475.png",
            "title": "DataBC"
        },
        "project": {
            "_id": "589104a8677cb9001c6b6d05",
            "code": "prj-data-bc-web-map-services",
            "isPublished": true,
            "name": "DataBC Web Map Services"
        },
        "proposalEmail": "Michelle.Douville@gov.bc.ca",
        "short": "Is Java one of your languages of choice?  Do you value the ability to visualize geographic data on open source software?  If so, check out this GeoServer product enhancement request and opportunity to work with the team @ DataBC.",
        "skills": [
            "GeoServer",
            "Java",
            "KML",
            "GitHub"
        ],
        "start": "2017-04-05T07:00:00.000Z",
        "status": "Pending",
        "tags": [],
        "updated": "2017-03-16T18:54:51.851Z",
        "updatedBy": {
            "_id": "58c89d9caa383e001d84d3fe",
            "displayName": "Nicole De Greef"
        },
        "userIs": {
            "admin": false,
            "gov": false,
            "member": false,
            "request": false
        },
        "wasPublished": true
    }
]'''

empty_code = r'''[
{
       "__v": 1,
        "_id": "58c9a3c1aa383e001d84d406",
        "assignedTo": null,
        "assignment": "2017-03-28T23:00:00.000Z",
        "code": "",
        "created": "2017-03-15T20:27:45.304Z",
        "createdBy": {
            "_id": "58c89d9caa383e001d84d3fe",
            "displayName": "Nicole De Greef"
        },
        "criteria": "<ol>\n<li style=\"box-sizing: border-box; margin-left: 0px;\">New KML output must match current, mapserver-based, physical address viewer (<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"http://openmaps.gov.bc.ca/kml/bcgov_physical_address_viewer.kml\" target=\"_blank\" rel=\"noopener noreferrer\">http://openmaps.gov.bc.ca/kml/bcgov_physical_address_viewer.kml</a>).</li>\n<ul style=\"box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; color: #24292e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';\">\n<li style=\"box-sizing: border-box; margin-left: 0px;\">Start up new, geoserver-based, physical address viewer.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Turn on Property Lines.ICF &ndash; Private Ownership Details layer in both viewers.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Turn on Site Addresses layer in both viewers.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Using Find an Address, zoom to 6621 Oldfield Rd, Central Saanich, bc.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Zoom around the associated parcel (e.g., PID 2845857) and confirm that the parcel details placemark is always in view as per the screenshots attached at&nbsp;<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"https://osgeo-org.atlassian.net/browse/GEOS-8033\" target=\"_blank\" rel=\"noopener noreferrer\">https://osgeo-org.atlassian.net/browse/GEOS-8033</a></li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Find other large parcels and confirm that the two versions of the physical address viewer work the same.</li>\n</ul>\n<ol style=\"box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; color: #24292e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';\" start=\"2\">\n<li style=\"box-sizing: border-box; margin-left: 0px;\">\n<p style=\"box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;\">The solution will also avoid duplicate labels where features appear in multiple adjacent tiles when creating tiled maps.</p>\n</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">\n<p style=\"box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;\">The code must be submitted to the&nbsp;<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"https://github.com/geoserver\" target=\"_blank\" rel=\"noopener noreferrer\">GeoServer project on GitHub</a>&nbsp;and accepted into the core GeoServer product.</p>\n</li>\n</ol>\n</ol>",
        "deadline": "2017-03-23T23:00:00.000Z",
        "description": "<p class=\"MsoNormal\">In GeoServer WMS requests for KML output, you can specify that if more than a given number of features are to be returned, render them in a single GroundOverlay plus a point placemark for each feature. In the case of polygonal features, the placemark is located at the centroid of each polygon. These centroids can easily be beyond the BBOX specified in the WMS request in which case the returned placemarks are out of the current map view, leaving Google Earth and Cesium users with no way of seeing the non-spatial attributes of a polygon in the GroundOverlay.</p>\n<p class=\"MsoNormal\">&nbsp;Enhance GeoServer WMS KML output so that Point placemarks associated with a GroundOverlay are positioned within the BBOX of the WMS request. &nbsp;This could be implemented as a new KM option (e.g., kmplacemarkLocation:centroid or kmplacemarkLocation:roving) subject to approval by the GeoServer community.</p>\n<p class=\"MsoNormal\">The solution will also avoid duplicate labels where features appear in multiple adjacent tiles when creating tiled maps.</p>\n<p class=\"MsoNormal\">For more details of the work required, please visit the following GeoServer ticket:</p>\n<p class=\"MsoNormal\"><a href=\"https://osgeo-org.atlassian.net/browse/GEOS-8033\" target=\"_blank\" rel=\"noopener noreferrer\">https://osgeo-org.atlassian.net/browse/GEOS-8033&nbsp;</a></p>",
        "earn": 2500,
        "evaluation": "<p class=\"MsoNormal\">Proposals will be evaluated based on the following:</p>\n<ul style=\"list-style-type: disc;\">\n<li class=\"MsoNormal\">Knowledge and experience with Java (30 points)</li>\n<li class=\"MsoNormal\">Knowledge and experience with GeoServer source code (30 points)</li>\n<li class=\"MsoNormal\">Knowledge and experience with KML output source code within GeoServer (40 points)</li>\n</ul>",
        "github": "https://github.com/bcgov/first-issue",
        "isPublished": true,
        "name": "First Issue",
        "program": {
            "_id": "589101d9677cb9001c6b6d01",
            "code": "pro-databc",
            "isPublished": true,
            "logo": "uploads/logo-1489508615475.png",
            "title": "DataBC"
        },
        "project": {
            "_id": "589104a8677cb9001c6b6d05",
            "code": "prj-data-bc-web-map-services",
            "isPublished": true,
            "name": "DataBC Web Map Services"
        },
        "proposalEmail": "Michelle.Douville@gov.bc.ca",
        "short": "Is Java one of your languages of choice?  Do you value the ability to visualize geographic data on open source software?  If so, check out this GeoServer product enhancement request and opportunity to work with the team @ DataBC.",
        "skills": [
            "GeoServer",
            "Java",
            "KML",
            "GitHub"
        ],
        "start": "2017-04-05T07:00:00.000Z",
        "status": "Pending",
        "tags": [],
        "updated": "2017-03-16T18:54:51.851Z",
        "updatedBy": {
            "_id": "58c89d9caa383e001d84d3fe",
            "displayName": "Nicole De Greef"
        },
        "userIs": {
            "admin": false,
            "gov": false,
            "member": false,
            "request": false
        },
        "wasPublished": true
    }
]'''

code_starts_with_slash = r'''[
   {
       "__v": 1,
        "_id": "58c9a3c1aa383e001d84d406",
        "assignedTo": null,
        "assignment": "2017-03-28T23:00:00.000Z",
        "code": "/first-issue",
        "created": "2017-03-15T20:27:45.304Z",
        "createdBy": {
            "_id": "58c89d9caa383e001d84d3fe",
            "displayName": "Nicole De Greef"
        },
        "criteria": "<ol>\n<li style=\"box-sizing: border-box; margin-left: 0px;\">New KML output must match current, mapserver-based, physical address viewer (<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"http://openmaps.gov.bc.ca/kml/bcgov_physical_address_viewer.kml\" target=\"_blank\" rel=\"noopener noreferrer\">http://openmaps.gov.bc.ca/kml/bcgov_physical_address_viewer.kml</a>).</li>\n<ul style=\"box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; color: #24292e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';\">\n<li style=\"box-sizing: border-box; margin-left: 0px;\">Start up new, geoserver-based, physical address viewer.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Turn on Property Lines.ICF &ndash; Private Ownership Details layer in both viewers.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Turn on Site Addresses layer in both viewers.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Using Find an Address, zoom to 6621 Oldfield Rd, Central Saanich, bc.</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Zoom around the associated parcel (e.g., PID 2845857) and confirm that the parcel details placemark is always in view as per the screenshots attached at&nbsp;<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"https://osgeo-org.atlassian.net/browse/GEOS-8033\" target=\"_blank\" rel=\"noopener noreferrer\">https://osgeo-org.atlassian.net/browse/GEOS-8033</a></li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">Find other large parcels and confirm that the two versions of the physical address viewer work the same.</li>\n</ul>\n<ol style=\"box-sizing: border-box; padding-left: 2em; margin-top: 0px; margin-bottom: 16px; color: #24292e; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';\" start=\"2\">\n<li style=\"box-sizing: border-box; margin-left: 0px;\">\n<p style=\"box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;\">The solution will also avoid duplicate labels where features appear in multiple adjacent tiles when creating tiled maps.</p>\n</li>\n<li style=\"box-sizing: border-box; margin-top: 0.25em; margin-left: 0px;\">\n<p style=\"box-sizing: border-box; margin-top: 0px; margin-bottom: 16px;\">The code must be submitted to the&nbsp;<a style=\"box-sizing: border-box; background-color: transparent; color: #0366d6; text-decoration: none;\" href=\"https://github.com/geoserver\" target=\"_blank\" rel=\"noopener noreferrer\">GeoServer project on GitHub</a>&nbsp;and accepted into the core GeoServer product.</p>\n</li>\n</ol>\n</ol>",
        "deadline": "2017-03-23T23:00:00.000Z",
        "description": "<p class=\"MsoNormal\">In GeoServer WMS requests for KML output, you can specify that if more than a given number of features are to be returned, render them in a single GroundOverlay plus a point placemark for each feature. In the case of polygonal features, the placemark is located at the centroid of each polygon. These centroids can easily be beyond the BBOX specified in the WMS request in which case the returned placemarks are out of the current map view, leaving Google Earth and Cesium users with no way of seeing the non-spatial attributes of a polygon in the GroundOverlay.</p>\n<p class=\"MsoNormal\">&nbsp;Enhance GeoServer WMS KML output so that Point placemarks associated with a GroundOverlay are positioned within the BBOX of the WMS request. &nbsp;This could be implemented as a new KM option (e.g., kmplacemarkLocation:centroid or kmplacemarkLocation:roving) subject to approval by the GeoServer community.</p>\n<p class=\"MsoNormal\">The solution will also avoid duplicate labels where features appear in multiple adjacent tiles when creating tiled maps.</p>\n<p class=\"MsoNormal\">For more details of the work required, please visit the following GeoServer ticket:</p>\n<p class=\"MsoNormal\"><a href=\"https://osgeo-org.atlassian.net/browse/GEOS-8033\" target=\"_blank\" rel=\"noopener noreferrer\">https://osgeo-org.atlassian.net/browse/GEOS-8033&nbsp;</a></p>",
        "earn": 2500,
        "evaluation": "<p class=\"MsoNormal\">Proposals will be evaluated based on the following:</p>\n<ul style=\"list-style-type: disc;\">\n<li class=\"MsoNormal\">Knowledge and experience with Java (30 points)</li>\n<li class=\"MsoNormal\">Knowledge and experience with GeoServer source code (30 points)</li>\n<li class=\"MsoNormal\">Knowledge and experience with KML output source code within GeoServer (40 points)</li>\n</ul>",
        "github": "https://github.com/bcgov/databc-web-map-services/issues/3",
        "isPublished": true,
        "name": "First Issue",
        "program": {
            "_id": "589101d9677cb9001c6b6d01",
            "code": "pro-databc",
            "isPublished": true,
            "logo": "uploads/logo-1489508615475.png",
            "title": "DataBC"
        },
        "project": {
            "_id": "589104a8677cb9001c6b6d05",
            "code": "prj-data-bc-web-map-services",
            "isPublished": true,
            "name": "DataBC Web Map Services"
        },
        "proposalEmail": "Michelle.Douville@gov.bc.ca",
        "short": "Is Java one of your languages of choice?  Do you value the ability to visualize geographic data on open source software?  If so, check out this GeoServer product enhancement request and opportunity to work with the team @ DataBC.",
        "skills": [
            "GeoServer",
            "Java",
            "KML",
            "GitHub"
        ],
        "start": "2017-04-05T07:00:00.000Z",
        "status": "Pending",
        "tags": [],
        "updated": "2017-03-16T18:54:51.851Z",
        "updatedBy": {
            "_id": "58c89d9caa383e001d84d3fe",
            "displayName": "Nicole De Greef"
        },
        "userIs": {
            "admin": false,
            "gov": false,
            "member": false,
            "request": false
        },
        "wasPublished": true
    }
]'''

