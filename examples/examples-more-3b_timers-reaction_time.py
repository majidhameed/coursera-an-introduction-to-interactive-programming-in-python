<!DOCTYPE html>
<!-- saved from url=(0053)http://www.codeskulptor.org/#user7-0oDHX0RMZD2cJZw.py -->
<html xmlns="http://www.w3.org/1999/xhtml"><head data-aij_comm="{&quot;name&quot;:&quot;$$&quot;}"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <title>CodeSkulptor</title>
    <link href="http://www.codeskulptor.org/favicon.ico" rel="shortcut icon">
    <link rel="stylesheet" type="text/css" href="./examples-more-3b_timers-reaction_time_files/codemirror.css">
    <link rel="stylesheet" type="text/css" href="./examples-more-3b_timers-reaction_time_files/jquery-ui-1.8.21.custom.css">
    <link rel="stylesheet" type="text/css" href="./examples-more-3b_timers-reaction_time_files/codeskulptor.css">
    <script type="text/javascript" async="" src="./examples-more-3b_timers-reaction_time_files/ga.js"></script><script type="text/javascript" src="./examples-more-3b_timers-reaction_time_files/skulpt.js"></script>
    <script type="text/javascript" src="./examples-more-3b_timers-reaction_time_files/builtin.js"></script>
    <script type="text/javascript" src="./examples-more-3b_timers-reaction_time_files/codemirror-compressed.js"></script>
    <script type="text/javascript" src="./examples-more-3b_timers-reaction_time_files/jquery.min.js"></script>
    <script type="text/javascript" src="./examples-more-3b_timers-reaction_time_files/jquery-ui.min.js"></script>
    <!-- <script type="text/javascript" src="js/jquery-1.7.2.min.js"></script> -->
    <!-- <script type="text/javascript" src="js/jquery-ui-1.8.21.custom.min.js"></script> -->
    <script type="text/javascript" src="./examples-more-3b_timers-reaction_time_files/codeskulptor-compressed.js"></script>

<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-33662649-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();
</script>
  <script src="chrome-extension://neappnndmnboecdfhflpbmfdhkanpaoa/lib/inject.js"></script><script src="./examples-more-3b_timers-reaction_time_files/jquery.min(1).js"></script><style>.lookupZCLHSS, .lookupforemostZCLHSS, .lookupdockedZCLHSS, .rowiframeZCLHSS, .celliframeZCLHSS, .iframeZCLHSS, .emptyZCLHSS, .barZCLHSS, .barforemostZCLHSS, .bardockedZCLHSS, .cellZCLHSS, .leftZCLHSS, .rightZCLHSS, .buttoncontainerZCLHSS, .buttonZCLHSS, .buttonimageZCLHSS, .waitingZCLHSS, .handleZCLHSS, .queryZCLHSS, .hintZCLHSS, .templateZCLHSS, .firstlevelgroupZCLHSS, .notfirstlevelgroupZCLHSS{
	    background: none !important;
	    border: 0px !important;
	    border-style: none !important;
	     color: black !important;
	     direction: ltr !important;
	     float: none !important;
	     font-family: sans-serif !important;
	     font-size: small !important;
	     font-style: normal !important;
	     font-variant: normal !important;
	     font-weight: normal !important;
	     letter-spacing: normal !important;
	     line-height: normal !important;
	     margin: 0px !important;
	    padding: 0px !important;
	    text-align: left !important;
	     text-decoration: none !important;
	     text-indent: 0px !important;
	     text-transform: none !important;
	     vertical-align: baseline !important;
	    white-space: normal !important;
}

div.lookupZCLHSS{
	     display: table !important;
	     -webkit-transition: -webkit-box-shadow 0.25s linear, border-color 0.25s linear !important;
}

div.lookupforemostZCLHSS{
}

div.lookupdockedZCLHSS{
}

div.rowiframeZCLHSS{
	     display: table-row !important;
}

div.rowiframeZCLHSS td.celliframeZCLHSS{
	      display: table-cell !important;
	      width: 100% !important;
	      height: 100% !important;
}

td.celliframeZCLHSS iframe.iframeZCLHSS{
	       display: inline !important;
	       width: 100% !important;
	       height: 100% !important;
	       background-color: white !important;
}

