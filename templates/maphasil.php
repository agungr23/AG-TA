<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/png" href="{{ url_for('static', filename='assets/img/Python-PNG.png') }}">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <title>AG Tugas Akhir</title>
    <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no' name='viewport' />
    <!--     Fonts and icons     -->
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700,200" rel="stylesheet" />
    <link href="https://use.fontawesome.com/releases/v5.0.6/css/all.css" rel="stylesheet">
    <!-- CSS Files -->
    <link href="{{ url_for('static', filename='assets/css/bootstrap.min.css') }}" rel="stylesheet" />
    <link href="{{ url_for('static', filename='assets/css/now-ui-dashboard.css') }}" rel="stylesheet" />
    <!-- CSS Just for demo purpose, don't include it in your project -->
    <link href="{{ url_for('static', filename='assets/demo/demo.css') }}" rel="stylesheet" />
</head>

<body class="">
    <div class="wrapper ">
        <div class="sidebar" data-color="orange">
            <!--
        Tip 1: You can change the color of the sidebar using: data-color="blue | green | orange | red | yellow"
    -->
            <div class="logo">
                <a class="simple-text logo-mini">
                    AG
                </a>
                <a class="simple-text logo-normal">
                    Tugas Akhir
                </a>
            </div>
            <div class="sidebar-wrapper">
                <ul class="nav">
                    <li class="active">
                        <a href="{{ url_for('map') }}">
                            <i class="now-ui-icons location_map-big"></i>
                            <p>Algoritma Genetika</p>
                        </a>
                    </li>
                    <li>
                        <a href="{{ url_for('index') }}">
                            <i class="now-ui-icons design_bullet-list-67"></i>
                            <p>Dataset</p>
                        </a>
                    </li>
                    
                </ul>
            </div>
        </div>
        <div class="main-panel">
            <!-- Navbar -->
            
            <!-- End Navbar -->
            <div class="content mt-4">
                <div class="row">
                    <div class="col-md-12">
                        <div class="card ">
                            <div class="card-header ">
                                <b>Hasil Perhitungan Algoritma Genetika</b>
                            </div>
                            <div class="card-header ">
                                <div class="row">
                                    <div class="col">
                                        <a href="{{ url_for('map') }}" class="btn btn-primary" role="button">Back</a>
                                    </div>
                                    <div class="col">
                                        <!-- <div class="row">
                                            Generasi : {{jgen}}
                                        </div>
                                        <div class="row">
                                            Populasi : {{jpol}}
                                        </div> -->
                                            
                                    </div>
                                </div>
                                
                            </div>
                            <div class="card-body ">
                                <!-- <div id="map" class="map"></div> -->
                                <div>
                                    <iframe src="{{url_for('mapku')}}" width="1015" height="450" style="border:0;" allowfullscreen="" loading="lazy" id="mapku"></iframe>
                                </div>
                            </div>
                            <!-- <div class="card-body">
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead class=" text-primary">
                                            <th>
                                                Nama
                                            </th>
                                        </thead>
                                        <tbody>
                                            {% for row in optimal_route %}
                                            <tr>
                                                <td>
                                                    {{ row[0] }}
                                                </td>
                                                
                                            </tr>
                                            {% endfor %}
                                        </tbody>
                                    </table>
                                </div>
                            </div> -->
                        </div>
                    </div>
                </div>
            </div>
            <footer class="footer">
                <div class="container-fluid">
                    <div class="copyright">
                        &copy;
                        <script>
                            document.write(new Date().getFullYear())
                        </script>
                    </div>
                </div>
            </footer>
        </div>
    </div>
</body>
<!--   Core JS Files   -->
<script src="{{ url_for('static', filename='assets/js/core/jquery.min.js') }}"></script>
<script src="{{ url_for('static', filename='assets/js/core/popper.min.js') }}"></script>
<script src="{{ url_for('static', filename='assets/js/core/bootstrap.min.js') }}"></script>
<script src="{{ url_for('static', filename='assets/js/plugins/perfect-scrollbar.jquery.min.js') }}"></script>
<!--  Google Maps Plugin    -->
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCK6wBEKMl4FJYDQPLS0zKL_GPoRpEPEJs"></script>
<!-- Chart JS -->
<script src="{{ url_for('static', filename='assets/js/plugins/chartjs.min.js') }}"></script>
<!--  Notifications Plugin    -->
<script src="{{ url_for('static', filename='assets/js/plugins/bootstrap-notify.js') }}"></script>
<!-- Control Center for Now Ui Dashboard: parallax effects, scripts for the example pages etc -->
<script src="{{ url_for('static', filename='assets/js/now-ui-dashboard.js') }}"></script>
<!-- Now Ui Dashboard DEMO methods, don't include it in your project! -->
<script src="{{ url_for('static', filename='assets/demo/demo.js') }}"></script>
<script>
    $(document).ready(function() {
        // Javascript method's body can be found in assets/js/demos.js
        demo.initGoogleMaps();
    });
</script>
<!-- <script>
    function gantimap(){
        document.getElementById("mapku").src = "{{url_for('mapku')}}"
    }
    
</script> -->

</html>
