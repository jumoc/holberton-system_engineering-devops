# Terminating a process with exec

exec {'kill':
  command => 'pkill killmenow'
}
