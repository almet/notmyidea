Analyse users' browsing context to build up a web recommender
#############################################################

:date: 2011-04-01
:tags: recommendations, browsers, users

No, this is not an april's fool ;)

Wow, it's been a long time. My year in Oxford is going really well. I realized
few days ago that the end of the year is approaching really quickly.
Exams are coming in one month or such and then I'll be working full time on my dissertation topic.

When I learned we'll have about 6 month to work on something, I first thought
about doing a packaging related stuff, but finally decided to start something
new. After all, that's the good time to learn.

Since a long time, I'm being impressed by the `last.fm <http://last.fm>`_
recommender system. They're *scrobbling* the music I listen to since something
like 5 years now and the recommendations they're doing  are really nice and
accurate (I discover **a lot** of new artists in my tastes listening to the 
"neighbour radio".) (by the way, `here is <http://lastfm.com/user/akounet/>`_ 
my lastfm account)

So I decided to work on recommender systems, to better understand what is it
about. 

Recommender systems are usually used to increase the sales of products
(like Amazon.com does) which is not really what I'm looking for (The one who
know me a bit know I'm kind of sick about all this consumerism going on).

Actually, the most simple thing I thought of was the web: I'm browsing it quite
every day and each time new content appears. I've stopped to follow `my feed
reader <https://bitbucket.org/bruno/aspirator/>`_ because of the
information overload, and reduced drastically the number of people I follow `on
twitter <http://twitter.com/ametaireau/>`_. 

Too much information kills the information.

You shall got what will be my dissertation topic: a recommender system for
the web. Well, such recommender systems already exists, so I will try to add contextual
information to them: you're probably not interested by the same topics at different 
times of the day, or depending on the computer you're using. We can also
probably make good use of the way you browse to create groups into the content
you're browsing (or even use the great firefox4 tab group feature).

There is a large part of concerns to have about user's privacy as well.

Here is my proposal (copy/pasted from the one I had to do for my master)

Introduction and rationale
==========================

Nowadays, people surf the web more and more often. New web pages are created
each day so the amount of information to retrieve is more important as the time
passes. These users uses the web in different contexts, from finding cooking
recipes to technical articles.

A lot of people share the same interest to various topics, and the quantity of
information is such than it's really hard to triage them efficiently without
spending hours doing it. Firstly because of the huge quantity of information
but also because the triage is something relative to each person. Although, this
triage can be facilitated by fetching the browsing information of all
particular individuals and put the in perspective.

Machine learning is a branch of Artificial Intelligence (AI) which deals with how
a program can learn from data. Recommendation systems are a particular
application area of machine learning which is able to recommend things (links
in our case) to the users, given a particular database containing the previous
choices users have made.

This browsing information is currently available in browsers. Even if it is not
in a very usable format, it is possible to transform it to something useful.
This information gold mine just wait to be used. Although, it is not as simple as
it can seems at the first approach: It is important to take care of the context
the user is in while browsing links. For instance, It's more likely that during
the day, a computer scientist will browse computing related links, and that during
the evening, he browse cooking recipes or something else.

Page contents are also interesting to analyse, because that's what people
browse and what actually contain the most interesting part of the information.
The raw data extracted from the browsing can then be translated into
something more useful (namely tags, type of resource, visit frequency,
navigation context etc.)

The goal of this dissertation is to create a recommender system for web links,
including this context information.

At the end of the dissertation, different pieces of software will be provided,
from raw data collection from the browser to a recommendation system.

Background Review
=================

This dissertation is mainly about data extraction, analysis and recommendation
systems. Two different research area can be isolated: Data preprocessing and
Information filtering.

The first step in order to make recommendations is to gather some data. The
more data we have available, the better it is (T. Segaran, 2007). This data can
be retrieved in various ways, one of them is to get it directly from user's
browsers.

Data preparation and extraction
-------------------------------

The data gathered from browsers is basically URLs and additional information
about the context of the navigation. There is clearly a need to extract more
information about the meaning of the data the user is browsing, starting by the
content of the web pages.

Because the information provided on the current Web is not meant to be read by
machines (T. Berners Lee, 2001) there is a need of tools to extract meaning from
web pages. The information needs to be preprocessed before stored in a machine
readable format, allowing to make recommendations (Choochart et Al, 2004).

