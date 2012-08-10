from asciidocapi import AsciiDocAPI
import os
import StringIO
import re
import unittest
import asciidoc_inputs

class Slidy2_conf_Test(unittest.TestCase):
	assert_message_format = "%s\r\n*** Expected :\r\n%s\r\n*** But was :\r\n%s"
	collected_inputs = ''

	def asciidoc_output(self,asciidoc_markup,backend='xhtml11',attributes=[],options=['--no-header-footer'],debug=False):
		infile = StringIO.StringIO(asciidoc_markup)
		outfile = StringIO.StringIO()
		asciidoc = AsciiDocAPI('../../../asciidoc.py')
		for option in options:
			asciidoc.options(option)
		for attribute in attributes:
			asciidoc.attributes[attribute] = 1
		asciidoc.execute(infile, outfile,backend)
		if debug: print asciidoc.messages
		return outfile.getvalue()

	def setUp(self):
		self.debug = False
		
	def tearDown(self):
		self.debug = False

	def test_AsciiDoc_version(self):
		m = 'AsciiDoc version > 8.6.5'
		out = self.asciidoc_output(asciidoc_inputs.d['asciidoc-version'],'slidy2')
		expected = r'<div class="paragraph">\r\n<p>(\d+)\.(\d+)\.(\d+)</p>\r\n</div>\r\n'
		mo = re.match(expected,out)
		self.assertTrue((int(mo.group(1)) > 8) or ((int(mo.group(1)) == 8) and (int(mo.group(2)) > 6)) or ((int(mo.group(1)) == 8) and (int(mo.group(2)) == 6) and (int(mo.group(3)) > 5)), self.assert_message_format % (m,expected,out))

	def test_incremental_bulleted_list(self):
		m = 'incremental on bulleted list'
		out = self.asciidoc_output(asciidoc_inputs.d['bulleted_list'],'slidy2',['incremental'])
		expected = r'<ul[^>]*class="[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_numbered_list(self):
		m = 'incremental on numbered list'
		out = self.asciidoc_output(asciidoc_inputs.d['numbered_list'],'slidy2',['incremental'])
		expected = r'<ol[^>]*class="[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_labeled_list(self):
		m = 'incremental on labeled list'
		out = self.asciidoc_output(asciidoc_inputs.d['labeled_list'],'slidy2',['incremental'])
		expected = r'<dl[^>]*class="[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_qanda_list(self):
		m = 'incremental on qanda list'
		out = self.asciidoc_output(asciidoc_inputs.d['qanda_list'],'slidy2',['incremental'])
		expected = r'<li[^>]*class="[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_callout_list(self):
		m = 'incremental on callout list'
		out = self.asciidoc_output(asciidoc_inputs.d['callout_list'],'slidy2',['incremental'])
		expected = r'<li[^>]*class="[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		###
		m = 'incremental on callout list + icons'
		out = self.asciidoc_output(asciidoc_inputs.d['callout_list'],'slidy2',['incremental','icons'])
		expected = r'<tbody[^>]*class="[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_paragraph(self):
		m = 'incremental on paragraph'
		out = self.asciidoc_output(asciidoc_inputs.d['paragraph'],'slidy2',['incremental'])
		expected = r'<div[^>]*class="[^"]*paragraph[^"]*".*\r\n<div[^>]*class="[^"]*incremental[^"]*">\r\n<p>.*</p>\r\n</div>\r\n</div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_admonitionparagraph(self):
		m = 'incremental on paragraph'
		out = self.asciidoc_output(asciidoc_inputs.d['admonitionparagraph'],'slidy2',['incremental'])
		expected = r'<div[^>]*class="[^"]*incremental[^"]*"><p>.*</p></div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_listingblock(self):
		m = 'incremental on listingblock'
		out = self.asciidoc_output(asciidoc_inputs.d['listingblock'],'slidy2',['incremental'])
		expected = r'<div[^>]*class="content[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_literalblock(self):
		m = 'incremental on literalblock'
		out = self.asciidoc_output(asciidoc_inputs.d['literalblock'],'slidy2',['incremental'])
		expected = r'<div[^>]*class="content[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_quoteblock(self):
		m = 'incremental on quoteblock'
		out = self.asciidoc_output(asciidoc_inputs.d['quoteblock'],'slidy2',['incremental'])
		expected = r'<div[^>]*class="attribution[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_verseblock(self):
		m = 'incremental on verseblock'
		out = self.asciidoc_output(asciidoc_inputs.d['verseblock'],'slidy2',['incremental'])
		expected = r'<pre[^>]*class="content[^"]*incremental[^"]*">.*</pre>\r\n<div[^>]*class="attribution[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_table(self):
		m = 'incremental on table'
		out = self.asciidoc_output(asciidoc_inputs.d['table'],'slidy2',['incremental'])
		expected = r'<tbody[^>]*class="[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_incremental_openblock(self):
		m = 'incremental on openblock'
		out = self.asciidoc_output(asciidoc_inputs.d['openblock'],'slidy2',['incremental'])
		expected = r'<div[^>]*class="openblock[^"]*incremental[^"]*"'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_nopagebreak(self):
		m = 'nopagebreak macro unset :slidepagebreak: attribute'
		out = self.asciidoc_output(asciidoc_inputs.d['nopagebreak'],'slidy2')
		expected = r'<div class="paragraph">\r\n<p>XXX</p>\r\n</div>\r\n<div class="paragraph">\r\n<p></p>\r\n</div>\r\n</div></div>\r\n<script.*/script>\r\n\r\n<div class="sect1">\r\n<h1 id="_section">section</h1>\r\n<script.*/script>\r\n<div class="sectionbody">\r\n<div class="paragraph">\r\n<p>ZZZ</p>\r\n</div>'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_pagebreak(self):
		m = 'pagebreak macro generate a new slide'
		out = self.asciidoc_output(asciidoc_inputs.d['pagebreak'],'slidy2')
		expected = r'</div></div>\r\n<script.*/script>\r\n</div><div class="slide[^"]*">\r\n<div class="sect1[^"]*">\r\n<script.*/script>\r\n<div class="sectionbody[^"]*">\r\n\r\n<div class="paragraph">\r\n<p>content\r\nXXX</p>\r\n</div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_backgroundblock(self):
		m = 'backgroundblock'
		out = self.asciidoc_output(asciidoc_inputs.d['backgroundblock'],'slidy2')
		expected = '<div class="background[^"]*"[^>]*>\r\n<div class="paragraph">\r\n<p>content</p>\r\n</div>\r\n</div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_inline_footnote(self):
		m = 'inline footnote:[text]'
		out = self.asciidoc_output(asciidoc_inputs.d['footnote'],'slidy2')
		expected = '<div class="paragraph">\r\n<p>content1 <script.*/script>\r\n\[1\] content2 <script.*/script>\r\n\[2\]</p>\r\n</div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_inline_footnoteref(self):
		m = 'inline footnoteref:[id]'
		out = self.asciidoc_output(asciidoc_inputs.d['footnoteref1'],'slidy2')
		expected = '<div class="paragraph">\r\n<p>content1 \[id1\] content2 \[id2\]</p>\r\n</div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		###
		m = 'inline footnoteref:[id,text]'
		out = self.asciidoc_output(asciidoc_inputs.d['footnoteref2'],'slidy2')
		expected = '<div class="paragraph">\r\n<p>content1 <script.*/script>\r\n\[id1\] content2 <script.*/script>\r\n\[id2\]</p>\r\n</div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))


	def test_incremental_imagesblock(self):
		images_base_markup = '<div style="margin-left: 4em; position: relative;"%s>\r\n<img src="backends/slidy2/tests/i1.png" alt="backends/slidy2/tests/i1.png" style="position: static; vertical-align: bottom" />\r\n<img src="backends/slidy2/tests/i1.png" alt="backends/slidy2/tests/i1.png" style="position: absolute; left: 0; top: 0" />\r\n<img src="backends/slidy2/tests/i1.png" alt="backends/slidy2/tests/i1.png" style="position: absolute; left: 0; top: 0" />\r\n</div>\r\n'
		m = 'images::[]'
		out = self.asciidoc_output(asciidoc_inputs.d['imagesblock'],'slidy2')
		expected = images_base_markup % ''
		r1 = re.compile(expected)
		self.assertEqual(out, expected, self.assert_message_format % (m,expected,out))
		###
		m = 'images::[] + incremental'
		out = self.asciidoc_output(asciidoc_inputs.d['imagesblock'],'slidy2',['incremental'])
		expected = images_base_markup % ' class="incremental"'
		self.assertEqual(out, expected, self.assert_message_format % (m,expected,out))
		###
		images_data_uri_base_markup = '<div style="margin-left: 4em; position: relative;"%s>\r\n<img alt="backends/slidy2/tests/i1.png" style="position: static; vertical-align: bottom"  src="data:image/png;base64,\r\niVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAAAXNSR0IArs4c6QAAAARnQU1BAACx\r\njwv8YQUAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAxJREFU\r\nGFdjeCujAgADJwEuFWu+6QAAAABJRU5ErkJggg==" />\r\n<img alt="backends/slidy2/tests/i1.png" style="position: absolute; left: 0; top: 0"  src="data:image/png;base64,\r\niVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAAAXNSR0IArs4c6QAAAARnQU1BAACx\r\njwv8YQUAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAxJREFU\r\nGFdjeCujAgADJwEuFWu+6QAAAABJRU5ErkJggg==" />\r\n<img alt="backends/slidy2/tests/i1.png" style="position: absolute; left: 0; top: 0"  src="data:image/png;base64,\r\niVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAAAXNSR0IArs4c6QAAAARnQU1BAACx\r\njwv8YQUAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAAxJREFU\r\nGFdjeCujAgADJwEuFWu+6QAAAABJRU5ErkJggg==" />\r\n</div>\r\n'
		m = 'images::[] + data-uri '
		out = self.asciidoc_output(asciidoc_inputs.d['imagesblock'],'slidy2',['data-uri'])
		expected = images_data_uri_base_markup % ''
		self.assertEqual(out, expected, self.assert_message_format % (m,expected,out))
		###
		m = 'images::[] + data-uri + incremental'
		out = self.asciidoc_output(asciidoc_inputs.d['imagesblock'],'slidy2',['data-uri','incremental'])
		expected = images_data_uri_base_markup % ' class="incremental"'
		self.assertEqual(out, expected, self.assert_message_format % (m,expected,out))

	def test_callout_inlinemacro(self):
		m = 'callout_inlinemacro'
		out = self.asciidoc_output(asciidoc_inputs.d['callout_inlinemacro'],'slidy2')
		expected = r'<b><1></b>\r\n<b><2></b>\r\n'
		r1 = re.compile(expected)
		#TODO self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		###
		m = 'callout_inlinemacro + icons'
		out = self.asciidoc_output(asciidoc_inputs.d['callout_inlinemacro'],'slidy2',['icons'])
		expected = r'<tbody>\r\n<tr><td><object data="./images/icons/callouts/1.svg" type="image/svg\+xml" title="1" width="4%"><img src="./images/icons/callouts/1.png" alt="1" /></object></td><td style="vertical-align: middle;">\r\nitem\r\n</td></tr>\r\n<tr><td><object data="./images/icons/callouts/2.svg" type="image/svg\+xml" title="2" width="4%"><img src="./images/icons/callouts/2.png" alt="2" /></object></td><td style="vertical-align: middle;">\r\nitem\r\n</td></tr>\r\n</tbody></table></div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_preamble(self):
		m = 'preamble slide'
		out = self.asciidoc_output('= title 0\r\npreamble\r\n== title 1\r\n\r\n content\r\n','slidy2')
		expected = '<div class="slide">\r\n<div id="preamble">\r\n<h1 style="visibility: hidden;">Preamble</h1>\r\n<script.*/script>\r\n<div class="sectionbody">\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_sect1(self):
		m = 'sect1 slide'
		out = self.asciidoc_output(asciidoc_inputs.d['sect1'],'slidy2',['numbered'])
		expected = '</div></div>\r\n<script.*/script>\r\n</div><div class="slide">\r\n\r\n<div class="sect1">\r\n<h1 id="_title_level_1">1\. title level 1</h1>\r\n<script.*/script>\r\n<div class="sectionbody">\r\n<div class="paragraph">\r\n<p>content</p>\r\n</div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_sect2(self):
		m = 'sect2 slide'
		out = self.asciidoc_output(asciidoc_inputs.d['sect2'],'slidy2',['numbered'])
		expected = '</div></div>\r\n<script.*/script>\r\n</div><div class="slide">\r\n\r\n<div class="sect2">\r\n<h1 id="_title_level_2">0\.1\. title level 2</h1>\r\n<script.*/script>\r\n<div class="sectionbody">\r\n<div class="paragraph">\r\n<p>content</p>\r\n</div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_sect3(self):
		m = 'sect3 slide'
		out = self.asciidoc_output(asciidoc_inputs.d['sect3'],'slidy2',['numbered'])
		expected = '</div></div>\r\n<script.*/script>\r\n</div><div class="slide">\r\n\r\n<div class="sect3">\r\n<h1 id="_title_level_3">0\.0\.1\. title level 3</h1>\r\n<script.*/script>\r\n<div class="sectionbody">\r\n<div class="paragraph">\r\n<p>content</p>\r\n</div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_sect4(self):
		m = 'sect4 slide'
		out = self.asciidoc_output(asciidoc_inputs.d['sect4'],'slidy2',['numbered'])
		expected = '</div></div>\r\n<script.*/script>\r\n</div><div class="slide">\r\n\r\n<div class="sect4">\r\n<h1 id="_title_level_4">0\.0\.0\.1\. title level 4</h1>\r\n<script.*/script>\r\n<div class="sectionbody">\r\n<div class="paragraph">\r\n<p>content</p>\r\n</div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_appendix(self):
		m = 'appendix slide'
		out = self.asciidoc_output(asciidoc_inputs.d['appendix'],'slidy2',['numbered'])
		expected = '</div></div>\r\n<script.*/script>\r\n</div><div class="slide">\r\n\r\n<div class="sect1">\r\n<h1 id="_title">1\. Appendix A: title</h1>\r\n<script.*/script>\r\n<div class="sectionbody">\r\n<div class="paragraph">\r\n<p>content</p>\r\n</div>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_header_head(self):
		m = 'empty header'
		out = self.asciidoc_output('= Document Title\r\n\r\n content\r\n','slidy2',options=[])
		expected = '<meta name="generator"[^>]+>\r\n<title>Document Title</title>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'header with author'
		out = self.asciidoc_output('= Document Title\r\n:author: Author\r\n\r\ncontent\r\n','slidy2',options=[])
		expected = '<meta name="copyright" content="Copyright &#169; Author" />\r\n<meta name="generator"[^>]+>\r\n<title>Document Title</title>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'header with description, keywords and duration'
		out = self.asciidoc_output('= Document Title\r\n:description: Description\r\n:keywords: Key words\r\n:duration: Duration\r\n\r\ncontent\r\n','slidy2',options=[])
		expected = '<meta name="generator"[^>]+>\r\n<meta name="description" content="Description" />\r\n<meta name="keywords" content="Key words" />\r\n<meta name="duration" content="Duration" />\r\n<title>Document Title</title>\r\n'
		r1 = re.compile(expected)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'header without linkcss'
		out = self.asciidoc_output('= Document Title\r\n\r\ncontent\r\n','slidy2',options=[])
		expected = '<meta name="generator"[^>]+>\r\n<title>Document Title</title>\r\n<style type="text/css">.*?AsciiDoc xhtml11 and html5 backends.*?</style>\r\n<style type="text/css">.*?</style>\r\n<style type="text/css" title="slidy_color_set_none">.*?</style>\r\n<style type="text/css" title="slidy_color_set_yellow">.*?</style>\r\n<style type="text/css" title="slidy_color_set_green">.*?</style>\r\n<style type="text/css" title="slidy_color_set_blue">.*?</style>\r\n<style type="text/css" title="slidy_color_set_black">.*?</style>\r\n%s<script type="text/javascript">.*?</script>\r\n'
		r1 = re.compile(expected % '',re.DOTALL)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'header without linkcss and with pygments'
		out = self.asciidoc_output('= Document Title\r\n\r\ncontent\r\n','slidy2',attributes=['pygments'],options=[])
		r1 = re.compile(expected % '<style type="text/css">.*?</style>\r\n',re.DOTALL)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'header without linkcss and with asciimath'
		out = self.asciidoc_output('= Document Title\r\n\r\ncontent\r\n','slidy2',attributes=['asciimath'],options=[])
		r1 = re.compile(expected % '' + '<script type="text/javascript">.*?</script>\r\n',re.DOTALL)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'header without linkcss and with latexmath'
		out = self.asciidoc_output('= Document Title\r\n\r\ncontent\r\n','slidy2',attributes=['latexmath'],options=[])
		r1 = re.compile(expected % '' + '<script type="text/javascript">.*?</script>\r\n',re.DOTALL)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'header with linkcss'
		out = self.asciidoc_output('= Document Title\r\n\r\ncontent\r\n','slidy2',attributes=['linkcss'],options=[])
		expected = '<meta name="generator"[^>]+>\r\n<title>Document Title</title>\r\n<link rel="stylesheet" href="./asciidoc.css" type="text/css" />\r\n<link rel="stylesheet" href="./slidy2.css" type="text/css" />\r\n<link rel="stylesheet" href="./slidy2_color_set_none.css" type="text/css" />\r\n<link rel="stylesheet" href="./slidy2_color_set_yellow.css" type="text/css" />\r\n<link rel="stylesheet" href="./slidy2_color_set_green.css" type="text/css" />\r\n<link rel="stylesheet" href="./slidy2_color_set_blue.css" type="text/css" />\r\n<link rel="stylesheet" href="./slidy2_color_set_black.css" type="text/css" />\r\n%s<script src="./slidy2.js" charset="utf-8" type="text/javascript"></script>\r\n'
		r1 = re.compile(expected % '')
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'header with linkcss and pygments'
		out = self.asciidoc_output('= Document Title\r\n\r\ncontent\r\n','slidy2',attributes=['linkcss','pygments'],options=[])
		r1 = re.compile(expected % '<link rel="stylesheet" href="./pygments.css" type="text/css" />\r\n')
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'header with linkcss and asciimath'
		out = self.asciidoc_output('= Document Title\r\n\r\ncontent\r\n','slidy2',attributes=['linkcss','asciimath'],options=[])
		r1 = re.compile(expected % '' + '<script type="text/javascript" src=".*?/javascripts/ASCIIMathML.js"></script>\r\n')
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'header with linkcss and latexmath'
		out = self.asciidoc_output('= Document Title\r\n\r\ncontent\r\n','slidy2',attributes=['linkcss','latexmath'],options=[])
		r1 = re.compile(expected % '' + '<script type="text/javascript" src=".*?/javascripts/LaTeXMathML.js"></script>\r\n')
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_header_body(self):
		m = 'body with notitle'
		out = self.asciidoc_output('= Document Title\r\n\r\n content\r\n','slidy2',attributes=['notitle'],options=[])
		expected = '<body class="article">\r\n<div id="header" class="slide">\r\n%s</div>\r\n'
		r1 = re.compile(expected % '')
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'body without notitle'
		out = self.asciidoc_output('= Document Title\r\n\r\n content\r\n','slidy2',options=[])
		r1 = re.compile(expected % '<h1>Document Title</h1>\r\n')
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'body with doctitle, author, email, revnumber, revdate, revremark'
		out = self.asciidoc_output('= Document Title\r\n:author: Author\r\n:email: email\r\n:revnumber: revnumber\r\n:revdate: revdate\r\n:revremark: revremark\r\n\r\n content\r\n','slidy2',options=[])
		expected_continue = '<h1>Document Title</h1>\r\n<span id="author">Author</span><br />\r\n<span id="email"><tt>&lt;<a href="mailto:email">email</a>&gt;</tt></span><br />\r\n<span id="revnumber">version revnumber,</span>\r\n<span id="revdate">revdate</span>\r\n<br /><span id="revremark">revremark</span>\r\n'
		r1 = re.compile(expected % expected_continue)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected % expected_continue,out))

	def test_footer(self):
		m = 'empty footer'
		out = self.asciidoc_output('= Document Title\r\n\r\n content\r\n','slidy2',options=[])
		expected = '<div id="footer" style="position: absolute; left: 5%; top: 80%; width: 90%;">\r\n<div id="footer-text">\r\nLast updated.*?\r\n</div>\r\n</div>\r\n</div></div>\r\n<script.*script>\r\n</div>\r\n<script type="text/javascript">.*?</script>\r\n</body>\r\n</html>'
		r1 = re.compile(expected,re.DOTALL)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'footer with badges'
		out = self.asciidoc_output('= Document Title\r\n\r\n content\r\n','slidy2',attributes=['badges'],options=[])
		# oups : cannot play with %s here because of 5%; ????
		expected = '<div id="footer" style="position: absolute; left: 5%; top: 80%; width: 90%;">\r\n<div id="footer-text">\r\nLast updated.*?\r\n</div>\r\n<div id="footer-badges">\r\nValid <a href="http://validator.w3.org/check\?uri=referer">XHTML</a>\r\nand <a href="http://jigsaw.w3.org/css-validator/check/referer">CSS</a>\.\r\n</div>\r\n</div>\r\n</div></div>\r\n<script.*?script>\r\n</div>\r\n<script type="text/javascript">.*?</script>\r\n</body>\r\n</html>'
		r1 = re.compile(expected,re.DOTALL)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))
		############
		m = 'footer with badges and icons'
		out = self.asciidoc_output('= Document Title\r\n\r\n content\r\n','slidy2',attributes=['badges','icons'],options=[])
		# oups : cannot play with %s here because of 5%; ????
		expected = '<div id="footer" style="position: absolute; left: 5%; top: 80%; width: 90%;">\r\n<div id="footer-text">\r\nLast updated.*?\r\n</div>\r\n<div id="footer-badges">\r\n<a href="http://validator.w3.org/check\?uri=referer">\r\n<img style="border:0;width:88px;height:31px"\r\nsrc="http://www.w3.org/Icons/valid-xhtml11-blue"\r\nalt="Valid XHTML 1.1" height="31" width="88" />\r\n</a>\r\n<a href="http://jigsaw.w3.org/css-validator/">\r\n<img style="border:0;width:88px;height:31px"\r\nsrc="http://jigsaw.w3.org/css-validator/images/vcss-blue"\r\nalt="Valid CSS!" />\r\n</a>\r\n<a href="http://www.mozilla.org/products/firefox/">\r\n<img style="border:none; width:110px; height:32px;"\r\nsrc="http://www.spreadfirefox.com/community/images/affiliates/Buttons/110x32/safer.gif"\r\nalt="Get Firefox!" />\r\n</a>\r\n</div>\r\n</div>\r\n</div></div>\r\n<script.*?script>\r\n</div>\r\n<script type="text/javascript">.*?</script>\r\n</body>\r\n</html>'
		r1 = re.compile(expected,re.DOTALL)
		self.assertTrue(r1.search(out), self.assert_message_format % (m,expected,out))

	def test_all_incremental_off(self):
		m = 'all incremental off'
		out = self.asciidoc_output(''.join(asciidoc_inputs.d.values()),'slidy2')
		expected = r'incremental'
		r1 = re.compile(expected)
		self.assertFalse(r1.search(out), self.assert_message_format % (m,expected,out))

				
if __name__ == "__main__":
	unittest.main()
