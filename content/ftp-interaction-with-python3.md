Title: FTP Interaction with Python3
Date: 2020-03-10 12:48
Modified: 2020-03-22 09:14
Author: Phil Grimes
Category: Blog
Tags: Programming, Python, Code
Slug: ftp-interaction-with-python3
Status: published

On a recent engagement, I found myself pivioting through several SSH tunnels, onto a relatively light-weight and restrictive linux box. As I was looking around, gaining some perspective as to options for my next move, I found a new route to a host in which I'd previously been unsuccessful in gaining access. This time, via anonymous FTP. The restrictive nature of the environment meant that I had a limited arsenal, but the full capailities of the python language, so I set to work. 

#Investigating FTP with Python3

##ftplib

Fortunately, Python offers a robust core library to handle FTP communications with ftplib. According to the documentation: 

>This module defines the class FTP and a few related items. The FTP class implements the client side of the FTP protocol. You can use this to write Python programs that perform a variety of automated FTP jobs, such as mirroring other FTP servers. It is also used by the module urllib.request to handle URLs that use FTP. For more information on FTP (File Transfer Protocol), see Internet RFC 959.

The documentation drops a little code snippet which shows us just how easily this library lets us interact with FTP servers. Since this core library is available as part of the "default" python installation, it seemed like a viable option for tackling the task at hand. 

So let's take a look at how we use it, shall we? 

##Interacting with FTP

Since we found a mechanism with which we can engage the target FTP server, I needed to learn how to unlock the power of this library. Fortunately, most python modules are really well [documented](https://docs.python.org/3/library/ftplib.html "ftplib Python Docs")- this is almost always where I start when learning a new library or module. 

The [documentation](https://docs.python.org/3/library/ftplib.html "ftplib Python Docs") is always a good start, even when you have the urge to go rip some code from stackoverflow or github. Learning how to solve the problem often comes with educational tidbits that one usually doesn't get from using someone else's solution. In this case, my little idea of a quick and dirty script turned into the desire to build a full-featured FTP client in python, for command line use.

As with all python modules/libraries, they first need to be imported: 

```python
from ftplib import FTP
```

And then to connect to our targeted server, with FTP running on the default port (21). I couldn't use my real example due to NDA, but we'll look at an open FTP server to share the spirit of the code: 

```python
ftp = FTP('ftp.debian.org')```

Once connected, we need to log in. Now remeber that I was writing this on the fly, during an engagement. I didn't have any credentials, but wanted to simply test for anonymous access to this server. Logging in with ftplib is quite simple, especially when there are no credentails to pass: 

```python
ftp.login()
'230 Login successful.'```

We get acknowledement of our login, and we're off to the races! One of the first things I always try to do is gain an understanding of the environment and my surroundings by listing the contents of the directory I'm in: 

```python
ftp.retrlines('LIST') ```

In a matter of minutes I was browsing the anonymous FTP server I'd been targeting, and most of that was spent reading the documentation. I was connected and logged in, thanks to the power of python, and able to display the help/welcome message, navigate around the files structure, browse directory contents, download files (upload was restricted), and more. I won't go into the full feature set of the library, because much of the methods/objects weren't of use to me during the testing. This was also because I had some mild interest in the project on Twitter, so I figured it would be fun to release sooner than later. If you find a bug, or have an enhancement or feature request, please speak up! It's always nice getting feedback! 

##Building the program

As is my nature, and most of my programming experience, this is starting out as a quick and dirty script. It's not pretty. It's not elegant. It just works. So while I am still evolving as a developer, and am open to any constructive criticism, I am also a hacker and my primary objctive in life will be to accomplis the mission set before me as quickly and efficiently as possible. And that's what I've done here. 

Since this project came to life during a professional engagement, my development process intintionally rapid. And when I found something worked, it was committed to the repository. I'd work through the problems I was trying to solve in the interpreter, then push the changes that worked out to the github repository. Hopefully you'll find it useful, but I hope even more that you offer some feedback as to how I can improve this code. 

#Conclusion

Just a little post to share my thoughts with you as I built out this code, I'm calling it EffTeePee. I wanted to get this out there to share with you, and I hope you find it useful! Thanks for taking the time to stop by my little corner of the internet, I'll hope to catch your attention again soon. 