Data preparation is composed of two steps: cleaning and structuring (
Castellano et Al, 2007). Because raw data can contain a lot of un-needed text
(such as menus, headers etc.) and need to be cleaned prior to be stored.
Multiple techniques can be used here and belongs to boilerplate removal and
full text extraction (Kohlschütter et Al, 2010).

Then, structuring the information: category, type of content (news, blog, wiki) 
can be extracted from raw data. This kind of information is not clearly defined
by HTML pages so there is a need of tools to recognise them.

Some context-related information can also be inferred from each resource. It can go
from the visit frequency to the navigation group the user was in while
browsing. It is also possible to determine if the user "liked" a resource, and
determine a mark for it, which can be used by information filtering a later
step (T. Segaran, 2007).

At this stage, structuring the data is required. Storing this kind of
information in RDBMS can be a bit tedious and require complex queries to get
back the data in an usable format. Graph databases can play a major role in the
simplification of information storage and querying.

Information filtering
---------------------

To filter the information, three techniques can be used (Balabanovic et
Al, 1997):

* The content-based approach states that if an user have liked something in the
  past, he is more likely to like similar things in the future. So it's about
  establishing a profile for the user and compare new items against it.
* The collaborative approach will rather recommend items that other similar users
  have liked. This approach consider only the relationship between users, and
  not the profile of the user we are making recommendations to.
* the hybrid approach, which appeared recently combine both of the previous
  approaches, giving recommendations when items score high regarding user's
  profile, or if a similar user already liked it.

Grouping is also something to consider at this stage (G. Myatt, 2007).
Because we are dealing with huge amount of data, it can be useful to detect group
of data that can fit together. Data clustering is able to find such groups (T.
Segaran, 2007).

References:

* Balabanović, M., & Shoham, Y. (1997). Fab: content-based, collaborative 
  recommendation. Communications of the ACM, 40(3), 66–72. ACM. 
  Retrieved March 1, 2011, from http://portal.acm.org/citation.cfm?id=245108.245124&amp;.
* Berners-Lee, T., Hendler, J., & Lassila, O. (2001). 
  The semantic web: Scientific american. Scientific American, 284(5), 34–43. 
  Retrieved November 21, 2010, from http://www.citeulike.org/group/222/article/1176986.
* Castellano, G., Fanelli, A., & Torsello, M. (2007). 
  LODAP: a LOg DAta Preprocessor for mining Web browsing patterns. Proceedings of the 6th Conference on 6th WSEAS Int. Conf. on Artificial Intelligence, Knowledge Engineering and Data Bases-Volume 6 (p. 12–17). World Scientific and Engineering Academy and Society (WSEAS). Retrieved March 8, 2011, from http://portal.acm.org/citation.cfm?id=1348485.1348488.
* Kohlschutter, C., Fankhauser, P., & Nejdl, W. (2010). Boilerplate detection using shallow text features. Proceedings of the third ACM international conference on Web search and data mining (p. 441–450). ACM. Retrieved March 8, 2011, from http://portal.acm.org/citation.cfm?id=1718542.
* Myatt, G. J. (2007). Making Sense of Data: A Practical Guide to Exploratory 
  Data Analysis and Data Mining.
* Segaran, T. (2007). Collective Intelligence.

Privacy
=======

The first thing that's come to people minds when it comes to process their
browsing data is privacy. People don't want to be stalked. That's perfectly
right, and I don't either.

But such a system don't have to deal with people identities. It's completely
possible to process completely anonymous data, and that's probably what I'm
gonna do.

By the way, if you have interesting thoughts about that, if you do know
projects that do seems related, fire the comments !

What's the plan ?
=================

There is a lot of different things to explore, especially because I'm
a complete novice in that field.

* I want to develop a firefox plugin, to extract the browsing informations (
  still, I need to know exactly which kind of informations to retrieve). The
  idea is to provide some *raw* browsing data, and then to transform it and to
  store it in the better possible way.
* Analyse how to store the informations in a graph database. What can be the
  different methods to store this data and to visualize the relationship
  between different pieces of data? How can I define the different contexts,
  and add those informations in the db?
* Process the data using well known recommendation algorithms. Compare the
  results and criticize their value.

There is plenty of stuff I want to try during this experimentation:

* I want to try using Geshi to visualize the connexion between the links,
  and the contexts
* Try using graph databases such as Neo4j
* Having a deeper look at tools such as scikit.learn (a machine learning
  toolkit in python)
* Analyse web pages in order to categorize them. Processing their
  contents as well, to do some keyword based classification will be done.

Lot of work on its way, yay !
