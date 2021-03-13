  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>biopython/Bio/SeqUtils/ProtParam.py at master · biopython/biopython · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon-precomposed" sizes="57x57" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="apple-touch-icon-114.png" />
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="apple-touch-icon-144.png" />
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="apple-touch-icon-144.png" />
    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="lPD3CIOS3fYpn/bSBoHfGeTPm7PcqrkJwdmabE35mLc=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-a2a679dc329adac0ae0f3c8a55962cd292b6bb2e.css" media="screen" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-ddbc9d73271e204f76d48b6abb07e8791f16a0d5.css" media="screen" rel="stylesheet" type="text/css" />
    


    <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-eee761b9d5e06efb064aaaf528c44ef8e1601e71.js" type="text/javascript"></script>
    <script src="https://a248.e.akamai.net/assets.github.com/assets/github-0832d3a4f56ad9dbeb7df41b3c0e3adb5261d40a.js" type="text/javascript"></script>
    

      <link rel='permalink' href='/biopython/biopython/blob/8a0e7250b2bd548c6586cc4bb3b3a2cbdaa99ab0/Bio/SeqUtils/ProtParam.py'>
    <meta property="og:title" content="biopython"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/biopython/biopython"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/e17c48d1ab6c19cc203ad82d691e3806?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="biopython - Official git repository for Biopython (converted from CVS)"/>

    <meta name="description" content="biopython - Official git repository for Biopython (converted from CVS)" />

  <link href="https://github.com/biopython/biopython/commits/master.atom" rel="alternate" title="Recent Commits to biopython:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob macintosh vis-public env-production ">
    <div id="wrapper">

      

      

      


        <div class="header header-logged-out">
          <div class="container clearfix">

            <a class="header-logo-wordmark" href="https://github.com/">
              <img alt="GitHub" class="github-logo-4x" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x.png?1337118065" />
              <img alt="GitHub" class="github-logo-4x-hover" height="30" src="https://a248.e.akamai.net/assets.github.com/images/modules/header/logov7@4x-hover.png?1337118065" />
            </a>

              
<ul class="top-nav">
    <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
  <li class="search"><a href="https://github.com/search">Search</a></li>
  <li class="features"><a href="https://github.com/features">Features</a></li>
    <li class="blog"><a href="https://github.com/blog">Blog</a></li>
