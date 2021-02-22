0. prepare
`docker-compose run web python manage makemigrations`
`docker-compose run web python manage migrate`

1. `docker-compose run web python manage automated_bot` - to run bot generated users and post form integers of .env file
2. `api/token/` and `api/token/refresh/` to work with JWT token obtain and refresh
3. `/api/post/<int:id>/like-post/` - set/unset like
4. POST `/api/user/` - `signup user {"email": "<str:email>", "password": "<str:q1w2e3r4t5>"}`
5. provide JWT default header to create post and like/unlike
6. directory `api/utils` - provide small util for check clearbit.com validation and emailhunter(hunter.io) 