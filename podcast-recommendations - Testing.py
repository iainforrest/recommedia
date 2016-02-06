#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Iain Forrest
#
# Created:     17/01/2016
# Copyright:   (c) Iain Forrest 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2, re
"""
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<script src="//cdn.optimizely.com/js/2629490064.js"></script>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Podcast &#8211; The Tim Ferriss Show | The Blog of Author Tim Ferriss</title>
	<link rel="profile" href="http://gmpg.org/xfn/11">
	<link rel="pingback" href="http://fourhourworkweek.com/xmlrpc.php">

	<meta name="google-site-verification" content="hIbo0UNkhIj5ogqV159jQPnPzLdpUrczqFJ_Ey8lX80" />
		<script src='https://r-login.wordpress.com/remote-login.php?action=js&amp;host=fourhourworkweek.com&amp;id=56542934&amp;t=1453658525&amp;back=http%3A%2F%2Ffourhourworkweek.com%2Fpodcast%2F' type="text/javascript"></script>
		<script type="text/javascript">
		/* <![CDATA[ */
			if ( 'function' === typeof WPRemoteLogin ) {
				document.cookie = "wordpress_test_cookie=test; path=/";
				if ( document.cookie.match( /(;|^)\s*wordpress_test_cookie\=/ ) ) {
					WPRemoteLogin();
				}
			}
		/* ]]> */
		</script>
		<link rel="alternate" type="application/rss+xml" title="The Blog of Author Tim Ferriss &raquo; Feed" href="http://fourhourworkweek.com/feed/" />
<link rel="alternate" type="application/rss+xml" title="The Blog of Author Tim Ferriss &raquo; Comments Feed" href="http://fourhourworkweek.com/comments/feed/" />
<link rel="alternate" type="application/rss+xml" title="The Blog of Author Tim Ferriss &raquo; Podcast &#8211; The Tim Ferriss&nbsp;Show Comments Feed" href="http://fourhourworkweek.com/podcast/feed/" />
	<script type="text/javascript">
		/* <![CDATA[ */
		function addLoadEvent(func) {
			var oldonload = window.onload;
			if (typeof window.onload != 'function') {
				window.onload = func;
			} else {
				window.onload = function () {
					oldonload();
					func();
				}
			}
		}
		/* ]]> */
	</script>
	<link rel='stylesheet' id='all-css-0' href='https://s2.wp.com/_static/??-eJyFj9EOgjAMRX/I2UhAfDF+C8wqg5U16ybh790kmhANvjRtc85uBxMr7caAYwCKim28m1FAyFic2bsedVhPey2yg9+aNQMK9Bi40YN6TVu4dh7TnrgJmSC8mgYtUsK2NOLj28ptl7I2YyZOtGpb9iiiUiUTSYUuBf05j/Ipyz8ggevNohoYXTDJlk/z9eYSBQ/DcHPRqy6XyflBTYgDSJgtZulC50NZFae6rIuqfwLxR5pK' type='text/css' media='all' />
<link rel='stylesheet' id='screen-css-1' href='https://s2.wp.com/wp-content/themes/vip/four-hour-work-week/css/reveal.css?m=1403637386g' type='text/css' media='screen' />
<link rel='stylesheet' id='all-css-2' href='https://s0.wp.com/_static/??-eJx9jtEOwiAMRX9IrEtI5h6M38JIBZZCCWXx98cyHzQqL+296T03hWdWllPFVCGuKtPqQhLAyEs45tmKnOB3zCErYmtq4PRh1INMKD204EzsmnTQUm+2B2WWelSDeFN2+LX7XyYsoR3+yC+2eowo4DU44tnQHrjH26D1NF7G4TotG8L2dBE=' type='text/css' media='all' />
<script type='text/javascript'>
/* <![CDATA[ */
var sranalytics = {"version":"0.1.4","pid":"56200ae1736b797ac300071c","iframe":"0","title":"Podcast - The Tim Ferriss Show","url":"http:\/\/fourhourworkweek.com\/podcast\/","date":"2014-06-13 20:40:41","channels":[],"tags":[],"authors":["Tim Ferriss"]};
/* ]]> */
</script>
<script type='text/javascript' src='https://s0.wp.com/_static/??-eJyFjt0KwjAMRl/Irk7nxS7EZ4k1bqn9s+k25tMbQQVxKAQCXw4nn56SomDccELWVuY6YJ6fq7K80r8A5anLULDyFF6wiaFgKA/WxyM5VANjhk4yEZ3jApciF4/MAi1cPytRGAmnv5jFksBcVEam25e19Cj/9EhJJzd0FFgz+SRdM4LpFQRwcyEjVhiBTaZUBMnvXIQHv6+bbbur15u2sXfa3ns8'></script>
<link rel='stylesheet' id='all-css-0' href='https://s2.wp.com/wp-content/mu-plugins/highlander-comments/style.css?m=1377793621g' type='text/css' media='all' />
<!--[if lt IE 8]>
<link rel='stylesheet' id='highlander-comments-ie7-css'  href='https://s2.wp.com/wp-content/mu-plugins/highlander-comments/style-ie7.css?m=1351637563g&#038;ver=20110606' type='text/css' media='all' />
<![endif]-->
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://fhww.wordpress.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://s1.wp.com/wp-includes/wlwmanifest.xml" />
<meta name="generator" content="WordPress.com" />
<link rel="canonical" href="http://fourhourworkweek.com/podcast/" />
<link rel='shortlink' href='http://wp.me/P3PfoO-3fA' />
<link rel="alternate" type="application/json+oembed" href="https://public-api.wordpress.com/oembed/1.0/?format=json&amp;url=http%3A%2F%2Ffourhourworkweek.com%2Fpodcast%2F&amp;for=wpcom-auto-discovery" /><link rel="alternate" type="application/xml+oembed" href="https://public-api.wordpress.com/oembed/1.0/?format=xml&amp;url=http%3A%2F%2Ffourhourworkweek.com%2Fpodcast%2F&amp;for=wpcom-auto-discovery" /><link rel="shortcut icon" type="image/x-icon" href="http://1.gravatar.com/blavatar/5a6ae22621a402b23b5a48c4b9aea05c?s=16" sizes="16x16" />
<link rel="icon" type="image/x-icon" href="http://1.gravatar.com/blavatar/5a6ae22621a402b23b5a48c4b9aea05c?s=16" sizes="16x16" />
<link rel="apple-touch-icon-precomposed" href="http://1.gravatar.com/blavatar/53cccdfdc7f3fd44dd002c4d2e5bc55e?s=114" />
<link rel='openid.server' href='http://fhww.wordpress.com/?openidserver=1' />
<link rel='openid.delegate' href='http://fhww.wordpress.com/' />
<link rel="search" type="application/opensearchdescription+xml" href="http://fourhourworkweek.com/osd.xml" title="The Blog of Author Tim Ferriss" />
<link rel="search" type="application/opensearchdescription+xml" href="https://s1.wp.com/opensearch.xml" title="WordPress.com" />
		<style>
			.wpcom-related-posts ul li {
				list-style-type: none;
				display: inline-block;
			}
		</style>
		<meta name="application-name" content="The Blog of Author Tim Ferriss" /><meta name="msapplication-window" content="width=device-width;height=device-height" /><meta name="msapplication-tooltip" content="Tim Ferriss&#039;s 4-Hour Workweek and Lifestyle Design Blog" /><meta name="msapplication-task" content="name=Subscribe;action-uri=http://fourhourworkweek.com/feed/;icon-uri=http://1.gravatar.com/blavatar/5a6ae22621a402b23b5a48c4b9aea05c?s=16" /><style type="text/css" id="custom-background-css">
body.custom-background { background-color: #1a1a1a; }
</style>
<style type="text/css" id="syntaxhighlighteranchor"></style>
		<link rel="stylesheet" id="custom-css-css" type="text/css" href="https://s1.wp.com/?custom-css=1&#038;csblog=3PfoO&#038;cscache=6&#038;csrev=77" />
			<!-- Facebook Pixel Code -->
	<script>
	!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','//connect.facebook.net/en_US/fbevents.js', '(http://t.yesware.com/tt/189ce8aabf6cb9c5927df074675571a85def616a/6af0f959b51064c4db8c66ec7fdc10d5/1c1368a357ccc9574fb9782bea46fc92/connect.facebook.net/en_US/fbevents.js)');
	fbq('init', '788987874513702');
	fbq('track', "PageView");
		</script>
	<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=788987874513702&ev=PageView&noscript=1 (https://t.yesware.com/tt/189ce8aabf6cb9c5927df074675571a85def616a/6af0f959b51064c4db8c66ec7fdc10d5/3ff9b5603fcc6a98a99b5511838209a5/www.facebook.com/tr?id=788987874513702&ev=PageView&noscript=1)"/></noscript>
	<!-- End Facebook Pixel Code -->

	<script src="https://s0.wp.com/wp-content/themes/vip/four-hour-work-week/js/header-scripts.js"></script>

	<!-- SumoMe JS call -->
	<script src="//load.sumome.com/" data-sumo-site-id="43e1e49a410f9d6be29c41d7333f49fc230e3d803898633ca35e964d08652d8f" async></script>
</head>

<body class="page page-id-12498 page-template-default custom-background mp6 customizer-styles-applied group-blog highlander-enabled highlander-light">
	<div id="page" class="hfeed site">
				<header id="masthead" class="site-header" role="banner">

			<div id='tfx-banner'>

				<div id='tfx_thumbnail' class='tfx-piece trailer-toggle'>
					<img src='https://s0.wp.com/wp-content/themes/vip/four-hour-work-week/images/tfx/thumb.png' />
				</div>

				<div id='tfx_logo' class='tfx-piece'>
					<img src='https://s0.wp.com/wp-content/themes/vip/four-hour-work-week/images/tfx/logo.png' />
				</div>

				<div id='tfx_tag' class='tfx-piece'>
					<img src='https://s0.wp.com/wp-content/themes/vip/four-hour-work-week/images/tfx/tag.png' />
				</div>

				<div id='tfx_cta' class='tfx-piece'>
					<a href='http://hyperurl.co/timferrissexperiment' target="_blank">
						<img src='https://s0.wp.com/wp-content/themes/vip/four-hour-work-week/images/tfx/cta.png' />
					</a>
				</div>

				<div id='tfx-trailer' class='tfx-piece'>
					<iframe id='yt-trailer' src="https://player.vimeo.com/video/149467630?portrait=0" width="440" height="248" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
					<a href='#' class='trailer-toggle'>
						<img src='https://s0.wp.com/wp-content/themes/vip/four-hour-work-week/images/tfx/close.png' />
					</a>
				</div>

				<div class='slide-item' id='slide01'></div>
				<div class='slide-item' id='slide02'></div>
				<div class='slide-item' id='slide03'></div>

			</div>

			<nav id="site-navigation" class="main-navigation" role="navigation">

				<div class="screen-reader-text skip-link"><a href="#content" title="Skip to content">Skip to content</a></div>
				<div class="mobile-text-menu-items">
					<a href="https://fhww.wordpress.com/podcast/"> Podcast</a>
					<a href="https://fhww.wordpress.com/tv/"> TV Show</a>
					<a href="http://www.amazon.com/Timothy-Ferriss/e/B001ILKBW2" target="_blank"> Books</a>
				</div>
				<div class="mobile-nav">
					<div class="menu-btn" id="hamburger-btn">
						<div></div>
						<div class="hamburger-inner">
							<span></span>
							<span></span>
							<span></span>
							<div class="close-hamburger-menu"><i class="top-nav-icons close-white"></i></div>
						</div>
					</div>
				</div>
				<div class="responsive-menu">
					<div class="menu-2015-nav-container"><ul id="menu-2015-nav" class="menu"><li id="menu-item-14850" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-14850"><a href="http://fourhourworkweek.com/blog/">Home</a></li>
<li id="menu-item-14851" class="menu-item menu-item-type-custom menu-item-object-custom current-menu-item menu-item-14851"><a href="http://fourhourworkweek.com/podcast/">Podcast</a></li>
<li id="menu-item-14849" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14849"><a href="http://fourhourworkweek.com/tv/">TV Show</a></li>
<li id="menu-item-15479" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-15479"><a href="http://www.amazon.com/Timothy-Ferriss/e/B001ILKBW2/?tag=offsitoftimfe-20">Books</a></li>
<li id="menu-item-14853" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-14853"><a href="http://fourhourworkweek.com/about/">About</a>
<ul class="sub-menu">
	<li id="menu-item-14858" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14858"><a href="http://fourhourworkweek.com/about/">Tim Ferriss Bio</a></li>
	<li id="menu-item-14854" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14854"><a href="http://fourhourworkweek.com/about/causes/">Causes</a></li>
	<li id="menu-item-14859" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14859"><a href="http://fourhourworkweek.com/media/">Media Kit and Samples</a></li>
	<li id="menu-item-14855" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14855"><a href="http://fourhourworkweek.com/about/terms-of-service/">Terms of Service</a></li>
	<li id="menu-item-14856" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14856"><a href="http://fourhourworkweek.com/ftc-disclosure-blog/">Disclosure &#8211; The Full Monty</a></li>
	<li id="menu-item-14857" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14857"><a href="http://fourhourworkweek.com/privacy-policy/">Privacy Policy</a></li>
</ul>
</li>
<li id="menu-item-14860" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-14860"><a href="http://fourhourworkweek.com/contact/">Contact</a>
<ul class="sub-menu">
	<li id="menu-item-14852" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14852"><a href="http://fourhourworkweek.com/media/">Media Kit and Samples</a></li>
	<li id="menu-item-14861" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14861"><a href="http://fourhourworkweek.com/corrections/">Corrections? Please Fill Out This Form.</a></li>
	<li id="menu-item-14863" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14863"><a href="http://fourhourworkweek.com/contact/">Contacts</a></li>
	<li id="menu-item-14862" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-14862"><a href="http://fourhourworkweek.com/jobs/">Jobs</a></li>
</ul>
</li>
</ul></div>				</div>

				<div id='nav-search'>
					<div id="search-btn">
						<!-- <img src="https://s0.wp.com/wp-content/themes/vip/four-hour-work-week/images/responsive/search-icon.png" class="search-icon search-icon-open"> -->
						<i class="top-nav-icons search-icon search-icon-open"></i>
						<i class="top-nav-icons search-icon search-icon-close"></i>
						<!-- <img src="https://s0.wp.com/wp-content/themes/vip/four-hour-work-week/images/responsive/close-menu.png" class="search-icon search-icon-close"> -->
					</div>
					<form role="search" method="get" class="search-form" action="http://fourhourworkweek.com/">
	<label>
		<span class="screen-reader-text">Search for:</span>
		<input type="search" class="search-field" value="Search" name="s" title="Search for:" onfocus="if (this.value == 'Search') {this.value = '';}" onblur="if (this.value == '') {this.value = 'Search';}">
	</label>
	<input type="submit" class="search-submit" value="Search">
</form>
				</div>

			</nav>

			<!-- #site-navigation -->

		</header><!-- #masthead -->

		<div id="content" class="site-content">

	<div id="primary" class="content-area">
		<main id="main" class="site-main" role="main">



<article id="post-12498" class="post-12498 page type-page status-publish hentry">
	<header class="entry-header">
		<h1 class="entry-title">Podcast &#8211; The Tim Ferriss&nbsp;Show</h1>
	</header><!-- .entry-header -->

	<div class="entry-content">
		<p><img class="aligncenter size-full wp-image-13792" src="https://fhww.files.wordpress.com/2014/06/edit_page_e280b9_the_blog_of_author_tim_ferriss_e28094_wordpress.png?w=640" alt="Edit_Page_???_The_Blog_of_Author_Tim_Ferriss_???_WordPress"   /><br />
<img class="aligncenter wp-image-24164" src="https://fhww.files.wordpress.com/2015/12/best_of_2015-partnerbadge-podcasts-en.png?w=417&#038;h=140" alt="Best_of_2015-PartnerBadge-Podcasts-EN" width="417" height="140" /></p>
<p>Most days, <strong><a href="https://itunes.apple.com/us/podcast/the-tim-ferriss-show/id863897795?mt=2" target="_blank">The Tim Ferriss Show</a></strong> is the <a href="http://note.io/RP4Sbo" target="_blank">#1 business podcast on all of iTunes</a>, and it&#8217;s been ranked #1 (of all podcasts) on many occasions. ??It was also selected as iTunes&#8217; &#8220;Best of 2014&#8221; and &#8220;Best of 2015.&#8221;?? In the last few months, downloads have shot past 45,000,000 downloads.</p>
<p>Each episode, I deconstruct world-class performers from eclectic areas (investing, sports, business, art, etc.) to extract??the tactics and tools??you can use.</p>
<p>Prior guests include Arnold Schwarzenegger, Ed Catmull (President of Pixar), Jamie Foxx, Tony Robbins, Peter Thiel, Rick Rubin (legendary music producer), Reid Hoffman (LinkedIn), Jon Favreau (Director/writer), Mike Shinoda (Linkin Park), Neil Strauss (7x NYT bestselling author), and dozens more.</p>
<ul>
<li><strong>Subscribe to the show (<a class="subscribe-podcast-itunes" href="https://itunes.apple.com/us/podcast/the-tim-ferriss-show/id863897795?mt=2" target="_blank">iTunes</a>, <a class="subscribe-podcast-non-itunes" href="http://feeds.feedburner.com/thetimferrissshow" target="_blank">non-iTunes feed</a>)</strong></li>
<li><strong>Already heard it once or twice?</strong>??Please <a href="https://itunes.apple.com/us/podcast/the-tim-ferriss-show/id863897795?mt=2" target="_blank">leave a short review here</a>, and tell me which??guests I should have on!</li>
</ul>
<h3>Show Notes, Links, and Resources for All Episodes</h3>
<p>Below are all the shows, listed from newest to oldest!</p>
<p>If easier, you can search in this blog&#8217;s search bar. Just type in the guest name + &#8220;podcast&#8221; (e.g. &#8220;Josh Waitzkin podcast&#8221;, &#8220;Kevin Rose podcast&#8221;, &#8220;Stephen Dubner podcast&#8221;, etc.).</p>
                        <p id="post-25055" class="podcast post-25055 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-seneca tag-stoic tag-stoicism tag-the-tao-of-seneca">
                <a href="http://fourhourworkweek.com/2016/01/22/the-tao-of-seneca/" target="_blank">The Tao of Seneca: Letters from a Stoic&nbsp;Master</a>
            </p>
                        <p id="post-24623" class="podcast post-24623 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-acting-advice tag-american-history-x tag-birdman tag-crowdrise tag-ed-norton tag-edward-norton tag-entheogen-research tag-fight-club tag-primal-fear tag-tyler-durden">
                <a href="http://fourhourworkweek.com/2016/01/18/edward-norton-on-mastery-must-read-books-and-the-future-of-crowdfunding/" target="_blank">Edward Norton on Mastery, Must-Read Books, and The Future of&nbsp;Crowdfunding</a>
            </p>
                        <p id="post-24867" class="podcast post-24867 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-business-mistakes tag-chris-sacca tag-instagram tag-kickstarter tag-lowercase-capital tag-shark-tank tag-startup-success tag-twitter tag-uber tag-venture-capital">
                <a href="http://fourhourworkweek.com/2016/01/15/chris-sacca-on-shark-tank-building-your-business-and-startup-mistakes/" target="_blank">Chris Sacca on Shark Tank, Building Your Business, and Startup&nbsp;Mistakes</a>
            </p>
                        <p id="post-24554" class="podcast post-24554 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-autodidacts tag-canonical-design tag-drugs-over-dinner tag-eric-weinstein tag-overton-window tag-psychedelic-drugs tag-thiel-capital">
                <a href="http://fourhourworkweek.com/2016/01/13/eric-weinstein/" target="_blank">Eric Weinstein on Challenging ???Reality,??? Working with Peter Thiel, and Destroying Education to Save&nbsp;It</a>
            </p>
                        <p id="post-24392" class="podcast post-24392 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-daymond-john tag-four-hour-workweek tag-fubu tag-shark-tank tag-the-power-of-broke tag-tim-ferriss tag-tim-ferriss-interview">
                <a href="http://fourhourworkweek.com/2016/01/06/daymond-john-and-how-to-turn-weaknesses-into-strengths/" target="_blank">Daymond John and How to Turn Weaknesses into&nbsp;Strengths</a>
            </p>
                        <p id="post-24408" class="podcast post-24408 post type-post status-publish format-standard hentry category-random category-the-tim-ferriss-show tag-415362749 tag-kevin-rose tag-new-years-resolutions">
                <a href="http://fourhourworkweek.com/2016/01/03/new-years-resolutions/" target="_blank">Recommendations and Resolutions for&nbsp;2016</a>
            </p>
                        <p id="post-24317" class="podcast post-24317 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-anything-you-want tag-cd-baby tag-cdbaby tag-derek-sivers tag-sivvers">
                <a href="http://fourhourworkweek.com/2015/12/28/derek-sivers-reloaded-on-success-habits-and-billionaires-with-perfect-abs/" target="_blank">Derek Sivers Reloaded &#8211; On Success Habits and Billionaires with Perfect&nbsp;Abs</a>
            </p>
                        <p id="post-24067" class="podcast post-24067 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-amelia tag-amelia-boone tag-boon tag-boone tag-death-race tag-spartan-race tag-worlds-toughest-mudder">
                <a href="http://fourhourworkweek.com/2015/12/22/amelia-boone/" target="_blank">Amelia Boone on Beating 99% of Men and Suffering for High&nbsp;Performance</a>
            </p>
                        <p id="post-24163" class="podcast post-24163 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-best-of-2015 tag-itunes tag-tim-ferris tag-tim-ferriss tag-tim-ferriss-show">
                <a href="http://fourhourworkweek.com/2015/12/19/25-great-things-i-learned-from-podcast-guests-in-2015/" target="_blank">25 Great Things I Learned from Podcast Guests in&nbsp;2015</a>
            </p>
                        <p id="post-23905" class="podcast post-23905 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-anything-you-want tag-cd-baby tag-derek-sivers tag-hell-yeah-or-no tag-now-now-now">
                <a href="http://fourhourworkweek.com/2015/12/14/derek-sivers-on-developing-confidence-finding-happiness-and-saying-no-to-millions/" target="_blank">Derek Sivers on Developing Confidence, Finding Happiness, and Saying &#8220;No&#8221; to&nbsp;Millions</a>
            </p>
                        <p id="post-23839" class="podcast post-23839 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-a-dozen-roses tag-bill-cosby tag-black-lives-matter tag-hollywood tag-impressions tag-in-living-color tag-jamie-fox tag-jamie-foxx tag-jim-carey tag-jim-carrey tag-kanye-west tag-life-lessons tag-mike-tyson tag-oprah tag-podcast tag-puff-daddy tag-quentin-tarantino tag-ray tag-ray-charles tag-standup-comedy tag-tarantino">
                <a href="http://fourhourworkweek.com/2015/12/06/jamie-foxx/" target="_blank">Jamie Foxx on Workout Routines, Success Habits, and Untold Hollywood&nbsp;Stories</a>
            </p>
                        <p id="post-23582" class="podcast post-23582 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-acting tag-actor tag-bahai tag-basoon-king tag-bassoon-king tag-dwight tag-dwight-schrute tag-memoir tag-office tag-rain-wilson tag-rainn-wilson tag-the-office">
                <a href="http://fourhourworkweek.com/2015/11/30/rainn-wilson/" target="_blank">Rainn Wilson on Meditation, The Sexy Nostril Exercise, and Acting as&nbsp;Therapy</a>
            </p>
                        <p id="post-23635" class="podcast post-23635 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-appreciate-more tag-complain-less tag-headspace tag-increase-focus tag-live-a-better-life tag-meditation tag-mindfulness tag-more-focus tag-work-harder">
                <a href="http://fourhourworkweek.com/2015/11/29/magic-of-mindfulness/" target="_blank">The Magic of Mindfulness: Complain Less, Appreciate More, and Live a Better&nbsp;Life</a>
            </p>
                        <p id="post-23428" class="podcast post-23428 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-b-j-novak tag-bj-novak tag-list-app tag-tech tag-the-list-app tag-the-office">
                <a href="http://fourhourworkweek.com/2015/11/25/bj-novak/" target="_blank">B.J. Novak of The Office on Creative Process, Handling Rejection, and Good&nbsp;Comedy</a>
            </p>
                        <p id="post-23415" class="podcast post-23415 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-80000hours-org tag-doing-good-better tag-givewell-org tag-will-macaskill tag-william-macaskill">
                <a href="http://fourhourworkweek.com/2015/11/22/will-macaskill/" target="_blank">Will MacAskill on Effective Altruism, Y Combinator, and Artificial&nbsp;Intelligence</a>
            </p>
                        <p id="post-23264" class="podcast post-23264 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-actor tag-being-an-actor tag-dances-with-wolves tag-jfk tag-jon-baird tag-kevin-costner tag-the-explorers-guild tag-the-explorers-guild-volume-one-a-passage-to-shambhala tag-the-story-of-the-bison tag-work-ethic">
                <a href="http://fourhourworkweek.com/2015/11/16/kevin-costner-the-near-death-audition-work-ethic-and-the-explorers-guild/" target="_blank">Kevin Costner on Building His Career, Positive Self-Talk, and Making Dances with Wolves&nbsp;Happen</a>
            </p>
                        <p id="post-21667" class="podcast post-21667 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-alain-de-botton tag-how-marcel-proust-can-change-your-life tag-in-search-of-lost-time tag-montaigne tag-proust tag-the-consolations-of-philosophy">
                <a href="http://fourhourworkweek.com/2015/11/10/alain-de-botton/" target="_blank">How Philosophy Can Change Your Life, Alain de&nbsp;Botton</a>
            </p>
                        <p id="post-21179" class="podcast post-21179 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-cancer tag-dom-dagostino tag-fasting tag-hypertrophy tag-ketone-esters tag-ketone-supplements tag-ketones tag-ketosis tag-muscle-growth tag-nutritional-ketosis tag-therapeutic-ketosis">
                <a href="http://fourhourworkweek.com/2015/11/03/dominic-dagostino/" target="_blank">Dom D&#8217;Agostino on Fasting, Ketosis, and the End of&nbsp;Cancer</a>
            </p>
                        <p id="post-21911" class="podcast post-21911 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-beme tag-casey-neistat tag-daddy-long-legs tag-film-maker tag-final-cut-pro-x tag-hbo tag-movie-maker tag-nike tag-the-neistat-brothers tag-vlog tag-vloggers tag-youtube">
                <a href="http://fourhourworkweek.com/2015/10/27/casey-neistat/" target="_blank">How Renegade Filmmaker Casey Neistat Breaks Rules, Reinvents Himself, and Gets Thanked For&nbsp;It</a>
            </p>
                        <p id="post-22720" class="podcast post-22720 post type-post status-publish format-standard hentry category-the-tim-ferriss-show">
                <a href="http://fourhourworkweek.com/2015/10/24/lisa-randall/" target="_blank">Thinking About Extra Dimensions with Physicist Lisa&nbsp;Randall</a>
            </p>
                        <p id="post-22619" class="podcast post-22619 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-climbing tag-extreme-sports tag-jimmy-chin tag-jimmy-chin-photograghy tag-meru tag-rock-climbing tag-sundance tag-sundance-film-festival">
                <a href="http://fourhourworkweek.com/2015/10/20/the-athlete-and-artist-who-cheats-death-jimmy-chin/" target="_blank">The Athlete (And Artist) Who Cheats Death, Jimmy&nbsp;Chin</a>
            </p>
                        <p id="post-22329" class="podcast post-22329 post type-post status-publish format-standard hentry category-the-tim-ferriss-show">
                <a href="http://fourhourworkweek.com/2015/10/17/5-tools-i-use-for-faster-and-better-sleep/" target="_blank">5 Tools I Use For Faster And Better&nbsp;Sleep</a>
            </p>
                        <p id="post-21632" class="podcast post-21632 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-ebay tag-girlboss tag-nasty-gal tag-nastygal tag-retail tag-sophia-amorusa">
                <a href="http://fourhourworkweek.com/2015/10/13/the-nasty-icon-of-retail-sophia-amoruso/" target="_blank">The Nasty Icon of Retail, Sophia&nbsp;Amoruso</a>
            </p>
                        <p id="post-21914" class="podcast post-21914 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-ceo tag-expa tag-facebook tag-founders tag-garrett-camp tag-investing tag-investing-strategy tag-lifestyle-business tag-startup tag-startup-advice tag-twitter tag-uber tag-venture-businesses">
                <a href="http://fourhourworkweek.com/2015/10/09/should-you-start-a-startup-or-build-a-cash-flow-business/" target="_blank">Should You Start a &#8216;Startup&#8217; or Build a Cash-Flow&nbsp;Business?</a>
            </p>
                        <p id="post-21662" class="podcast post-21662 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-chris-sacca tag-chrystal-sacca tag-richard-betts tag-scratch-sniff tag-scratch-and-sniff tag-whiskey tag-whisky tag-wine">
                <a href="http://fourhourworkweek.com/2015/10/05/richard-betts/" target="_blank">The Tattooed Heretic of Wine and Whiskey, Richard&nbsp;Betts</a>
            </p>
                        <p id="post-21706" class="podcast post-21706 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-investing tag-real-estate tag-start-up tag-start-ups tag-startup tag-startups tag-stocks tag-warren-buffett">
                <a href="http://fourhourworkweek.com/2015/10/02/the-5-things-i-did-to-become-a-better-investor/" target="_blank">The 5 Things I Did To Become a Better&nbsp;Investor</a>
            </p>
                        <p id="post-21568" class="podcast post-21568 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-comedy tag-comedy-writers tag-evan-goldberg tag-funny-people tag-judd-apatow tag-knocked-up tag-movies tag-neighbors tag-pineapple-express tag-podcast tag-rogen tag-seth tag-seth-rogan tag-seth-rogen tag-superbad tag-the-interview tag-this-is-the-end">
                <a href="http://fourhourworkweek.com/2015/09/29/seth-rogen-and-evan-goldberg/" target="_blank">Comedy&#8217;s Dynamic Duo, Seth Rogen and Evan&nbsp;Goldberg</a>
            </p>
                        <p id="post-21295" class="podcast post-21295 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-extreme-ownership tag-jock-willink tag-jocko tag-john-willink tag-military tag-navy tag-navy-seals tag-seal tag-seals tag-special-forces tag-special-operations tag-special-ops tag-willink">
                <a href="http://fourhourworkweek.com/2015/09/25/jocko-willink/" target="_blank">The Scariest Navy SEAL Imaginable&#8230;And What He Taught&nbsp;Me</a>
            </p>
                        <p id="post-20793" class="podcast post-20793 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-affirmations tag-cartoons tag-dilbert tag-hypnotism tag-popular-cartoons tag-popular-comic-strips tag-positive-affirmations tag-scott-adams tag-writing-humor tag-writing-style">
                <a href="http://fourhourworkweek.com/2015/09/22/scott-adams-the-man-behind-dilbert/" target="_blank">Scott Adams: The Man Behind&nbsp;Dilbert</a>
            </p>
                        <p id="post-20832" class="podcast post-20832 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-habits-of-successful-people tag-meditation tag-morning-habits tag-morning-rituals tag-morning-routines tag-morning-tea tag-rituals-of-successful-people">
                <a href="http://fourhourworkweek.com/2015/09/18/5-morning-rituals/" target="_blank">5 Morning Rituals That Help Me Win The&nbsp;Day</a>
            </p>
                        <p id="post-19791" class="podcast post-19791 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-5-meo-dmt tag-ayahuasca tag-dr-martin-engle tag-dr-martin-polanco tag-iboga tag-ibogaine tag-lsd tag-podcast tag-psilocybin tag-psychedelic tag-psychedelics tag-the-tim-ferriss-show tag-traumatic-brain-injury">
                <a href="http://fourhourworkweek.com/2015/09/14/are-psychedelic-drugs-the-next-medical-breakthrough/" target="_blank">Are Psychedelic Drugs the Next Medical&nbsp;Breakthrough?</a>
            </p>
                        <p id="post-20335" class="podcast post-20335 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-drunk-dial tag-drunkdial tag-podcast tag-prank-calls tag-tim-ferris tag-tim-ferriss tag-timothy-ferris tag-timothy-ferriss">
                <a href="http://fourhourworkweek.com/2015/09/11/drunk-dialing/" target="_blank">Drunk Dialing Fans&#8211;Celebrating The 100th Podcast&nbsp;Episode!</a>
            </p>
                        <p id="post-19077" class="podcast post-19077 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-breath-exercises tag-breathing tag-exercises tag-hof tag-hoff tag-hold-your-breath tag-immune-system tag-meditation tag-protect-from-disease tag-the-iceman tag-wim tag-wim-hof tag-wim-hoff">
                <a href="http://fourhourworkweek.com/2015/09/07/the-iceman-wim-hof/" target="_blank">&#8220;The Iceman,&#8221; Wim&nbsp;Hof</a>
            </p>
                        <p id="post-19611" class="podcast post-19611 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-greylock-partners tag-linkedin tag-michael-mccullough tag-paypal tag-questbridge tag-reid-hoffman tag-startups">
                <a href="http://fourhourworkweek.com/2015/08/31/the-oracle-of-silicon-valley-reid-hoffman-plus-michael-mccullough/" target="_blank">The Oracle of Silicon Valley, Reid Hoffman (Plus: Michael&nbsp;McCullough)</a>
            </p>
                        <p id="post-19334" class="podcast post-19334 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-brene-brown tag-courage tag-podcast tag-rising-strong tag-shame tag-ted-talks tag-the-tim-ferriss-show tag-vulnerability">
                <a href="http://fourhourworkweek.com/2015/08/28/brene-brown-on-vulnerability-and-home-run-ted-talks/" target="_blank">Bren?? Brown on Vulnerability and Home Run TED&nbsp;Talks</a>
            </p>
                        <p id="post-18890" class="podcast post-18890 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-how-to-make-an-impression tag-how-to-network tag-networking tag-networking-events tag-networking-tips tag-south-by-southwest tag-sxsw tag-the-4-hour-workweek tag-the-tim-ferriss-show tag-tim-ferriss">
                <a href="http://fourhourworkweek.com/2015/08/26/how-to-build-a-world-class-network-in-record-time/" target="_blank">How to Build a World-Class Network in Record&nbsp;Time</a>
            </p>
                        <p id="post-18031" class="podcast post-18031 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-creativity tag-el-mariachi tag-el-rey tag-film-making tag-journaling tag-movie-making tag-movies tag-robert-rodriguez tag-the-tim-ferriss-show">
                <a href="http://fourhourworkweek.com/2015/08/23/the-wizard-of-hollywood-robert-rodriguez/" target="_blank">The &#8220;Wizard&#8221; of Hollywood, Robert&nbsp;Rodriguez</a>
            </p>
                        <p id="post-18643" class="podcast post-18643 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-angel-investing tag-angel-investor tag-angel-list tag-angellist tag-business-success tag-founders tag-investments tag-naval-ravikant tag-podcast tag-startup tag-the-tim-ferriss-show tag-venture-capital tag-venture-hacks">
                <a href="http://fourhourworkweek.com/2015/08/18/the-evolutionary-angel-naval-ravikant/" target="_blank">The Person I Call Most for Startup&nbsp;Advice</a>
            </p>
                        <p id="post-15991" class="podcast post-15991 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-artificial-intelligence tag-designer-babies tag-kevin-kelly tag-podcast tag-the-tim-ferriss-show tag-wired-magazine">
                <a href="http://fourhourworkweek.com/2015/08/07/kevin-kelly-on-artificial-intelligence-and-designer-babies/" target="_blank">Kevin Kelly on Artificial Intelligence and Designer&nbsp;Babies</a>
            </p>
                        <p id="post-15985" class="podcast post-15985 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-ceo tag-chairman tag-evernote tag-phil-libin tag-podcast tag-the-tim-ferriss-show">
                <a href="http://fourhourworkweek.com/2015/08/04/phil-libin/" target="_blank">What Evernote&#8217;s Phil Libin Learned from Jeff Bezos, Reid Hoffman, and&nbsp;Others</a>
            </p>
                        <p id="post-15668" class="podcast post-15668 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-arranged-marriage tag-fear-of-missing-out tag-fomo tag-guided-meditation tag-mindfulness tag-podcast tag-tara-brach tag-the-tim-ferriss-show">
                <a href="http://fourhourworkweek.com/2015/07/31/tara-brach/" target="_blank">Tara Brach on Meditation and Overcoming FOMO (Fear Of Missing&nbsp;Out)</a>
            </p>
                        <p id="post-15681" class="podcast post-15681 post type-post status-publish format-standard hentry category-the-tim-ferriss-show">
                <a href="http://fourhourworkweek.com/2015/07/28/jane-mcgonigal/" target="_blank">Jane McGonigal on Getting More Done with Less Stress and The Health Benefits of&nbsp;Gaming</a>
            </p>
                        <p id="post-15683" class="podcast post-15683 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-being-interesting tag-brain-pickings tag-brainpickings tag-creating-more-time tag-favorite-books tag-maria-popova tag-productivity tag-starting-a-successful-blog tag-time-efficiency">
                <a href="http://fourhourworkweek.com/2015/07/24/maria-popova-starting-a-successful-blog/" target="_blank">Maria Popova on Being Interesting, Creating More Time in a Day, And How to Start A Successful&nbsp;Blog</a>
            </p>
                        <p id="post-15687" class="podcast post-15687 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-active-release-techniques tag-charles-poliquin tag-fat-loss tag-hormone-replacement-therapy tag-joint-recovery tag-muscle-gain tag-strength-sensei">
                <a href="http://fourhourworkweek.com/2015/07/21/charles-poliquin/" target="_blank">Charles Poliquin on Strength Training, Shredding Body Fat, and Increasing Testosterone and Sex&nbsp;Drive</a>
            </p>
                        <p id="post-15671" class="podcast post-15671 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-billion-dollar-business tag-education-system tag-evolution-of-healthcare tag-human-longevity tag-peter-diamandis tag-planteary-resources tag-x-prize">
                <a href="http://fourhourworkweek.com/2015/07/17/peter-diamandis-on-the-education-system/" target="_blank">Peter Diamandis on Disrupting the Education System, The Evolution of Healthcare, and Building a Billion-Dollar&nbsp;Business</a>
            </p>
                        <p id="post-15673" class="podcast post-15673 post type-post status-publish format-standard hentry category-the-tim-ferriss-experiment-tfx category-the-tim-ferriss-show tag-big-wave tag-brian-mackenzie tag-brian-mckenzie tag-crossfit-endurance tag-gabby-reece tag-gabrielle-reece tag-gabrielle-reese tag-laird-hamilton tag-model tag-surfing tag-volleyball">
                <a href="http://fourhourworkweek.com/2015/07/15/laird-hamilton-the-king-of-big-wave-surfing-plus-gabrielle-reece-and-brian-mackenzie/" target="_blank">Laird Hamilton, The King of Big Wave Surfing (Plus: Gabrielle Reece and Brian&nbsp;MacKenzie)</a>
            </p>
                        <p id="post-15609" class="podcast post-15609 post type-post status-publish format-standard hentry category-the-tim-ferriss-show">
                <a href="http://fourhourworkweek.com/2015/07/10/general-stanley-mcchrystal-on-anti-war-americans-pushing-your-limits-and-the-three-military-tests-you-should-take/" target="_blank">General Stan McChrystal on Anti-War Americans, Pushing Your Limits, and The Three Military Tests You Should&nbsp;Take</a>
            </p>
                        <p id="post-15607" class="podcast post-15607 post type-post status-publish format-standard hentry category-the-tim-ferriss-show">
                <a href="http://fourhourworkweek.com/2015/07/08/sam-harris-on-daily-routines-the-trolley-scenario-and-5-books-everyone-should-read/" target="_blank">Sam Harris on Daily Routines, The Trolley Scenario, and 5 Books Everyone Should&nbsp;Read</a>
            </p>
                        <p id="post-15554" class="podcast post-15554 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-article tag-chris-fussell tag-christopher tag-fussell tag-general tag-jsoc tag-mcchrystal tag-mccrystal tag-memoir tag-military tag-my-share-of-the-task tag-podcast tag-rolling-stone tag-socom tag-special-forces tag-special-operations tag-special-ops tag-specops tag-stan tag-stanley tag-team-of-team">
                <a href="http://fourhourworkweek.com/2015/07/05/stanley-mcchrystal/" target="_blank">General Stan McChrystal on Eating One Meal Per Day, Special Ops, and Mental&nbsp;Toughness</a>
            </p>
                        <p id="post-15505" class="podcast post-15505 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-whitney-cummings">
                <a href="http://fourhourworkweek.com/2015/06/26/whitney-cummings/" target="_blank">Whitney Cummings on Turning Pain Into&nbsp;Creativity</a>
            </p>
                        <p id="post-15448" class="podcast post-15448 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-adam-gazzaley tag-current-stimulation tag-direct tag-neuroracer tag-neuroscience tag-tdcs tag-tms tag-transcranial tag-ucsf">
                <a href="http://fourhourworkweek.com/2015/06/22/adam-gazzaley/" target="_blank">The Maverick of Brain&nbsp;Optimization</a>
            </p>
                        <p id="post-15403" class="podcast post-15403 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-book tag-chef tag-facebook tag-instagram tag-nutrition tag-sam-kass tag-twitter tag-white-house tag-writing">
                <a href="http://fourhourworkweek.com/2015/06/18/sam-kass/" target="_blank">Sam Kass on Reinventing Yourself and Baptism by&nbsp;Fire</a>
            </p>
                        <p id="post-15328" class="podcast post-15328 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-braintree tag-bryan-johnson tag-hampton-creek tag-human-longevity tag-human-longevity-inc tag-matternet tag-os-fund tag-planetary-resources tag-vicarious">
                <a href="http://fourhourworkweek.com/2015/06/12/bryan-johnson/" target="_blank">The Rags to Riches Philosopher: Bryan Johnson&#8217;s Path to $800&nbsp;Million</a>
            </p>
                        <p id="post-15151" class="podcast post-15151 post type-post status-publish format-standard hentry category-investing category-the-tim-ferriss-show tag-billionaire tag-capital tag-chris-saca tag-chris-sacca tag-cover tag-forbes tag-instagram tag-kickstarter tag-lowercase tag-lowercase-capital tag-midas tag-twitter tag-uber">
                <a href="http://fourhourworkweek.com/2015/05/30/chris-sacca/" target="_blank">Chris Sacca on Being Different and Making&nbsp;Billions</a>
            </p>
                        <p id="post-15202" class="podcast post-15202 post type-post status-publish format-standard hentry category-the-tim-ferriss-show">
                <a href="http://fourhourworkweek.com/2015/05/28/how-to-build-a-large-audience-from-scratch-and-more/" target="_blank">How to Build a Large Audience From Scratch (And&nbsp;More)</a>
            </p>
                        <p id="post-13771" class="podcast post-13771 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-astro-teller tag-danielle-teller tag-google-x tag-googlex tag-sacred-cows">
                <a href="http://fourhourworkweek.com/2015/05/20/google-x/" target="_blank">Is It Time to Kill Sacred Cows In Your&nbsp;Relationship?</a>
            </p>
                        <p id="post-15050" class="podcast post-15050 post type-post status-publish format-standard hentry category-performance-psychology category-practical-philosophy category-the-tim-ferriss-show tag-beastie-boys tag-eminem tag-jay-z tag-kanya-west tag-lady-gaga tag-rick-rubin tag-slayer">
                <a href="http://fourhourworkweek.com/2015/05/15/rick-rubin/" target="_blank">Rick Rubin on Cultivating World-Class Artists (Jay Z, Johnny Cash, etc.), Losing 100+ Pounds, and Breaking Down The&nbsp;Complex</a>
            </p>
                        <p id="post-15028" class="podcast post-15028 post type-post status-publish format-standard hentry category-the-tim-ferriss-experiment-tfx category-the-tim-ferriss-show tag-appsumo tag-body tag-build-a-business tag-creative tag-creativelive tag-entrepreneur tag-fitness tag-health tag-kagan tag-live tag-lose-weight tag-noah tag-noah-kagan tag-start-up tag-sumome tag-tim-ferriss-experiment">
                <a href="http://fourhourworkweek.com/2015/05/07/noah-kagan/" target="_blank">How Facebook&#8217;s #30 Employee Quickly Built 4 Businesses and Gained 40 Pounds with Weight&nbsp;Training</a>
            </p>
                        <p id="post-14953" class="podcast post-14953 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-computer tag-computer-virus tag-drone tag-drones tag-hacker tag-kamkar tag-masterlock tag-sammy tag-samy-kamkar tag-tim-ferris tag-tim-ferris-experiment tag-tim-ferris-show tag-tim-ferriss-experiment tag-tim-ferriss-show tag-worm">
                <a href="http://fourhourworkweek.com/2015/05/02/samy-kamkar/" target="_blank">How One Computer Hacker Conquered Online Dating, Opens Locked Cars, and&nbsp;More</a>
            </p>
                        <p id="post-14781" class="podcast post-14781 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-floyd-mayweather tag-hhh tag-joe-defranco tag-jr tag-paul-levesque tag-the-undertake tag-triple-h tag-wwe">
                <a href="http://fourhourworkweek.com/2015/04/20/triple-h/" target="_blank">Triple H on Pre-Fight Rituals, Injury Avoidance, and Floyd Mayweather,&nbsp;Jr.</a>
            </p>
                        <p id="post-14734" class="podcast post-14734 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-chef tag-director tag-disney tag-elf tag-favreau tag-favrou tag-iron-man tag-iron-man-2 tag-john tag-jon tag-jon-favreau tag-jungle-book tag-screenplay tag-screenwriter tag-swingers tag-the tag-writer">
                <a href="http://fourhourworkweek.com/2015/04/14/jon-favreau/" target="_blank">Hit Filmmaker Jon Favreau&#8217;s Techniques and&nbsp;Routines</a>
            </p>
                        <p id="post-14745" class="podcast post-14745 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-how-to-earn-your-freedom tag-rolf-potts tag-vagabonding tag-world-travel">
                <a href="http://fourhourworkweek.com/2015/04/10/how-to-earn-your-freedom/" target="_blank">How to Earn Your Freedom&#8230;And A Motorcycle Ride Across&nbsp;China?</a>
            </p>
                        <p id="post-14565" class="podcast post-14565 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-blaze tag-fox tag-fox-news tag-glen-beck tag-glenn-beck tag-libertarian tag-news tag-texas tag-the-blaze">
                <a href="http://fourhourworkweek.com/2015/04/06/glenn-beck/" target="_blank">Inside the Mind of Glenn Beck, You Find&#8230;Walt Disney and Orson&nbsp;Welles?</a>
            </p>
                        <p id="post-14621" class="podcast post-14621 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-amanda-palmer tag-art-of-asking tag-dresden-dolls tag-ted tag-ted-talk tag-the-art-of-asking tag-theatre-is-evil">
                <a href="http://fourhourworkweek.com/2015/03/30/amanda-palmer/" target="_blank">Amanda Palmer on How to Fight, Meditate, and Make Good&nbsp;Art</a>
            </p>
                        <p id="post-14661" class="podcast post-14661 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-entheogen tag-iboga tag-ibogaine tag-james-fadiman tag-jim-fadiman tag-lsd tag-magic-mushrooms tag-mushrooms tag-psilocybin tag-psychedelic tag-psychedelic-explorers-guide tag-psychedelics tag-ram-dass tag-risks tag-timothy-leary">
                <a href="http://fourhourworkweek.com/2015/03/21/james-fadiman/" target="_blank">The Psychedelic Explorer&#8217;s Guide &#8211; Risks, Micro-Dosing, Ibogaine, and&nbsp;More</a>
            </p>
                        <p id="post-14640" class="podcast post-14640 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-blood-tests tag-ferris tag-ferriss tag-mark-hart tag-nusi tag-pete-attia tag-peter-attia tag-podcast tag-raoul-pal tag-tim tag-timothy">
                <a href="http://fourhourworkweek.com/2015/03/18/mark-hart-raoul-pal-peter-attia/" target="_blank">Optimizing Investing, Blood, Hormones, and Life (Podcast Double-Header: #63 and&nbsp;#65)</a>
            </p>
                        <p id="post-14542" class="podcast post-14542 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-cross-fit tag-crossfit tag-crossfit-games tag-kelly-starrett tag-sf-crossfit">
                <a href="http://fourhourworkweek.com/2015/03/04/the-good-the-bad-and-the-ugly-of-crossfit/" target="_blank">The Good, The Bad, and The Ugly of&nbsp;CrossFit</a>
            </p>
                        <p id="post-14190" class="podcast post-14190 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-boreta tag-glitch-mob tag-justin-boreta tag-the-glitch-mob">
                <a href="http://fourhourworkweek.com/2015/02/23/glitch-mob/" target="_blank">Productivity Secrets of a Master DJ (Meditation, Morning Routines, and&nbsp;More)</a>
            </p>
                        <p id="post-14388" class="podcast post-14388 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-automatic tag-automattic tag-matt-mullenweg tag-remote-working tag-the-year-without-pants tag-word-press tag-wordpress">
                <a href="http://fourhourworkweek.com/2015/02/09/matt-mullenweg/" target="_blank">Matt Mullenweg on Polyphasic Sleep, Tequila, and Building Billion-Dollar&nbsp;Companies</a>
            </p>
                        <p id="post-14338" class="podcast post-14338 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-arnold tag-arnold-schwarzenegger tag-genisys tag-get-to-the-choppa tag-governator tag-ill-be-back tag-predator tag-terminator tag-terminator-genisys">
                <a href="http://fourhourworkweek.com/2015/02/02/arnold-schwarzenegger/" target="_blank">Tim Ferriss Interviews Arnold Schwarzenegger on Psychological Warfare (And Much&nbsp;More)</a>
            </p>
                        <p id="post-14234" class="podcast post-14234 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-alex-blumberg tag-creativelive tag-gimlet-media tag-ira-glass tag-npr tag-podcast tag-reply-all tag-start-up tag-startup tag-startup-podcast tag-storytelling tag-this-american-life tag-we-made-a-mistake">
                <a href="http://fourhourworkweek.com/2015/01/29/alex-blumberg/" target="_blank">How to Create a Blockbuster&nbsp;Podcast</a>
            </p>
                        <p id="post-14202" class="podcast post-14202 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-bold tag-diamandis tag-elon-musk tag-eric-schmidt tag-global-learning tag-jeff-bezos tag-kurzweil tag-larry-page tag-pete tag-peter tag-peter-diamandis tag-x-prize tag-xprize">
                <a href="http://fourhourworkweek.com/2015/01/20/elon-musk-and-jeff-bezos/" target="_blank">How to Think Like Elon Musk and Jeff&nbsp;Bezos</a>
            </p>
                        <p id="post-14141" class="podcast post-14141 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-dead-lift tag-deadlift tag-kettlebell tag-pavel tag-pavel-tsatsouline tag-strength tag-strong-first tag-strongfirst tag-swing">
                <a href="http://fourhourworkweek.com/2015/01/15/pavel-tsatsouline/" target="_blank">Pavel Tsatsouline on the Science of Strength and the Art of Physical&nbsp;Performance</a>
            </p>
                        <p id="post-14022" class="podcast post-14022 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-jessica-richman tag-jonathan-eisen tag-microbiome tag-neil-gaiman tag-ubiome">
                <a href="http://fourhourworkweek.com/2015/01/10/microbiome/" target="_blank">Are We Really 10% Human and 90% Bacteria? Exploring The Microbiome&#8230;</a>
            </p>
                        <p id="post-13958" class="podcast post-13958 post type-post status-publish format-standard hentry category-performance-psychology category-the-4-hour-chef category-the-tim-ferriss-show tag-ed-cook tag-ed-cooke tag-josh-foer tag-joshua-foer tag-memory-devices tag-memrise tag-mnemonics tag-moonwalking-with-einstein tag-usa-national-memory-champion tag-world-memory-championships">
                <a href="http://fourhourworkweek.com/2014/12/30/ed-cooke/" target="_blank">Ed Cooke, Grandmaster of Memory, on Mental Performance, Imagination, and Productive&nbsp;Mischief</a>
            </p>
                        <p id="post-13739" class="podcast post-13739 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-4-hour-workweek tag-four-hour-workweek tag-success-story tag-updated">
                <a href="http://fourhourworkweek.com/2014/12/23/4-hour-work-week-2015/" target="_blank">What I&#8217;d Add To The 4-Hour Workweek for 2015 (And Much&nbsp;More)</a>
            </p>
                        <p id="post-13854" class="podcast post-13854 post type-post status-publish format-standard hentry category-physical-performance category-the-tim-ferriss-show tag-nusi tag-nutrition-science-initiative tag-nutritional-science-initiative tag-peter-attia">
                <a href="http://fourhourworkweek.com/2014/12/18/peter-attia/" target="_blank">Dr. Peter Attia on Life-Extension, Drinking Jet Fuel, Ultra-Endurance, Human Foie Gras, and&nbsp;More</a>
            </p>
                        <p id="post-13897" class="podcast post-13897 post type-post status-publish format-standard hentry category-physical-performance category-science-2 category-the-4-hour-body category-the-tim-ferriss-show tag-fatty-liver-disease tag-liver-cirrhosis tag-nusi tag-peter-attia">
                <a href="http://fourhourworkweek.com/2014/12/17/foie-gras/" target="_blank">Human Foie Gras &#8212; A Golden&nbsp;Opportunity</a>
            </p>
                        <p id="post-13677" class="podcast post-13677 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-data-breach tag-fbi tag-future-crime tag-future-crimes tag-hacking tag-interpol tag-marc-goodman">
                <a href="http://fourhourworkweek.com/2014/12/09/future-crimes/" target="_blank">Marc Goodman, FBI Futurist, on High-Tech Crime and How to Protect&nbsp;Yourself</a>
            </p>
                        <p id="post-13283" class="podcast post-13283 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-bryan-callen tag-comedy tag-comic tag-fighter-and-the-kid tag-martial-arts tag-standup">
                <a href="http://fourhourworkweek.com/2014/12/01/bryan-callen/" target="_blank">Bryan Callen on Eating Corgis (Yes, The Dogs) and Improving&nbsp;Creativity</a>
            </p>
                        <p id="post-13614" class="podcast post-13614 post type-post status-publish format-standard hentry category-random category-the-tim-ferriss-show tag-darya-rose tag-graham-hancock tag-kevin-rose tag-random-show tag-refinery29 tag-summer-tomato tag-too-many-cooks">
                <a href="http://fourhourworkweek.com/2014/11/25/the-random-show-hating-tech-hidden-japanese-gems-sexual-awkwardness-and-more/" target="_blank">The Random Show: Hating Tech, Hidden Japanese Gems, Sexual Awkwardness, and&nbsp;More</a>
            </p>
                        <p id="post-13331" class="podcast post-13331 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-nick-ganju tag-ping-pong tag-poker tag-zocdoc">
                <a href="http://fourhourworkweek.com/2014/11/21/nick-ganju/" target="_blank">Nick Ganju on The Majesty of Ping Pong, Poker, and How to Write Hit&nbsp;Songs</a>
            </p>
                        <p id="post-13329" class="podcast post-13329 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-30-rock tag-addiction tag-bisexual tag-bisexuality tag-comedy tag-drugs tag-margaret-cho tag-stand-up tag-standup">
                <a href="http://fourhourworkweek.com/2014/11/10/margaret-cho/" target="_blank">Margaret Cho on Comedy, Bisexuality, and The Slow-Carb&nbsp;Diet</a>
            </p>
                        <p id="post-13232" class="podcast post-13232 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-airbnb tag-bootsnall tag-budget-airfare tag-couchsurfing tag-rolf-potts tag-roundtrip tag-tickets tag-vagabonding tag-world-travel">
                <a href="http://fourhourworkweek.com/2014/11/04/rolf-potts/" target="_blank">Rolf Potts on Travel Tactics, Creating Time Wealth, and Lateral&nbsp;Thinking</a>
            </p>
                        <p id="post-13321" class="podcast post-13321 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-brian-koppelman tag-chase-jarvis tag-ed-catmull tag-james-altucher tag-jason-silva tag-joe-de-sena tag-josh tag-joshua-waitzkin tag-mike-shinoda tag-neil-strauss tag-peter-thiel tag-ramit-sethi tag-ryan-holiday tag-sam-harris tag-tony-robbins tag-tracy-dinunzio">
                <a href="http://fourhourworkweek.com/2014/10/29/the-books-that-shaped-billionaires-mega-bestselling-authors-and-other-prodigies/" target="_blank">The Unusual Books That Shaped Billionaires, Mega-Bestselling Authors, and Other&nbsp;Prodigies</a>
            </p>
                        <p id="post-13199" class="podcast post-13199 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-andrewzimmern tag-andrew-zimmern tag-bizarre-foods tag-dining-with-death">
                <a href="http://fourhourworkweek.com/2014/10/28/andrew-zimmern-on-simple-cooking-tricks-developing-tv-and-addiction/" target="_blank">Andrew Zimmern on Simple Cooking Tricks, Developing TV, and&nbsp;Addiction</a>
            </p>
                        <p id="post-13164" class="podcast post-13164 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-brain-pickings tag-brainpickings tag-maria-popova">
                <a href="http://fourhourworkweek.com/2014/10/21/brain-pickings/" target="_blank">Maria Popova on Writing, Workflow, and&nbsp;Workarounds</a>
            </p>
                        <p id="post-13120" class="podcast post-13120 post type-post status-publish format-standard hentry category-investing category-the-tim-ferriss-show tag-all-weather tag-anthony-robbins tag-carl-icahn tag-david-swensen tag-investing tag-money-master-the-game tag-paul-tudor-jones tag-ray-dalio tag-robbins tag-tony-robbins">
                <a href="http://fourhourworkweek.com/2014/10/15/money-master-the-game/" target="_blank">Tony Robbins on Morning Routines, Peak Performance, and Mastering&nbsp;Money</a>
            </p>
                        <p id="post-13102" class="podcast post-13102 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-harvard-business-school tag-i-will-teach-you-to-be-rich tag-negotiation tag-personal-finance tag-ramit tag-ramit-sethi tag-richard-branson tag-sethi tag-stanford">
                <a href="http://fourhourworkweek.com/2014/10/09/ramit-sethi-on-persuasion-and-turning-a-blog-into-a-multi-million-dollar-business/" target="_blank">Ramit Sethi on Persuasion and Turning a Blog Into a Multi-Million-Dollar Business</a>
            </p>
                        <p id="post-13087" class="podcast post-13087 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-anthony-robbins tag-date-with-destiny tag-diamandis tag-global-learning tag-pete tag-peter tag-peter-diamandis tag-tony-robbins tag-x-prize tag-xprize">
                <a href="http://fourhourworkweek.com/2014/10/07/global-learning-xprize/" target="_blank">Tony Robbins and Peter Diamandis (XPRIZE) on the Magic of Thinking&nbsp;BIG</a>
            </p>
                        <p id="post-13058" class="podcast post-13058 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-bootstrapping tag-finding-a-co-founder tag-john-doerr tag-recycled-bride tag-richard-branson tag-tracy-di-nunzio tag-tracy-dinunzio tag-tradesy tag-tradesy-com tag-women-in-tech">
                <a href="http://fourhourworkweek.com/2014/09/30/the-tim-ferriss-show-tracy-dinunzio-on-rapid-growth-and-rapid-learning/" target="_blank">The Tim Ferriss Show: Tracy DiNunzio on Rapid Growth and Rapid&nbsp;Learning</a>
            </p>
                        <p id="post-12967" class="podcast post-12967 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-blake-masters tag-book tag-clarium tag-founders-fund tag-peter-theil tag-peter-thiel tag-zero-to-one">
                <a href="http://fourhourworkweek.com/2014/09/09/peter-thiel/" target="_blank">The Tim Ferriss Show: Interview with Peter Thiel, Billionaire Investor and Company&nbsp;Creator</a>
            </p>
                        <p id="post-12868" class="podcast post-12868 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-1000-true-fans tag-cool-tools tag-kevin-kelly tag-kk-org tag-long-now-foundation">
                <a href="http://fourhourworkweek.com/2014/08/29/kevin-kelly/" target="_blank">The Tim Ferriss Show: Interview of Kevin Kelly, Co-Founder of WIRED, Polymath, Most Interesting Man In The&nbsp;World?</a>
            </p>
                        <p id="post-12837" class="podcast post-12837 post type-post status-publish format-standard hentry category-random category-the-tim-ferriss-show tag-ferris tag-ferriss tag-foundation tag-kevin-rose tag-random-show tag-the-random-show tag-tim tag-timothy">
                <a href="http://fourhourworkweek.com/2014/08/22/the-random-show-episode-25-gut-bacteria-meditation-startups-and-more/" target="_blank">The Random Show, Episode 25 &#8212; Gut Bacteria, Meditation, Startups, and&nbsp;More</a>
            </p>
                        <p id="post-12777" class="podcast post-12777 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-animation tag-creativity tag-ed-catmull tag-inc tag-pixar tag-podcast tag-tim-ferris tag-tim-ferriss tag-toy-story">
                <a href="http://fourhourworkweek.com/2014/08/12/ed-catmull/" target="_blank">The Tim Ferriss Show, Episode 22: Ed Catmull, President of Pixar, on Steve Jobs, Stories, and Lessons&nbsp;Learned</a>
            </p>
                        <p id="post-12700" class="podcast post-12700 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-fort-minor tag-linkin-park tag-mike-shinoda tag-podcast tag-remember-the-name tag-tim-ferris tag-tim-ferriss">
                <a href="http://fourhourworkweek.com/2014/08/04/mike-shinoda/" target="_blank">The Tim Ferriss Show, Episode 21: Mike Shinoda of Linkin Park &#8211; Making Art, Making Music, Getting To 60+ Million&nbsp;Albums</a>
            </p>
                        <p id="post-12667" class="podcast post-12667 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-dan-carlin tag-hardcore-history tag-podcast tag-tim-ferris tag-tim-ferriss">
                <a href="http://fourhourworkweek.com/2014/07/29/the-tim-ferriss-show-episode-20-dan-carlin-hardcore-history-building-podcasts-creativity-and-more/" target="_blank">The Tim Ferriss Show, Episode 20: Dan Carlin &#8211; Hardcore History, Building Podcasts, Creativity, and&nbsp;More</a>
            </p>
                        <p id="post-12609" class="podcast post-12609 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-choose-yourself tag-claudia-altucher tag-james-altucher tag-the-power-of-no">
                <a href="http://fourhourworkweek.com/2014/07/11/james-altucher/" target="_blank">The Tim Ferriss Show, Episode 18: James Altucher on How to Say &#8220;No&#8221;, Fail Better, and Build&nbsp;Businesses</a>
            </p>
                        <p id="post-12576" class="podcast post-12576 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-death-race tag-desena tag-joe-de-sena tag-joseph tag-spartan-race tag-spartan-up">
                <a href="http://fourhourworkweek.com/2014/07/01/spartan-race/" target="_blank">The Tim Ferriss Show, Episode 16: Joe De Sena on Grit, Endurance, and Building&nbsp;Empires</a>
            </p>
                        <p id="post-12539" class="podcast post-12539 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-emergency tag-neil-strauss tag-pickup-artists tag-pua tag-style tag-the-game">
                <a href="http://fourhourworkweek.com/2014/06/24/neil-strauss/" target="_blank">The Tim Ferriss Podcast, Ep 15: Neil Strauss, Author of The&nbsp;Game</a>
            </p>

<div id="jp-post-flair" class="sharedaddy sd-like-enabled sd-sharing-enabled"><div class="sharedaddy sd-sharing-enabled"><div class="robots-nocontent sd-block sd-social sd-social-icon-text sd-sharing"><h3 class="sd-title">Share this:</h3><div class="sd-content"><ul><li class="share-facebook"><a rel="nofollow" data-shared="sharing-facebook-12498" class="share-facebook sd-button share-icon" href="http://fourhourworkweek.com/podcast/?share=facebook" target="_blank" title="Share on Facebook"><span>Facebook</span></a></li><li class="share-twitter"><a rel="nofollow" data-shared="sharing-twitter-12498" class="share-twitter sd-button share-icon" href="http://fourhourworkweek.com/podcast/?share=twitter" target="_blank" title="Click to share on Twitter"><span>Twitter</span></a></li><li class="share-email"><a rel="nofollow" data-shared="" class="share-email sd-button share-icon" href="http://fourhourworkweek.com/podcast/?share=email" target="_blank" title="Click to email"><span>Email</span></a></li><li class="share-reddit"><a rel="nofollow" data-shared="" class="share-reddit sd-button share-icon" href="http://fourhourworkweek.com/podcast/?share=reddit" target="_blank" title="Click to share on Reddit"><span>Reddit</span></a></li><li class="share-end"></li></ul></div></div></div></div>				<p id="fhcp">Watch <a href="http://fourhourworkweek.com/tv/">The Tim Ferriss Experiment</a>, the new #1-rated TV show with "the world's best human guinea pig" (Newsweek), Tim Ferriss. It's Mythbusters meets Jackass. Shot and edited by the Emmy-award winning team behind Anthony Bourdain's No Reservations and Parts Unknown. <a href="http://fourhourworkweek.com/tv/">Here's the trailer</a>.</p>
	</div><!-- .entry-content -->
	</article><!-- #post-## -->


		</main><!-- #main -->
	</div><!-- #primary -->

	<div id="secondary" class="widget-area" role="complementary">

			<h3>Tim on Facebook&hellip;</h3>
	<div id="fb-root"></div>
	<script>(function(d, s, id) {var js, fjs = d.getElementsByTagName(s)[0]; if (d.getElementById(id)) return; js = d.createElement(s); js.id = id; js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=2530096808"; fjs.parentNode.insertBefore(js, fjs); }(document, 'script', 'facebook-jssdk'));</script>
	<div class="fb-like" data-href="https://www.facebook.com/TimFerriss" data-width="300" data-show-faces="true" data-send="false"></div><aside id="tf-popular-category-2" class="widget widget_tf-popular-category"><h1 class="widget-title">Popular Podcasts</h1><ul class="popular-post-list">								<li class="post-21295 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-extreme-ownership tag-jock-willink tag-jocko tag-john-willink tag-military tag-navy tag-navy-seals tag-seal tag-seals tag-special-forces tag-special-operations tag-special-ops tag-willink">
									<h4><a href="http://fourhourworkweek.com/2015/09/25/jocko-willink/">The Scariest Navy SEAL Imaginable&#8230;And What He Taught&nbsp;Me</a></h4>
								</li><!-- #post-21295 -->
																<li class="post-24408 post type-post status-publish format-standard hentry category-random category-the-tim-ferriss-show tag-415362749 tag-kevin-rose tag-new-years-resolutions">
									<h4><a href="http://fourhourworkweek.com/2016/01/03/new-years-resolutions/">Recommendations and Resolutions for&nbsp;2016</a></h4>
								</li><!-- #post-24408 -->
																<li class="post-24623 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-acting-advice tag-american-history-x tag-birdman tag-crowdrise tag-ed-norton tag-edward-norton tag-entheogen-research tag-fight-club tag-primal-fear tag-tyler-durden">
									<h4><a href="http://fourhourworkweek.com/2016/01/18/edward-norton-on-mastery-must-read-books-and-the-future-of-crowdfunding/">Edward Norton on Mastery, Must-Read Books, and The Future of&nbsp;Crowdfunding</a></h4>
								</li><!-- #post-24623 -->
																<li class="post-24317 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-anything-you-want tag-cd-baby tag-cdbaby tag-derek-sivers tag-sivvers">
									<h4><a href="http://fourhourworkweek.com/2015/12/28/derek-sivers-reloaded-on-success-habits-and-billionaires-with-perfect-abs/">Derek Sivers Reloaded &#8211; On Success Habits and Billionaires with Perfect&nbsp;Abs</a></h4>
								</li><!-- #post-24317 -->
								</ul><!-- .popular-post-list --></aside><aside id="tf-popular-in-category-2" class="widget widget_tf-popular-in-category"><h1 class="widget-title">Most Popular</h1><ul class="popular-post-list">							<li class="post-9559 post type-post status-publish format-standard hentry category-physical-performance tag-berardi tag-georges-st-pierre tag-nate-green tag-ufc">
								<h4><a href="http://fourhourworkweek.com/2013/05/06/how-to-cut-weight-ufc/">How To Lose 20-30 Pounds In 5 Days: The Extreme Weight Cutting and Rehydration Secrets of UFC&nbsp;Fighters</a></h4>
							</li><!-- #post-9559 -->
														<li class="post-12498 page type-page status-publish hentry">
								<h4><a href="http://fourhourworkweek.com/podcast/">Podcast &#8211; The Tim Ferriss&nbsp;Show</a></h4>
							</li><!-- #post-12498 -->
														<li class="post-19 post type-post status-publish format-standard hentry category-physical-performance category-the-4-hour-body category-uncategorized tag-fat-loss tag-how-to-lose-fat tag-ketogenic-diet tag-lose-fat tag-six-pack-abs">
								<h4><a href="http://fourhourworkweek.com/2007/04/06/how-to-lose-20-lbs-of-fat-in-30-days-without-doing-any-exercise/">How to Lose 20 lbs. of Fat in 30 Days&#8230; Without Doing Any&nbsp;Exercise</a></h4>
							</li><!-- #post-19 -->
														<li class="post-21295 post type-post status-publish format-standard hentry category-the-tim-ferriss-show tag-extreme-ownership tag-jock-willink tag-jocko tag-john-willink tag-military tag-navy tag-navy-seals tag-seal tag-seals tag-special-forces tag-special-operations tag-special-ops tag-willink">
								<h4><a href="http://fourhourworkweek.com/2015/09/25/jocko-willink/">The Scariest Navy SEAL Imaginable&#8230;And What He Taught&nbsp;Me</a></h4>
							</li><!-- #post-21295 -->
							</ul><!-- .popular-post-list --></aside><aside id="categories-2" class="widget widget_categories"><h1 class="widget-title">Topics</h1>		<ul>
	<li class="cat-item cat-item-4529301"><a href="http://fourhourworkweek.com/category/30-day-challenges/" >30-Day Challenges</a> (2)
</li>
	<li class="cat-item cat-item-47167197"><a href="http://fourhourworkweek.com/category/4-hour-case-studies/" >4-Hour Case Studies</a> (47)
</li>
	<li class="cat-item cat-item-44070"><a href="http://fourhourworkweek.com/category/automation/" >Automation</a> (7)
</li>
	<li class="cat-item cat-item-3990"><a href="http://fourhourworkweek.com/category/dance/" >Dance</a> (3)
</li>
	<li class="cat-item cat-item-19614065"><a href="http://fourhourworkweek.com/category/e-mail-detox/" >E-mail Detox</a> (21)
</li>
	<li class="cat-item cat-item-183"><a href="http://fourhourworkweek.com/category/entrepreneurship/" >Entrepreneurship</a> (55)
</li>
	<li class="cat-item cat-item-4427571"><a href="http://fourhourworkweek.com/category/filling-the-void/" >Filling the Void</a> (89)
</li>
	<li class="cat-item cat-item-1559"><a href="http://fourhourworkweek.com/category/gadgets/" >Gadgets</a> (15)
</li>
	<li class="cat-item cat-item-18399339"><a href="http://fourhourworkweek.com/category/geoarbitrage/" >Geoarbitrage</a> (8)
</li>
	<li class="cat-item cat-item-831"><a href="http://fourhourworkweek.com/category/interviews/" >Interviews</a> (28)
</li>
	<li class="cat-item cat-item-6635"><a href="http://fourhourworkweek.com/category/investing/" >Investing</a> (17)
</li>
	<li class="cat-item cat-item-1934"><a href="http://fourhourworkweek.com/category/language/" >Language</a> (16)
</li>
	<li class="cat-item cat-item-191382788"><a href="http://fourhourworkweek.com/category/low-information-diet-and-selective-ignorance/" >Low-Information Diet</a> (41)
</li>
	<li class="cat-item cat-item-175"><a href="http://fourhourworkweek.com/category/marketing/" >Marketing</a> (52)
</li>
	<li class="cat-item cat-item-2342036"><a href="http://fourhourworkweek.com/category/performance-psychology/" >Mental Performance</a> (39)
</li>
	<li class="cat-item cat-item-2324767"><a href="http://fourhourworkweek.com/category/mini-retirements/" >Mini-retirements</a> (24)
</li>
	<li class="cat-item cat-item-81565949"><a href="http://fourhourworkweek.com/category/muse-examples/" >Muse Examples</a> (9)
</li>
	<li class="cat-item cat-item-891"><a href="http://fourhourworkweek.com/category/nonsense/" >Nonsense</a> (5)
</li>
	<li class="cat-item cat-item-142755019"><a href="http://fourhourworkweek.com/category/opening-the-kimono-otk/" >Opening the Kimono &#8211; OTK</a> (4)
</li>
	<li class="cat-item cat-item-15450272"><a href="http://fourhourworkweek.com/category/outsourcing-life/" >Outsourcing Life</a> (16)
</li>
	<li class="cat-item cat-item-4936765"><a href="http://fourhourworkweek.com/category/physical-performance/" >Physical Performance</a> (45)
</li>
	<li class="cat-item cat-item-907119"><a href="http://fourhourworkweek.com/category/practical-philosophy/" >Practical Philosophy</a> (31)
</li>
	<li class="cat-item cat-item-17903"><a href="http://fourhourworkweek.com/category/presentations/" >Presentations</a> (3)
</li>
	<li class="cat-item cat-item-121507898"><a href="http://fourhourworkweek.com/category/protecting-personal-time/" >Protecting Time</a> (12)
</li>
	<li class="cat-item cat-item-76656104"><a href="http://fourhourworkweek.com/category/quarterly-shipments/" >Quarterly Shipments</a> (3)
</li>
	<li class="cat-item cat-item-30"><a href="http://fourhourworkweek.com/category/random/" >Random</a> (28)
</li>
	<li class="cat-item cat-item-7759746"><a href="http://fourhourworkweek.com/category/remote-offices/" >Remote Offices</a> (7)
</li>
	<li class="cat-item cat-item-191382790"><a href="http://fourhourworkweek.com/category/how-to-live-like-a-rockstar-in/" >Rockstar Living in&#8230;</a> (5)
</li>
	<li class="cat-item cat-item-4161848"><a href="http://fourhourworkweek.com/category/science-2/" >Science</a> (4)
</li>
	<li class="cat-item cat-item-46646188"><a href="http://fourhourworkweek.com/category/the-4-hour-body/" >The 4-Hour Body &#8211; 4HB</a> (47)
</li>
	<li class="cat-item cat-item-62858329"><a href="http://fourhourworkweek.com/category/the-4-hour-chef/" >The 4-Hour Chef &#8211; 4HC</a> (39)
</li>
	<li class="cat-item cat-item-134462025"><a href="http://fourhourworkweek.com/category/the-4-hour-chef-recipes/" >The 4-Hour Chef Recipes</a> (1)
</li>
	<li class="cat-item cat-item-83069833"><a href="http://fourhourworkweek.com/category/the-4-hour-workweek-book/" >The Book &#8211; 4HWW</a> (43)
</li>
	<li class="cat-item cat-item-63837380"><a href="http://fourhourworkweek.com/category/the-slow-carb-diet/" >The Slow-Carb Diet</a> (4)
</li>
	<li class="cat-item cat-item-222172150"><a href="http://fourhourworkweek.com/category/the-tim-ferriss-experiment-tfx/" >The Tim Ferriss Experiment &#8211; TFX</a> (11)
</li>
	<li class="cat-item cat-item-223337489"><a href="http://fourhourworkweek.com/category/the-tim-ferriss-show/" >The Tim Ferriss Show</a> (110)
</li>
	<li class="cat-item cat-item-178667560"><a href="http://fourhourworkweek.com/category/tim-ferriss-book-club/" >Tim Ferriss Book Club</a> (6)
</li>
	<li class="cat-item cat-item-200"><a href="http://fourhourworkweek.com/category/travel/" >Travel</a> (66)
</li>
	<li class="cat-item cat-item-1"><a href="http://fourhourworkweek.com/category/uncategorized/" >Uncategorized</a> (37)
</li>
	<li class="cat-item cat-item-6131995"><a href="http://fourhourworkweek.com/category/writing-and-blogging/" >Writing and Blogging</a> (23)
</li>
		</ul>
</aside>	</div><!-- #secondary -->

	</div><!-- #content -->
<div class="newsletter"></div>
	<footer id="colophon" class="site-footer" role="contentinfo">
		<div class="site-info">
			<span class="align-left"><a href="/sitemap.xml">XML Sitemap</a> / <a href="/about/terms-of-service/">Site Terms of Service</a> / <a href="http://vip.wordpress.com/" rel="nofollow" target="_blank">Powered by WordPress.com VIP</a></span>
		</div><!-- .site-info -->
		<div class="copyright-info">
			Copyright &copy; 2007&#8211;2016 Tim Ferriss.<br />
			THE 4-HOUR&reg; is a registered trademark of Tim Ferriss.<br />
			All rights reserved.
		</div>
	</footer><!-- #colophon -->
</div><!-- #page -->

<!-- wpcom_wp_footer -->
<script type='text/javascript' src='//0.gravatar.com/js/gprofiles.js?ver=201603y'></script>
<script type='text/javascript'>
/* <![CDATA[ */
var WPGroHo = {"my_hash":""};
/* ]]> */
</script>
<script type='text/javascript' src='https://s2.wp.com/wp-content/mu-plugins/gravatar-hovercards/wpgroho.js?m=1380573781g'></script>

	<script>
		//initialize and attach hovercards to all gravatars
		jQuery( document ).ready( function( $ ) {

			if (typeof Gravatar === "undefined"){
				return;
			}

			if ( typeof Gravatar.init !== "function" ) {
				return;
			}

			Gravatar.profile_cb = function( hash, id ) {
				WPGroHo.syncProfileData( hash, id );
			};
			Gravatar.my_hash = WPGroHo.my_hash;
			Gravatar.init( 'body', '#wp-admin-bar-my-account' );
		});
	</script>

		<div style="display:none">
	</div>
<script type='text/javascript'>
/* <![CDATA[ */
var HighlanderComments = {"loggingInText":"Logging In\u2026","submittingText":"Posting Comment\u2026","postCommentText":"Post Comment","connectingToText":"Connecting to %s","commentingAsText":"%1$s: You are commenting using your %2$s account.","logoutText":"Log Out","loginText":"Log In","connectURL":"https:\/\/fhww.wordpress.com\/public.api\/connect\/?action=request","logoutURL":"https:\/\/fhww.wordpress.com\/wp-login.php?action=logout&_wpnonce=7b0131b9fd","homeURL":"http:\/\/fourhourworkweek.com\/","postID":"12498","gravDefault":"identicon","enterACommentError":"Please enter a comment","enterEmailError":"Please enter your email address here","invalidEmailError":"Invalid email address","enterAuthorError":"Please enter your name here","gravatarFromEmail":"This picture will show whenever you leave a comment. Click to customize it.","logInToExternalAccount":"Log in to use details from one of these accounts.","change":"Change","changeAccount":"Change Account","comment_registration":"","userIsLoggedIn":"","isJetpack":"0","text_direction":"ltr"};
/* ]]> */
</script>
<script type='text/javascript' src='https://s2.wp.com/_static/??/wp-content/js/jquery/jquery.autoresize.js,/wp-content/mu-plugins/highlander-comments/script.js?m=1424115551j'></script>

	<script type="text/javascript">
		window.WPCOM_sharing_counts = {"http:\/\/fourhourworkweek.com\/podcast\/":12498};
	</script>
		<script type="text/javascript">
			var windowOpen;
		jQuery(document).on( 'ready post-load', function(){
			jQuery( 'a.share-facebook' ).on( 'click', function() {
				if ( 'undefined' !== typeof windowOpen ){ // If there's another sharing window open, close it.
					windowOpen.close();
				}
				windowOpen = window.open( jQuery(this).attr( 'href' ), 'wpcomfacebook', 'menubar=1,resizable=1,width=600,height=400' );
				return false;
			});
		});
		</script>
				<script type="text/javascript">
			var windowOpen;
		jQuery(document).on( 'ready post-load', function(){
			jQuery( 'a.share-twitter' ).on( 'click', function() {
				if ( 'undefined' !== typeof windowOpen ){ // If there's another sharing window open, close it.
					windowOpen.close();
				}
				windowOpen = window.open( jQuery(this).attr( 'href' ), 'wpcomtwitter', 'menubar=1,resizable=1,width=600,height=350' );
				return false;
			});
		});
		</script>
			<div id="sharing_email" style="display: none;">
		<form action="/podcast/" method="post">
			<label for="target_email">Send to Email Address</label>
			<input type="email" name="target_email" id="target_email" value="" />


				<label for="source_name">Your Name</label>
				<input type="text" name="source_name" id="source_name" value="" />

				<label for="source_email">Your Email Address</label>
				<input type="email" name="source_email" id="source_email" value="" />

						<input type="text" id="jetpack-source_f_name" name="source_f_name" class="input" value="" size="25" autocomplete="off" />
			<script> document.getElementById('jetpack-source_f_name').value = ''; </script>
			<div class="recaptcha" id="sharing_recaptcha"></div><input type="hidden" name="recaptcha_public_key" id="recaptcha_public_key" value="6LcYW8MSAAAAADBAuEH9yaPcF7lWh11Iq62ZKtoo" />
			<img style="float: right; display: none" class="loading" src="http://s2.wp.com/wp-content/mu-plugins/post-flair/sharing/images/loading.gif?m=1315610318g" alt="loading" width="16" height="16" />
			<input type="submit" value="Send Email" class="sharing_send" />
			<a rel="nofollow" href="#cancel" class="sharing_cancel">Cancel</a>

			<div class="errors errors-1" style="display: none;">
				Post was not sent - check your email addresses!			</div>

			<div class="errors errors-2" style="display: none;">
				Email check failed, please try again			</div>

			<div class="errors errors-3" style="display: none;">
				Sorry, your blog cannot share posts by email.			</div>
		</form>
	</div>
<script type='text/javascript'>
/* <![CDATA[ */
var comment_like_text = {"loading":"Loading..."};
/* ]]> */
</script>
<script type='text/javascript'>
/* <![CDATA[ */
var wpcomVipAnalytics = {"is_404":"0","is_home":"0","is_single":"0","is_front_page":"0","is_archive":"0","percentToTrack":"1"};
/* ]]> */
</script>
<script type='text/javascript'>
/* <![CDATA[ */
var JetpackEmojiSettings = {"base_url":"http:\/\/s0.wp.com\/wp-content\/mu-plugins\/emoji\/twemoji\/"};
/* ]]> */
</script>
<script type='text/javascript'>
/* <![CDATA[ */
var sharing_js_options = {"lang":"en","counts":"1"};
/* ]]> */
</script>
<script type='text/javascript' src='https://s2.wp.com/_static/??-eJyVj91uwjAMRl9oxgOBtl1Me5aQGuo0P16cEHj7tZOQ2oHEuImlz+fENjYBm2KhWNApdnRiS3JeOX3BWStUEF+PHBVtCmGMwPNAOjme96iNhZ6RFsFfsfQURuzEgodUM/TT01IeoBENk64cxFMmY/vn5cARKX5XqtSB2sxSFMbw+hNH62u33DOT+MtqBt05cgPTUPc7G0w0/lLY3hw3Eygkx1jaoj7kHRUxdoD/0Y8oSVrg4A1n1N5kjsdrHaWv8Lne7jZv6/ft64f7AY9hz4I='></script>
<script type="text/javascript">
// <![CDATA[
(function() {
try{
  if ( window.external &&'msIsSiteMode' in window.external) {
    if (window.external.msIsSiteMode()) {
      var jl = document.createElement('script');
      jl.type='text/javascript';
      jl.async=true;
      jl.src='/wp-content/plugins/ie-sitemode/custom-jumplist.php';
      var s = document.getElementsByTagName('script')[0];
      s.parentNode.insertBefore(jl, s);
    }
  }
}catch(e){}
})();
// ]]>
</script><script src="//stats.wp.com/w.js?50" type="text/javascript" async defer></script>
<script type="text/javascript">
_tkq = window._tkq || [];
_stq = window._stq || [];
_tkq.push(['storeContext', {'blog_id':'56542934','blog_tz':'-8','user_lang':'en','blog_lang':'en','user_id':'0'}]);
_stq.push(['view', {'blog':'56542934','v':'wpcom','tz':'-8','user_id':'0','post':'12498','subd':'fhww'}]);
function st_vt() {var x=document.createElement("img");x.src="http://pixel.wp.com/g.gif?blog=56542934&v=wpcomvt&tz=-8&user_id=0&post=12498&subd=fhww&rand="+Math.random();}
_stq.push(['extra', {'crypt':'UE40eW5QN0p8M2Y/RE1BNmNJfGhxNCVxUDExYmtXRThKbHcwXTdETWI1alhvb1oseHImN101ZFpEakVpYjlQYVFLYzBaVHRtPz0wXS9bMy85LGc/Zi9qTHZYQnJoVEVNRUVYTllEfk9TS3h+VUI2ZytpcTZpS0kudVM5S2hhNzFlfHRGPzd+UUZhdGxfPWxjP3JbSUJsTUkxY3h+VXc1bl9SeURraDdSc2ZsVUdEQk50RG1WM3JWM0lFaDNfQjJUSTJtPTFJU3pGcnVxa3B5ZjAsVUYleDJbQ01pNC1FNnYwJXM9an5SaWNtLE5RSVNbZ05rbmg0dENjZUs4NyVZZkNCal9F'}]);
_stq.push([ 'clickTrackerInit', '56542934', '12498' ]);
	</script>
<noscript><img src="http://pixel.wp.com/b.gif?v=noscript" style="height:0px;width:0px;overflow:hidden" alt="" /></noscript>
	<script type="text/javascript">
		adroll_adv_id = "23VJ6FL565GNZH3M6CMH2J";
		adroll_pix_id = "FTQCCOT57JHWVLQA7TU7IT";

		(function () {
			var _onload = function(){
				if (document.readyState && !/loaded|complete/.test(document.readyState)){setTimeout(_onload, 10);return}
				if (!window.__adroll_loaded){__adroll_loaded=true;setTimeout(_onload, 50);return}
				var scr = document.createElement("script");
				var host = (("https:" == document.location.protocol) ? "https://s.adroll.com" : "http://a.adroll.com");
				scr.setAttribute('async', 'true');
				scr.type = "text/javascript";
				scr.src = host + "/j/roundtrip.js";

				((document.getElementsByTagName('head') || [null])[0] || document.getElementsByTagName('script')[0].parentNode).appendChild(scr);
			};

			if (window.addEventListener) {window.addEventListener('load', _onload, false);}
			else {window.attachEvent('onload', _onload)}
		}());
	</script>
	<script>
if ( 'object' === typeof wpcom_mobile_user_agent_info ) {

	wpcom_mobile_user_agent_info.init();
	var mobileStatsQueryString = "";

	if( false !== wpcom_mobile_user_agent_info.matchedPlatformName )
		mobileStatsQueryString += "&x_" + 'mobile_platforms' + '=' + wpcom_mobile_user_agent_info.matchedPlatformName;

	if( false !== wpcom_mobile_user_agent_info.matchedUserAgentName )
		mobileStatsQueryString += "&x_" + 'mobile_devices' + '=' + wpcom_mobile_user_agent_info.matchedUserAgentName;

	if( wpcom_mobile_user_agent_info.isIPad() )
		mobileStatsQueryString += "&x_" + 'ipad_views' + '=' + 'views';

	if( "" != mobileStatsQueryString ) {
		new Image().src = document.location.protocol + '//pixel.wp.com/g.gif?v=wpcom-no-pv' + mobileStatsQueryString + '&baba=' + Math.random();
	}

}
</script><script type='text/javascript' src='http://platform.twitter.com/widgets.js?ver=20111117'></script>

<script src="https://s0.wp.com/wp-content/themes/vip/four-hour-work-week/js/min/footer-scripts-min.js"></script>
<img src="https://ad.doubleclick.net/ddm/activity/src=5039270;type=vod7g0;cat=vod-r00;u1=59931;u2=documentary;u3=;u4=website;u5=y;u6=;u7=;u9=;ord=1?" width="1" height="1" />
<script type="text/javascript">
var ftRandom = Math.random()*1000000; document.write('<iframe style="position:absolute; visibility:hidden; width:1px; height:1px;" src="https://servedby.flashtalking.com/container/6462;41712;4773;iframe/?spotName=Vimeo_Retargeting&U1=59931&U4=documentary&U5=landing_page&U6=allowed_in_trending&U7=&U8=trending_counter_off&U9=&cachebuster='+ftRandom+'"></iframe>');
</script>
</body>
</html>
'''
"""
import htmlentitydefs
import os

