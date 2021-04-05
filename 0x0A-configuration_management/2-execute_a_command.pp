# Terminating a process with exec

exec {'kill':
  path    => '/usr/bin',
  onlyif  => 'pgrep killmenow',
  command => 'pkill killmenow',
}
