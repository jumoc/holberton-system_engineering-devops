# Setup config file
file_line { 'config_password':
  path   => '/etc/ssh/ssh_config',
  line   => '\tPasswordAuthentication no',
}

file_line { 'config_key':
  path   => '/etc/ssh/ssh_config',
  line   => '\tIdentityFile "~/.ssh/holberton"',
}
