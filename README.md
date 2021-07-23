# Django and Vue.js project, something like hastebin, but much more straightforward.
##Backend endpoints:
+ GET /notes/- notes list.
+ GET /notes/:pk/ - specific note, where pk it's 8-characters random string.
+ POST /notes/upload/ - enpoint for file upload. Converts files to note.
+ GET /users/ - users list.
+ GET /users/:pk/ - specific user, where pk - autoincrement integer.
+ GET /paswordlessTokens/ - paswordless tokens list.
+ GET /paswordlessTokens/:pk - specific paswordless token. pk - autoincrement integer.
+ POST /token/login/<str:user_email>/ - Sends login-verification mail with link to user email, if user registered.
+ POST /token/auth/<str:user_email>/ - Sends auth-verification mail with link to user email, if user not registered.
+ POST /token/check/<str:token_id>/ - Login user into api, if token is valid. If user not registered - creates user account and then login. Sends session token as response.
+ GET /subscribe/key/ - Returns stripe publishable key.
+ POST /subscribe/<str:product_name>/ - Create stripe checkout session. Returns checkout session id.
+ POST /stripe/webhook/ - Webhook for payment confirmation. Takes stripe event object, creates customer and updates user privilege.

#WIP: Login on frontend      