iframe.emptyZCLHSS{
	       background-image: url('chrome-extension://hljnlfolmbmibdjaikiaepgepgnldclj/img/128.png') !important;
	       background-position: 50% 50% !important;
	       background-repeat: no-repeat !important;
}

div.barZCLHSS{
	     display: table-row !important;
	     -webkit-transition: background 0.25s linear !important;
	     width: 100% !important;
	     cursor: move !important;
	     background: lightgrey !important;
}

div.barforemostZCLHSS{
	background: #84b7ea !important;
}

div.bardockedZCLHSS{
	background: #336699 !important;
}

div.barZCLHSS div.cellZCLHSS{
	     display: table-cell !important;
	     vertical-align: middle !important;
}

div.leftZCLHSS{
	     padding-right: 16px !important;
	     text-align: left !important;
}

div.rightZCLHSS{
	     white-space: nowrap !important;
	     text-align: right !important;
}

span.buttoncontainerZCLHSS{
	     display:inline !important;
}

a.buttonZCLHSS:link{
	     display:inline !important;
	     -webkit-user-select: none !important;
	     color: transparent !important;
}

a.buttonZCLHSS img.buttonimageZCLHSS{
	     display:inline !important;
	     vertical-align: middle !important;
}

img.waitingZCLHSS{
	     display:inline !important;
	     cursor: pointer !important;
	     -webkit-user-select: none !important;
	     vertical-align: middle !important;
	     padding-left: 6px !important;
	 padding-right: 6px !important;
}

div.handleZCLHSS{
	     display:block !important;
	     cursor: se-resize !important;
	     left: 100% !important;
	     top: 100% !important;
	     margin-left: -4px !important;
	     margin-top: -4px !important;
	     position: absolute !important;
	     width: 8px !important;
	 height: 8px !important;
}

input.queryZCLHSS{
	     display:inline-block !important;
	     background: white !important;
	     vertical-align: top !important;
	     border: 1px solid darkgrey !important;
	      font-size: 13px !important;
	      padding-top: 1px !important;
	 padding-bottom: 1px !important;
	     width: 12em !important;
}

.hintZCLHSS{
	      color: lightgrey !important;
	      font-style:italic !important;
}

select.templateZCLHSS{
	     display:inline-block !important;
	     background: white !important;
	     font-size: 13px !important;
	      border: 1px solid darkgrey !important;
	      vertical-align: top !important;
	     white-space: pre !important;
	     width: 9em !important;
	     margin-right: 2px !important;
}

optgroup.firstlevelgroupZCLHSS{
	      color: blue !important;
}

.notfirstlevelgroupZCLHSS{
	      color: black !important;
}

</style><style>.tipCTXWWP, .arrowCTXWWP, .arrowupCTXWWP, .arrowdownCTXWWP, .mainCTXWWP, .closeCTXWWP, .barCTXWWP, .rowCTXWWP, .cellCTXWWP, .leftCTXWWP, .rightCTXWWP, .displaytitleCTXWWP, .refreshCTXWWP, .pagingCTXWWP, .brandCTXWWP, .textCTXWWP, .leftlabelCTXWWP, .selectCTXWWP, .checkboxCTXWWP, .waitingCTXWWP, .buttoncontainerCTXWWP, .buttonCTXWWP, .buttonimageCTXWWP, .flagCTXWWP, .noticebarscontainerCTXWWP, .noticebarCTXWWP, .iframecontentCTXWWP{
	    background: none !important;
	    border: 0px !important;
	    border-style: none !important;
	     color: black !important;
	     direction: ltr !important;
	     float: none !important;
	     font-family: sans-serif !important;
	     font-size: small !important;
	     font-style: normal !important;
	     font-variant: normal !important;
	     font-weight: normal !important;
	     letter-spacing: normal !important;
	     line-height: normal !important;
	     margin: 0px !important;
	    padding: 0px !important;
	    text-align: left !important;
	     text-decoration: none !important;
	     text-indent: 0px !important;
	     text-transform: none !important;
	     vertical-align: baseline !important;
	    white-space: normal !important;
}

div.tipCTXWWP{
	     position: absolute !important;
	     display:block !important;
}

div.arrowCTXWWP{
	display:block !important;
}

canvas.arrowupCTXWWP{
	      display: inline !important;
	      vertical-align: bottom !important;
}

