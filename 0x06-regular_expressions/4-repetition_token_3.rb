#!/usr/bin/env ruby
reg = /hbt{0,}n/
puts ARGV[0].scan(reg).join