http_list = ['http://fourhourworkweek.com/podcast/']

podcast_find_pattern = '''<p\s #search through html for <p with trailing whitespace
        id="post-       #whitespace is followed by a post ids
        ([0-9]{5})"     #Match the 5 number post id and store that
        .*?<a\shref=    #Skip any extra characters including newlines until a link is found
        "(.*?)"         #Match the http link inside the ""
        .*?>            #Skip any other characters in the <a> tag. ie. target="_blank"
        (.*?)<\/a>      #Match the text before the </a> as the title
        .*?<\/p>        #move to end of the post paragraph
        '''

book_find_pattern = '''
        <li><a\shref="
        (.*?)
        \?tag.*?>
        (.*?)
        <\/a>
        \sby\s
        (\w+\W\w+)
        <\/li>
        '''

db_parent_pattern = 'http\:\/\/w*\.?(.*?)\.com' #matches with or without www

def unescape(text):
    '''Copied from http://effbot.org/zone/re-sub.htm#unescape-html
    uses re to search through the string and use the internal function fixup
    to substitute the unicode elements for there character equivilents'''
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)


def get_page(url):
    parent_db = get_re(db_parent_pattern, url, '', 'search')
    p = urllib2.urlopen(url)
    main_page = unescape(p.read().decode('utf-8'))
    return main_page, parent_db


