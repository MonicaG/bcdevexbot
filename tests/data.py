"""
test responses for the BCDevExchange API calls
"""
no_issues = '{"issues": []}'

one_issue = r'''{
    "issues": [
        {
            "assignee": null,
            "body": "<a rel=\"Inspiration\" href=\"https://github.com/BCDevExchange/docs/blob/master/discussion/projectstates.md\"><img alt=\"An idea being explored and shaped. Open for discussion, but may never go anywhere.\" style=\"border-width:0\" src=\"http://bcdevexchange.org/badge/1.svg\" title=\"An idea being explored and shaped. Open for discussion, but may never go anywhere.\" /></a> \r\n\r\n# Story:\r\n\r\nAs a product owner I have discovered that the favourites tree is not working correctly as there is a threshold after which the favourites content tree becomes non-functional.\r\n\r\n \r\n\r\n# Additional detail:\r\n\r\n \r\n\r\nGoto: http://www.bclaws.ca/civix/content/complete/statreg/?xsl=/templates/browse.xsl and click on Favourites. As a “Content Distributor” the user may already have a favourites tree but when they point a lot of content at it (Goto: http://www.bclaws.ca/civix/content/arch_oic/arc_oic/?xsl=/templates/browse.xsl) the content tree becomes overwhelmed; so as an interim solution it was removed. So it’s not so much that the piece of work is adding documents, this is done through the application layer and consumed through the API interface, but that as I add documents the trees performance degrades to an unacceptable level.\r\n\r\n \r\n\r\n# Acceptance criteria:\r\n\r\n1. Javascript tree contains a list of nodes that users can select.\r\n\r\n2. Tree is created using the content API as described: http://www.bclaws.ca/civix/template/complete/api/EP_API_content.html\r\n\r\n3. Selected nodes are stored in a cookie called favIDS, as a list of ancestors separated by comma. Each selection/deselection of a folder/document updates the cookie and adds/deletes the corresponding ancestor to the listTree and should default open to the lowest complete branch. Examples:\r\n\r\n\t* If “A” is selected in its entirety Tree should open to the “A” folder\r\n\r\n\t* If “Access to Education” is selected in its entirety Tree should open to “Access to Education”\r\n\r\n\t* If “Access to Education” and the “P” folder is selected in its entirety the Tree should open to both “Access to Education” and the “P” folder\r\n\r\n4. The list should also be adjusted such that if a parent is selected, the parent ancestor is added to the list and existing children ancestors are deleted.\r\n\r\n5. The Advanced favourite search feature will grab all the ancestors in the cookie. If html5 storage is present, it is used instead of the cookie.\r\n\r\n6. Tree must be able to be cleared using the clear favourites as per:\r\nhttp://www.bclaws.ca/civix/content/complete/statreg/?xsl=/templates/browse.xsl\r\n\r\n7. Tree should not substantially degrade in performance when used against larger document collections such as the Historical OIC collection:\r\nhttp://www.bclaws.ca/civix/content/arch_oic/arc_oic/\r\n\r\n8. Tree should outperform current tree load time by 3X when initially loaded with browser session information cleared. Firefox web-developer profiler will be used to determine the success of the test.\r\n\r\n# How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines](https://github.com/bcgov/bc-laws-api/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page](https://bcdevexchange.org/programs/BC%20Laws) for more information on our work.",
            "closed_at": null,
            "comments": 17,
            "comments_url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4/comments",
            "created_at": "2015-09-03T21:20:00Z",
            "devXProgramNm": "BC Laws",
            "events_url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4/events",
            "html_url": "https://github.com/bcgov/bc-laws-api/issues/4",
            "id": 101,
            "labels": [
                {
                    "color": "0052cc",
                    "name": "$1000",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/$1000"
                },
                {
                    "color": "fc2929",
                    "name": "bug",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/bug"
                },
                {
                    "color": "159818",
                    "name": "help wanted",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/help%20wanted"
                },
                {
                    "color": "eb6420",
                    "name": "Java",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/Java"
                },
                {
                    "color": "eb6420",
                    "name": "jQuery",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/jQuery"
                },
                {
                    "color": "eb6420",
                    "name": "JSON",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/JSON"
                },
                {
                    "color": "eb6420",
                    "name": "restAPI",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/restAPI"
                },
                {
                    "color": "eb6420",
                    "name": "XML",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/XML"
                }
            ],
            "labels_url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4/labels{/name}",
            "locked": false,
            "milestone": null,
            "number": 4,
            "repository_url": "https://api.github.com/repos/bcgov/bc-laws-api",
            "state": "open",
            "title": "Favourites Tree Threshold Limit Break",
            "updated_at": "2016-03-21T18:36:04Z",
            "url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4",
            "user": {
                "avatar_url": "https://avatars.githubusercontent.com/u/123?v=3",
                "events_url": "https://api.github.com/users/user1/events{/privacy}",
                "followers_url": "https://api.github.com/users/user1/followers",
                "following_url": "https://api.github.com/users/user1/following{/other_user}",
                "gists_url": "https://api.github.com/users/user1/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/user1",
                "id": 123,
                "login": "user1",
                "organizations_url": "https://api.github.com/users/user1/orgs",
                "received_events_url": "https://api.github.com/users/user1/received_events",
                "repos_url": "https://api.github.com/users/user1/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/user1/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/user1/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/user1"
            }
        }
    ]
}'''

