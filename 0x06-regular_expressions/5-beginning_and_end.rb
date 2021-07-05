#!/usr/bin/env ruby
reg = /[h].[n]/
puts ARGV[0].scan(reg).join
