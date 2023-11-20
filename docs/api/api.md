<h1>API</h1>

[⇦ Back to main README](../../README.md)

<!-- TOC -->

* [CRUD Table](#crud-table)
    * [User Profile:](#user-profile)
    * [Video:](#video)
    * [Rating:](#rating)
    * [Comment:](#comment)

<!-- TOC -->

## CRUD Table

### User Profile:

| HTTP   | URI                 | CRUD operation                                       | view name    |
|--------|---------------------|------------------------------------------------------|--------------|
| POST   | /api/users          | Create a new user                                    | user_create  |
| PUT    | /api/users/{userId} | Edit a user’s profile                                | user_update  |
| GET    | /api/users/{userId} | Retrieve a user’s profile                            | user_profile |
| DELETE | /api/users/{userId} | Delete a user’s profile (after a successful request) | user_delete  |
| GET    | /api/users          | Retrieve a list of all users                         | user_list    |

---

### Video:

| HTTP   | URI                                  | CRUD operation                                         | view name    |
|--------|--------------------------------------|--------------------------------------------------------|--------------|
| POST   | /api/users/{userId}/videos           | Upload a new video                                     | video_create |
| DELETE | /api/users/{userId}/videos/{videoId} | Delete a user’s video                                  | video_delete |
| PUT    | /api/users/{userId}/videos/{videoId} | Edit a user’s video                                    | video_update |
| GET    | /api/users/{userId}/videos/{videoId} | Retrieve a user’s video                                | video_detail |
| GET    | /api/videos                          | Retrieve a list of all videos                          | video_list   |
| GET    | /api/videos?search={keyword}         | Retrieve a list of videos that match the given keyword | video_search |

---

### Rating:

| HTTP   | URI                                                     | CRUD operation                          | view name     |
|--------|---------------------------------------------------------|-----------------------------------------|---------------|
| POST   | /api/users/{userId}/videos/{videoId}/ratings            | Create a new rating for a video         | rating_create |
| GET    | /api/users/{userId}/videos/{videoId}/ratings            | Retrieve all ratings for a user’s video | rating_list   |
| GET    | /api/videos/{videoId}/ratings/{ratingId}                | Retrieve a specific rating on a video   | rating_detail |
| DELETE | /api/users/{userId}/videos/{videoId}/ratings/{ratingId} | Delete a user’s rating                  | rating_delete |
| PUT    | /api/users/{userId}/videos/{videoId}/ratings/{ratingId} | Edit a user’s rating                    | rating_update |

---

### Comment:

| HTTP   | URI                                                       | CRUD operation                           | view name      |
|--------|-----------------------------------------------------------|------------------------------------------|----------------|
| POST   | /api/users/{userId}/videos/{videoId}/comments             | Create a new comment for a video         | comment_create |
| GET    | /api/users/{userId}/videos/{videoId}/comments             | Retrieve all comments for a user’s video | comment_list   |
| GET    | /api/videos/{videoId}/comments/{commentId}                | Retrieve a specific comment on a video   | comment_detail |
| DELETE | /api/users/{userId}/videos/{videoId}/comments/{commentId} | Delete a user’s comment                  | comment_delete |
| PUT    | /api/users/{userId}/videos/{videoId}/comments/{commentId} | Edit a user’s comment                    | comment_update |