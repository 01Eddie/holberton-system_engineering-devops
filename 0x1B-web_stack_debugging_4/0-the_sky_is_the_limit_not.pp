# Sky is the limit, let's bring that limit higher
exec { 'limit_req':
   command => "sed -i 's/15/3000/' /etc/default/nginx",
   path    => '/bin'
}
exec { 'nginx_restart':
   command => '/usr/sbin/service nginx restart'
}
