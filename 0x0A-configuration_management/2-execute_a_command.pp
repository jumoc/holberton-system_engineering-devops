# Terminating a process with exec

exec {'kill':
  onlyif  => 'pgrep killmenow'
  command => 'pkill killmenow'
}
