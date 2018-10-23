<!DOCTYPE html>
<html lang="en">

  <head>

  <!-- 	<script type="text/javascript">
  		
/*do {
    var img1 = document.getElementById("nm1");
    img1.src = "../images/1"
}
while (0);  
*/
  	</script> -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Portfolio Item - Start Bootstrap Template</title>

    <!-- Bootstrap core CSS -->
    <link href="static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="static/css/portfolio-item.css" rel="stylesheet">
     <!--  <script type="text/javascript">
        function loadDoc() {
          document.getElementById("demo").innerHTML = "Reading";
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    document.getElementById("demo").innerHTML = "Inside";
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "file:///C:/Users/Mayank/Documents/w4/w2/crowd-counting-MCNN-master/templates/val.txt", true);
  xhttp.send();
  document.getElementById("demo").innerHTML = "Read";
}
      </script> -->
      
  </head>

  <body>
      
    </div> 
  	 <img id = "nm1" src="1.jpg" alt="">
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container">
        <a class="navbar-brand" href="#" id ="headoof">Start Bootstrap</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item active">
              <a class="nav-link" href="#">Home
                <span class="sr-only">(current)</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Services</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Page Content -->
    <div class="container">

      <!-- Portfolio Item Heading -->
      <h1 class="my-4">Page Heading
        <small>Secondary Text</small>
      </h1>

      <!-- Portfolio Item Row -->
      <div class="row">

        <div class="col-md-8">
          <img id="bg" src="{{ url_for('video_feed') }}" alt="gandmara">
        </div>

        <div class="col-md-4">
          <h3 class="my-3"><?php
          $myfile = fopen("val1.txt", "r") or die("Unable to open file!");
          echo fread($myfile,filesize("val1.txt"));
          fclose($myfile);
      ?></h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam viverra euismod odio, gravida pellentesque urna varius vitae. Sed dui lorem, adipiscing in adipiscing et, interdum nec metus. Mauris ultricies, justo eu convallis placerat, felis enim.</p>
          <h3 class="my-3">Project Details</h3>
          <ul>
            <li>Lorem Ipsum</li>
            <li>Dolor Sit Amet</li>
            <li>Consectetur</li>
            <li>Adipiscing Elit</li>
          </ul>
        </div>

      </div>
      <!-- /.row -->

      <!-- Related Projects Row -->
      <h3 class="my-4">Related Projects</h3>

      <div class="row">

        <div class="col-md-3 col-sm-6 mb-4">
          <a href="#">
            <img id="bg" src="{{ url_for('video_feed') }}" height="300" width="500">
          </a>
        </div>

        <div class="col-md-3 col-sm-6 mb-4">
          <a href="#">
           
          </a>
        </div>

        <div class="col-md-3 col-sm-6 mb-4">
          <a href="#">
            <img id="bg" src="{{ url_for('video_feed') }}" height="300" width="500">
          </a>
        </div>

        <div class="col-md-3 col-sm-6 mb-4">
          <a href="#">
            
          </a>
        </div>

      </div>
      <!-- /.row -->

    </div>
      <!-- /.row -->

    </div>
    <!-- /.container -->

    <!-- Footer -->
    <footer class="py-5 bg-dark">
      <div class="container">
        <p class="m-0 text-center text-white">Copyright &copy; Your Website 2018</p>
      </div>
      <!-- /.container -->
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src="static/vendor/jquery/jquery.min.js"></script>
    <script src="static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
    <p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = "My First JavaScript";
loadDoc();
</script>
   <!--  <script type="text/javascript">
          document.getElementById("headoof").innerHTML = "Reading";
         // readTextFile("file:///C:/Users/Mayank/Documents/w4/w2/crowd-counting-MCNN-master/val.txt")
     
    </script> -->
  </body>

</html>