</ul>


            <div class="header-actions">
                <a class="button primary classy" href="https://github.com/signup">Sign up for free</a>
              <a class="button classy" href="https://github.com/login?return_to=%2Fbiopython%2Fbiopython%2Fblob%2Fmaster%2FBio%2FSeqUtils%2FProtParam.py">Sign in</a>
            </div>

          </div>
        </div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu">
          <div class="container">
            <div class="title-actions-bar">
              


                  <ul class="pagehead-actions">


          <li>
            <span class="star-button"><a href="/login?return_to=%2Fbiopython%2Fbiopython" class="minibutton js-toggler-target entice tooltipped leftwards" title="You must be signed in to use this feature" rel="nofollow"><span class="mini-icon mini-icon-star"></span>Star</a><a class="social-count js-social-count" href="/biopython/biopython/stargazers">297</a></span>
          </li>
          <li>
            <a href="/login?return_to=%2Fbiopython%2Fbiopython" class="minibutton js-toggler-target fork-button entice tooltipped leftwards"  title="You must be signed in to fork a repository" rel="nofollow"><span class="mini-icon mini-icon-fork"></span>Fork</a><a href="/biopython/biopython/network" class="social-count">150</a>
          </li>
    </ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-icon mega-icon-public-repo"></span>
                <span class="author vcard">
                  <a href="/biopython" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">biopython</span>
                  </a></span> /
                <strong><a href="/biopython/biopython" class="js-current-repository">biopython</a></strong>
              </h1>
            </div>

            

  <ul class="tabs">
    <li><a href="/biopython/biopython" class="selected" highlight="repo_sourcerepo_downloadsrepo_commitsrepo_tagsrepo_branches">Code</a></li>
    <li><a href="/biopython/biopython/network" highlight="repo_network">Network</a></li>
    <li><a href="/biopython/biopython/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>12</span></a></li>




    <li><a href="/biopython/biopython/graphs" highlight="repo_graphsrepo_contributors">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
      <li><a href="/biopython/biopython/tags" class="tabnav-tab" highlight="repo_tags">Tags <span class="counter ">41</span></a></li>
      <li><a href="/biopython/biopython/downloads" class="tabnav-tab" highlight="repo_downloads">Downloads <span class="counter blank">0</span></a></li>
    </ul>
    
  </span>

  <div class="tabnav-widget scope">


    <div class="context-menu-container js-menu-container js-context-menu">
      <a href="#"
         class="minibutton bigger switcher js-menu-target js-commitish-button btn-branch repo-tree"
         data-hotkey="w"
         data-ref="master">
         <span><em class="mini-icon mini-icon-branch"></em><i>branch:</i> master</span>
      </a>

      <div class="context-pane commitish-context js-menu-content">
        <a href="#" class="close js-menu-close"><span class="mini-icon mini-icon-remove-close"></span></a>
        <div class="context-title">Switch branches/tags</div>
        <div class="context-body pane-selector commitish-selector js-navigation-container">
          <div class="filterbar">
            <input type="text" id="context-commitish-filter-field" class="js-navigation-enable js-filterable-field" placeholder="Filter branches/tags">
            <ul class="tabs">
              <li><a href="#" data-filter="branches" class="selected">Branches</a></li>
                <li><a href="#" data-filter="tags">Tags</a></li>
            </ul>
          </div>

          <div class="js-filter-tab js-filter-branches">
            <div data-filterable-for="context-commitish-filter-field" data-filterable-type=substring>
                <div class="commitish-item branch-commitish selector-item js-navigation-item js-navigation-target selected">
                  <span class="mini-icon mini-icon-confirm"></span>
                  <h4>
                      <a href="/biopython/biopython/blob/master/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="master" rel="nofollow">master</a>
                  </h4>
                </div>
            </div>
            <div class="no-results">Nothing to show</div>
          </div>

            <div class="js-filter-tab js-filter-tags " style="display:none">
              <div data-filterable-for="context-commitish-filter-field" data-filterable-type=substring>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/start/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="start" rel="nofollow">start</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-160/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-160" rel="nofollow">biopython-160</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-159/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-159" rel="nofollow">biopython-159</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-158a/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-158a" rel="nofollow">biopython-158a</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-158/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-158" rel="nofollow">biopython-158</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-157/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-157" rel="nofollow">biopython-157</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-156/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-156" rel="nofollow">biopython-156</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-155b/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-155b" rel="nofollow">biopython-155b</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-155/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-155" rel="nofollow">biopython-155</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-154b/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-154b" rel="nofollow">biopython-154b</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-154/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-154" rel="nofollow">biopython-154</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-153/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-153" rel="nofollow">biopython-153</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-152/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-152" rel="nofollow">biopython-152</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-151b/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-151b" rel="nofollow">biopython-151b</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-151/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-151" rel="nofollow">biopython-151</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-150b/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-150b" rel="nofollow">biopython-150b</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-150/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-150" rel="nofollow">biopython-150</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-149b/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-149b" rel="nofollow">biopython-149b</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-149/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-149" rel="nofollow">biopython-149</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-148/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-148" rel="nofollow">biopython-148</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-147/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-147" rel="nofollow">biopython-147</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-146/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-146" rel="nofollow">biopython-146</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-145/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-145" rel="nofollow">biopython-145</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-144/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-144" rel="nofollow">biopython-144</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-143/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-143" rel="nofollow">biopython-143</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-142/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-142" rel="nofollow">biopython-142</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-141/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-141" rel="nofollow">biopython-141</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-140b/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-140b" rel="nofollow">biopython-140b</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-130/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-130" rel="nofollow">biopython-130</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-124/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-124" rel="nofollow">biopython-124</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-123/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-123" rel="nofollow">biopython-123</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-122/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-122" rel="nofollow">biopython-122</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-121/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-121" rel="nofollow">biopython-121</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-120/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-120" rel="nofollow">biopython-120</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-110/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-110" rel="nofollow">biopython-110</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-100a4/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-100a4" rel="nofollow">biopython-100a4</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-100a3/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-100a3" rel="nofollow">biopython-100a3</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-100a2/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-100a2" rel="nofollow">biopython-100a2</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-100a1/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-100a1" rel="nofollow">biopython-100a1</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-090d02/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-090d02" rel="nofollow">biopython-090d02</a>
                    </h4>
                  </div>
                  <div class="commitish-item tag-commitish selector-item js-navigation-item js-navigation-target ">
                    <span class="mini-icon mini-icon-confirm"></span>
                    <h4>
                        <a href="/biopython/biopython/blob/biopython-090d01/Bio/SeqUtils/ProtParam.py" class="js-navigation-open" data-name="biopython-090d01" rel="nofollow">biopython-090d01</a>
                    </h4>
                  </div>
              </div>
              <div class="no-results">Nothing to show</div>
            </div>
        </div>
      </div><!-- /.commitish-context-context -->
    </div>
  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/biopython/biopython" class="selected tabnav-tab" highlight="repo_source">Files</a></li>
    <li><a href="/biopython/biopython/commits/master" class="tabnav-tab" highlight="repo_commits">Commits</a></li>
    <li><a href="/biopython/biopython/branches" class="tabnav-tab" highlight="repo_branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:ed6cb05ca93baa02de126a1639f8ecd0 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:ed6cb05ca93baa02de126a1639f8ecd0 -->

