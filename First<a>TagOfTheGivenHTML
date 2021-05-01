from bs4 import BeautifulSoup
html_doc = """
<!DOCTYPE html>

<html lang="en">
 <head>

  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="description" content="Breaking News English.com - Mini Lessons. Comes with more reading, activities, quizzes and a listening.">
  <title>Breaking News English | 2-Page Mini Lessons</title>

  <meta name="keywords" content="ESL online activity, Mini Lessons, Breaking News English, Online Activities">
  
  <!-- Stylesheets -->
  <link rel="stylesheet" href="style-mbd.css" type="text/css" media="all">
  


  <!-- meta tag for Facebook Insights -->
  <meta property="fb:admins" content="BreakingNewsEnglish" />        
                
  <meta property="og:title" content="Breaking News English - Mini Lessons" />
  <meta property="og:description" content="English News Lessons in 7 levels with graded multi-level listening and variable scrolled-reading, and all-skills activities." />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="http://www.breakingnewsenglish.com/mini_lessons.html" />
  <meta property="og:image" content="http://www.breakingnewsenglish.com/images/fb-og.jpg" />
  <meta property="og:site_name" content="www.breakingnewsenglish.com" />


  <!-- Mobile Specific Metas -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

</head>

<body class="page page-help right-sidebar">

<div id="masthead" class="section site-header">
  <div class="container">
    <div id="branding" class="content-container match-height">

        <h1 class="site-title"><a href="/" title="Thousands of free news english lessons - 7 levels, 27-Page handouts, 2-page mini-lessons, speed reading, 5-speed listening, mp3s &amp; 30+ online activities. Easier / Harder lessons every 2 days. English news lessons cover current events / current affairs topics on World News, Business News, Entertainment, Technology, Science...">Breaking News English</a></h1>
        
<h6><a href="index.html">Home</a>&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;<a href="help.html">Help This Site</a></h6>
</div><!-- #branding -->

    <div id="ideas-activities-ebook" class="content-container match-height">
      <h3 class="h5"><a title="New ideas and printable handouts that save you time - for news English and current affairs / current events lessons." href="book.html"><span>1,000 Ideas e-Book</span></a></h3>
    </div><!-- #ideas-activities-ebook -->

    <div id="more-free-lessons" class="content-container match-height">
      <h3 class="h5"><a href="http://www.freeeslmaterials.com/sean_banville_lessons.html" title="Thousands of news English lessons with printable handouts, MP3 listening, online quizzes and more. ESL / EFL lesson plans based on current events / current affairs." target="_blank"><span>Free English Lesson Websites</span></a></h3>
    </div><!-- #more-free-lessons -->

  </div><!-- .container -->
</div><!-- header .section -->



&nbsp;

<div class="advert section">
  <div class="container">
    <div class="content-container">
      <!-- Google Ad -->
      
      <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- r-activities -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-7356791340648458"
     data-ad-slot="9132895073"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
    </div><!-- .content-container -->    
  </div><!-- .container -->
</div><!-- .section -->

<div id="main" class="section">
  <div class="container section-header">
    <div class="content-container">
     <header>
       <h3>2-Page Mini  Lessons</h3></header>
    </div><!-- .content-container -->
  </div><!-- .container -->

  <div class="container">
    
    <div id="primary" class="content-area match-height">
        <div class="content-container">       
          <!-- Sharing -->
          <div class="sharing">
            <ul id="social-media-list" class="inline no-bullets">
              <li id="facebook-like">
                <iframe src="https://www.facebook.com/plugins/like.php?href=http%3A%2F%2Fwww.breakingnewsenglish.com%2Fmini_lessons.html&amp;width&amp;layout=button&amp;action=like&amp;show_faces=false&amp;share=true&amp;height=35" style="border:none; overflow:hidden; height:35px; display: inline; max-width: 100px;"></iframe>
              </li><!-- #facebook-like -->
              <li>
                <a title="... to a friend, student, colleague..." href="javascript:mailpage()">
                <strong>E-mail this <br>
                to a friend</strong> </a>
              </li>
              
              <li>
                <a href="https://twitter.com/share" class="twitter-share-button" data-size="large" data-count="none"></a>
              </li>
              <li>
                <a href="https://feeds.feedburner.com/breakingnewsenglish" title="Subscribe to my feed" rel="alternate" type="application/rss+xml"><strong>RSS<br>Feed
                </strong></a>
              </li>
            </ul><!-- #social-media-list .no-bullets -->
          </div>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print("Text of the first <a> tag:")
print(soup.find('a').text)

