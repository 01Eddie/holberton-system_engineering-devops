# 0. Strace is your friend

exec { 'wordpress':
	provider => "shell",
	command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
	path     => ['/bin', '/usr/bin'],
}

