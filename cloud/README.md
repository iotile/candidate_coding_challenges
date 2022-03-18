# Please do not publish a solution in either a fork or clone. Keep all of your work local!
#### If you do want to store your work, we ask that you keep it in a private repo (github lets everyone do this now).

## Introduction

This project is designed to get you familiar with some basic functionalities of our ArchFX Cloud product.

Arch has built a complete framework to help factories monitoring their production lines. Arch FX Cloud is the core of
this product, as it is the main user interface but also the link with all our other products.

It is basically a webapp served by a Django server, with all the needed backend tools.

To test the skills you will need to be part of the Cloud team, we will build a small API running with Django.

*It should take less than 1 hour to complete. If you think some parts need more, please tell us.*

## Description

The goal of this exercise is to build an API that will allow a user to register time blocks with a name
and then query the resulting timeline.

1. Setup a Django server within a Docker container. This server will need a PostgreSQL database to store models, which
   will also be into a Docker container. We recommend describing these containers using docker-compose.
2. Define the `Timeblock` model and migrations to save it in DB.
   - id: int (auto-increment)
   - name: str
   - start_time: datetime
   - end_time: datetime
3. Add API routes using the `django-rest-framework` library. You have to choose the names and methods.
   1. A route to create a new timeblock (save it in DB).
   2. A route to get the list of all saved timeblocks.
   3. A route to get a timeblock info from its id.
   4. A route to delete a timeblock by its id.
   5. A route to get the resulting timeline (you can mock it for now: we'll compute the timeline in next step).
4. Compute the timeline based on all the timeblocks in DB, and return it on API route call.
   It is basically a data structure that would be used by some frontend to display a contiguous timeline.
   We have to resolve overlapping (if 2 timeblocks overlap the resulting name will be the concatenation of the 2 names)
   and gaps (no timeblock defined during some time).

For example (times are written as integers for simplicity): 
 - Timeblocks: {name: 'A', start_time: 0, end_time: 2}, {name: 'B', start_time: 4, end_time: 8} and {name: 'C', start_time: 6, end_time: 10}.
 - Timeline (as ascii blocks, but you must return a data structure):
```
+-----+-----+-----+-----+-----+
|  A  |  -  |  B  | B&C |  C  |
+-----+-----+-----+-----+-----+
0     2     4     6     8     10
```

## Misc informations

- We'll use Python3, preferably with type hinting.
- API responses are formatted in JSON.
- You should handle errors with correct HTTP status code.
- Authentication is not needed (could be some sort of bonus).
- You should use `django-rest-frameworks` serializers.
- You should write some unit tests.
- Timeblock computation should be optimized as much as possible.
- If you think there are missing information, please fell free to choose your way to do. We'll discuss it later.

## Code submission

You can send us either a link to a Git repository, or a ZIP file by email.
We expect you to provide:
 - docker files (a docker-compose file, Dockerfiles if needed)
 - the django code folder
 - a README to explain how to spawn your server and make the API requests
