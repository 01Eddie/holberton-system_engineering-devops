#!/usr/bin/env ruby
reg = /hbt{1,}n/
puts ARGV[0].scan(reg).join
