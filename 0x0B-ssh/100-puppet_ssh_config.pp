# Setup config file
file_line { 'config_password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'BatchMode yes',
}

file_line { 'config_key':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile "~/.ssh/holberton"',
}
