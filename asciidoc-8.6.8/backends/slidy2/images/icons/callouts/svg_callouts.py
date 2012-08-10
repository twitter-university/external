#!/usr/bin/env python
# creates SVG callout icons
# to run under the backends/slidy2/images/icons/callouts/ directory

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for nb in numbers:
 file = "%s.svg" % nb
 try:
  f = open(file, "wt")
  f.write('<?xml version="1.0" standalone="no"?>\n')
  f.write('<?xml-stylesheet href="callout.css" type="text/css"?>\n')
  f.write('<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" version="1.1">\n')
  f.write('<g>\n')
  f.write('  <circle cx="50" cy="50" r="50" class="callout" />\n')
  f.write('  <text x="50" y="80" text-anchor="middle" font-family="Trebuchet MS" font-weight="bold" font-size="80" fill="white" class="callout">%d</text>\n' % nb )
  f.write('</g>\n')
  f.write('</svg>\n')
  f.close()
  print "%s created" % file
 except IOError, (errno, strerror):
  print "*** ERROR %s : File %s *** %s" % (errno, file, strerror)


