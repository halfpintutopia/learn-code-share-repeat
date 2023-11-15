<h1>Learn Code Share Repeat</h1> 

_I aim to address the existing limitations in online video-sharing platforms where educational content
related to programming and coding becomes outdated, irrelevant, and plagued by non-constructive comments._

_I want to develop a solution that empowers coders to share their knowledge through video content in a way that ensures
the content remains up-to-date, well-explained, and transparent and fosters constructive interactions among users._

_The goal is to create an innovative web application that serves as a tool to enhance knowledge and understanding,
taking inspiration from the Richard Feynman technique, where the quality of content is paramount, and the community of
learners and experts collaborates to enhance the learning experience._

<!-- TOC -->
  * [UX/UI](#uxui)
  * [Agile](#agile)
    * [Future Implementations](#future-implementations)
  * [Schema](#schema)
  * [References](#references)
    * [Inspiration](#inspiration)
    * [Design](#design)
    * [Django](#django)
    * [Docker](#docker)
    * [GraphQL](#graphql)
    * [Progressive Web App (PWA)](#progressive-web-app-pwa)
<!-- TOC -->

## UX/UI

For further details see the following documentation:

* [Define and Ideate](docs/design/define_and_ideate.md)
* [Five Planes of Design](docs/design/five-planes.md)

## Agile

| Start Date | Due Date | Feature                      | Epic             | User Story                                                                                               | Task                                                                                                                                            | Automated Testing                              | Manual Testing                          | Assessment Criteria                                                                                               | Dependencies                      | Label       |
|------------|----------|------------------------------|------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------|-------------|
| 20 Nov     | 30 Nov   | User Registration            | Registration     | As a user, I want to register so that I can create an account                                            | Implement Django User model, Create registration form in React, Connect form to Django backend                                                  | Write unit tests for registration              | Test registration form manually         | User can register with email and password, User receives confirmation email                                       | None                              | Must Have   |
| 1 Dec      | 5 Dec    | User Authentication          | Authentication   | As a user, I want to login so that I can access my account                                               | Implement Django authentication, Create login form in React, Connect form to Django backend                                                     | Write unit tests for authentication            | Test login form manually                | User can login with email and password, User receives error message for incorrect credentials                     | Depends on Registration Epic      | Must Have   |
|            |          |                              | Authentication   | As a user, I want to reset my password so that I can regain access to my account if I forget my password | Implement Django password reset, Create password reset form in React, Connect form to Django backend                                            | Write unit tests for password reset            | Test password reset form manually       | User can request password reset, User receives email with password reset link, User can reset password using link | Depends on User Registration Epic | Must Have   |
| 6 Dec      | 10 Dec   | Video Upload                 | Video Management | As a user, I want to upload videos so that I can share my content                                        | Implement Django model for videos, Create video upload form in React, Connect form to Django backend                                            | Write unit tests for video upload              | Test video upload form manually         | User can upload video with title and description, Uploaded video is saved in user’s account                       | Depends on Authentication Epic    | Must Have   |
| 11 Dec     | 15 Dec   | Video Display                | Video Management | As a user, I want to view videos so that I can watch content                                             | Create video display component in React, Connect component to Django backend                                                                    | Write unit tests for video display             | Test video display manually             | User can view videos, Video display includes title and description                                                | Depends on Video Upload Task      | Must Have   |
| 16 Dec     | 20 Dec   | Rating and Commenting System | User Interaction | As a user, I want to rate and comment on videos so that I can give feedback                              | Implement Django models for ratings and comments, Create rating and comment components in React, Connect components to Django backend           | Write unit tests for rating and commenting     | Test rating and commenting manually     | User can rate and comment on videos, Ratings and comments are saved and displayed                                 | Depends on Video Display Task     | Should Have |
| 21 Dec     | 25 Dec   | User Profiles                | User Management  | As a user, I want to customize my profile so that I can express myself                                   | Implement Django model for user profiles, Create profile customization form in React, Connect form to Django backend                            | Write unit tests for profile customization     | Test profile customization manually     | User can add profile picture, description, and social links, User profile updates are saved and displayed         | Depends on Authentication Epic    | Should Have |
| 26 Dec     | 30 Dec   | User Interactions            | User Interaction | As a user, I want to follow others and receive notifications so that I can engage with the community     | Implement Django models for follows and notifications, Create follow and notification components in React, Connect components to Django backend | Write unit tests for follows and notifications | Test follows and notifications manually | User can follow others and receive notifications, Follows and notifications are saved and displayed               | Depends on User Profiles Task     | Could Have  |

### Future Implementations

* Search and Discover: Improve search and discovery functionalities, allowing users to find videos by title, tags, and content type.
* Content Moderation: Strengthen content moderation to maintain a positive and safe user experience.
* Open-Source Components: Explore integrating open-source components for video hosting, content management, and other system-level improvements to enhance efficiency and stability.
* Generative AI: Introduce generative AI for advanced content recommendation, summarisation, and user engagement insights.
* Micro-Learning Modules: Introduce micro-learning modules alongside video uploads, where users can engage with short, interactive coding challenges or quizzes related to the video content.
* Interactive Coding Environment: Offer an in-browser coding environment that allows users to practice coding while watching tutorial videos.
* Real-Time Coding Collaboration: Enable real-time coding collaboration between users, where they can work on coding projects together.
* AI-Driven Video Analytics: Implement AI-driven video analytics to track user interactions within videos.
* Live Streaming Workshops: Introduce live streaming workshops and webinars where coding experts can provide real-time instruction.
* Personalised Learning Paths: Develop an AI-based recommendation system that offers personalised learning paths for users.
* Virtual Coding Mentor: Implement a virtual coding mentor powered by AI, which can provide personalised feedback and guidance based on a user’s coding activity and progress.
* AI-Enhanced Collaboration: Use AI to enhance real-time coding collaboration. It can suggest solutions, identify errors, and provide real-time code analysis.
* Gamification and Tournaments: Introduce gamification elements and coding tournaments where users can compete and earn badges or rewards for achieving coding milestones.
* Multilingual Learning: Expand the platform to support multiple languages, making coding education accessible globally.
* Blockchain-Based Credentials: Explore blockchain technology to issue verifiable certificates or credentials for completed courses and coding challenges.

## Schema

![ERD for Learn Code Share Repeat](docs/media/images/lcsr_erd.png)

## References

### Inspiration

- [How to Learn Anything with the Feynman Technique](https://todoist.com/inspiration/feynman-technique)
- [The Feynman Technique Can Help You Remember Everything You Read](https://learntrepreneurs.com/how-to-improve-the-way-you-learn/the-feynman-technique-can-help-you-remember-everything-you-read-2/)
- [The Feynman Technique | YouTube](https://www.youtube.com/watch?v=tkm0TNFzIeg)
- [Building in brighton covered in graffiti](https://www.alamy.com/stock-photo-building-in-brighton-covered-in-graffiti-23416737.html)
- [YouTube](https://www.youtube.com/)
- [FrontendMasters](https://frontendmasters.com/)
- [Vimeo](https://vimeo.com/)

### Design

- [Adobe Color](https://color.adobe.com)

### Django

- [Django Authentication Tutorial | Auth0](https://auth0.com/blog/django-authentication/)
- [Django | Auth0](https://auth0.com/docs/quickstart/webapp/django/01-login)
- [Secure Your Django web apps with Auth0](https://www.linkedin.com/pulse/secure-your-django-web-apps-auth0-sanchit-khurana/)
- [Tutorial | Django Girl](https://tutorial.djangogirls.org)
- [Adding Social Authentication to Django](https://testdriven.io/blog/django-social-auth/)

### Docker

- [How to dockerize a Django and React application](https://www.honeybadger.io/blog/docker-django-react/)
- [React + Django + Postgres](https://forums.docker.com/t/react-django-postgres/136637)

### GraphQL

- [Code using GraphQL](https://graphql.org/code/)
- [GraphQL in Django Backend (Graphene) - React Tutorial 63](https://www.youtube.com/watch?v=zzUcL7sOQEM)
- [Django + GraphQL + React —1. Integrate GraphQL into your Django project](https://zoejoyuliao.medium.com/django-graphql-react-1-integrate-graphql-into-your-django-project-ff51237bb5d9)
- [Django + GraphQL + React —2. Integrate GraphQL into your Django project](https://zoejoyuliao.medium.com/django-graphql-react-2-integrate-graphql-into-your-react-project-71fa74f1cb00)

### Progressive Web App (PWA)

- [Make PWA of a Django Project](https://www.geeksforgeeks.org/make-pwa-of-a-django-project/)