def get_re(pattern, text, flags='', re_type='findall'):
    '''An abstracted regex function for multi-types
    Flags are added in the form (?sx) and concat with pattern before compile
    Currently only set for re_type=='search' and 'findall'(default)
    Function returns a string if search and a list of strings in findall or None'''
    pattern = pattern + flags
    expression = re.compile(pattern)
    if re_type == 'search':
        result = expression.search(text)
        return result.group(1) if result else None #checks for result and returns string if found and none if not
    elif re_type =='findall':
        result = expression.findall(text)
    else: result = None
    return result if result else None

def process_matches(list_of_items):
    for item in list_of_items:
        #title = unescape(item[2])
        print item[0] + ' | ' + item[1] + ' | ' + item[2]


def main():
    #offline main_page = html #get_page(http)
    http = http_list[0]
    main_page, parent_db = get_page(http)
    podcasts = get_re(podcast_find_pattern, main_page, '(?xs)','findall')

    test_pod = podcasts[1][1]
    #print test_pod
    pod_page, parent_db = get_page(test_pod)

    print pod_page[0:100]
    #   print parent_db

    books = get_re(book_find_pattern, pod_page, '(?x)', 'findall')

    print books

    '''
    print main_page[0:500]
    print parent_db
    #podcasts = get_podcasts(main_page)

    podcasts = get_re(podcast_find_pattern, main_page, '(?xs)','findall')
    if podcasts: process_matches(podcasts)

    print len(podcasts)

    #print podcasts[0]
    '''


#main()

print 'current working dir : ' + os.getcwd()

