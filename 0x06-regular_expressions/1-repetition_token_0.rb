#!/usr/bin/env ruby
reg = /hbt{1,5}n/
puts ARGV[0].scan(reg).join