two_issues = r'''{
    "issues": [
        {
            "assignee": null,
            "body": "<a rel=\"Inspiration\" href=\"https://github.com/BCDevExchange/docs/blob/master/discussion/projectstates.md\"><img alt=\"An idea being explored and shaped. Open for discussion, but may never go anywhere.\" style=\"border-width:0\" src=\"http://bcdevexchange.org/badge/1.svg\" title=\"An idea being explored and shaped. Open for discussion, but may never go anywhere.\" /></a> \r\n\r\n# Story:\r\n\r\nAs a product owner I have discovered that the favourites tree is not working correctly as there is a threshold after which the favourites content tree becomes non-functional.\r\n\r\n \r\n\r\n# Additional detail:\r\n\r\n \r\n\r\nGoto: http://www.bclaws.ca/civix/content/complete/statreg/?xsl=/templates/browse.xsl and click on Favourites. As a “Content Distributor” the user may already have a favourites tree but when they point a lot of content at it (Goto: http://www.bclaws.ca/civix/content/arch_oic/arc_oic/?xsl=/templates/browse.xsl) the content tree becomes overwhelmed; so as an interim solution it was removed. So it’s not so much that the piece of work is adding documents, this is done through the application layer and consumed through the API interface, but that as I add documents the trees performance degrades to an unacceptable level.\r\n\r\n \r\n\r\n# Acceptance criteria:\r\n\r\n1. Javascript tree contains a list of nodes that users can select.\r\n\r\n2. Tree is created using the content API as described: http://www.bclaws.ca/civix/template/complete/api/EP_API_content.html\r\n\r\n3. Selected nodes are stored in a cookie called favIDS, as a list of ancestors separated by comma. Each selection/deselection of a folder/document updates the cookie and adds/deletes the corresponding ancestor to the listTree and should default open to the lowest complete branch. Examples:\r\n\r\n\t* If “A” is selected in its entirety Tree should open to the “A” folder\r\n\r\n\t* If “Access to Education” is selected in its entirety Tree should open to “Access to Education”\r\n\r\n\t* If “Access to Education” and the “P” folder is selected in its entirety the Tree should open to both “Access to Education” and the “P” folder\r\n\r\n4. The list should also be adjusted such that if a parent is selected, the parent ancestor is added to the list and existing children ancestors are deleted.\r\n\r\n5. The Advanced favourite search feature will grab all the ancestors in the cookie. If html5 storage is present, it is used instead of the cookie.\r\n\r\n6. Tree must be able to be cleared using the clear favourites as per:\r\nhttp://www.bclaws.ca/civix/content/complete/statreg/?xsl=/templates/browse.xsl\r\n\r\n7. Tree should not substantially degrade in performance when used against larger document collections such as the Historical OIC collection:\r\nhttp://www.bclaws.ca/civix/content/arch_oic/arc_oic/\r\n\r\n8. Tree should outperform current tree load time by 3X when initially loaded with browser session information cleared. Firefox web-developer profiler will be used to determine the success of the test.\r\n\r\n# How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines](https://github.com/bcgov/bc-laws-api/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page](https://bcdevexchange.org/programs/BC%20Laws) for more information on our work.",
            "closed_at": null,
            "comments": 17,
            "comments_url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4/comments",
            "created_at": "2015-09-03T21:20:00Z",
            "devXProgramNm": "BC Laws",
            "events_url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4/events",
            "html_url": "https://github.com/bcgov/bc-laws-api/issues/4",
            "id": 101,
            "labels": [
                {
                    "color": "0052cc",
                    "name": "$1000",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/$1000"
                },
                {
                    "color": "fc2929",
                    "name": "bug",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/bug"
                },
                {
                    "color": "159818",
                    "name": "help wanted",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/help%20wanted"
                },
                {
                    "color": "eb6420",
                    "name": "Java",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/Java"
                },
                {
                    "color": "eb6420",
                    "name": "jQuery",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/jQuery"
                },
                {
                    "color": "eb6420",
                    "name": "JSON",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/JSON"
                },
                {
                    "color": "eb6420",
                    "name": "restAPI",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/restAPI"
                },
                {
                    "color": "eb6420",
                    "name": "XML",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/XML"
                }
            ],
            "labels_url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4/labels{/name}",
            "locked": false,
            "milestone": null,
            "number": 4,
            "repository_url": "https://api.github.com/repos/bcgov/bc-laws-api",
            "state": "open",
            "title": "Favourites Tree Threshold Limit Break",
            "updated_at": "2016-03-21T18:36:04Z",
            "url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4",
            "user": {
                "avatar_url": "https://avatars.githubusercontent.com/u/123?v=3",
                "events_url": "https://api.github.com/users/user1/events{/privacy}",
                "followers_url": "https://api.github.com/users/user1/followers",
                "following_url": "https://api.github.com/users/user1/following{/other_user}",
                "gists_url": "https://api.github.com/users/user1/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/user1",
                "id": 123,
                "login": "user1",
                "organizations_url": "https://api.github.com/users/user1/orgs",
                "received_events_url": "https://api.github.com/users/user1/received_events",
                "repos_url": "https://api.github.com/users/user1/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/user1/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/user1/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/user1"
            }
        },
        {
            "assignee": null,
            "body": "# Load More\r\n## Background\r\nWe are looking to build upon the default core SAGE framework/WP OOTB commenting system.  As fans of the plug and play model, we are trying to accomplish this in a modular way for obvious reasons.  Through UX testing, our audience has identified three short comings to overcome: sorting, filtering and sequential loading.  This ticket, we are going to focus on sequential loading. \r\n\r\n### Story\r\nI want to be able to interact with groupings of comments dynamically so I can restrict the information presented to me for a more effective consultation experience.\r\n\r\n## Acceptance Criteria\r\n1. A user will read through a subset of comments on a page or post and:\r\n  * select 'load more' to view the next subset of comments \r\n  * can continue to select 'load more' until all comments are present \r\n2. A user will read through a subset of replies within a thread on a page or post and:\r\n  * select 'load more' to view the next subset of comments \r\n  * can continue to select 'load more' until all comments are present \r\n3. The admin of the blog can set the number of comments and replies within a set.\r\n4. Ideally, the solution will perform these using AJAX calls.\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines] (https://github.com/bcgov/citizen-engagement-web-toolkit/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page] (https://bcdevexchange.org/programs/Citizen%20Engagement%20Web%20Toolkit)  for more information on our work.",
            "closed_at": null,
            "comments": 22,
            "comments_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/comments",
            "created_at": "2015-12-12T00:54:18Z",
            "devXProgramNm": "Citizen Engagement Web Toolkit",
            "events_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/events",
            "html_url": "https://github.com/bcgov/citizen-engagement-web-toolkit/issues/7",
            "id": 102,
            "labels": [
                {
                    "color": "0052cc",
                    "name": "$1000",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/$1000"
                },
                {
                    "color": "eb6420",
                    "name": "Bootstrap",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/Bootstrap"
                },
                {
                    "color": "eb6420",
                    "name": "CSS",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/CSS"
                },
                {
                    "color": "84b6eb",
                    "name": "enhancement",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/enhancement"
                },
                {
                    "color": "159818",
                    "name": "help wanted",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/help%20wanted"
                },
                {
                    "color": "eb6420",
                    "name": "HTML",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/HTML"
                },
                {
                    "color": "eb6420",
                    "name": "JavaScript",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/JavaScript"
                },
                {
                    "color": "eb6420",
                    "name": "jQuery",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/jQuery"
                },
                {
                    "color": "eb6420",
                    "name": "PHP",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/PHP"
                },
                {
                    "color": "eb6420",
                    "name": "WordPress",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/WordPress"
                }
            ],
            "labels_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/labels{/name}",
            "locked": false,
            "milestone": null,
            "number": 7,
            "repository_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit",
            "state": "open",
            "title": "Upgrade WP Sage Core Commenting - Part Three - Load More",
            "updated_at": "2016-03-08T23:02:07Z",
            "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7",
            "user": {
                "avatar_url": "https://avatars.githubusercontent.com/u/9876?v=3",
                "events_url": "https://api.github.com/users/user2/events{/privacy}",
                "followers_url": "https://api.github.com/users/user2/followers",
                "following_url": "https://api.github.com/users/user2/following{/other_user}",
                "gists_url": "https://api.github.com/users/user2/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/user2",
                "id": 9876,
                "login": "user2",
                "organizations_url": "https://api.github.com/users/user2/orgs",
                "received_events_url": "https://api.github.com/users/user2/received_events",
                "repos_url": "https://api.github.com/users/user2/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/user2/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/user2/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/user2"
            }
        }
    ]
}'''


