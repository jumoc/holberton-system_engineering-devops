# Setup config file
file_line { 'config_password':
  path   => '/etc/ssh/ssh_config',
  line   => 'BatchMode yes',
}

file_line { 'config_key':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile "~/.ssh/holberton"',
}
