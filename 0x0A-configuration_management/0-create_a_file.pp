# create a file

file { '/tmp/holberton':
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  source  => 'puppet:///modules/etc/holberton',
	content => 'I love Puppet'
   }

