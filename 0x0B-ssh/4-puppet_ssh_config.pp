# Setup config file
file_line { 'config_password':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'config_key':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile "~/.ssh/holberton"',
}