missing_id = r'''{
    "issues": [
        {
            "assignee": null,
            "body": "<a rel=\"Inspiration\" href=\"https://github.com/BCDevExchange/docs/blob/master/discussion/projectstates.md\"><img alt=\"An idea being explored and shaped. Open for discussion, but may never go anywhere.\" style=\"border-width:0\" src=\"http://bcdevexchange.org/badge/1.svg\" title=\"An idea being explored and shaped. Open for discussion, but may never go anywhere.\" /></a> \r\n\r\n# Story:\r\n\r\nAs a product owner I have discovered that the favourites tree is not working correctly as there is a threshold after which the favourites content tree becomes non-functional.\r\n\r\n \r\n\r\n# Additional detail:\r\n\r\n \r\n\r\nGoto: http://www.bclaws.ca/civix/content/complete/statreg/?xsl=/templates/browse.xsl and click on Favourites. As a “Content Distributor” the user may already have a favourites tree but when they point a lot of content at it (Goto: http://www.bclaws.ca/civix/content/arch_oic/arc_oic/?xsl=/templates/browse.xsl) the content tree becomes overwhelmed; so as an interim solution it was removed. So it’s not so much that the piece of work is adding documents, this is done through the application layer and consumed through the API interface, but that as I add documents the trees performance degrades to an unacceptable level.\r\n\r\n \r\n\r\n# Acceptance criteria:\r\n\r\n1. Javascript tree contains a list of nodes that users can select.\r\n\r\n2. Tree is created using the content API as described: http://www.bclaws.ca/civix/template/complete/api/EP_API_content.html\r\n\r\n3. Selected nodes are stored in a cookie called favIDS, as a list of ancestors separated by comma. Each selection/deselection of a folder/document updates the cookie and adds/deletes the corresponding ancestor to the listTree and should default open to the lowest complete branch. Examples:\r\n\r\n\t* If “A” is selected in its entirety Tree should open to the “A” folder\r\n\r\n\t* If “Access to Education” is selected in its entirety Tree should open to “Access to Education”\r\n\r\n\t* If “Access to Education” and the “P” folder is selected in its entirety the Tree should open to both “Access to Education” and the “P” folder\r\n\r\n4. The list should also be adjusted such that if a parent is selected, the parent ancestor is added to the list and existing children ancestors are deleted.\r\n\r\n5. The Advanced favourite search feature will grab all the ancestors in the cookie. If html5 storage is present, it is used instead of the cookie.\r\n\r\n6. Tree must be able to be cleared using the clear favourites as per:\r\nhttp://www.bclaws.ca/civix/content/complete/statreg/?xsl=/templates/browse.xsl\r\n\r\n7. Tree should not substantially degrade in performance when used against larger document collections such as the Historical OIC collection:\r\nhttp://www.bclaws.ca/civix/content/arch_oic/arc_oic/\r\n\r\n8. Tree should outperform current tree load time by 3X when initially loaded with browser session information cleared. Firefox web-developer profiler will be used to determine the success of the test.\r\n\r\n# How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines](https://github.com/bcgov/bc-laws-api/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page](https://bcdevexchange.org/programs/BC%20Laws) for more information on our work.",
            "closed_at": null,
            "comments": 17,
            "comments_url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4/comments",
            "created_at": "2015-09-03T21:20:00Z",
            "devXProgramNm": "BC Laws",
            "events_url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4/events",
            "html_url": "https://github.com/bcgov/bc-laws-api/issues/4",
            "id": 101,
            "labels": [
                {
                    "color": "0052cc",
                    "name": "$1000",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/$1000"
                },
                {
                    "color": "fc2929",
                    "name": "bug",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/bug"
                },
                {
                    "color": "159818",
                    "name": "help wanted",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/help%20wanted"
                },
                {
                    "color": "eb6420",
                    "name": "Java",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/Java"
                },
                {
                    "color": "eb6420",
                    "name": "jQuery",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/jQuery"
                },
                {
                    "color": "eb6420",
                    "name": "JSON",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/JSON"
                },
                {
                    "color": "eb6420",
                    "name": "restAPI",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/restAPI"
                },
                {
                    "color": "eb6420",
                    "name": "XML",
                    "url": "https://api.github.com/repos/bcgov/bc-laws-api/labels/XML"
                }
            ],
            "labels_url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4/labels{/name}",
            "locked": false,
            "milestone": null,
            "number": 4,
            "repository_url": "https://api.github.com/repos/bcgov/bc-laws-api",
            "state": "open",
            "title": "Favourites Tree Threshold Limit Break",
            "updated_at": "2016-03-21T18:36:04Z",
            "url": "https://api.github.com/repos/bcgov/bc-laws-api/issues/4",
            "user": {
                "avatar_url": "https://avatars.githubusercontent.com/u/123?v=3",
                "events_url": "https://api.github.com/users/user1/events{/privacy}",
                "followers_url": "https://api.github.com/users/user1/followers",
                "following_url": "https://api.github.com/users/user1/following{/other_user}",
                "gists_url": "https://api.github.com/users/user1/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/user1",
                "id": 123,
                "login": "user1",
                "organizations_url": "https://api.github.com/users/user1/orgs",
                "received_events_url": "https://api.github.com/users/user1/received_events",
                "repos_url": "https://api.github.com/users/user1/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/user1/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/user1/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/user1"
            }
        },
        {
            "assignee": null,
            "body": "# Load More\r\n## Background\r\nWe are looking to build upon the default core SAGE framework/WP OOTB commenting system.  As fans of the plug and play model, we are trying to accomplish this in a modular way for obvious reasons.  Through UX testing, our audience has identified three short comings to overcome: sorting, filtering and sequential loading.  This ticket, we are going to focus on sequential loading. \r\n\r\n### Story\r\nI want to be able to interact with groupings of comments dynamically so I can restrict the information presented to me for a more effective consultation experience.\r\n\r\n## Acceptance Criteria\r\n1. A user will read through a subset of comments on a page or post and:\r\n  * select 'load more' to view the next subset of comments \r\n  * can continue to select 'load more' until all comments are present \r\n2. A user will read through a subset of replies within a thread on a page or post and:\r\n  * select 'load more' to view the next subset of comments \r\n  * can continue to select 'load more' until all comments are present \r\n3. The admin of the blog can set the number of comments and replies within a set.\r\n4. Ideally, the solution will perform these using AJAX calls.\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines] (https://github.com/bcgov/citizen-engagement-web-toolkit/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page] (https://bcdevexchange.org/programs/Citizen%20Engagement%20Web%20Toolkit)  for more information on our work.",
            "closed_at": null,
            "comments": 22,
            "comments_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/comments",
            "created_at": "2015-12-12T00:54:18Z",
            "devXProgramNm": "Citizen Engagement Web Toolkit",
            "events_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/events",
            "html_url": "https://github.com/bcgov/citizen-engagement-web-toolkit/issues/7",
            "labels": [
                {
                    "color": "0052cc",
                    "name": "$1000",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/$1000"
                },
                {
                    "color": "eb6420",
                    "name": "Bootstrap",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/Bootstrap"
                },
                {
                    "color": "eb6420",
                    "name": "CSS",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/CSS"
                },
                {
                    "color": "84b6eb",
                    "name": "enhancement",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/enhancement"
                },
                {
                    "color": "159818",
                    "name": "help wanted",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/help%20wanted"
                },
                {
                    "color": "eb6420",
                    "name": "HTML",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/HTML"
                },
                {
                    "color": "eb6420",
                    "name": "JavaScript",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/JavaScript"
                },
                {
                    "color": "eb6420",
                    "name": "jQuery",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/jQuery"
                },
                {
                    "color": "eb6420",
                    "name": "PHP",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/PHP"
                },
                {
                    "color": "eb6420",
                    "name": "WordPress",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/WordPress"
                }
            ],
            "labels_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/labels{/name}",
            "locked": false,
            "milestone": null,
            "number": 7,
            "repository_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit",
            "state": "open",
            "title": "Upgrade WP Sage Core Commenting - Part Three - Load More",
            "updated_at": "2016-03-08T23:02:07Z",
            "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7",
            "user": {
                "avatar_url": "https://avatars.githubusercontent.com/u/9876?v=3",
                "events_url": "https://api.github.com/users/user2/events{/privacy}",
                "followers_url": "https://api.github.com/users/user2/followers",
                "following_url": "https://api.github.com/users/user2/following{/other_user}",
                "gists_url": "https://api.github.com/users/user2/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/user2",
                "id": 9876,
                "login": "user2",
                "organizations_url": "https://api.github.com/users/user2/orgs",
                "received_events_url": "https://api.github.com/users/user2/received_events",
                "repos_url": "https://api.github.com/users/user2/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/user2/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/user2/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/user2"
            }
        },
        {
            "assignee": null,
            "body": "# Sorting\r\n## Background\r\nWe are looking to build upon the default core SAGE framework/WP OOTB commenting system.  As fans of the plug and play model, we are trying to accomplish this in a modular way for obvious reasons.  Through UX testing, our audience has identified three short comings to overcome: sorting, filtering and sequential loading.  This ticket, we are going to focus on Sorting.\r\n\r\n### Story\r\nI want to be able to sort blog comments by date and number of replies so that I can find information more easily to engage in consultations. \r\n\r\n## Acceptance Criteria\r\n1. A user selects a sort by date toggle: \r\n  * the initial state is most recent.  \r\n  * Toggle and the comments are returned by oldest.  \r\n  * Toggle again and the sort and the comments are returned by most recent.\r\n2. A user selects to sort by number of replies toggle, the initial state is default, with no sort applied at all. \r\n  * Toggle once and the comments are returned by the highest number of replies, \r\n  * toggle twice and the comments are returned by the least number of replies, \r\n  * and finally toggle three times and the comments are returned at the default.  \r\n3.  Ideally, the solution will have AJAX response for UX.\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines] (https://github.com/bcgov/citizen-engagement-web-toolkit/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page] (https://bcdevexchange.org/programs/Citizen%20Engagement%20Web%20Toolkit)  for more information on our work.",
            "closed_at": null,
            "comments": 19,
            "comments_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/5/comments",
            "created_at": "2015-12-11T19:37:22Z",
            "devXProgramNm": "Citizen Engagement Web Toolkit",
            "events_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/5/events",
            "html_url": "https://github.com/bcgov/citizen-engagement-web-toolkit/issues/5",
            "id": 103,
            "labels": [
                {
                    "color": "0052cc",
                    "name": "$1000",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/$1000"
                },
                {
                    "color": "eb6420",
                    "name": "Bootstrap",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/Bootstrap"
                },
                {
                    "color": "eb6420",
                    "name": "CSS",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/CSS"
                },
                {
                    "color": "84b6eb",
                    "name": "enhancement",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/enhancement"
                },
                {
                    "color": "159818",
                    "name": "help wanted",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/help%20wanted"
                },
                {
                    "color": "eb6420",
                    "name": "HTML",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/HTML"
                },
                {
                    "color": "eb6420",
                    "name": "JavaScript",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/JavaScript"
                },
                {
                    "color": "eb6420",
                    "name": "jQuery",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/jQuery"
                },
                {
                    "color": "eb6420",
                    "name": "PHP",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/PHP"
                },
                {
                    "color": "eb6420",
                    "name": "WordPress",
                    "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/WordPress"
                }
            ],
            "labels_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/5/labels{/name}",
            "locked": false,
            "milestone": null,
            "number": 5,
            "repository_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit",
            "state": "open",
            "title": "Upgrade WP Sage Core Commenting - Part One - Sorting",
            "updated_at": "2016-02-23T00:19:34Z",
            "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/5",
            "user": {
                "avatar_url": "https://avatars.githubusercontent.com/u/1009?v=3",
                "events_url": "https://api.github.com/users/user3/events{/privacy}",
                "followers_url": "https://api.github.com/users/user3/followers",
                "following_url": "https://api.github.com/users/user3/following{/other_user}",
                "gists_url": "https://api.github.com/users/user3/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/user3",
                "id": 1009,
                "login": "user3",
                "organizations_url": "https://api.github.com/users/user3/orgs",
                "received_events_url": "https://api.github.com/users/user3/received_events",
                "repos_url": "https://api.github.com/users/user3/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/user3/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/user3/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/user3"
            }
        }
    ]
}'''