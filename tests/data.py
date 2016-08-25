""" Test responses for the BCDevExchange API calls """

no_issues = '{"open": [], "closed": [], "inprogress": [], "blocked": []}'

one_issue = r'''{
   "open": [
        {
          "url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10",
          "repository_url": "https://api.github.com/repos/bcgov/interactive-infographic",
          "labels_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10/labels{/name}",
          "comments_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10/comments",
          "events_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10/events",
          "html_url": "https://github.com/bcgov/first-issue",
          "id": 101,
          "number": 10,
          "title": "First Issue",
          "user": {
            "login": "jeetz2",
            "id": 18408736,
            "avatar_url": "https://avatars.githubusercontent.com/u/18408736?v=3",
            "gravatar_id": "",
            "url": "https://api.github.com/users/jeetz2",
            "html_url": "https://github.com/jeetz2",
            "followers_url": "https://api.github.com/users/jeetz2/followers",
            "following_url": "https://api.github.com/users/jeetz2/following{/other_user}",
            "gists_url": "https://api.github.com/users/jeetz2/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/jeetz2/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/jeetz2/subscriptions",
            "organizations_url": "https://api.github.com/users/jeetz2/orgs",
            "repos_url": "https://api.github.com/users/jeetz2/repos",
            "events_url": "https://api.github.com/users/jeetz2/events{/privacy}",
            "received_events_url": "https://api.github.com/users/jeetz2/received_events",
            "type": "User",
            "site_admin": false
          },
          "labels": [
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/$1000",
              "name": "$1000",
              "color": "0052cc"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/help%20wanted",
              "name": "help wanted",
              "color": "128A0C"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Java",
              "name": "Java",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Jquery",
              "name": "Jquery",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/UI/UX",
              "name": "UI/UX",
              "color": "eb6420"
            }
          ],
          "state": "open",
          "locked": false,
          "assignee": null,
          "assignees": [],
          "milestone": null,
          "comments": 7,
          "created_at": "2016-08-05T21:50:58Z",
          "updated_at": "2016-08-19T22:20:49Z",
          "closed_at": null,
          "body": "# Background\r\nThe OCIO is looking for the development of an online infographic for users to interact with. The purpose is to clearly convey multi-dimensional information in a user-friendly, interactive, digital format. \r\n\r\nA prototype of the online infographic was developed by @coakenfold which demonstrates basic functionality (reference  #9). The OCIO now wants to build out a minimum viable product (MVP) based on the prototype and a **recently updated** [OCIO Strategic FrameWork diagram](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/ocio_framework_2016%20v4.pdf).\r\n\r\nSee the [Readme](https://github.com/bcgov/interactive-infographic/blob/master/README.md) for more info.\r\n\r\n### Story\r\nAs a product owner, I want to be able to create an MVP of an interactive infographic web-app so that that I can circulate it among my government colleagues for feedback.\r\n\r\n## Acceptance Criteria\r\n\r\n1. Develop a MVP of a dynamic version of the [OCIO Strategic FrameWork diagram](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/ocio_framework_2016%20v4.pdf). See this [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png) that illustrates how the interactive infographic might be structured. The MVP should make all of the relevant elements in the diagram interactive (e.g. bootstrap jQuery plugins: accordion, popovers, video, etc...). The MVP should also be made aesthetically appealing and visually similar to the latest diagram provided. Some exceptions are expected and the developer should communicate any recommended changes that would improve the online experience (e.g. the developer can ignore/remove the 3 vertical columns on the left side of the diagram). Dummy text content can be used where required and government staff can update the content after the issue is closed.\r\n\r\nThe following acceptance criteria from the previous issue (#2) remain applicable:\r\n2. Allow the insertion and deletion of content boxes (i.e. rows, see [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png)).\r\n3. Allow the insertion and deletion of content elements (i.e. see [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png)).\r\n4. Content box should have the ability to contain multiple content elements that scale according to the number of content elements. \r\n5. Allow the insertion and deletion of graphics (and perhaps text) into the content elements.\r\n6. When a user clicks on a content element (every row, or content box, should have this capability), an accordion window will expand/appear underneath. This [second diagram](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/user-interaction.png) illustrates how a user might interact with the infographic.\r\n7. Allow the insertion and deletion of content in accordion windows, including text and hyperlinks (possibly graphics).\r\n8. Support vector graphics. You can use example graphics and text for the prototype.\r\n9. Provide the final product in a format that can be run on any computer (localhost) through any modern web-browser.\r\n10. Device agnostic and responsive.\r\n11. Use of commonly known, open web frameworks.\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines](https://github.com/bcgov/interactive-infographic/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page](https://bcdevexchange.org/programs/OCIO%20Tech%20Strategies)  for more information on our work.\r\n",
          "program": "OCIO Tech Strategies",
          "skill": [
            "Java",
            "Jquery",
            "UI/UX"
          ],
          "earn": [
            "$1000"
          ]
        }
    ],
   "closed": [
        {
          "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7",
          "repository_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit",
          "labels_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/labels{/name}",
          "comments_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/comments",
          "events_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/events",
          "html_url": "https://github.com/bcgov/citizen-engagement-web-toolkit/issues/7",
          "id": 121821329,
          "number": 7,
          "title": "Upgrade WP Sage Core Commenting - Part Three - Load More",
          "user": {
            "login": "juhewitt",
            "id": 15350676,
            "avatar_url": "https://avatars.githubusercontent.com/u/15350676?v=3",
            "gravatar_id": "",
            "url": "https://api.github.com/users/juhewitt",
            "html_url": "https://github.com/juhewitt",
            "followers_url": "https://api.github.com/users/juhewitt/followers",
            "following_url": "https://api.github.com/users/juhewitt/following{/other_user}",
            "gists_url": "https://api.github.com/users/juhewitt/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/juhewitt/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/juhewitt/subscriptions",
            "organizations_url": "https://api.github.com/users/juhewitt/orgs",
            "repos_url": "https://api.github.com/users/juhewitt/repos",
            "events_url": "https://api.github.com/users/juhewitt/events{/privacy}",
            "received_events_url": "https://api.github.com/users/juhewitt/received_events",
            "type": "User",
            "site_admin": false
          },
          "labels": [
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/$1000",
              "name": "$1000",
              "color": "0052cc"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/Bootstrap",
              "name": "Bootstrap",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/CSS",
              "name": "CSS",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/enhancement",
              "name": "enhancement",
              "color": "84b6eb"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/help%20wanted",
              "name": "help wanted",
              "color": "159818"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/HTML",
              "name": "HTML",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/JavaScript",
              "name": "JavaScript",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/jQuery",
              "name": "jQuery",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/PHP",
              "name": "PHP",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/WordPress",
              "name": "WordPress",
              "color": "eb6420"
            }
          ],
          "state": "closed",
          "locked": false,
          "assignee": null,
          "assignees": [],
          "milestone": null,
          "comments": 22,
          "created_at": "2015-12-12T00:54:18Z",
          "updated_at": "2016-03-08T23:02:07Z",
          "closed_at": "2016-03-08T23:02:02Z",
          "body": "# Load More\r\n## Background\r\nWe are looking to build upon the default core SAGE framework/WP OOTB commenting system.  As fans of the plug and play model, we are trying to accomplish this in a modular way for obvious reasons.  Through UX testing, our audience has identified three short comings to overcome: sorting, filtering and sequential loading.  This ticket, we are going to focus on sequential loading. \r\n\r\n### Story\r\nI want to be able to interact with groupings of comments dynamically so I can restrict the information presented to me for a more effective consultation experience.\r\n\r\n## Acceptance Criteria\r\n1. A user will read through a subset of comments on a page or post and:\r\n  * select 'load more' to view the next subset of comments \r\n  * can continue to select 'load more' until all comments are present \r\n2. A user will read through a subset of replies within a thread on a page or post and:\r\n  * select 'load more' to view the next subset of comments \r\n  * can continue to select 'load more' until all comments are present \r\n3. The admin of the blog can set the number of comments and replies within a set.\r\n4. Ideally, the solution will perform these using AJAX calls.\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines] (https://github.com/bcgov/citizen-engagement-web-toolkit/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page] (https://bcdevexchange.org/programs/Citizen%20Engagement%20Web%20Toolkit)  for more information on our work.",
          "program": "Citizen Engagement Web Toolkit",
          "skill": [
            "Bootstrap",
            "CSS",
            "HTML",
            "JavaScript",
            "jQuery",
            "PHP",
            "WordPress"
          ],
          "earn": [
            "$1000"
          ]
        }
    ],
    "inprogress": [],
    "blocked": []
}'''

