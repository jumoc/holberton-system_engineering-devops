# Setup config file
file_line { 'config_password':
  path => '/etc/ssh/ssh_config',
  line => '\tBatchMode yes',
}

file_line { 'config_key':
  path => '/etc/ssh/ssh_config',
  line => '\tIdentityFile "~/.ssh/holberton"',
}
