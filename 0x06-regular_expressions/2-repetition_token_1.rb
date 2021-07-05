#!/usr/bin/env ruby
reg = /hb{0,1}tn/
puts ARGV[0].scan(reg).join