two_issues = r'''{
   "open": [
        {
          "url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10",
          "repository_url": "https://api.github.com/repos/bcgov/interactive-infographic",
          "labels_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10/labels{/name}",
          "comments_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10/comments",
          "events_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10/events",
          "html_url": "https://github.com/bcgov/first-issue",
          "id": 101,
          "number": 10,
          "title": "First Issue",
          "user": {
            "login": "jeetz2",
            "id": 18408736,
            "avatar_url": "https://avatars.githubusercontent.com/u/18408736?v=3",
            "gravatar_id": "",
            "url": "https://api.github.com/users/jeetz2",
            "html_url": "https://github.com/jeetz2",
            "followers_url": "https://api.github.com/users/jeetz2/followers",
            "following_url": "https://api.github.com/users/jeetz2/following{/other_user}",
            "gists_url": "https://api.github.com/users/jeetz2/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/jeetz2/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/jeetz2/subscriptions",
            "organizations_url": "https://api.github.com/users/jeetz2/orgs",
            "repos_url": "https://api.github.com/users/jeetz2/repos",
            "events_url": "https://api.github.com/users/jeetz2/events{/privacy}",
            "received_events_url": "https://api.github.com/users/jeetz2/received_events",
            "type": "User",
            "site_admin": false
          },
          "labels": [
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/$1000",
              "name": "$1000",
              "color": "0052cc"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/help%20wanted",
              "name": "help wanted",
              "color": "128A0C"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Java",
              "name": "Java",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Jquery",
              "name": "Jquery",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/UI/UX",
              "name": "UI/UX",
              "color": "eb6420"
            }
          ],
          "state": "open",
          "locked": false,
          "assignee": null,
          "assignees": [],
          "milestone": null,
          "comments": 7,
          "created_at": "2016-08-05T21:50:58Z",
          "updated_at": "2016-08-19T22:20:49Z",
          "closed_at": null,
          "body": "# Background\r\nThe OCIO is looking for the development of an online infographic for users to interact with. The purpose is to clearly convey multi-dimensional information in a user-friendly, interactive, digital format. \r\n\r\nA prototype of the online infographic was developed by @coakenfold which demonstrates basic functionality (reference  #9). The OCIO now wants to build out a minimum viable product (MVP) based on the prototype and a **recently updated** [OCIO Strategic FrameWork diagram](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/ocio_framework_2016%20v4.pdf).\r\n\r\nSee the [Readme](https://github.com/bcgov/interactive-infographic/blob/master/README.md) for more info.\r\n\r\n### Story\r\nAs a product owner, I want to be able to create an MVP of an interactive infographic web-app so that that I can circulate it among my government colleagues for feedback.\r\n\r\n## Acceptance Criteria\r\n\r\n1. Develop a MVP of a dynamic version of the [OCIO Strategic FrameWork diagram](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/ocio_framework_2016%20v4.pdf). See this [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png) that illustrates how the interactive infographic might be structured. The MVP should make all of the relevant elements in the diagram interactive (e.g. bootstrap jQuery plugins: accordion, popovers, video, etc...). The MVP should also be made aesthetically appealing and visually similar to the latest diagram provided. Some exceptions are expected and the developer should communicate any recommended changes that would improve the online experience (e.g. the developer can ignore/remove the 3 vertical columns on the left side of the diagram). Dummy text content can be used where required and government staff can update the content after the issue is closed.\r\n\r\nThe following acceptance criteria from the previous issue (#2) remain applicable:\r\n2. Allow the insertion and deletion of content boxes (i.e. rows, see [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png)).\r\n3. Allow the insertion and deletion of content elements (i.e. see [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png)).\r\n4. Content box should have the ability to contain multiple content elements that scale according to the number of content elements. \r\n5. Allow the insertion and deletion of graphics (and perhaps text) into the content elements.\r\n6. When a user clicks on a content element (every row, or content box, should have this capability), an accordion window will expand/appear underneath. This [second diagram](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/user-interaction.png) illustrates how a user might interact with the infographic.\r\n7. Allow the insertion and deletion of content in accordion windows, including text and hyperlinks (possibly graphics).\r\n8. Support vector graphics. You can use example graphics and text for the prototype.\r\n9. Provide the final product in a format that can be run on any computer (localhost) through any modern web-browser.\r\n10. Device agnostic and responsive.\r\n11. Use of commonly known, open web frameworks.\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines](https://github.com/bcgov/interactive-infographic/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page](https://bcdevexchange.org/programs/OCIO%20Tech%20Strategies)  for more information on our work.\r\n",
          "program": "OCIO Tech Strategies",
          "skill": [
            "Java",
            "Jquery",
            "UI/UX"
          ],
          "earn": [
            "$1000"
          ]
        },
        {
          "url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/2",
          "repository_url": "https://api.github.com/repos/bcgov/interactive-infographic",
          "labels_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/2/labels{/name}",
          "comments_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/2/comments",
          "events_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/2/events",
          "html_url": "https://github.com/bcgov/second-issue",
          "id": 102,
          "number": 2,
          "title": "Second Issue",
          "user": {
            "login": "lmullane",
            "id": 12040839,
            "avatar_url": "https://avatars.githubusercontent.com/u/12040839?v=3",
            "gravatar_id": "",
            "url": "https://api.github.com/users/lmullane",
            "html_url": "https://github.com/lmullane",
            "followers_url": "https://api.github.com/users/lmullane/followers",
            "following_url": "https://api.github.com/users/lmullane/following{/other_user}",
            "gists_url": "https://api.github.com/users/lmullane/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/lmullane/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/lmullane/subscriptions",
            "organizations_url": "https://api.github.com/users/lmullane/orgs",
            "repos_url": "https://api.github.com/users/lmullane/repos",
            "events_url": "https://api.github.com/users/lmullane/events{/privacy}",
            "received_events_url": "https://api.github.com/users/lmullane/received_events",
            "type": "User",
            "site_admin": false
          },
          "labels": [
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/$1000",
              "name": "$1000",
              "color": "0052cc"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Graphic%20Design",
              "name": "Graphic Design",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/help%20wanted",
              "name": "help wanted",
              "color": "128A0C"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/HTML",
              "name": "HTML",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Java",
              "name": "Java",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Jquery",
              "name": "Jquery",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/UI/UX",
              "name": "UI/UX",
              "color": "eb6420"
            }
          ],
          "state": "open",
          "locked": false,
          "assignee": null,
          "assignees": [],
          "milestone": null,
          "comments": 23,
          "created_at": "2016-06-08T22:08:22Z",
          "updated_at": "2016-07-21T17:39:14Z",
          "closed_at": null,
          "body": "# Background\r\nThe OCIO is looking for the development of an online infographic for users to interact with. The purpose is to clearly convey multi-dimensional information in a user-friendly, interactive, digital format. \r\n\r\nThe work entails the development of a working prototype of a dynamic version of the [OCIO Strategic FrameWork diagram](https://raw.githubusercontent.com/bcgov/interactive-infographic/master/wireframe/OCIO_Strategy_Framework.png). The prototype must enable the layout and content to change as the strategy may change over time. \r\n\r\nSee the [Readme](https://github.com/bcgov/interactive-infographic/blob/master/README.md) for more info.\r\n\r\n### Story\r\nAs a product owner, I want to be able to create a working prototype of an interactive web-app so that that I can improve the experience and understanding of government strategy by using a visual, interactive digital format.\r\n\r\n## Acceptance Criteria\r\n\r\n\r\n1. Develop a working prototype of a dynamic version of the [OCIO Strategic FrameWork diagram](https://raw.githubusercontent.com/bcgov/interactive-infographic/master/wireframe/OCIO_Strategy_Framework.png). See this [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png) that illustrates how the interactive infographic might be structured.\r\n2. Allow the insertion and deletion of content boxes (i.e. rows, see [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png)).\r\n3. Allow the insertion and deletion of content elements (i.e. see [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png)).\r\n4. Content box should have the ability to contain multiple content elements that scale according to the number of content elements. Challenge us on this one if it's unrealistic.\r\n5. Allow the insertion and deletion of graphics (and perhaps text) into the content elements.\r\n6. When a user clicks on a content element (every row, or content box, should have this capability), an accordion window will expand/appear underneath. This [second diagram](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/user-interaction.png) illustrates how a user might interact with the infographic.\r\n7. Allow the insertion and deletion of content in accordion windows, including text and hyperlinks (possibly graphics).\r\n8. Support vector graphics. You can use example graphics and text for the prototype.\r\n9. Provide the final product in a format that can be run on any computer (localhost) through any modern web-browser.\r\n10. Device agnostic and responsive.\r\n11. Use of commonly known, open web frameworks.\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines](https://github.com/bcgov/interactive-infographic/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page](https://bcdevexchange.org/programs/OCIO%20Tech%20Strategies)  for more information on our work.\r\n",
          "program": "OCIO Tech Strategies",
          "skill": [
            "Graphic Design",
            "HTML",
            "Java",
            "Jquery",
            "UI/UX"
          ],
          "earn": [
            "$1000"
          ]
        }
    ],
   "closed": [
        {
          "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7",
          "repository_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit",
          "labels_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/labels{/name}",
          "comments_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/comments",
          "events_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/events",
          "html_url": "https://github.com/bcgov/citizen-engagement-web-toolkit/issues/7",
          "id": 121821329,
          "number": 7,
          "title": "Upgrade WP Sage Core Commenting - Part Three - Load More",
          "user": {
            "login": "juhewitt",
            "id": 15350676,
            "avatar_url": "https://avatars.githubusercontent.com/u/15350676?v=3",
            "gravatar_id": "",
            "url": "https://api.github.com/users/juhewitt",
            "html_url": "https://github.com/juhewitt",
            "followers_url": "https://api.github.com/users/juhewitt/followers",
            "following_url": "https://api.github.com/users/juhewitt/following{/other_user}",
            "gists_url": "https://api.github.com/users/juhewitt/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/juhewitt/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/juhewitt/subscriptions",
            "organizations_url": "https://api.github.com/users/juhewitt/orgs",
            "repos_url": "https://api.github.com/users/juhewitt/repos",
            "events_url": "https://api.github.com/users/juhewitt/events{/privacy}",
            "received_events_url": "https://api.github.com/users/juhewitt/received_events",
            "type": "User",
            "site_admin": false
          },
          "labels": [
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/$1000",
              "name": "$1000",
              "color": "0052cc"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/Bootstrap",
              "name": "Bootstrap",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/CSS",
              "name": "CSS",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/enhancement",
              "name": "enhancement",
              "color": "84b6eb"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/help%20wanted",
              "name": "help wanted",
              "color": "159818"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/HTML",
              "name": "HTML",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/JavaScript",
              "name": "JavaScript",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/jQuery",
              "name": "jQuery",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/PHP",
              "name": "PHP",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/WordPress",
              "name": "WordPress",
              "color": "eb6420"
            }
          ],
          "state": "closed",
          "locked": false,
          "assignee": null,
          "assignees": [],
          "milestone": null,
          "comments": 22,
          "created_at": "2015-12-12T00:54:18Z",
          "updated_at": "2016-03-08T23:02:07Z",
          "closed_at": "2016-03-08T23:02:02Z",
          "body": "# Load More\r\n## Background\r\nWe are looking to build upon the default core SAGE framework/WP OOTB commenting system.  As fans of the plug and play model, we are trying to accomplish this in a modular way for obvious reasons.  Through UX testing, our audience has identified three short comings to overcome: sorting, filtering and sequential loading.  This ticket, we are going to focus on sequential loading. \r\n\r\n### Story\r\nI want to be able to interact with groupings of comments dynamically so I can restrict the information presented to me for a more effective consultation experience.\r\n\r\n## Acceptance Criteria\r\n1. A user will read through a subset of comments on a page or post and:\r\n  * select 'load more' to view the next subset of comments \r\n  * can continue to select 'load more' until all comments are present \r\n2. A user will read through a subset of replies within a thread on a page or post and:\r\n  * select 'load more' to view the next subset of comments \r\n  * can continue to select 'load more' until all comments are present \r\n3. The admin of the blog can set the number of comments and replies within a set.\r\n4. Ideally, the solution will perform these using AJAX calls.\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines] (https://github.com/bcgov/citizen-engagement-web-toolkit/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page] (https://bcdevexchange.org/programs/Citizen%20Engagement%20Web%20Toolkit)  for more information on our work.",
          "program": "Citizen Engagement Web Toolkit",
          "skill": [
            "Bootstrap",
            "CSS",
            "HTML",
            "JavaScript",
            "jQuery",
            "PHP",
            "WordPress"
          ],
          "earn": [
            "$1000"
          ]
        }
    ],
    "inprogress": [],
    "blocked": []
}'''


