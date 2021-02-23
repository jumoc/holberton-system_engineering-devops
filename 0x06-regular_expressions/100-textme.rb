#!/usr/bin/env ruby
puts ARGV[0].scan(/(?:\bfrom\b|\bto\b|\bflags\b):([^\]]+)/).join(",")
