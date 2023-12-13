<h1>API</h1>

[⇦ Back to main README](../../README.md)

<!-- TOC -->

* [API Structure](#api-structure)
    * [Navigational Map for API](#navigational-map-for-api)
    * [Endpoints](#endpoints)
        * [User Profile:](#user-profile)
        * [Video:](#video)
        * [Rating:](#rating)
        * [Comment:](#comment)

<!-- TOC -->

## API Structure

### Navigational Map for API

- /api
    - /users
        - POST: Create a new user (user_create)
        - GET: Retrieve a list of all users (user_list)
        - /{userId}
            - PUT: Edit a user’s profile (user_update)
            - GET: Retrieve a user’s profile (user_profile)
            - DELETE: Delete a user’s profile (user_delete)
    - /upload
        - /videos
            - POST: Upload a new video (video_create)
    - /manage
        - /videos
            - /{videoId}
                - DELETE: Delete a user’s video (video_delete)
                - PUT: Edit a user’s video (video_update)
    - /{videoId}
        - GET: Retrieve a video (video_detail)
        - /ratings
            - POST: Create a new rating for a video (rating_create)
            - GET: Retrieve all ratings for a video (rating_list)
            - /{ratingId}
                - GET: Retrieve a specific rating on a video (rating_detail)
                - DELETE: Delete a user’s rating (rating_delete)
                - PUT: Edit a user’s rating (rating_update)
        - /comments
            - POST: Create a new comment for a video (comment_create)
            - GET: Retrieve all comments for a video (comment_list)
            - /{commentId}
                - GET: Retrieve a specific comment on a video (comment_detail)
                - DELETE: Delete a user’s comment (comment_delete)
                - PUT: Edit a user’s comment (comment_update)
    - /videos
        - GET: Retrieve a list of all videos (video_list)
        - ?search={keyword}: Retrieve a list of videos that match the given keyword (video_search)

### Endpoints

#### User Profile:

| HTTP   | URI         | CRUD operation                                       | view name    |        |
|--------|-------------|------------------------------------------------------|--------------|--------|
| POST   | /api/users  | Create a new user                                    | user_create  | LIST   |
| PUT    | /api/{slug} | Edit a user’s profile                                | user_update  | DETAIL |
| GET    | /api/{slug} | Retrieve a user’s profile                            | user_profile | DETAIL |
| DELETE | /api/{slug} | Delete a user’s profile (after a successful request) | user_delete  | DETAIL |
| GET    | /api/users  | Retrieve a list of all users                         | user_list    | LIST   |

---

#### Video:

| HTTP   | URI                          | CRUD operation                                         | view name    |        |
|--------|------------------------------|--------------------------------------------------------|--------------|--------|
| POST   | /api/upload/videos           | Upload a new video                                     | video_create | LIST   |
| DELETE | /api/manage/videos/{videoId} | Delete a user’s video                                  | video_delete | DETAIL |
| PUT    | /api/manage/videos/{videoId} | Edit a user’s video                                    | video_update | DETAIL |
| GET    | /api/{videoId}               | Retrieve a video                                       | video_detail | DETAIL |
| GET    | /api/videos                  | Retrieve a list of all videos                          | video_list   | LIST   |
| GET    | /api/videos?search={keyword} | Retrieve a list of videos that match the given keyword | video_search | LIST   |

---

#### Rating:

| HTTP   | URI                               | CRUD operation                          | view name     |        |
|--------|-----------------------------------|-----------------------------------------|---------------|--------|
| POST   | /api/{videoId}/ratings            | Create a new rating for a video         | rating_create | LIST   |
| GET    | /api/{videoId}/ratings            | Retrieve all ratings for a user’s video | rating_list   | LIST   |
| GET    | /api/{videoId}/ratings/{ratingId} | Retrieve a specific rating on a video   | rating_detail | DETAIL |
| DELETE | /api/{videoId}/ratings/{ratingId} | Delete a user’s rating                  | rating_delete | DETAIL |
| PUT    | /api/{videoId}/ratings/{ratingId} | Edit a user’s rating                    | rating_update | DETAIL |

---

#### Comment:

| HTTP   | URI                                 | CRUD operation                           | view name      |        |
|--------|-------------------------------------|------------------------------------------|----------------|--------|
| POST   | /api/{videoId}/comments             | Create a new comment for a video         | comment_create | LIST   |
| GET    | /api/{videoId}/comments             | Retrieve all comments for a user’s video | comment_list   | LIST   |
| GET    | /api/{videoId}/comments/{commentId} | Retrieve a specific comment on a video   | comment_detail | DETAIL |
| DELETE | /api/{videoId}/comments/{commentId} | Delete a user’s comment                  | comment_delete | DETAIL |
| PUT    | /api/{videoId}/comments/{commentId} | Edit a user’s comment                    | comment_update | DETAIL |