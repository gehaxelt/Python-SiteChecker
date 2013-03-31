SiteChecker
===========

##Description##

The sitechecker.py is a small script, which checks the availability of websites defined by you. The check is performed every minute.

The code isn't the best one and might be improved.

##Usage##

Create a file sites.txt with one url per line. E.g.

```
http://technik.blogbasis.net
http://blogbasis.net
```

Create a writeable directory "log". The logfiles will be stored there. 


Run the script with python2.7

    python2.7 sitechecker.py 


