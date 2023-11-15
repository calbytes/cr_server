# cnet_db_server
a simple backend db web server for my website

This applicatin is running Flask and Gunicorn.

#run server on :8080
gunicorn -w 4 -b 0.0.0.0:8080 app:app