<div id="slider">


    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>
      <div class="breadcrumb">
        <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/biopython/biopython" class="js-slide-to" data-direction="back" itemscope="url"><span itemprop="title">biopython</span></a></span></span> / <span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/biopython/biopython/tree/master/Bio" class="js-slide-to" data-direction="back" itemscope="url"><span itemprop="title">Bio</span></a></span> / <span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/biopython/biopython/tree/master/Bio/SeqUtils" class="js-slide-to" data-direction="back" itemscope="url"><span itemprop="title">SeqUtils</span></a></span> / <strong class="final-path">ProtParam.py</strong> <span class="js-clippy mini-icon mini-icon-clippy " data-clipboard-text="Bio/SeqUtils/ProtParam.py" data-copied-hint="copied!" data-copy-hint="copy to clipboard"></span>
      </div>

      <a href="/biopython/biopython/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>

        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/d952dbe2a8736e6860ba5a808c8d923c?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><a href="/cbrueffer" rel="author">cbrueffer</a></span>
    <time class="js-relative-date" datetime="2012-12-05T23:59:15-08:00" title="2012-12-05 23:59:15">December 05, 2012</time>
    <div class="commit-title">
        <a href="/biopython/biopython/commit/f57bacee36c57d4e3834faa5e68159a29a9bf658" class="message">Different PEP8 fixes, mostly spacing around inline comments (E261, E2…</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>4</strong> contributors</a></p>
          <a class="avatar tooltipped downwards" title="peterjc" href="/biopython/biopython/commits/master/Bio/SeqUtils/ProtParam.py?author=peterjc"><img height="20" src="https://secure.gravatar.com/avatar/871426dddc1a9f702316c1ca03a33d9b?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="cbrueffer" href="/biopython/biopython/commits/master/Bio/SeqUtils/ProtParam.py?author=cbrueffer"><img height="20" src="https://secure.gravatar.com/avatar/d952dbe2a8736e6860ba5a808c8d923c?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="kblin" href="/biopython/biopython/commits/master/Bio/SeqUtils/ProtParam.py?author=kblin"><img height="20" src="https://secure.gravatar.com/avatar/53842a70aa9f84f59423e5f0bf5b3d93?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>
    <a class="avatar tooltipped downwards" title="cmccoy" href="/biopython/biopython/commits/master/Bio/SeqUtils/ProtParam.py?author=cmccoy"><img height="20" src="https://secure.gravatar.com/avatar/0cf46d3ffedb153a97fe69cb4719e0fd?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="20" /></a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2>Users on GitHub who have contributed to this file</h2>
      <ul class="facebox-user-list">
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/871426dddc1a9f702316c1ca03a33d9b?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/peterjc">peterjc</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/d952dbe2a8736e6860ba5a808c8d923c?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/cbrueffer">cbrueffer</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/53842a70aa9f84f59423e5f0bf5b3d93?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/kblin">kblin</a>
        </li>
        <li>
          <img height="24" src="https://secure.gravatar.com/avatar/0cf46d3ffedb153a97fe69cb4719e0fd?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
          <a href="/cmccoy">cmccoy</a>
        </li>
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/biopython/biopython/blob/8a0e7250b2bd548c6586cc4bb3b3a2cbdaa99ab0/Bio/SeqUtils/ProtParam.py" data-title="biopython/Bio/SeqUtils/ProtParam.py at master · biopython/biopython · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">file</span>
                  <span>293 lines (225 sloc)</span>
                <span>11.308 kb</span>
              </div>
              <ul class="button-group actions">
                  <li>
                      <a class="grouped-button minibutton bigger lighter js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  </li>
                <li><a href="/biopython/biopython/raw/master/Bio/SeqUtils/ProtParam.py" class="minibutton grouped-button bigger lighter" id="raw-url">Raw</a></li>
                  <li><a href="/biopython/biopython/blame/master/Bio/SeqUtils/ProtParam.py" class="minibutton grouped-button bigger lighter">Blame</a></li>
                <li><a href="/biopython/biopython/commits/master/Bio/SeqUtils/ProtParam.py" class="minibutton grouped-button bigger lighter" rel="nofollow">History</a></li>
              </ul>
            </div>
                <div class="data type-python">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
</pre>
          </td>
          <td width="100%">
                <div class="highlight"><pre><div class='line' id='LC1'><span class="c"># Copyright Yair Benita Y.Benita@pharm.uu.nl</span></div><div class='line' id='LC2'><span class="c"># Biopython (http://biopython.org) license applies</span></div><div class='line' id='LC3'><br/></div><div class='line' id='LC4'><span class="sd">&quot;&quot;&quot;Simple protein analysis.</span></div><div class='line' id='LC5'><br/></div><div class='line' id='LC6'><span class="sd">Example,</span></div><div class='line' id='LC7'><br/></div><div class='line' id='LC8'><span class="sd">X = ProteinAnalysis(&quot;MAEGEITTFTALTEKFNLPPGNYKKPKLLYCSNGGHFLRILPDGTVDGTRDRSDQHIQLQLSAESVGEVYIKSTETGQYLAMDTSGLLYGSQTPSEECLFLERLEENHYNTYTSKKHAEKNWFVGLKKNGSCKRGPRTHYGQKAILFLPLPV&quot;)</span></div><div class='line' id='LC9'><span class="sd">print X.count_amino_acids()</span></div><div class='line' id='LC10'><span class="sd">print X.get_amino_acids_percent()</span></div><div class='line' id='LC11'><span class="sd">print X.molecular_weight()</span></div><div class='line' id='LC12'><span class="sd">print X.aromaticity()</span></div><div class='line' id='LC13'><span class="sd">print X.instability_index()</span></div><div class='line' id='LC14'><span class="sd">print X.flexibility()</span></div><div class='line' id='LC15'><span class="sd">print X.isoelectric_point()</span></div><div class='line' id='LC16'><span class="sd">print X.secondary_structure_fraction()</span></div><div class='line' id='LC17'><span class="sd">print X.protein_scale(ProtParamData.kd, 9, 0.4)</span></div><div class='line' id='LC18'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC21'><span class="kn">import</span> <span class="nn">ProtParamData</span>  <span class="c"># Local</span></div><div class='line' id='LC22'><span class="kn">import</span> <span class="nn">IsoelectricPoint</span>  <span class="c"># Local</span></div><div class='line' id='LC23'><span class="kn">from</span> <span class="nn">Bio.Seq</span> <span class="kn">import</span> <span class="n">Seq</span></div><div class='line' id='LC24'><span class="kn">from</span> <span class="nn">Bio.Alphabet</span> <span class="kn">import</span> <span class="n">IUPAC</span></div><div class='line' id='LC25'><span class="kn">from</span> <span class="nn">Bio.Data</span> <span class="kn">import</span> <span class="n">IUPACData</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'><span class="k">class</span> <span class="nc">ProteinAnalysis</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Class containing methods for protein analysis.</span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'><span class="sd">    The constructor takes two arguments.</span></div><div class='line' id='LC32'><span class="sd">    The first is the protein sequence as a string, which is then converted to a</span></div><div class='line' id='LC33'><span class="sd">    sequence object using the Bio.Seq module. This is done just to make sure</span></div><div class='line' id='LC34'><span class="sd">    the sequence is a protein sequence and not anything else.</span></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'><span class="sd">    The second argument is optional. If set to True, the weight of the amino</span></div><div class='line' id='LC37'><span class="sd">    acids will be calculated using their monoisotopic mass (the weight of the</span></div><div class='line' id='LC38'><span class="sd">    most abundant isotopes for each element), instead of the average molecular</span></div><div class='line' id='LC39'><span class="sd">    mass (the averaged weight of all stable isotopes for each element).</span></div><div class='line' id='LC40'><span class="sd">    If set to false (the default value) or left out, the IUPAC average</span></div><div class='line' id='LC41'><span class="sd">    molecular mass will be used for the calculation.</span></div><div class='line' id='LC42'><br/></div><div class='line' id='LC43'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">prot_sequence</span><span class="p">,</span> <span class="n">monoisotopic</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">prot_sequence</span><span class="o">.</span><span class="n">islower</span><span class="p">():</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sequence</span> <span class="o">=</span> <span class="n">Seq</span><span class="p">(</span><span class="n">prot_sequence</span><span class="o">.</span><span class="n">upper</span><span class="p">(),</span> <span class="n">IUPAC</span><span class="o">.</span><span class="n">protein</span><span class="p">)</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">sequence</span> <span class="o">=</span> <span class="n">Seq</span><span class="p">(</span><span class="n">prot_sequence</span><span class="p">,</span> <span class="n">IUPAC</span><span class="o">.</span><span class="n">protein</span><span class="p">)</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">amino_acids_content</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">amino_acids_percent</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sequence</span><span class="p">)</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">monoisotopic</span> <span class="o">=</span> <span class="n">monoisotopic</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">count_amino_acids</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Count standard amino acids, returns a dict.</span></div><div class='line' id='LC56'><br/></div><div class='line' id='LC57'><span class="sd">        Counts the number times each amino acid is in the protein</span></div><div class='line' id='LC58'><span class="sd">        sequence. Returns a dictionary {AminoAcid:Number}.</span></div><div class='line' id='LC59'><br/></div><div class='line' id='LC60'><span class="sd">        The return value is cached in self.amino_acids_content.</span></div><div class='line' id='LC61'><span class="sd">        It is not recalculated upon subsequent calls.</span></div><div class='line' id='LC62'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">amino_acids_content</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prot_dic</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">([(</span><span class="n">k</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span> <span class="k">for</span> <span class="n">k</span> <span class="ow">in</span> <span class="n">IUPACData</span><span class="o">.</span><span class="n">protein_letters</span><span class="p">])</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">aa</span> <span class="ow">in</span> <span class="n">prot_dic</span><span class="p">:</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">prot_dic</span><span class="p">[</span><span class="n">aa</span><span class="p">]</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sequence</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="n">aa</span><span class="p">)</span></div><div class='line' id='LC67'><br/></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">amino_acids_content</span> <span class="o">=</span> <span class="n">prot_dic</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">amino_acids_content</span></div><div class='line' id='LC71'><br/></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">get_amino_acids_percent</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Calculate the amino acid content in percentages.</span></div><div class='line' id='LC74'><br/></div><div class='line' id='LC75'><span class="sd">        The same as count_amino_acids only returns the Number in percentage of</span></div><div class='line' id='LC76'><span class="sd">        entire sequence. Returns a dictionary of {AminoAcid:percentage}.</span></div><div class='line' id='LC77'><br/></div><div class='line' id='LC78'><span class="sd">        The return value is cached in self.amino_acids_percent.</span></div><div class='line' id='LC79'><br/></div><div class='line' id='LC80'><span class="sd">        input is the dictionary self.amino_acids_content.</span></div><div class='line' id='LC81'><span class="sd">        output is a dictionary with amino acids as keys.</span></div><div class='line' id='LC82'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">amino_acids_percent</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aa_counts</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">count_amino_acids</span><span class="p">()</span></div><div class='line' id='LC85'><br/></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">percentages</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">aa</span> <span class="ow">in</span> <span class="n">aa_counts</span><span class="p">:</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">percentages</span><span class="p">[</span><span class="n">aa</span><span class="p">]</span> <span class="o">=</span> <span class="n">aa_counts</span><span class="p">[</span><span class="n">aa</span><span class="p">]</span> <span class="o">/</span> <span class="nb">float</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="p">)</span></div><div class='line' id='LC89'><br/></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">amino_acids_percent</span> <span class="o">=</span> <span class="n">percentages</span></div><div class='line' id='LC91'><br/></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">amino_acids_percent</span></div><div class='line' id='LC93'><br/></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">molecular_weight</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Calculate MW from Protein sequence&quot;&quot;&quot;</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># make local dictionary for speed</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">monoisotopic</span><span class="p">:</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">water</span> <span class="o">=</span> <span class="mf">18.01</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">iupac_weights</span> <span class="o">=</span> <span class="n">IUPACData</span><span class="o">.</span><span class="n">monoisotopic_protein_weights</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">iupac_weights</span> <span class="o">=</span> <span class="n">IUPACData</span><span class="o">.</span><span class="n">protein_weights</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">water</span> <span class="o">=</span> <span class="mf">18.02</span></div><div class='line' id='LC103'><br/></div><div class='line' id='LC104'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aa_weights</span> <span class="o">=</span> <span class="p">{}</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">iupac_weights</span><span class="p">:</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># remove a molecule of water from the amino acid weight</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aa_weights</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">iupac_weights</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">-</span> <span class="n">water</span></div><div class='line' id='LC108'><br/></div><div class='line' id='LC109'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">total_weight</span> <span class="o">=</span> <span class="n">water</span> <span class="c"># add just one water molecule for the whole sequence</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">aa</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">sequence</span><span class="p">:</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">total_weight</span> <span class="o">+=</span> <span class="n">aa_weights</span><span class="p">[</span><span class="n">aa</span><span class="p">]</span></div><div class='line' id='LC112'><br/></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">total_weight</span></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">aromaticity</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Calculate the aromaticity according to Lobry, 1994.</span></div><div class='line' id='LC117'><br/></div><div class='line' id='LC118'><span class="sd">        Calculates the aromaticity value of a protein according to Lobry, 1994.</span></div><div class='line' id='LC119'><span class="sd">        It is simply the relative frequency of Phe+Trp+Tyr.</span></div><div class='line' id='LC120'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aromatic_aas</span> <span class="o">=</span> <span class="s">&#39;YWF&#39;</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aa_percentages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_amino_acids_percent</span><span class="p">()</span></div><div class='line' id='LC123'><br/></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aromaticity</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">([</span><span class="n">aa_percentages</span><span class="p">[</span><span class="n">aa</span><span class="p">]</span> <span class="k">for</span> <span class="n">aa</span> <span class="ow">in</span> <span class="n">aromatic_aas</span><span class="p">])</span></div><div class='line' id='LC125'><br/></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">aromaticity</span></div><div class='line' id='LC127'><br/></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">instability_index</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Calculate the instability index according to Guruprasad et al 1990.</span></div><div class='line' id='LC130'><br/></div><div class='line' id='LC131'><span class="sd">        Implementation of the method of Guruprasad et al. 1990 to test a</span></div><div class='line' id='LC132'><span class="sd">        protein for stability. Any value above 40 means the protein is unstable</span></div><div class='line' id='LC133'><span class="sd">        (has a short half life).</span></div><div class='line' id='LC134'><br/></div><div class='line' id='LC135'><span class="sd">        See: Guruprasad K., Reddy B.V.B., Pandit M.W.</span></div><div class='line' id='LC136'><span class="sd">        Protein Engineering 4:155-161(1990).</span></div><div class='line' id='LC137'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">index</span> <span class="o">=</span> <span class="n">ProtParamData</span><span class="o">.</span><span class="n">DIWV</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">score</span> <span class="o">=</span> <span class="mf">0.0</span></div><div class='line' id='LC140'><br/></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">length</span> <span class="o">-</span> <span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">this</span><span class="p">,</span> <span class="nb">next</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sequence</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span><span class="o">+</span><span class="mi">2</span><span class="p">]</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dipeptide_value</span> <span class="o">=</span> <span class="n">index</span><span class="p">[</span><span class="n">this</span><span class="p">][</span><span class="nb">next</span><span class="p">]</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">score</span> <span class="o">+=</span> <span class="n">dipeptide_value</span></div><div class='line' id='LC145'><br/></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">(</span><span class="mf">10.0</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="p">)</span> <span class="o">*</span> <span class="n">score</span></div><div class='line' id='LC147'><br/></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">flexibility</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Calculate the flexibility according to Vihinen, 1994.</span></div><div class='line' id='LC150'><br/></div><div class='line' id='LC151'><span class="sd">        No argument to change window size because parameters are specific for a</span></div><div class='line' id='LC152'><span class="sd">        window=9. The parameters used are optimized for determining the flexibility.</span></div><div class='line' id='LC153'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flexibilities</span> <span class="o">=</span> <span class="n">ProtParamData</span><span class="o">.</span><span class="n">Flex</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">window_size</span> <span class="o">=</span> <span class="mi">9</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">weights</span> <span class="o">=</span> <span class="p">[</span><span class="mf">0.25</span><span class="p">,</span> <span class="mf">0.4375</span><span class="p">,</span> <span class="mf">0.625</span><span class="p">,</span> <span class="mf">0.8125</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">scores</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC158'><br/></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">length</span> <span class="o">-</span> <span class="n">window_size</span><span class="p">):</span></div><div class='line' id='LC160'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">subsequence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sequence</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span><span class="o">+</span><span class="n">window_size</span><span class="p">]</span></div><div class='line' id='LC161'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">score</span> <span class="o">=</span> <span class="mf">0.0</span></div><div class='line' id='LC162'><br/></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">window_size</span> <span class="o">//</span> <span class="mi">2</span><span class="p">):</span></div><div class='line' id='LC164'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">front</span> <span class="o">=</span> <span class="n">subsequence</span><span class="p">[</span><span class="n">j</span><span class="p">]</span></div><div class='line' id='LC165'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">back</span> <span class="o">=</span> <span class="n">subsequence</span><span class="p">[</span><span class="n">window_size</span> <span class="o">-</span> <span class="n">j</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">score</span> <span class="o">+=</span> <span class="p">(</span><span class="n">flexibilities</span><span class="p">[</span><span class="n">front</span><span class="p">]</span> <span class="o">+</span> <span class="n">flexibilities</span><span class="p">[</span><span class="n">back</span><span class="p">])</span> <span class="o">*</span> <span class="n">weights</span><span class="p">[</span><span class="n">j</span><span class="p">]</span></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">middle</span> <span class="o">=</span> <span class="n">subsequence</span><span class="p">[</span><span class="n">window_size</span> <span class="o">//</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC169'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">score</span> <span class="o">+=</span> <span class="n">flexibilities</span><span class="p">[</span><span class="n">middle</span><span class="p">]</span></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">score</span> <span class="o">/</span> <span class="mf">5.25</span><span class="p">)</span></div><div class='line' id='LC172'><br/></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">scores</span></div><div class='line' id='LC174'><br/></div><div class='line' id='LC175'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">gravy</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC176'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Calculate the gravy according to Kyte and Doolittle.&quot;&quot;&quot;</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">total_gravy</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">ProtParamData</span><span class="o">.</span><span class="n">kd</span><span class="p">[</span><span class="n">aa</span><span class="p">]</span> <span class="k">for</span> <span class="n">aa</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">sequence</span><span class="p">)</span></div><div class='line' id='LC178'><br/></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">total_gravy</span> <span class="o">/</span> <span class="bp">self</span><span class="o">.</span><span class="n">length</span></div><div class='line' id='LC180'><br/></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">_weight_list</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">window</span><span class="p">,</span> <span class="n">edge</span><span class="p">):</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Makes a list of relative weight of the</span></div><div class='line' id='LC183'><span class="sd">        window edges compared to the window center. The weights are linear.</span></div><div class='line' id='LC184'><span class="sd">        it actually generates half a list. For a window of size 9 and edge 0.4</span></div><div class='line' id='LC185'><span class="sd">        you get a list of [0.4, 0.55, 0.7, 0.85].</span></div><div class='line' id='LC186'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC187'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">unit</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="p">(</span><span class="mf">1.0</span> <span class="o">-</span> <span class="n">edge</span><span class="p">)</span> <span class="o">/</span> <span class="p">(</span><span class="n">window</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">weights</span> <span class="o">=</span> <span class="p">[</span><span class="mf">0.0</span><span class="p">]</span> <span class="o">*</span> <span class="p">(</span><span class="n">window</span> <span class="o">//</span> <span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC189'><br/></div><div class='line' id='LC190'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">window</span> <span class="o">//</span> <span class="mi">2</span><span class="p">):</span></div><div class='line' id='LC191'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">weights</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">edge</span> <span class="o">+</span> <span class="n">unit</span> <span class="o">*</span> <span class="n">i</span></div><div class='line' id='LC192'><br/></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">weights</span></div><div class='line' id='LC194'><br/></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">protein_scale</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">param_dict</span><span class="p">,</span> <span class="n">window</span><span class="p">,</span> <span class="n">edge</span><span class="o">=</span><span class="mf">1.0</span><span class="p">):</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Compute a profile by any amino acid scale.</span></div><div class='line' id='LC197'><br/></div><div class='line' id='LC198'><span class="sd">        An amino acid scale is defined by a numerical value assigned to each type of</span></div><div class='line' id='LC199'><span class="sd">        amino acid. The most frequently used scales are the hydrophobicity or</span></div><div class='line' id='LC200'><span class="sd">        hydrophilicity scales and the secondary structure conformational parameters</span></div><div class='line' id='LC201'><span class="sd">        scales, but many other scales exist which are based on different chemical and</span></div><div class='line' id='LC202'><span class="sd">        physical properties of the amino acids.  You can set several parameters that</span></div><div class='line' id='LC203'><span class="sd">        control the computation  of a scale profile, such as the window size and the</span></div><div class='line' id='LC204'><span class="sd">        window edge relative weight value.</span></div><div class='line' id='LC205'><br/></div><div class='line' id='LC206'><span class="sd">        WindowSize: The window size is the length</span></div><div class='line' id='LC207'><span class="sd">        of the interval to use for the profile computation. For a window size n, we</span></div><div class='line' id='LC208'><span class="sd">        use the i-(n-1)/2 neighboring residues on each side to compute</span></div><div class='line' id='LC209'><span class="sd">        the score for residue i. The score for residue i is the sum of the scaled values</span></div><div class='line' id='LC210'><span class="sd">        for these amino acids, optionally weighted according to their position in the</span></div><div class='line' id='LC211'><span class="sd">        window.</span></div><div class='line' id='LC212'><br/></div><div class='line' id='LC213'><span class="sd">        Edge: The central amino acid of the window always has a weight of 1.</span></div><div class='line' id='LC214'><span class="sd">        By default, the amino acids at the remaining window positions have the same</span></div><div class='line' id='LC215'><span class="sd">        weight, but you can make the residue at the center of the window  have a</span></div><div class='line' id='LC216'><span class="sd">        larger weight than the others by setting the edge value for the  residues at</span></div><div class='line' id='LC217'><span class="sd">        the beginning and end of the interval to a value between 0 and 1. For</span></div><div class='line' id='LC218'><span class="sd">        instance, for Edge=0.4 and a window size of 5 the weights will be: 0.4, 0.7,</span></div><div class='line' id='LC219'><span class="sd">        1.0, 0.7, 0.4.</span></div><div class='line' id='LC220'><br/></div><div class='line' id='LC221'><span class="sd">        The method returns a list of values which can be plotted to</span></div><div class='line' id='LC222'><span class="sd">        view the change along a protein sequence.  Many scales exist. Just add your</span></div><div class='line' id='LC223'><span class="sd">        favorites to the ProtParamData modules.</span></div><div class='line' id='LC224'><br/></div><div class='line' id='LC225'><span class="sd">        Similar to expasy&#39;s ProtScale: http://www.expasy.org/cgi-bin/protscale.pl</span></div><div class='line' id='LC226'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># generate the weights</span></div><div class='line' id='LC228'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#   _weight_list returns only one tail. If the list should be [0.4,0.7,1.0,0.7,0.4]</span></div><div class='line' id='LC229'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#   what you actually get from _weights_list is [0.4,0.7]. The correct calculation is done</span></div><div class='line' id='LC230'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#   in the loop.</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">weights</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_weight_list</span><span class="p">(</span><span class="n">window</span><span class="p">,</span> <span class="n">edge</span><span class="p">)</span></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">scores</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC233'><br/></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># the score in each Window is divided by the sum of weights</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># (* 2 + 1) since the weight list is one sided:</span></div><div class='line' id='LC236'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sum_of_weights</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">weights</span><span class="p">)</span> <span class="o">*</span> <span class="mi">2</span> <span class="o">+</span> <span class="mi">1</span></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">length</span> <span class="o">-</span> <span class="n">window</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">subsequence</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">sequence</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span><span class="o">+</span><span class="n">window</span><span class="p">]</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">score</span> <span class="o">=</span> <span class="mf">0.0</span></div><div class='line' id='LC241'><br/></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">window</span> <span class="o">//</span> <span class="mi">2</span><span class="p">):</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># walk from the outside of the Window towards the middle.</span></div><div class='line' id='LC244'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Iddo: try/except clauses added to avoid raising an exception on a non-standard amino acid</span></div><div class='line' id='LC245'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC246'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">front</span> <span class="o">=</span> <span class="n">param_dict</span><span class="p">[</span><span class="n">subsequence</span><span class="p">[</span><span class="n">j</span><span class="p">]]</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">back</span> <span class="o">=</span> <span class="n">param_dict</span><span class="p">[</span><span class="n">subsequence</span><span class="p">[</span><span class="n">window</span> <span class="o">-</span> <span class="n">j</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]]</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">score</span> <span class="o">+=</span> <span class="n">weights</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="o">*</span> <span class="n">front</span> <span class="o">+</span> <span class="n">weights</span><span class="p">[</span><span class="n">j</span><span class="p">]</span> <span class="o">*</span> <span class="n">back</span></div><div class='line' id='LC249'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;warning: </span><span class="si">%s</span><span class="s"> or </span><span class="si">%s</span><span class="s"> is not a standard amino acid.</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="n">subsequence</span><span class="p">[</span><span class="n">j</span><span class="p">],</span> <span class="n">subsequence</span><span class="p">[</span><span class="n">window</span> <span class="o">-</span> <span class="n">j</span> <span class="o">-</span> <span class="mi">1</span><span class="p">]))</span></div><div class='line' id='LC252'><br/></div><div class='line' id='LC253'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Now add the middle value, which always has a weight of 1.</span></div><div class='line' id='LC254'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">middle</span> <span class="o">=</span> <span class="n">subsequence</span><span class="p">[</span><span class="n">window</span> <span class="o">//</span> <span class="mi">2</span><span class="p">]</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">middle</span> <span class="ow">in</span> <span class="n">param_dict</span><span class="p">:</span></div><div class='line' id='LC256'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">score</span> <span class="o">+=</span> <span class="n">param_dict</span><span class="p">[</span><span class="n">middle</span><span class="p">]</span></div><div class='line' id='LC257'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC258'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&#39;warning: </span><span class="si">%s</span><span class="s">  is not a standard amino acid.</span><span class="se">\n</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">middle</span><span class="p">))</span></div><div class='line' id='LC259'><br/></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">scores</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">score</span> <span class="o">/</span> <span class="n">sum_of_weights</span><span class="p">)</span></div><div class='line' id='LC261'><br/></div><div class='line' id='LC262'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">scores</span></div><div class='line' id='LC263'><br/></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">isoelectric_point</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Calculate the isoelectric point.</span></div><div class='line' id='LC266'><br/></div><div class='line' id='LC267'><span class="sd">        Uses the module IsoelectricPoint to calculate the pI of a protein.</span></div><div class='line' id='LC268'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC269'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aa_content</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">count_amino_acids</span><span class="p">()</span></div><div class='line' id='LC270'><br/></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ie_point</span> <span class="o">=</span> <span class="n">IsoelectricPoint</span><span class="o">.</span><span class="n">IsoelectricPoint</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">sequence</span><span class="p">,</span> <span class="n">aa_content</span><span class="p">)</span></div><div class='line' id='LC272'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">ie_point</span><span class="o">.</span><span class="n">pi</span><span class="p">()</span></div><div class='line' id='LC273'><br/></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">secondary_structure_fraction</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC275'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;Calculate fraction of helix, turn and sheet.</span></div><div class='line' id='LC276'><br/></div><div class='line' id='LC277'><span class="sd">        Returns a list of the fraction of amino acids which tend</span></div><div class='line' id='LC278'><span class="sd">        to be in Helix, Turn or Sheet.</span></div><div class='line' id='LC279'><br/></div><div class='line' id='LC280'><span class="sd">        Amino acids in helix: V, I, Y, F, W, L.</span></div><div class='line' id='LC281'><span class="sd">        Amino acids in Turn: N, P, G, S.</span></div><div class='line' id='LC282'><span class="sd">        Amino acids in sheet: E, M, A, L.</span></div><div class='line' id='LC283'><br/></div><div class='line' id='LC284'><span class="sd">        Returns a tuple of three integers (Helix, Turn, Sheet).</span></div><div class='line' id='LC285'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC286'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">aa_percentages</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">get_amino_acids_percent</span><span class="p">()</span></div><div class='line' id='LC287'><br/></div><div class='line' id='LC288'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">helix</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">([</span><span class="n">aa_percentages</span><span class="p">[</span><span class="n">r</span><span class="p">]</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="s">&#39;VIYFWL&#39;</span><span class="p">])</span></div><div class='line' id='LC289'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">turn</span>  <span class="o">=</span> <span class="nb">sum</span><span class="p">([</span><span class="n">aa_percentages</span><span class="p">[</span><span class="n">r</span><span class="p">]</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="s">&#39;NPGS&#39;</span><span class="p">])</span></div><div class='line' id='LC290'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sheet</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">([</span><span class="n">aa_percentages</span><span class="p">[</span><span class="n">r</span><span class="p">]</span> <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="s">&#39;EMAL&#39;</span><span class="p">])</span></div><div class='line' id='LC291'><br/></div><div class='line' id='LC292'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">helix</span><span class="p">,</span> <span class="n">turn</span><span class="p">,</span> <span class="n">sheet</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>
      </div>

      <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
      <div id="jump-to-line" style="display:none">
        <h2>Jump to Line</h2>
        <form accept-charset="UTF-8" class="js-jump-to-line-form">
          <input class="textfield js-jump-to-line-field" type="text">
          <div class="full-button">
            <button type="submit" class="classy">
              Go
            </button>
          </div>
        </form>
      </div>

    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1347543532" height="64" width="64">
</div>


        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2012 <span title="0.05514s from fe15.rs.github.com">GitHub</span> Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    

<div id="keyboard_shortcuts_pane" class="instapaper_ignore readability-extra" style="display:none">
  <h2>Keyboard Shortcuts <small><a href="#" class="js-see-all-keyboard-shortcuts">(see all)</a></small></h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus command bar</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column middle" style='display:none'>
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Expand URL to its canonical form</dd>
      </dl>
    </div><!-- /.column.first -->

    <div class="column last js-hidden-pane" style='display:none'>
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selection down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selection up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
        <dd>Submit comment</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> shift p</dt>
        <dd>Preview comment</dd>
      </dl>
    </div><!-- /.columns.last -->

  </div><!-- /.columns.equacols -->

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Issues</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>x</dt>
          <dd>Toggle selection</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
          <dd>Submit comment</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> shift p</dt>
          <dd>Preview comment</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>c</dt>
          <dd>Create issue</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Create label</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>i</dt>
          <dd>Back to inbox</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>u</dt>
          <dd>Back to issues</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>/</dt>
          <dd>Focus issues search</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Issues Dashboard</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open issue</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>

    <h3>Network Graph</h3>
    <div class="columns equacols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt><span class="badmono">←</span> <em>or</em> h</dt>
          <dd>Scroll left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">→</span> <em>or</em> l</dt>
          <dd>Scroll right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↑</span> <em>or</em> k</dt>
          <dd>Scroll up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt><span class="badmono">↓</span> <em>or</em> j</dt>
          <dd>Scroll down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Toggle visibility of head labels</dd>
        </dl>
      </div><!-- /.column.first -->
      <div class="column last">
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">←</span> <em>or</em> shift h</dt>
          <dd>Scroll all the way left</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">→</span> <em>or</em> shift l</dt>
          <dd>Scroll all the way right</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↑</span> <em>or</em> shift k</dt>
          <dd>Scroll all the way up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift <span class="badmono">↓</span> <em>or</em> shift j</dt>
          <dd>Scroll all the way down</dd>
        </dl>
      </div><!-- /.column.last -->
    </div>
  </div>

  <div class="js-hidden-pane" >
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first js-hidden-pane" >
        <h3>Source Code Browsing</h3>
        <dl class="keyboard-mappings">
          <dt>t</dt>
          <dd>Activates the file finder</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>l</dt>
          <dd>Jump to line</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>w</dt>
          <dd>Switch branch/tag</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>y</dt>
          <dd>Expand URL to its canonical form</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>
    <div class="columns threecols">
      <div class="column first">
        <h3>Browsing Commits</h3>
        <dl class="keyboard-mappings">
          <dt><span class="platform-mac">⌘</span><span class="platform-other">ctrl</span> <em>+</em> enter</dt>
          <dd>Submit comment</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>escape</dt>
          <dd>Close form</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>p</dt>
          <dd>Parent commit</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o</dt>
          <dd>Other parent commit</dd>
        </dl>
      </div>
    </div>
  </div>

  <div class="js-hidden-pane" style='display:none'>
    <div class="rule"></div>
    <h3>Notifications</h3>

    <div class="columns threecols">
      <div class="column first">
        <dl class="keyboard-mappings">
          <dt>j</dt>
          <dd>Move selection down</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>k</dt>
          <dd>Move selection up</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>o <em>or</em> enter</dt>
          <dd>Open notification</dd>
        </dl>
      </div><!-- /.column.first -->

      <div class="column second">
        <dl class="keyboard-mappings">
          <dt>e <em>or</em> shift i <em>or</em> y</dt>
          <dd>Mark as read</dd>
        </dl>
        <dl class="keyboard-mappings">
          <dt>shift m</dt>
          <dd>Mute thread</dd>
        </dl>
      </div><!-- /.column.first -->
    </div>
  </div>

</div>

    <div id="markdown-help" class="instapaper_ignore readability-extra">
  <h2>Markdown Cheat Sheet</h2>

  <div class="cheatsheet-content">

  <div class="mod">
    <div class="col">
      <h3>Format Text</h3>
      <p>Headers</p>
      <pre>
# This is an &lt;h1&gt; tag
## This is an &lt;h2&gt; tag
###### This is an &lt;h6&gt; tag</pre>
     <p>Text styles</p>
     <pre>
*This text will be italic*
_This will also be italic_
**This text will be bold**
__This will also be bold__

*You **can** combine them*
</pre>
    </div>
    <div class="col">
      <h3>Lists</h3>
      <p>Unordered</p>
      <pre>
* Item 1
* Item 2
  * Item 2a
  * Item 2b</pre>
     <p>Ordered</p>
     <pre>
1. Item 1
2. Item 2
3. Item 3
   * Item 3a
   * Item 3b</pre>
    </div>
    <div class="col">
      <h3>Miscellaneous</h3>
      <p>Images</p>
      <pre>
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)
</pre>
     <p>Links</p>
     <pre>
http://github.com - automatic!
[GitHub](http://github.com)</pre>
<p>Blockquotes</p>
     <pre>
As Kanye West said:

> We're living the future so
> the present is our past.
</pre>
    </div>
  </div>
  <div class="rule"></div>

  <h3>Code Examples in Markdown</h3>
  <div class="col">
      <p>Syntax highlighting with <a href="http://github.github.com/github-flavored-markdown/" title="GitHub Flavored Markdown" target="_blank">GFM</a></p>
      <pre>
```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```</pre>
    </div>
    <div class="col">
      <p>Or, indent your code 4 spaces</p>
      <pre>
Here is a Python code example
without syntax highlighting:

    def foo:
      if not bar:
        return true</pre>
    </div>
    <div class="col">
      <p>Inline code for comments</p>
      <pre>
I think you should use an
`&lt;addr&gt;` element here instead.</pre>
    </div>
  </div>

  </div>
</div>


    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.05606' data-host='fe15'></span>
    
  </body>
</html>

