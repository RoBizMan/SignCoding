# [SIGNCODING](https://signcoding-d529cc1ebf99.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/RoBizMan/SignCoding)](https://github.com/RoBizMan/SignCoding/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/RoBizMan/SignCoding)](https://github.com/RoBizMan/SignCoding/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/RoBizMan/SignCoding)](https://github.com/RoBizMan/SignCoding)

---

## Introduction

Welcome to SignCoding: Where Programming Meets Sign Language Tutoring! At SignCoding, we bridge the gap between ambition and achievement, providing an inclusive environment tailored to your unique needs. Whether you are starting your coding journey or looking to enhance your skills, our dedicated sign language tutors are here to ensure seamless and effective communication. Join us today and transform your learning experience!

The primary goal of SignCoding is to create an empowering, inclusive platform that connects aspiring programmers with expert sign language tutors. By fostering a supportive learning environment, SignCoding aims to help deaf and hard-of-hearing individuals achieve their full potential in the programming world.


## Target Audience

SignCoding is designed for aspiring programmers and developers who are deaf or hard of hearing. Our platform is perfect for individuals who want to learn programming languages like HTML, CSS, JavaScript, Python, and more in a supportive and inclusive environment. Whether you are a beginner eager to start your coding journey or an experienced coder looking to refine your skills, SignCoding welcomes you to connect, learn, and grow with us.


## Value Proposition

At SignCoding, users can benefit from a streamlined learning experience focused on programming and effective communication. Our verified sign language tutors are experts in programming languages and are here to help you grasp concepts quickly and efficiently. The platform is designed to empower deaf and hard-of-hearing students by providing a curriculum that equips them with the skills needed to thrive in today’s tech landscape.

Join SignCoding today and unlock your potential in a learning environment where programming meets sign language tutoring!

![screenshot](documentation/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://signcoding-d529cc1ebf99.herokuapp.com)

---

## UX

In this project, I follow the Five Planes of User Experience model invented by Jesse James Garrett.

### Five Planes of User Experience

This model aids in transforming from abstract ideas, such as creating objectives of the project and identifying the user needs, to concrete concepts, such as assembling visual elements to produce the visual design of the idea to meet the project's objectives and users' needs.

#### The Strategy Plane
The vision for SignCoding is to be a unique, inclusive learning platform where aspiring programmers can connect with expert sign language tutors and seamlessly learn programming languages. Unlike other platforms, SignCoding creates an accessible and empowering environment for deaf and hard-of-hearing students, ensuring effective communication and support throughout their coding journey.

##### Business Goals:
- Community Engagement: Foster a supportive community of aspiring programmers who share their learning experiences and progress. We value your feedback and aim to shape SignCoding based on your needs and preferences.
- Inclusive Learning: Create a dynamic and accessible learning platform enriched by high-quality tutoring services for deaf and hard-of-hearing students.
- Brand Identity: Establish SignCoding as the go-to platform for inclusive programming education, renowned for its intuitive, user-friendly interface and expert sign language tutors.

##### User Needs:
- Aspiring Programmers: A learning platform that provides expert sign language tutors to help them master programming languages like HTML, CSS, JavaScript, Python, and more.
- Deaf and Hard-of-Hearing Students: An inclusive environment where communication is seamless and learning is tailored to their unique needs.
- Skill Seekers: Users who prefer a straightforward and practical learning experience focused on grasping programming concepts without unnecessary complexity.

In this context, the core value of SignCoding lies in providing a streamlined, inclusive learning experience focused on programming education and effective communication through sign language.

#### Scope Plane

Based on the main objective and goals set out in the Strategy Plane, these requirements for developing the website are broken down into two categories:

##### Functional Requirements:
- User Accounts and Profiles: Users should be able to create an account, set up a basic profile, and access tutoring sessions and services.
- Tutoring Sessions: A simple process for users to book and attend sign language tutoring sessions focused on programming languages.
- Tutor Listings: Display a list of tutors with their programming languages, sign languages, day availabilities, and time slot availabilities.
- Booking History: Users should be able to view their booking history and manage their sessions.
- Primary Navigation: Users should be able to navigate between their profile, tutor listings, and booking history.

##### Content Requirements:
- Tutor Profiles: Profiles for tutors showcasing their expertise, available programming and sign languages, and schedule.
- User Profiles: Basic profiles showing the user's booking history and upcoming sessions.

#### The Structure Plane

The requirements outlined in the Scope Plane were then used to create a structure for the website. A site map below shows how users can navigate the website easily.

![screenshot](documentation/ux/diagram.png)

#### The Skeleton Plane

Please refer to the [Wireframes](#Wireframes) section for more detailed wireframing.

#### The Surface Plane

[Click here to view the live site.](https://signcoding-d529cc1ebf99.herokuapp.com)

### Colour Scheme

I used [Color Hunt](https://colorhunt.co/palette/3c0008f9f6ee000000ffc107#justCreated) to generate my colour palette.

![screenshot](documentation/ux/colour_palette.png)

- `#F9F6EE` is used for the primary background, inverted font colour and secondary button.
- `#3C0008` is used for the primary navbar, main button, and footer colour.
- `#FFC107` is used for the secondary button.
- `#000` is used for the main font colour.

The colour palette for SignCoding represents the harmony between coding and sign language education, using vibrant colours to symbolise inclusivity and communication.  However, the colour palette needed to pass the minimum colour contrast set by the Web Content Accessibility Guide (WCAG). The colour palette was tested using [Coolors' Color Contrast Checker](https://coolors.co/contrast-checker/). The result below shows that these colours passed the minimum WCAG contrast ratio.

<details>
<summary>Color Contrast Checker</summary>

![screenshot](documentation/ux/white_maroon.png)
![screenshot](documentation/ux/yellow_maroon.png)
![screenshot](documentation/ux/black_white.png)
</details>

<br>

### Typography

- [Bootstrap's native font stack](https://getbootstrap.com/docs/5.3/content/reboot/#native-font-stack) was used throughout the site.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer and buttons in a detailed gram view.

---

## User Stories

### New Site Users

- As a new site user, I would like to create an account, so that I can access tutoring services.
- As a new site user, I would like to browse available tutors, so that I can find the right match for my learning needs.
- As a new site user, I would like to book a tutoring session, so that I can start learning programming with a sign language tutor.

### Returning Site Users

- As a returning site user, I would like to view my booking history, so that I can keep track of my past sessions.

- As a returning site user, I would like to check tutor profiles' date and time availability, so that I can book new sessions as per my schedule.

- As a returning site user, I would like to update my profile information, so that my details remain current.

### Site Admin

- As a site administrator, I should be able to manage user accounts, so that I can ensure a secure and efficient platform.

- As a site administrator, I should be able to monitor tutor availability, so that I can maintain an up-to-date list of available sessions.

- As a site administrator, I should be able to handle booking requests, so that I can ensure smooth scheduling and session management.

---