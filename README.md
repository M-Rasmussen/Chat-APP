App can be found at https://rasmussenchatapp.herokuapp.com/

cd ~/environment && git clone https://github.com/NJIT-CS490/project2-m1-mtr26

1 Set up react and flask

a) pip install flask
b) nvm install 7 
c) npm install  
d) pip install flask-socketio
e) pip install eventlet
f) npm install -g webpack
g) npm install --save-dev webpack
h) npm install socket.io-client --save
i) npm install --save-dev style-loader 
j) npm install --save-dev css-loader 
	if any error messages, then use sudo pip or sudo npm. 

2 Get PSQL to work with python 

a) update yum: sudo yum update
b) upgrade pip: sudo /usr/local/bin/pip install --upgrade pip
c) get psycopg2: sudo /usr/local/bin/pip install psycopg2-binary
d) get SQLAlchemy: sudo /usr/local/bin/pip install Flask-SQLAlchemy==2.1

3) Setting up PSQL

a) install PostGreSQL:sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs
b) initialize PSQL database: sudo service postgresql initdb 
c) Start PSQL: sudo service postgresql start
d) Make a new superuser: sudo -u postgres createuser --superuser $USER
e) Make a new database: sudo -u postgres createdb $USER
f) make sure the user was created errors in the above 2 commands are ok and expected. 
 	i)psql
	ii) \du look for ec2-user as a user
	iii) \l look for ec2-user as a database
g)Make a new user: create user [username] superuser password '[password]'; 
h) \q is to quit
replace username with your username and password pick one. 

i)Then create a sql file with: DATABASE_URL='postgresql://[username]:[password]@localhost/postgres'
	
4) Read/write SQLAlchemy
a)sudo vim /var/lib/pgsql9/data/pg_hba.conf
b) :%s/ident/md5/g ( replace all the ident terms with md5)
c) sudo service postgresql restart

5) RUN APP
a) To run your app enter: npm run watch
b) In a new terminal enter: python app.py
	When you preview the running app then the app will be running.

6) APIs
a) Create an account at https://rapidapi.com/ 
b) https://english.api.rakuten.net/LemmoTresto/api/joke3/details is the API THAT WAS USED.
c) Get host adn key from the api and insert the things below into your env file. 

        rapidapihost= enter the api host here 
        rapidapikey= enter the api key here

The other API used was
https://funtranslations.com/api/ 
However, there is no key or individual aspect that you need to sign up for. 


Heroku: 
Make account at heroku.com
a) login: heroku login -i
b) create app: heroku create
c) heroku addons:create heroku-postgresql:hobby-dev
d) heroku pg:wait
e) psql
f) ALTER DATASE [postgres(database being used)] OWNER TO [uesrname^^ used in step 4];
g)\l you should see that the name of the database is next to the owner that you just entered. 
h)\q to exit form psql
i) PGUSER=[username] heroku pg:push postgres DATABASE_URL
j) heroku pg:psql to connect to heroku server data base.
k) create requirments.txt and populate it
l) create Procfile and enter web: python app.py
m) Enter the key and host from your env file into your heroku app via the app settings page under config vars




Pip install coverage
Pip install black
pip install pylint
pip install requests_mock
pip install bag

GENERAL ISSUES: always make sure your database is running: sudo service postgresql start
if you have trouble downloading things enter sudo infront of the command

Known Issues:

One of the biggest issues that I am having is displaying the database information aka chat with react, but I figured out a work around explained in the first technical issue. I think it would be better to be send the information without having to concat them originally, so I bet I will have to solve this issue for milestone two. If I had more time I would have like to figure that out more because my app works, but it creates multiple spots that I have to parse through code which makes it even more inefficient. It is in the Chatbox react file along with the app py emit_all_messages functions that concat it. 


Technical ISSUES.

I was having a really hard time with using react to accept the information and then add it to the use case. I know that I could have fixed it better than the way that I did, but the main issue was the SQL calls that I was doing. I have the information stored in the database in two colums. I could probably switch that up differently and it should work better. But I was passing all the information as one and it would just add the last item along with the rest. So instead I used the example from class and concatinated the information before I sent it over to react from python. And I changed the style with a function that gets the first few letters of the string and if its bot: then the style would change. This is not ideal, and if someone makes their user name bot: or bot:[anything] it would be the same style as the bot. 

Another Technical issue I was having was dealing with css and having the screen be completely full even if there is not enough information. I went on w3 schools and found out that you can use vh and vw which represent the size of the screen. For example 90vh would be 90% of the screen size vertically and same idea with width. 

Lastly, I had a techincal issue when I was setting up the database to then push it to heroku. The issue that I was having was that when I went into the pg_hba.conf file and I noticed the one on my base machine was actually wrong. It was peer instead of md-5. I was not sure why that was the case, and I thought I changed it duing the class period but I slowed down and redid all the steps and found that I was missing information on that step. 

*Information on how to run programs and download the requirements were taken from Shresht CS 490 github lecture files 
