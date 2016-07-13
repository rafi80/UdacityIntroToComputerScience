'''
Created on 15 wrz 2013

@author: Stefan
'''

import urllib2
page1 =' <a href="/privacy/cookies/managing/cookie-settings.html">change your cookie settings</a> at any time. </p> <ul> <li id="bbccookies-continue"> <button type="button" id="bbccookies-continue-button">Continue</button> </li> <li id="bbccookies-more"><a href="/privacy/cookies/bbc">Find out more</a></li></ul> </div> ]]></script> <script type="text/javascript">/*<![CDATA[*/ (function(){if(bbccookies._showPrompt()){var i=document,b=i.getElementById("blq-pre-mast"),f=i.getElementById("blq-global"),h=i.getElementById("blq-container"),c=i.getElementById("blq-bbccookies-tmpl"),a,g,e;if(b&&i.createElement){a=i.createElement("div");a.id="bbccookies";e=c.innerHTML;e=e.replace("<"+"![CDATA[","").replace("]]"+">","");a.innerHTML=e;if(f){f.insertBefore(a,b)}else{h.insertBefore(a,b)}g=i.getElementById("bbccookies-continue-button");g.onclick=function(){a.parentNode.removeChild(a);return false};bbccookies._setPolicy()}}})(); /*]]>*/</script>  <div id="blq-masthead" class="blq-clearfix blq-mast-bg-white blq-masthead-focus blq-lang-en-GB blq-ltr"> <span id="blq-mast-background"><span></span></span>  <div id="blq-mast" class="blq-rst">  <div id="blq-mast-bar" class="blq-masthead-container blq-default-worldwide"> <div id="blq-blocks"> <a href="/" hreflang="en-GB"> <abbr title="British Broadcasting Corporation" class="blq-home"> <img src="http://static.bbci.co.uk/frameworks/barlesque/2.51.4/desktop/3.5/img/blq-blocks_grey_alpha.png" alt="BBC" width="84" height="24" /> </abbr> </a> </div> <div id="blq-acc-links"> <h2 id="page-top">Accessibility links</h2> <ul>  <li><a href="#blq-content">Skip to content</a></li>  <li><a href="#blq-local-nav">Skip to local navigation</a></li>  <li><a href="/accessibility/">Accessibility Help</a></li> </ul> </div> <div id="blq-sign-in" class="blq-gel">  </div> <div id="blq-nav"> <h2>bbc.co.uk navigation</h2>     <ul id="blq-nav-main">   <li id="blq-nav-news"> <a href="http://www.bbc.com/news/">News</a> </li>    <li id="blq-nav-sport"> <a href="http://www.bbc.co.uk/sport/">Sport</a> </li>    <li id="blq-nav-weather"> <a href="http://www.bbc.co.uk/weather/">Weather</a> </li>    <li id="blq-nav-capital"> <a href="http://www.bbc.com/capital/">Capital</a> </li>    <li id="blq-nav-culture"> <a href="http://www.bbc.com/culture/">Culture</a> </li>    <li id="blq-nav-autos"> <a href="http://www.bbc.com/autos/">Autos</a> </li>    <li id="blq-nav-tv"> <a href="/tv/">TV</a> </li>    <li id="blq-nav-radio"> <a href="/radio/">Radio</a> </li>    <li id="blq-nav-more"> <a href="/a-z/">More&hellip;</a>'
#page1 = 'Jump to:                    <a href="#mw-navigation">navigation</a>,'
#page1 = 'dsada "dupa.1"'


def get_page(url):
    return urllib2.urlopen(url).read()

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None,0
    else:
        start_quote=page.find('"',start_link)
        end_quote= page.find('"',start_quote+1)
        url = page[start_quote+1:end_quote]
        return url, end_quote

def print_all_links(page):
    while True :
        url, endpos = get_next_target(page) 
        if url:
            print url
            page = page[endpos:]
            get_next_target(page)
        else:
            break
          
print_all_links(get_page("http://xkcd.com/353") )
print_all_links(page1)