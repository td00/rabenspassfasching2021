<?php
if(isset($_GET['bild'])) {  

    ?>
    <!DOCTYPE html>
<!--[if lte IE 8]> <html class="oldie" lang="en"> <![endif]-->
<!--[if IE 9]> <html class="ie9" lang="en"> <![endif]-->
<!--[if gt IE 9]><!--> <html lang="en"> <!--<![endif]-->
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="format-detection" content="telephone=no">
	<title>Grossbildansicht<?php ?></title>
	<link href='css/fonts.css' rel='stylesheet' type='text/css'>
	<link href="css/jquery.bxslider.css" rel="stylesheet" />
	<link href="css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
	<link rel="stylesheet" href="css/style.css" />
	<!--[if lt IE 9]>
		<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->
	
</head>
<body>
	<div id="wrapper" class="gallery">
		<div class="wrapper-holder">
			<header id="header">
				<div class="left-part"></div>
				<a id="logo" href="index.html">Faschingswettbewerb</a>
			</header>
			<div class="dvdr"></div>
			<div class="container">
				<section id="main">
                    <?php
                    if(isset($_GET['vorname'])) {
                    ?>
                    <h1>Bild von <?php echo $_GET['vorname'];?>:</h1>
					<?php
                    } else {
                        ?>
                        <h1>Bild:</h1>
                        <?php  
                    }
                    ?>
                    <button type="button" class="btn btn-secondary" onclick="goBack()">Zur&uuml;ck</button>
                    <br />
                    <?php
                    echo '<img src="zeichnungen/'.$_GET['bild'].'" alt="'.$_GET['alt'].'" />';
                    ?>
					<br />
					<button type="button" class="btn btn-secondary" onclick="goBack()">Zur&uuml;ck</button>


<script>
function goBack() {
  window.history.back();
}
</script>
				</section>
					<div class="footer-bottom">
						<div class="holder">
							<p>Copyright 2014 Kid’ school. All rights reserved.</p>
						</div>
					</div>
				</div>
			</div>
		</footer>	
	</div>

	<script type="text/javascript" src="js/jquery-3.5.1.js"></script>
	<script type="text/javascript" src="js/jquery.bxslider.min.js"></script>
	<script type="text/javascript" src="js/jquery.placeholder.js"></script>
	<script type="text/javascript" src="js/imagesloaded.pkgd.min.js"></script>
	<script type="text/javascript" src="js/isotope.pkgd.min.js"></script>
	<script type="text/javascript" src="js/main.js"></script>
</body>
</html>
    <?php
} else { 
    die('hello'); 
}
//<meta http-equiv="refresh" content="0; URL=gallerie.html"'
?>
