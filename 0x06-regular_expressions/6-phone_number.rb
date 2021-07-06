#!/usr/bin/env ruby
reg = /^\d{10}/
puts ARGV[0].scan(reg).join