canvas.downupCTXWWP{
	      display: inline !important;
	      vertical-align: top !important;
}

div.mainCTXWWP{
	display: block !important;
}

img.closeCTXWWP{
	      display: block !important;
	      -webkit-transition: opacity 0.5s linear !important;
	      float: right !important;
	      margin-right: -5px !important;
	      margin-top: -5px !important;
}

div.barCTXWWP{
	     display: table !important;
	      margin-bottom: 4px !important;
	     -webkit-user-select: none !important;
	     width: 100% !important;
}

div.rowCTXWWP{
	display: table-row !important;
}

div.cellCTXWWP{
	      display: table-cell !important;
	      vertical-align: middle !important;
}

.leftCTXWWP{
	      padding-right: 16px !important;
	      text-align: left !important;
}

.rightCTXWWP{
	text-align: right !important;
}

span.refreshCTXWWP{
	display: inline !important;
}

span.pagingCTXWWP{
	      display: inline !important;
	      font-size: x-small !important;
}

span.buttoncontainerCTXWWP{
	display: inline !important;
}

span.displaytitleCTXWWP{
	      display: inline !important;
	      padding-left: 6px !important;
	      font-size: small !important;
	      font-weight: bold !important;
}

span.displaytitleCTXWWP a:link{
	       display: inline !important;
	       color: #0645AD !important;
	       text-decoration: none !important;
}

span.displaytitleCTXWWP img{
	display: inline !important;
}

span.brandCTXWWP{
	      display: inline !important;
	      font-size: x-small !important;
}

.brandCTXWWP a{
	       display: inline !important;
	       font-size: x-small !important;
}

.brandCTXWWP a:link{
	       display: inline !important;
	       color: #0645AD !important;
	       text-decoration: none !important;
}

.brandCTXWWP a:visited{
	       display: inline !important;
	       color: #0B0080 !important;
	       text-decoration: none !important;
}

span.textCTXWWP{
	      display: inline !important;
	      font-size: x-small !important;
}

label.leftlabelCTXWWP{
	      display: inline !important;
	      font-size: x-small !important;
	      margin-right: 3px !important;
}

select.selectCTXWWP{
	       display: inline-block !important;
	       border: 1px solid darkgrey !important;
	       white-space: pre !important;
	       font-size: x-small !important;
}

input.checkboxCTXWWP{
	      display: inline-block !important;
	      vertical-align: text-top !important;
	      font-size: x-small !important;
	      margin-right: 0.3em !important;
}

img.waitingCTXWWP{
	      display: inline !important;
	      -webkit-user-select: none !important;
	      vertical-align: middle !important;
	      padding-left: 3px !important;
}

a.buttonCTXWWP, a.buttonCTXWWP:link{
	      display: inline !important;
	      -webkit-user-select: none !important;
	      color: transparent !important;
	      margin-right: 2px !important;
}

img.buttonimageCTXWWP{
	      display: inline !important;
	      vertical-align: middle !important;
}

img.flagCTXWWP{
	      display: inline !important;
	      vertical-align: middle !important;
	      padding-bottom:2px !important;
}

img.buttonselectedCTXWWP{
	      display: inline !important;
	      background: #dd8 !important;
	      border: 1px solid #bb6 !important;
	      margin: -1px !important;
	      border-radius: 2px !important;
}

div.noticebarscontainerCTXWWP{
	     display: block !important;
	     text-align: left !important;
	     margin-bottom: 4px !important;
	     overflow-y: auto !important;
}

div.noticebarCTXWWP{
	     display: block !important;
	     background: white !important;
	     font-size: x-small !important;
	     border-left: 3px solid lightGrey !important;
	     margin-bottom: 1px !important;
	     padding-left: 2px !important;
}

div.noticebarCTXWWP img{
	      display: inline !important;
	      margin-right: 1px !important;
	      vertical-align: text-top !important;
}

div.noticebarCTXWWP a{
	      display: inline !important;
	      font-family: sans-serif !important;
	       font-style: normal !important;
	       font-variant: normal !important;
	       font-weight: normal !important;
	       font-size: x-small !important;
}

div.noticebarCTXWWP a:link{
	      display: inline !important;
	      color: #0645AD !important;
	      text-decoration: none !important;
}

