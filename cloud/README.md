# Please do not publish a solution in either a fork or clone. Keep all of your work local!
#### If you do want to store your work, we ask that you keep it in a private repo (github lets everyone do this now).

## Introduction

This project is designed to get you familiar with some basic functionalities of our ArchFX Cloud product.

Arch has built a complete framework to help factories monitoring their production lines. Arch FX Cloud is the core of
this product, as it is the main user interface but also the link with all our other products.

It is basically a webapp served by a Django server, with all the needed backend tools.

To test the skills you will need to be part of the Cloud team, we will build a small API running with Django. Please,
consider you are writing this code as if you wanted to submit a PR to the team (it is not a dirty PoC, the only shortcuts to
take are the ones defined the part "Misc informations" below).

## Description

The goal of this exercise is to build an API that will allow a user to register time blocks with a name
and then query the resulting timeline. The timeblocks duration can be from seconds to several days (no assumption on that).
Let's imagine, it can represent a production line status (running, idle, down) and the resulting timeline could be used
by the frontend to display an overall timeline to sum up the line status, at any time, for the last past week.

1. Define the `Timeblock` model and migrations to save it in DB.
   - id: int (auto-increment)
   - name: str
   - start_time: datetime
   - end_time: datetime
2. Add API routes using the `django-rest-framework` library. You have to choose the names and methods.
   1. A route to create a new timeblock (save it in DB).
   2. A route to get the list of all saved timeblocks.
   3. A route to get a timeblock info from its id.
   4. A route to delete a timeblock by its id.
   5. A route to get the resulting timeline (you can mock it for now: we'll compute the timeline in next step).
3. Compute the timeline based on all the timeblocks in DB, and return it on API route call.
   It is basically a data structure that would be used by some frontend to display a contiguous timeline.
   We have to resolve overlapping (if 2 timeblocks overlap the resulting name will be the concatenation of the 2 names)
   and gaps (no timeblock defined during some time).

For example (times are written as integers for simplicity, please remind they are datetime objects according to 1.): 
 - Timeblocks: {name: 'A', start_time: 0, end_time: 2}, {name: 'B', start_time: 4, end_time: 8} and {name: 'C', start_time: 6, end_time: 10}.
 - Timeline (as ascii blocks, but you must return a data structure):
```
+-----+-----+-----+-----+-----+
|  A  |  -  |  B  | B&C |  C  |
+-----+-----+-----+-----+-----+
0     2     4     6     8     10
```

**Bonus**

You can add:
 - a Redis cache to return timeline that have been already computed

OR

 - a celery worker to process the timeline asynchronously

## Misc informations

- We'll use Python3.8, preferably with type hinting.
- A basic skeleton is provided in the `skeleton/` folder. You are free to use it or not. To start it,
  just run `docker-compose up` from the `skeleton/` folder.
- API responses are formatted in JSON.
- You should handle errors with correct HTTP status code.
- Authentication is not needed.
- You must use `django-rest-frameworks` serializers.
- You must write some unit tests.
- Minimal documentation/comments are expected (no need to write all docstrings, just explain non self-explanatory code).
- Timeline computation should be optimized as much as possible. Optimal algorithm is not required, but we'll discuss about the time/space complexity.
- You can add external tools to help you improve your code quality (flake8, isort, coverage, ...etc).
- If you think there are missing information, please fell free to choose your best way to do. We'll discuss it later.

## Code submission

You can send us either a link to a Git repository, or a ZIP file by email. As we request that you don't publish your solution publicly, you could use private Github repositories and add your interviewer as a collaborator to give him/her access to your work.
We expect you to provide:
 - docker files (a docker-compose file, Dockerfiles if needed)
 - the django code folder
 - a README to explain how to spawn your server and make the API requests
