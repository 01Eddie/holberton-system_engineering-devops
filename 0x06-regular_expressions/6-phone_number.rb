#!/usr/bin/env ruby
reg = /^[0-9]{10}/
puts ARGV[0].scan(reg).join