div.noticebarCTXWWP a:visited{
	      display: inline !important;
	      color: #0B0080 !important;
	      text-decoration: none !important;
}

iframe.iframecontentCTXWWP{
	     display: inline !important;
	     width: 100% !important;
}

</style><style id="simplehl_hlstyle_DJGVSU">.simplehl1_NEIGFC { display: inline!important;font-family:inherit!important; font-style:inherit!important; font-variant:inherit!important; font-weight:inherit!important; border-color: transparent !important; color: #000000!important; background-color: rgba(255,0,0,0.7)!important; font-size: inherit!important; -webkit-transition-property: color, background-color, -webkit-box-shadow; -webkit-transition-duration: 0.5s, 0.5s, 0.5s; -webkit-transition-timing-function: linear, linear, linear; padding: 0.2em!important; -webkit-box-shadow: rgba(0,0,0,0.42) 3px 3px 4px!important; border-radius: 6px!important; } .simplehl2_NEIGFC { display: inline!important;font-family:inherit!important; font-style:inherit!important; font-variant:inherit!important; font-weight:inherit!important; border-color: transparent !important; color: #000000!important; background-color: rgba(255,165,0,0.7)!important; font-size: inherit!important; -webkit-transition-property: color, background-color, -webkit-box-shadow; -webkit-transition-duration: 0.5s, 0.5s, 0.5s; -webkit-transition-timing-function: linear, linear, linear; padding: 0.2em!important; -webkit-box-shadow: rgba(0,0,0,0.42) 3px 3px 4px!important; border-radius: 6px!important; } .simplehl3_NEIGFC { display: inline!important;font-family:inherit!important; font-style:inherit!important; font-variant:inherit!important; font-weight:inherit!important; border-color: transparent !important; color: #000000!important; background-color: rgba(255,255,96,0.7)!important; font-size: inherit!important; -webkit-transition-property: color, background-color, -webkit-box-shadow; -webkit-transition-duration: 0.5s, 0.5s, 0.5s; -webkit-transition-timing-function: linear, linear, linear; padding: 0.2em!important; -webkit-box-shadow: rgba(0,0,0,0.42) 3px 3px 4px!important; border-radius: 6px!important; } .simplehl4_NEIGFC { display: inline!important;font-family:inherit!important; font-style:inherit!important; font-variant:inherit!important; font-weight:inherit!important; border-color: transparent !important; color: #000000!important; background-color: rgba(96,255,96,0.7)!important; font-size: inherit!important; -webkit-transition-property: color, background-color, -webkit-box-shadow; -webkit-transition-duration: 0.5s, 0.5s, 0.5s; -webkit-transition-timing-function: linear, linear, linear; padding: 0.2em!important; -webkit-box-shadow: rgba(0,0,0,0.42) 3px 3px 4px!important; border-radius: 6px!important; } .simplehl5_NEIGFC { display: inline!important;font-family:inherit!important; font-style:inherit!important; font-variant:inherit!important; font-weight:inherit!important; border-color: transparent !important; color: #000000!important; background-color: rgba(96,255,255,0.7)!important; font-size: inherit!important; -webkit-transition-property: color, background-color, -webkit-box-shadow; -webkit-transition-duration: 0.5s, 0.5s, 0.5s; -webkit-transition-timing-function: linear, linear, linear; padding: 0.2em!important; -webkit-box-shadow: rgba(0,0,0,0.42) 3px 3px 4px!important; border-radius: 6px!important; } .simplehl6_NEIGFC { display: inline!important;font-family:inherit!important; font-style:inherit!important; font-variant:inherit!important; font-weight:inherit!important; border-color: transparent !important; color: #000000!important; background-color: rgba(255,96,255,0.7)!important; font-size: inherit!important; -webkit-transition-property: color, background-color, -webkit-box-shadow; -webkit-transition-duration: 0.5s, 0.5s, 0.5s; -webkit-transition-timing-function: linear, linear, linear; padding: 0.2em!important; -webkit-box-shadow: rgba(0,0,0,0.42) 3px 3px 4px!important; border-radius: 6px!important; } .simplehl7_NEIGFC { display: inline!important;font-family:inherit!important; font-style:inherit!important; font-variant:inherit!important; font-weight:inherit!important; border-color: transparent !important; color: #FFFFFF!important; background-color: rgba(0,0,0,0.7)!important; font-size: inherit!important; -webkit-transition-property: color, background-color, -webkit-box-shadow; -webkit-transition-duration: 0.5s, 0.5s, 0.5s; -webkit-transition-timing-function: linear, linear, linear; padding: 0.2em!important; -webkit-box-shadow: rgba(0,0,0,0.42) 3px 3px 4px!important; border-radius: 6px!important; } </style><style id="simplehl_flashstyle_TZVMTU">@-webkit-keyframes flash {         0% {             opacity: 1;         }         100% {             opacity: 0;         }}</style></head>

  <body>
    <div id="main">
      <div id="controls" class="topbar">
        <div style="float:left">
          <button type="button" id="run" class="tb-button-icon ui-state-default ui-button ui-widget ui-corner-all ui-button-icon-only" accesskey="R" role="button" aria-disabled="false" title="Run"><span class="ui-button-icon-primary ui-icon ui-icon-play"></span><span class="ui-button-text">Run</span></button>
          <button type="button" id="save" class="tb-button-icon ui-state-default ui-button ui-widget ui-corner-all ui-button-icon-only ui-button-disabled ui-state-disabled" accesskey="S" role="button" aria-disabled="true" title="Save" disabled=""><span class="ui-button-icon-primary ui-icon ui-icon-disk"></span><span class="ui-button-text">Save</span></button>
          <a id="dlhref" href="http://codeskulptor-user7.commondatastorage.googleapis.com/user7-0oDHX0RMZD2cJZw.py"></a>
          <button type="button" id="dl" class="tb-button-icon ui-state-default ui-button ui-widget ui-corner-all ui-button-icon-only" role="button" aria-disabled="false" title="Download"><span class="ui-button-icon-primary ui-icon ui-icon-arrowthickstop-1-s"></span><span class="ui-button-text">Download</span></button>
          <button type="button" id="fresh" class="tb-button-icon ui-state-default ui-button ui-widget ui-corner-all ui-button-icon-only" role="button" aria-disabled="false" title="Fresh URL"><span class="ui-button-icon-primary ui-icon ui-icon-suitcase"></span><span class="ui-button-text">Fresh URL</span></button>
          <button type="button" id="loadlocal" class="tb-button-icon ui-state-default ui-button ui-widget ui-corner-all ui-button-icon-only" role="button" aria-disabled="false" title="Open Local"><span class="ui-button-icon-primary ui-icon ui-icon-folder-open"></span><span class="ui-button-text">Open Local<input type="file" id="localfile"></span></button>
          <button type="button" id="reset" class="tb-button-icon ui-state-default ui-button ui-widget ui-corner-all ui-button-icon-only" accesskey="X" role="button" aria-disabled="false" title="Reset"><span class="ui-button-icon-primary ui-icon ui-icon-arrowreturnthick-1-w"></span><span class="ui-button-text">Reset</span></button>
        </div>
        <img id="brand" src="./examples-more-3b_timers-reaction_time_files/codeskulptor.png" alt="CodeSkulptor" style="left: 535.5px;">
        <div style="float:right">
          <a id="docanchor" href="http://www.codeskulptor.org/docs.html" target="_blank"></a>
          <button type="button" id="docs" class="tb-button-text ui-state-default ui-button ui-widget ui-corner-all ui-button-text-icon-primary" role="button" aria-disabled="false"><span class="ui-button-icon-primary ui-icon ui-icon-info"></span><span class="ui-button-text">Docs</span></button>
          <a id="demoanchor" href="http://www.codeskulptor.org/demos.html" target="_blank"></a>
          <button type="button" id="demos" class="tb-button-text ui-state-default ui-button ui-widget ui-corner-all ui-button-text-icon-primary" role="button" aria-disabled="false"><span class="ui-button-icon-primary ui-icon ui-icon-script"></span><span class="ui-button-text">Demos</span></button>
          <a id="tipanchor" href="https://class.coursera.org/interactivepython-2012-001/forum/thread?thread_id=4764" target="_blank"></a>
          <button type="button" id="tips" class="tb-button-text ui-state-default ui-button ui-widget ui-corner-all ui-button-text-icon-primary" role="button" aria-disabled="false"><span class="ui-button-icon-primary ui-icon ui-icon-lightbulb"></span><span class="ui-button-text">Coursera Tips</span></button>
        </div>
      </div>
      <div id="active">
        <div id="eddiv">
          <form action="http://codeskulptor-user7.commondatastorage.googleapis.com/" method="post" enctype="multipart/form-data" id="codeform">
            <input type="hidden" name="key" id="keyid" value="user7-0oDHX0RMZD2cJZw.py">
            <input type="hidden" name="Content-Type" value="text/x-python">
            <input type="hidden" name="GoogleAccessId" id="googleid" value="GOOGOC4O3IBWEZMQYHRU">
            <input type="hidden" name="Policy" id="policy" value="eyJleHBpcmF0aW9uIjogIjIwMTMtMDEtMDFUMTI6MDA6MDAuMDAwWiIsCgogICJjb25kaXRpb25zIjogWwogICAgeyJidWNrZXQiOiAiY29kZXNrdWxwdG9yLXVzZXI3In0sCiAgICBbInN0YXJ0cy13aXRoIiwgIiRrZXkiLCAidXNlcjciXSwKICAgIFsiZXEiLCAiJENvbnRlbnQtVHlwZSIsICJ0ZXh0L3gtcHl0aG9uIl0sCiAgICBbImNvbnRlbnQtbGVuZ3RoLXJhbmdlIiwgMCwgNjU1MzZdCiAgXQp9Cg==">
            <input type="hidden" name="Signature" id="signature" value="9X11uqAtlx4X050KJrANEeeFGg4=">
            <textarea id="code" name="file" style="display: none;"></textarea><div class="CodeMirror"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 132px; left: 190px;"><textarea style="position: absolute; padding: 0; width: 1px; height: 1em" wrap="off" autocorrect="off" autocapitalize="off"></textarea></div><div class="CodeMirror-scrollbar" style="display: block; height: 504px;"><div class="CodeMirror-scrollbar-inner" style="height: 1434px;"></div></div><div class="CodeMirror-scroll cm-s-default" tabindex="-1" style="height: 521px;"><div style="position: relative; min-height: 1434px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-gutter" style="height: 1434px;"><div class="CodeMirror-gutter-text"><pre>1</pre><pre>2</pre><pre>3</pre><pre>4</pre><pre>5</pre><pre>6</pre><pre>7</pre><pre>8</pre><pre>9</pre><pre>10</pre><pre>11</pre><pre>12</pre><pre>13</pre><pre>14</pre><pre>15</pre><pre>16</pre><pre>17</pre><pre>18</pre><pre>19</pre><pre>20</pre><pre>21</pre><pre>22</pre><pre>23</pre><pre>24</pre><pre>25</pre><pre>26</pre><pre>27</pre><pre>28</pre><pre>29</pre><pre>30</pre><pre>31</pre><pre>32</pre><pre>33</pre><pre>34</pre><pre>35</pre><pre>36</pre><pre>37</pre><pre>38</pre><pre>39</pre><pre>40</pre><pre>41</pre><pre>42</pre><pre>43</pre><pre>44</pre><pre>45</pre><pre>46</pre><pre>47</pre><pre>48</pre><pre>49</pre><pre>50</pre><pre>51</pre><pre>52</pre><pre>53</pre><pre>54</pre><pre>55</pre><pre>56</pre><pre>57</pre><pre>58</pre><pre>59</pre><pre>60</pre><pre>61</pre><pre>62</pre><pre>63</pre><pre>64</pre><pre>65</pre><pre>66</pre><pre>67</pre><pre>68</pre><pre>69</pre><pre>70</pre><pre>71</pre><pre>72</pre><pre>73</pre><pre>74</pre><pre>75</pre><pre>76</pre><pre>77</pre><pre>78</pre><pre>79</pre></div></div><div class="CodeMirror-lines"><div style="position: relative; z-index: 0; outline: none; min-width: 775px; margin-left: 40px;"><div style="position: absolute; width: 100%; height: 0px; overflow: hidden; visibility: hidden;"><pre><span class="cm-keyword">import</span> <span class="cm-variable">simplegui</span><span id="CodeMirror-temp-ba0d23"> </span></pre></div><pre class="CodeMirror-cursor" style="top: 126px; left: 144px; visibility: hidden;">&nbsp;</pre><pre class="CodeMirror-cursor" style="visibility: hidden; left: 774px;">&nbsp;</pre><div style="position: relative; z-index: -1; display: none;"></div><div style=""><pre><span class="cm-comment"># Timers</span></pre><pre><span class="cm-comment"># Reaction Time</span></pre><pre> </pre><pre> </pre><pre><span class="cm-comment"># This program tests your reaction in milliseconds using a</span></pre><pre><span class="cm-comment">#<span class="cm-tab">   </span>timer. Notice the uses of start() and stop() methods.</span></pre><pre> </pre><pre><span class="cm-keyword">import</span> <span class="cm-variable">simplegui</span></pre><pre><span class="cm-keyword">import</span> <span class="cm-variable">random</span></pre><pre> </pre><pre><span class="cm-comment"># Global Variables</span></pre><pre> </pre><pre><span class="cm-variable">canvas_width</span> = <span class="cm-number">200</span></pre><pre><span class="cm-variable">canvas_height</span> = <span class="cm-number">200</span></pre><pre><span class="cm-variable">reaction_time</span> = <span class="cm-number">0</span></pre><pre><span class="cm-comment"># Used to see if the circle should be drawn</span></pre><pre><span class="cm-variable">started</span> = <span class="cm-builtin">False</span></pre><pre><span class="cm-variable">count</span> = <span class="cm-number">0</span></pre><pre> </pre><pre><span class="cm-comment"># Event Handlers</span></pre><pre> </pre><pre><span class="cm-keyword">def</span> <span class="cm-variable">check_start</span>():</pre><pre>    <span class="cm-keyword">global</span> <span class="cm-variable">started</span>, <span class="cm-variable">count</span></pre><pre>    <span class="cm-variable">count</span> += <span class="cm-number">1</span></pre><pre>    <span class="cm-comment"># This makes sure that the circle won't be drawn for at</span></pre><pre>    <span class="cm-comment">#<span class="cm-tab">   </span>least one second after starting the frame or clicking</span></pre><pre>    <span class="cm-comment">#<span class="cm-tab">   </span>the restart button.</span></pre><pre>    <span class="cm-keyword">if</span> <span class="cm-variable">count</span> <span class="cm-operator">&gt;</span> <span class="cm-number">10</span>:</pre><pre>        <span class="cm-comment"># This increases the likelihood of starting and ensures</span></pre><pre>        <span class="cm-comment">#<span class="cm-tab">   </span>that the game will start within a time limit.</span></pre><pre>        <span class="cm-keyword">if</span> <span class="cm-variable">count</span> <span class="cm-operator">/</span> <span class="cm-number">500</span> <span class="cm-operator">&gt;</span> <span class="cm-variable">random</span>.<span class="cm-variable">random</span>():</pre><pre>            <span class="cm-variable">started</span> = <span class="cm-builtin">True</span></pre><pre>            <span class="cm-variable">reaction_timer</span>.<span class="cm-variable">start</span>()</pre><pre>            <span class="cm-variable">circle_timer</span>.<span class="cm-variable">stop</span>()</pre><pre> </pre><pre><span class="cm-keyword">def</span> <span class="cm-variable">increment</span>():</pre><pre>    <span class="cm-keyword">global</span> <span class="cm-variable">reaction_time</span></pre><pre>    <span class="cm-variable">reaction_time</span> += <span class="cm-number">1</span></pre><pre>    </pre><pre><span class="cm-keyword">def</span> <span class="cm-variable">stop_button</span>():</pre><pre>    <span class="cm-keyword">if</span> <span class="cm-variable">started</span>:</pre><pre>        <span class="cm-variable">reaction_timer</span>.<span class="cm-variable">stop</span>()</pre><pre>        <span class="cm-keyword">print</span> <span class="cm-string">"Your reaction time was"</span>, <span class="cm-variable">reaction_time</span>, <span class="cm-string">"milliseconds"</span></pre><pre>        </pre><pre><span class="cm-keyword">def</span> <span class="cm-variable">draw</span>(<span class="cm-variable">canvas</span>):</pre><pre>    <span class="cm-keyword">if</span> <span class="cm-variable">started</span>:</pre><pre>        <span class="cm-variable">canvas</span>.<span class="cm-variable">draw_circle</span>([<span class="cm-variable">canvas_width</span> <span class="cm-operator">/</span> <span class="cm-number">2</span>, <span class="cm-variable">canvas_height</span> <span class="cm-operator">/</span> <span class="cm-number">2</span>], <span class="cm-number">60</span>, <span class="cm-number">2</span>, <span class="cm-string">"Red"</span>, <span class="cm-string">"Red"</span>)</pre><pre>        </pre><pre><span class="cm-keyword">def</span> <span class="cm-variable">restart</span>():</pre><pre>    <span class="cm-keyword">global</span> <span class="cm-variable">started</span>, <span class="cm-variable">count</span>, <span class="cm-variable">reaction_time</span></pre><pre>    <span class="cm-variable">started</span> = <span class="cm-builtin">False</span></pre><pre>    <span class="cm-variable">count</span> = <span class="cm-number">0</span></pre><pre>    <span class="cm-variable">reaction_time</span> = <span class="cm-number">0</span></pre><pre>    <span class="cm-variable">circle_timer</span>.<span class="cm-variable">start</span>()</pre><pre>    </pre><pre> </pre><pre><span class="cm-comment"># Frame</span></pre><pre> </pre><pre><span class="cm-variable">frame</span> = <span class="cm-variable">simplegui</span>.<span class="cm-variable">create_frame</span>(<span class="cm-string">"Reaction Time"</span>, <span class="cm-variable">canvas_width</span>, <span class="cm-variable">canvas_height</span>) </pre><pre> </pre><pre><span class="cm-comment"># Register Event Handlers</span></pre><pre> </pre><pre><span class="cm-variable">frame</span>.<span class="cm-variable">set_draw_handler</span>(<span class="cm-variable">draw</span>)</pre><pre> </pre><pre><span class="cm-comment"># By the way, these are labels. You can check the docs for</span></pre><pre><span class="cm-comment">#<span class="cm-tab">   </span>more info.</span></pre><pre><span class="cm-variable">label</span> = <span class="cm-variable">frame</span>.<span class="cm-variable">add_label</span>(<span class="cm-string">"Get ready..."</span>)</pre><pre><span class="cm-variable">frame</span>.<span class="cm-variable">add_label</span>(<span class="cm-string">"Press 'stop' when the red circle appears."</span>)</pre><pre>                        </pre><pre><span class="cm-variable">frame</span>.<span class="cm-variable">add_button</span>(<span class="cm-string">"Stop"</span>, <span class="cm-variable">stop_button</span>, <span class="cm-number">75</span>)</pre><pre><span class="cm-variable">frame</span>.<span class="cm-variable">add_button</span>(<span class="cm-string">"Restart"</span>, <span class="cm-variable">restart</span>, <span class="cm-number">75</span>)</pre><pre> </pre><pre><span class="cm-comment"># Note that the timers do not have the same name or purpose</span></pre><pre><span class="cm-variable">circle_timer</span> = <span class="cm-variable">simplegui</span>.<span class="cm-variable">create_timer</span>(<span class="cm-number">100</span>, <span class="cm-variable">check_start</span>)</pre><pre><span class="cm-variable">reaction_timer</span> = <span class="cm-variable">simplegui</span>.<span class="cm-variable">create_timer</span>(<span class="cm-number">1</span>, <span class="cm-variable">increment</span>)</pre><pre> </pre><pre><span class="cm-comment"># Start Frame and circle_timer</span></pre><pre><span class="cm-variable">frame</span>.<span class="cm-variable">start</span>()</pre><pre><span class="cm-variable">circle_timer</span>.<span class="cm-variable">start</span>()</pre></div></div></div></div></div></div></div>
          </form>
        </div>
        <div id="splitbar" style="height: 521px;">
          <div id="grip" style="top: 250.5px;">
          <img src="./examples-more-3b_timers-reaction_time_files/ui-icons_00246a_256x240.png">
          </div>
        </div>
        <div id="console" style="height: 521px;"></div>
      </div>
      <div id="bottom">
        CodeSkulptor was built by <a href="http://www.cs.rice.edu/~rixner/">
        Scott Rixner</a> and is based
        upon <a href="http://codemirror.net/">CodeMirror</a> and
        <a href="http://skulpt.org/">Skulpt</a>.
      </div>
    </div>
  

</body></html>