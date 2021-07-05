#!/usr/bin/env ruby
reg = /[A-Z]/
puts ARGV[0].scan(reg).join