missing_id = r'''{
   "open": [
        {
          "url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10",
          "repository_url": "https://api.github.com/repos/bcgov/interactive-infographic",
          "labels_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10/labels{/name}",
          "comments_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10/comments",
          "events_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/10/events",
          "html_url": "https://github.com/bcgov/first-issue",
          "id": 101,
          "number": 10,
          "title": "First Issue",
          "user": {
            "login": "jeetz2",
            "id": 18408736,
            "avatar_url": "https://avatars.githubusercontent.com/u/18408736?v=3",
            "gravatar_id": "",
            "url": "https://api.github.com/users/jeetz2",
            "html_url": "https://github.com/jeetz2",
            "followers_url": "https://api.github.com/users/jeetz2/followers",
            "following_url": "https://api.github.com/users/jeetz2/following{/other_user}",
            "gists_url": "https://api.github.com/users/jeetz2/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/jeetz2/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/jeetz2/subscriptions",
            "organizations_url": "https://api.github.com/users/jeetz2/orgs",
            "repos_url": "https://api.github.com/users/jeetz2/repos",
            "events_url": "https://api.github.com/users/jeetz2/events{/privacy}",
            "received_events_url": "https://api.github.com/users/jeetz2/received_events",
            "type": "User",
            "site_admin": false
          },
          "labels": [
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/$1000",
              "name": "$1000",
              "color": "0052cc"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/help%20wanted",
              "name": "help wanted",
              "color": "128A0C"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Java",
              "name": "Java",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Jquery",
              "name": "Jquery",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/UI/UX",
              "name": "UI/UX",
              "color": "eb6420"
            }
          ],
          "state": "open",
          "locked": false,
          "assignee": null,
          "assignees": [],
          "milestone": null,
          "comments": 7,
          "created_at": "2016-08-05T21:50:58Z",
          "updated_at": "2016-08-19T22:20:49Z",
          "closed_at": null,
          "body": "# Background\r\nThe OCIO is looking for the development of an online infographic for users to interact with. The purpose is to clearly convey multi-dimensional information in a user-friendly, interactive, digital format. \r\n\r\nA prototype of the online infographic was developed by @coakenfold which demonstrates basic functionality (reference  #9). The OCIO now wants to build out a minimum viable product (MVP) based on the prototype and a **recently updated** [OCIO Strategic FrameWork diagram](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/ocio_framework_2016%20v4.pdf).\r\n\r\nSee the [Readme](https://github.com/bcgov/interactive-infographic/blob/master/README.md) for more info.\r\n\r\n### Story\r\nAs a product owner, I want to be able to create an MVP of an interactive infographic web-app so that that I can circulate it among my government colleagues for feedback.\r\n\r\n## Acceptance Criteria\r\n\r\n1. Develop a MVP of a dynamic version of the [OCIO Strategic FrameWork diagram](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/ocio_framework_2016%20v4.pdf). See this [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png) that illustrates how the interactive infographic might be structured. The MVP should make all of the relevant elements in the diagram interactive (e.g. bootstrap jQuery plugins: accordion, popovers, video, etc...). The MVP should also be made aesthetically appealing and visually similar to the latest diagram provided. Some exceptions are expected and the developer should communicate any recommended changes that would improve the online experience (e.g. the developer can ignore/remove the 3 vertical columns on the left side of the diagram). Dummy text content can be used where required and government staff can update the content after the issue is closed.\r\n\r\nThe following acceptance criteria from the previous issue (#2) remain applicable:\r\n2. Allow the insertion and deletion of content boxes (i.e. rows, see [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png)).\r\n3. Allow the insertion and deletion of content elements (i.e. see [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png)).\r\n4. Content box should have the ability to contain multiple content elements that scale according to the number of content elements. \r\n5. Allow the insertion and deletion of graphics (and perhaps text) into the content elements.\r\n6. When a user clicks on a content element (every row, or content box, should have this capability), an accordion window will expand/appear underneath. This [second diagram](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/user-interaction.png) illustrates how a user might interact with the infographic.\r\n7. Allow the insertion and deletion of content in accordion windows, including text and hyperlinks (possibly graphics).\r\n8. Support vector graphics. You can use example graphics and text for the prototype.\r\n9. Provide the final product in a format that can be run on any computer (localhost) through any modern web-browser.\r\n10. Device agnostic and responsive.\r\n11. Use of commonly known, open web frameworks.\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines](https://github.com/bcgov/interactive-infographic/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page](https://bcdevexchange.org/programs/OCIO%20Tech%20Strategies)  for more information on our work.\r\n",
          "program": "OCIO Tech Strategies",
          "skill": [
            "Java",
            "Jquery",
            "UI/UX"
          ],
          "earn": [
            "$1000"
          ]
        },
        {
          "url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/2",
          "repository_url": "https://api.github.com/repos/bcgov/interactive-infographic",
          "labels_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/2/labels{/name}",
          "comments_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/2/comments",
          "events_url": "https://api.github.com/repos/bcgov/interactive-infographic/issues/2/events",
          "html_url": "https://github.com/bcgov/second-issue",
          "number": 2,
          "title": "Second Issue",
          "user": {
            "login": "lmullane",
            "id": 12040839,
            "avatar_url": "https://avatars.githubusercontent.com/u/12040839?v=3",
            "gravatar_id": "",
            "url": "https://api.github.com/users/lmullane",
            "html_url": "https://github.com/lmullane",
            "followers_url": "https://api.github.com/users/lmullane/followers",
            "following_url": "https://api.github.com/users/lmullane/following{/other_user}",
            "gists_url": "https://api.github.com/users/lmullane/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/lmullane/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/lmullane/subscriptions",
            "organizations_url": "https://api.github.com/users/lmullane/orgs",
            "repos_url": "https://api.github.com/users/lmullane/repos",
            "events_url": "https://api.github.com/users/lmullane/events{/privacy}",
            "received_events_url": "https://api.github.com/users/lmullane/received_events",
            "type": "User",
            "site_admin": false
          },
          "labels": [
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/$1000",
              "name": "$1000",
              "color": "0052cc"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Graphic%20Design",
              "name": "Graphic Design",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/help%20wanted",
              "name": "help wanted",
              "color": "128A0C"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/HTML",
              "name": "HTML",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Java",
              "name": "Java",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/Jquery",
              "name": "Jquery",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/interactive-infographic/labels/UI/UX",
              "name": "UI/UX",
              "color": "eb6420"
            }
          ],
          "state": "open",
          "locked": false,
          "assignee": null,
          "assignees": [],
          "milestone": null,
          "comments": 23,
          "created_at": "2016-06-08T22:08:22Z",
          "updated_at": "2016-07-21T17:39:14Z",
          "closed_at": null,
          "body": "# Background\r\nThe OCIO is looking for the development of an online infographic for users to interact with. The purpose is to clearly convey multi-dimensional information in a user-friendly, interactive, digital format. \r\n\r\nThe work entails the development of a working prototype of a dynamic version of the [OCIO Strategic FrameWork diagram](https://raw.githubusercontent.com/bcgov/interactive-infographic/master/wireframe/OCIO_Strategy_Framework.png). The prototype must enable the layout and content to change as the strategy may change over time. \r\n\r\nSee the [Readme](https://github.com/bcgov/interactive-infographic/blob/master/README.md) for more info.\r\n\r\n### Story\r\nAs a product owner, I want to be able to create a working prototype of an interactive web-app so that that I can improve the experience and understanding of government strategy by using a visual, interactive digital format.\r\n\r\n## Acceptance Criteria\r\n\r\n\r\n1. Develop a working prototype of a dynamic version of the [OCIO Strategic FrameWork diagram](https://raw.githubusercontent.com/bcgov/interactive-infographic/master/wireframe/OCIO_Strategy_Framework.png). See this [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png) that illustrates how the interactive infographic might be structured.\r\n2. Allow the insertion and deletion of content boxes (i.e. rows, see [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png)).\r\n3. Allow the insertion and deletion of content elements (i.e. see [wireframe](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/wireframe.png)).\r\n4. Content box should have the ability to contain multiple content elements that scale according to the number of content elements. Challenge us on this one if it's unrealistic.\r\n5. Allow the insertion and deletion of graphics (and perhaps text) into the content elements.\r\n6. When a user clicks on a content element (every row, or content box, should have this capability), an accordion window will expand/appear underneath. This [second diagram](https://github.com/bcgov/interactive-infographic/blob/master/wireframe/user-interaction.png) illustrates how a user might interact with the infographic.\r\n7. Allow the insertion and deletion of content in accordion windows, including text and hyperlinks (possibly graphics).\r\n8. Support vector graphics. You can use example graphics and text for the prototype.\r\n9. Provide the final product in a format that can be run on any computer (localhost) through any modern web-browser.\r\n10. Device agnostic and responsive.\r\n11. Use of commonly known, open web frameworks.\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines](https://github.com/bcgov/interactive-infographic/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page](https://bcdevexchange.org/programs/OCIO%20Tech%20Strategies)  for more information on our work.\r\n",
          "program": "OCIO Tech Strategies",
          "skill": [
            "Graphic Design",
            "HTML",
            "Java",
            "Jquery",
            "UI/UX"
          ],
          "earn": [
            "$1000"
          ]
        },
        {
          "url": "https://api.github.com/repos/bcgov/databc-web-map-services/issues/1",
          "repository_url": "https://api.github.com/repos/bcgov/databc-web-map-services",
          "labels_url": "https://api.github.com/repos/bcgov/databc-web-map-services/issues/1/labels{/name}",
          "comments_url": "https://api.github.com/repos/bcgov/databc-web-map-services/issues/1/comments",
          "events_url": "https://api.github.com/repos/bcgov/databc-web-map-services/issues/1/events",
          "html_url": "https://github.com/bcgov/issue-three",
          "id": 103,
          "number": 1,
          "title": "Third Issue",
          "user": {
            "login": "myopic73",
            "id": 8550351,
            "avatar_url": "https://avatars.githubusercontent.com/u/8550351?v=3",
            "gravatar_id": "",
            "url": "https://api.github.com/users/myopic73",
            "html_url": "https://github.com/myopic73",
            "followers_url": "https://api.github.com/users/myopic73/followers",
            "following_url": "https://api.github.com/users/myopic73/following{/other_user}",
            "gists_url": "https://api.github.com/users/myopic73/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/myopic73/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/myopic73/subscriptions",
            "organizations_url": "https://api.github.com/users/myopic73/orgs",
            "repos_url": "https://api.github.com/users/myopic73/repos",
            "events_url": "https://api.github.com/users/myopic73/events{/privacy}",
            "received_events_url": "https://api.github.com/users/myopic73/received_events",
            "type": "User",
            "site_admin": false
          },
          "labels": [
            {
              "url": "https://api.github.com/repos/bcgov/databc-web-map-services/labels/$1000",
              "name": "$1000",
              "color": "0052cc"
            },
            {
              "url": "https://api.github.com/repos/bcgov/databc-web-map-services/labels/bug",
              "name": "bug",
              "color": "fc2929"
            },
            {
              "url": "https://api.github.com/repos/bcgov/databc-web-map-services/labels/GeoServer",
              "name": "GeoServer",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/databc-web-map-services/labels/help%20wanted",
              "name": "help wanted",
              "color": "159818"
            },
            {
              "url": "https://api.github.com/repos/bcgov/databc-web-map-services/labels/Java",
              "name": "Java",
              "color": "eb6420"
            }
          ],
          "state": "open",
          "locked": false,
          "assignee": null,
          "assignees": [],
          "milestone": null,
          "comments": 22,
          "created_at": "2016-05-11T21:45:33Z",
          "updated_at": "2016-06-01T21:38:36Z",
          "closed_at": null,
          "body": "## Background\r\nWe currently use [GeoServer](http://geoserver.org/), and it's great, except for a little bug. KML Placemarks do not correctly locate when there is a KMSCORE=0 and mode=refresh for SDE EPSG:3005 polygon data. The ground overlay returned is correct, but the KML placemarks don't look like the coordinates have been converted from the native SRS of EPSG:3005. See the bug ticket here posted in the GeoServer community: [https://osgeo-org.atlassian.net/browse/GEOS-7369](https://osgeo-org.atlassian.net/browse/GEOS-7369)\r\n\r\nWe use GeoServer for our WMS services which outputs KML of spatial data housed in the BC Warehouse. The WMS services are accessible to the public and also consumed by our services, including placemarks the BC Data Catalogue which uses the WMS for map previews of spatial data.\r\n\r\n### Story\r\nA a Government of B.C. spatial web developer, I want GeoServer to correctly locate KML placemarks so I can display spatial information accessible to the public via KML/Google Earth.\r\n\r\n\r\n## Acceptance Criteria\r\n\r\n\r\n1. KML Placesmarks locate properly when there is a KMSCORE=0 and mode=refresh for SDE EPSG:3005 polygon data.\r\n2. The solutions works within the GeoServer 2.8 code base.\r\n\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nPlease read the [Contribution Guidelines](https://github.com/bcgov/databc-web-map-services/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nIf you are interested in working on this issue, please let us know by posting a comment below.\r\n\r\nAnd check out our [Partners page](https://bcdevexchange.org/programs/DataBC%20Web%20Mapping) for more information on our work.\r\n",
          "program": "DataBC Web Mapping",
          "skill": [
            "GeoServer",
            "Java"
          ],
          "earn": [
            "$1000"
          ]
        }
    ],
   "closed": [
        {
          "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7",
          "repository_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit",
          "labels_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/labels{/name}",
          "comments_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/comments",
          "events_url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/issues/7/events",
          "html_url": "https://github.com/bcgov/citizen-engagement-web-toolkit/issues/7",
          "id": 121821329,
          "number": 7,
          "title": "Upgrade WP Sage Core Commenting - Part Three - Load More",
          "user": {
            "login": "juhewitt",
            "id": 15350676,
            "avatar_url": "https://avatars.githubusercontent.com/u/15350676?v=3",
            "gravatar_id": "",
            "url": "https://api.github.com/users/juhewitt",
            "html_url": "https://github.com/juhewitt",
            "followers_url": "https://api.github.com/users/juhewitt/followers",
            "following_url": "https://api.github.com/users/juhewitt/following{/other_user}",
            "gists_url": "https://api.github.com/users/juhewitt/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/juhewitt/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/juhewitt/subscriptions",
            "organizations_url": "https://api.github.com/users/juhewitt/orgs",
            "repos_url": "https://api.github.com/users/juhewitt/repos",
            "events_url": "https://api.github.com/users/juhewitt/events{/privacy}",
            "received_events_url": "https://api.github.com/users/juhewitt/received_events",
            "type": "User",
            "site_admin": false
          },
          "labels": [
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/$1000",
              "name": "$1000",
              "color": "0052cc"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/Bootstrap",
              "name": "Bootstrap",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/CSS",
              "name": "CSS",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/enhancement",
              "name": "enhancement",
              "color": "84b6eb"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/help%20wanted",
              "name": "help wanted",
              "color": "159818"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/HTML",
              "name": "HTML",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/JavaScript",
              "name": "JavaScript",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/jQuery",
              "name": "jQuery",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/PHP",
              "name": "PHP",
              "color": "eb6420"
            },
            {
              "url": "https://api.github.com/repos/bcgov/citizen-engagement-web-toolkit/labels/WordPress",
              "name": "WordPress",
              "color": "eb6420"
            }
          ],
          "state": "closed",
          "locked": false,
          "assignee": null,
          "assignees": [],
          "milestone": null,
          "comments": 22,
          "created_at": "2015-12-12T00:54:18Z",
          "updated_at": "2016-03-08T23:02:07Z",
          "closed_at": "2016-03-08T23:02:02Z",
          "body": "# Load More\r\n## Background\r\nWe are looking to build upon the default core SAGE framework/WP OOTB commenting system.  As fans of the plug and play model, we are trying to accomplish this in a modular way for obvious reasons.  Through UX testing, our audience has identified three short comings to overcome: sorting, filtering and sequential loading.  This ticket, we are going to focus on sequential loading. \r\n\r\n### Story\r\nI want to be able to interact with groupings of comments dynamically so I can restrict the information presented to me for a more effective consultation experience.\r\n\r\n## Acceptance Criteria\r\n1. A user will read through a subset of comments on a page or post and:\r\n  * select 'load more' to view the next subset of comments \r\n  * can continue to select 'load more' until all comments are present \r\n2. A user will read through a subset of replies within a thread on a page or post and:\r\n  * select 'load more' to view the next subset of comments \r\n  * can continue to select 'load more' until all comments are present \r\n3. The admin of the blog can set the number of comments and replies within a set.\r\n4. Ideally, the solution will perform these using AJAX calls.\r\n\r\n## How to contribute\r\n\r\nWe will evaluate each pull request and choose the best solution to the issue based on the acceptance criteria. Submit the best solution and you could be paid $1000.\r\n\r\nMore than one pull request may be considered for payment on this issue.\r\n\r\nPlease read the [Contribution Guidelines] (https://github.com/bcgov/citizen-engagement-web-toolkit/blob/master/CONTRIBUTING.md) for the Terms that set the rules for participation in a Pay for Pull, including how you’ll get paid if you are successful.\r\n\r\nHave questions? Please post your questions in the comments section below this issue.\r\n\r\nAnd check out our [Partners page] (https://bcdevexchange.org/programs/Citizen%20Engagement%20Web%20Toolkit)  for more information on our work.",
          "program": "Citizen Engagement Web Toolkit",
          "skill": [
            "Bootstrap",
            "CSS",
            "HTML",
            "JavaScript",
            "jQuery",
            "PHP",
            "WordPress"
          ],
          "earn": [
            "$1000"
          ]
        }
    ],
    "inprogress": [],
    "blocked": []
}'''