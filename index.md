---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
title: "The Book of Statistical Proofs"
---

<!-- Style -->
<style type="text/css" media="screen">
  .container {
    text-align: center;
  }
  .list {
    text-align: left;
  }
  h1 {
    font-size: 4em;
    line-height: 1;
    letter-spacing: -1px;
  }
  form {
	text-align: center;
  }
</style>

<!-- Script -->
<script type="text/javascript"> 
function openURL()
{
	// get text box content
    var name = document.getElementById('q').value;
	
	// create Google search URL
    var url = 'https://www.google.com/search?q=site%3AStatProofBook.github.io+%22' + encodeURIComponent(name) + '%22';

    // open Google search URL
    window.location.href = url;
}
</script>

Welcome to **The Book of Statistical Proofs** -- <br>
*a centralized, open and collaboratively edited archive <br>
of statistical theorems for the computational sciences*! <br>

<table style="border:none">
  <tr>
    <td style="text-align:center">
	  <a href="/I/ToC">Table of Contents</a> <br>
	  <img src="Index_1.png"> <br>
	  Proofs & Definitions
	</td>
    <td style="text-align:center">
	  <a href="/I/PbN">Proof by Number</a> <br>
	  <img src="Index_2.png"> <br>
	  <a href="/I/DbN">Definition by Number</a>
	</td>
    <td style="text-align:center">
	  <a href="/I/PbT">Proof by Topic</a> <br>
	  <img src="Index_3.png"> <br>
	  <a href="/I/DbT">Definition by Topic</a>
	</td>
  </tr>
</table>

<div align="center">
  You can also <a href="https://github.com/StatProofBook/StatProofBookTools/blob/master/write_book/StatProofBook.pdf">view</a> or <a href="https://github.com/StatProofBook/StatProofBookTools/raw/master/write_book/StatProofBook.pdf">download</a> the entire book as a single PDF
</div>

<form name="Search">
  or do a full-text <a href="/search">search</a>: &ensp;
  <input type="text" maxlength="100" name="q" id="q"/>
  <input type="button" onclick="openURL()" value="Google Search"/>
</form>