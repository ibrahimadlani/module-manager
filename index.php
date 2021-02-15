<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Module Manager</title>
  <meta name="description" content="">
  <meta name="author" content="Ibrahim ADLANI">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="//fonts.googleapis.com/css?family=Raleway:400,300,600" rel="stylesheet" type="text/css">
  <link rel="stylesheet" href="css/normalize.css">
  <link rel="stylesheet" href="css/skeleton.css">
  <link rel="stylesheet" href="css/master.css">
  <link rel="icon" type="image/png" href="images/favicon.png">
</head>
<body>
  <div class="container">
    <div class="row">
      <div class="">
        <h2 style="margin-bottom:0px;">Module Manager</h2>
        <p>Emploie du temps des deuxièmes années en formation initial de l'<a href="http://www.uphf.fr">Université Polytechnique des Hauts-de-France</a>.</p>
        <table class="u-full-width">
            <thead>
                <tr>
                  <th>Créneaux</th>
                  <th>Type</th>
                  <th>Nom</th>
                  <th>Module</th>
                  <th>Professeur</th>
                  <th>Commentaire</th>
                </tr>
            </thead>
            <tbody id="tablebody">
                
            </tbody>
        </table>
      </div>
    </div>
  </div>
  <?php 
  $d =  date('j');
  $m =  date('n');
  $y =  date('Y');

  $fileContent = file_get_contents("data/".$d."-".$m."-".$y.".json");
  ?>
  <script>var json = '<?php echo $fileContent; ?>';</script>
  <script src="js/script.js"></script>
</body>
</html>
