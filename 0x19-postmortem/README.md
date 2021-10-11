# Postmortem
## Issue Summary
On October 2, it was discovered that one of our Nginx web servers was unable to receive all HTTP requests. We tested many HTTP method types including CRUD operations and noticed that only some of the requests have gone through. Through several stages of research and debugging, we found that the issue was the ulimit in the Ubuntu package as it was set too low and limited the use of system-wide resources.

![alt](https://i.pinimg.com/736x/16/d5/84/16d584a17e9fd32b02a39fc50361d6bf.jpg)
## Timeline
- 14:00 UTC: It was found that not all of our HTTP requests were not being sent to the server.

- 14:15pm: We check the error logs within nginx with
```cat var/log/nginx/error.log```

```
2019/03/07 21:07:55 [emerg] 654#0: epoll_create() failed (24: Too many open files)
2019/03/07 21:07:55 [alert] 649#0: worker process 654 exited with fatal code 2 and cannot be respawned

- 14:25 UTC: To measure how many requests would go through, we tested it using ApacheBench and simulated sending 2000 HTTP requests to the server. We noticed we were receiving too many failed GET requests, approximate 1900.
```
ab -n 2000 -c 100 localhost/
```
2019/03/07 21:32:19 [crit] 651#0: *1 open() "/usr/share/nginx/html/index.html" failed (24: Too many open files),
client: ::1, server: localhost, request: "GET / HTTP/1.0", host: "localhost"
2019/03/07 21:32:19 [crit] 651#0: *2 open() "/usr/share/nginx/html/index.html" failed (24: Too many open files), 
client: ::1, server: localhost, request: "GET / HTTP/1.0", host: "localhost"
```


- 14:35 UTC: After looking at the Nginx configuration, we found that there had to be a limit on the number of open file descriptors per process because the error logs mentioned too many open files. We look for where the limitation might be.


- 14:40 UTC: It was decided to check the descriptor limit inside ```/etc/default/nginx```. We found that the limit is 15, which is too low to handle the number of requests and responses we wanted. We decided to increase the amount to 500.
```ULIMIT="n -3000"```

- 14:41 UTC: We restart the server with the new ulimit. Using apachebench now returned all requests with 0 failed requests. The problem is now solved.

- 14:50 UTC: We created a puppet script to automate the process and set the amount of resources for ULIMIT.

```
exec { 'limit_req':
  command => 'sed -i "s/15/3000/" /etc/default/nginx',
  path    => '/bin',
}
exec { 'nginx_restart':
  command => '/usr/sbin/service nginx restart',
}
```

## Root cause and resolution
The root cause was ulimit within Nginx’s config files. We found out that the issue was 24: Too many open files. So somewhere within our server, there had to be a limit on the number of open file descriptors per process. We permanently fixed the issue by making a puppet script using sed and replacing the limit as well as restarting the server.

## Corrective and preventative measures
Configurations should be tested first using ApacheBench and other tools to make sure all responses and requests work properly before being deployed out. The server should also be reviewed by other peers in a testing environment.